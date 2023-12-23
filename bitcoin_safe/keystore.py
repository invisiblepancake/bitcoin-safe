import logging
from typing import Dict

logger = logging.getLogger(__name__)

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from bitcoin_usb.address_types import AddressType, AddressTypes
from packaging import version

from .i18n import _
from .gui.qt.new_wallet_welcome_screen import NewWalletWelcomeScreen
from .gui.qt.balance_dialog import (
    COLOR_FROZEN,
    COLOR_CONFIRMED,
    COLOR_FROZEN_LIGHTNING,
    COLOR_LIGHTNING,
    COLOR_UNCONFIRMED,
    COLOR_UNMATURED,
)
from .gui.qt.util import add_tab_to_tabs, read_QIcon
import bdkpython as bdk
from .storage import BaseSaveableClass, SaveAllClass
import copy
from .descriptors import AddressType, MultipathDescriptor
from bitcoin_usb.device import SimplePubKeyProvider
from bitcoin_usb.address_types import ConstDerivationPaths


class KeyStoreType(SaveAllClass):
    def __init__(self, id, name, description, icon_filename, networks="all") -> None:
        self.id = id
        self.name = name
        self.description = description
        self.icon_filename = icon_filename
        self.networks = (
            [
                bdk.Network.BITCOIN,
                bdk.Network.REGTEST,
                bdk.Network.TESTNET,
                bdk.Network.SIGNET,
            ]
            if networks == "all"
            else networks
        )


class KeyStoreTypes:
    hwi = KeyStoreType(
        "hwi", "USB hardware signer", "Connect \nUSB \nhardware signer", "usb.svg"
    )
    file = KeyStoreType(
        "file",
        "SD card",
        "Import signer details\nvia SD card",
        "sd-card.svg",
    )
    qr = KeyStoreType(
        "qr",
        "QR Code",
        "Import signer details\nvia QR code",
        "camera.svg",
    )
    watch_only = KeyStoreType(
        "watch_only",
        "Watch-Only",
        "xPub / Public Key\nInformation",
        "key-hole-icon.svg",
    )
    seed = KeyStoreType(
        "seed",
        "Seed",
        "Mnemonic Seed\n(Testnet only)",
        "logo.svg",
        networks=[bdk.Network.REGTEST, bdk.Network.TESTNET, bdk.Network.SIGNET],
    )  # add networks here to make the seed option visible

    @classmethod
    def list_types(cls, network: bdk.Network):
        return [
            v
            for v in [cls.hwi, cls.file, cls.qr, cls.watch_only, cls.seed]
            if network in v.networks
        ]

    @classmethod
    def list_names(cls, network: bdk.Network):
        return [v.name for v in cls.list_types(network)]


class KeyStore(SimplePubKeyProvider, BaseSaveableClass):
    VERSION = "0.0.1"

    def __init__(
        self,
        xpub,
        fingerprint,
        key_origin: str,
        label,
        mnemonic: str = None,
        description: str = "",
        derivation_path: str = ConstDerivationPaths.receive,
    ) -> None:
        super().__init__(
            xpub=xpub,
            fingerprint=fingerprint,
            key_origin=key_origin,
            derivation_path=derivation_path,
        )

        self.label = label
        self.mnemonic: str = mnemonic
        self.description = description

    def clone(self) -> "KeyStore":
        return KeyStore(**self.__dict__)

    def to_singlesig_multipath_descriptor(self, address_type: AddressType, network):
        "Uses the bdk descriptor templates to create the descriptor from xpub or seed"
        descriptors = [
            address_type.bdk_descriptor(
                bdk.DescriptorPublicKey.from_string(self.xpub),
                self.fingerprint,
                keychainkind,
                network,
            )
            if not self.mnemonic
            else address_type.bdk_descriptor_secret(
                bdk.DescriptorSecretKey(
                    network, bdk.Mnemonic.from_str(self.mnemonic), ""
                ),
                keychainkind,
                network,
            )
            for keychainkind in [
                bdk.KeychainKind.EXTERNAL,
                bdk.KeychainKind.INTERNAL,
            ]
        ]
        return MultipathDescriptor(*descriptors)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def serialize(self):
        d = super().serialize()

        # you must copy it, so you not't change any calues
        full_dict = self.__dict__.copy()
        # the deepcopy must be done AFTER there is no bdk type in there any more
        d.update(copy.deepcopy(full_dict))
        return d

    @classmethod
    def deserialize(cls, dct, class_kwargs=None):
        super().deserialize(dct, class_kwargs=class_kwargs)

        return KeyStore(**dct)

    @classmethod
    def deserialize_migration(cls, dct: Dict):
        "this class should be oveerwritten in child classes"
        if version.parse(str(dct["VERSION"])) <= version.parse("0.0.0"):
            if "derivation_path" in dct:
                dct["key_origin"] = dct["derivation_path"]
                del dct["derivation_path"]

        # now the version is newest, so it can be deleted from the dict
        if "VERSION" in dct:
            del dct["VERSION"]
        return dct

    def from_other_keystore(self, other_keystore):
        self.xpub = other_keystore.xpub
        self.fingerprint = other_keystore.fingerprint
        self.key_origin = other_keystore.key_origin
        self.label = other_keystore.label
        self.mnemonic = other_keystore.mnemonic
        self.description = other_keystore.description

    def merge_with(self, other_keystore: "KeyStore"):
        # fill in missing info in keystores
        keys = ["xpub", "fingerprint", "key_origin", "label", "description"]
        for key in keys:
            # if both are filled, they have to be identical
            if getattr(self, key) and getattr(other_keystore, key):
                assert getattr(self, key) == getattr(other_keystore, key)

            # fill mine if other_keystore has it
            if not getattr(self, key) and getattr(other_keystore, key):
                setattr(self, key, getattr(other_keystore, key))

        if not self.mnemonic and other_keystore.mnemonic:
            self.mnemonic = other_keystore.mnemonic
