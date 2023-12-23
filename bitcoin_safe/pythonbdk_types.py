import logging
from typing import Dict, List
import bdkpython as bdk
import enum
from .util import serialized_to_hex
from .storage import SaveAllClass

logger = logging.getLogger(__name__)


class Recipient:
    def __init__(self, address, amount, label=None, checked_max_amount=False) -> None:
        self.address = address
        self.amount = amount
        self.label = label
        self.checked_max_amount = checked_max_amount

    def __hash__(self):
        "Necessary for the caching"
        return hash(self.__dict__)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def clone(self):
        return Recipient(self.address, self.amount, self.label, self.checked_max_amount)


class OutPoint(bdk.OutPoint):
    def __key__(self):
        return tuple(v for k, v in sorted(self.__dict__.items()))

    def __hash__(self):
        "Necessary for the caching"
        return hash(self.__key__())

    def __str__(self) -> str:
        return f"{self.txid}:{self.vout}"

    def __repr__(self) -> str:
        return str(f"{self.__class__.__name__}({self.txid},{self.vout})")

    def __eq__(self, other):
        if isinstance(other, OutPoint):
            return (self.txid, self.vout) == (other.txid, other.vout)
        return False

    @classmethod
    def from_bdk(cls, bdk_outpoint: bdk.OutPoint):
        if isinstance(bdk_outpoint, OutPoint):
            return bdk_outpoint
        if isinstance(bdk_outpoint, str):
            return cls.from_str(bdk_outpoint)
        return OutPoint(bdk_outpoint.txid, bdk_outpoint.vout)

    @classmethod
    def from_str(cls, outpoint_str: str):
        if isinstance(outpoint_str, OutPoint):
            return outpoint_str
        txid, vout = outpoint_str.split(":")
        return OutPoint(txid, int(vout))


class TxOut(bdk.TxOut):
    def __key__(self):
        return (serialized_to_hex(self.script_pubkey.to_bytes()), self.value)

    def __hash__(self):
        "Necessary for the caching"
        return hash(self.__key__())

    def __str__(self) -> str:
        return str(self.__key__())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__key__()})"

    @classmethod
    def from_bdk(cls, tx_out: bdk.TxOut):
        if isinstance(tx_out, TxOut):
            return tx_out
        return TxOut(tx_out.value, tx_out.script_pubkey)

    def __eq__(self, other):
        if isinstance(other, TxOut):
            return (self.value, serialized_to_hex(self.script_pubkey.to_bytes())) == (
                other.value,
                serialized_to_hex(other.script_pubkey.to_bytes()),
            )
        return False


class PythonUtxo:
    def __init__(self, address: str, outpoint: OutPoint, txout: TxOut) -> None:
        self.outpoint = outpoint
        self.txout = txout
        self.address = address
        self.is_spent_by_txid: str = None


class UtxosForInputs:
    def __init__(
        self, utxos, included_opportunistic_merging_utxos=None, spend_all_utxos=False
    ) -> None:
        if included_opportunistic_merging_utxos is None:
            included_opportunistic_merging_utxos = []

        self.utxos = utxos
        self.included_opportunistic_merging_utxos = included_opportunistic_merging_utxos
        self.spend_all_utxos = spend_all_utxos


class FullTxDetail:
    """
    for all outputs and inputs, where it has a full PythonUtxo .
    """

    def __init__(self, tx: bdk.TransactionDetails, received=None, send=None) -> None:
        self.outputs: Dict[str, PythonUtxo] = (
            received if received else {}
        )  # outpoint_str: PythonUtxo
        self.inputs: Dict[str, PythonUtxo] = (
            send if send else {}
        )  # outpoint_str: PythonUtxo
        self.tx = tx
        self.txid = tx.txid

    @classmethod
    def fill_received(
        cls, tx: bdk.TransactionDetails, bdkwallet: "BdkWallet"
    ) -> "FullTxDetail":
        res = FullTxDetail(tx)
        txid = tx.txid
        for vout, txout in enumerate(tx.transaction.output()):
            address = bdkwallet.get_address_of_txout(TxOut.from_bdk(txout))
            out_point = OutPoint(txid, vout)
            if address is None:
                continue
            python_utxo = PythonUtxo(address, out_point, txout)
            python_utxo.is_spent_by_txid = False
            res.outputs[str(out_point)] = python_utxo
        return res

    def fill_inputs(
        self,
        lookup_dict_fulltxdetail: Dict[str, "FullTxDetail"],
    ):
        for input in self.tx.transaction.input():
            prev_outpoint = OutPoint.from_bdk(input.previous_output)
            prev_outpoint_str = str(prev_outpoint)

            # check if I have the prev_outpoint fulltxdetail
            if prev_outpoint.txid not in lookup_dict_fulltxdetail:
                self.inputs[prev_outpoint_str] = None
                continue
            fulltxdetail = lookup_dict_fulltxdetail[prev_outpoint.txid]
            if prev_outpoint_str not in fulltxdetail.outputs:
                self.inputs[prev_outpoint_str] = None
                continue
            python_utxo = fulltxdetail.outputs[prev_outpoint_str]
            python_utxo.is_spent_by_txid = self.tx.txid
            self.inputs[prev_outpoint_str] = python_utxo


class AddressInfoMin(SaveAllClass):
    def __init__(self, address, index, keychain):
        self.address = address
        self.index = index
        self.keychain = keychain

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __key__(self):
        return tuple(v for k, v in sorted(self.__dict__.items()))

    def __hash__(self):
        "Necessary for the caching"
        return hash(self.__key__())

    @classmethod
    def from_bdk_address_info(cls, bdk_address_info: bdk.AddressInfo):
        return AddressInfoMin(
            bdk_address_info.address.as_string(),
            bdk_address_info.index,
            bdk_address_info.keychain,
        )


class BlockchainType(enum.Enum):
    CompactBlockFilter = enum.auto()
    Electrum = enum.auto()
    Esplora = enum.auto()
    RPC = enum.auto()

    @classmethod
    def from_text(cls, t):
        if t == "Compact Block Filters":
            return cls.CompactBlockFilter
        elif t == "Electrum Server":
            return cls.Electrum
        elif t == "Esplora Server":
            return cls.Esplora
        elif t == "RPC":
            return cls.RPC

    @classmethod
    def to_text(cls, t):
        if t == cls.CompactBlockFilter:
            return "Compact Block Filters"
        elif t == cls.Electrum:
            return "Electrum Server"
        elif t == cls.Esplora:
            return "Esplora Server"
        elif t == cls.RPC:
            return "RPC"


class CBFServerType(enum.Enum):
    Automatic = enum.auto()
    Manual = enum.auto()

    @classmethod
    def from_text(cls, t):
        if t == "Automatic":
            return cls.Automatic
        elif t == "Manual":
            return cls.Manual

    @classmethod
    def to_text(cls, t):
        if t == cls.Automatic:
            return "Automatic"
        elif t == cls.Manual:
            return "Manual"


def robust_address_str_from_script(
    script_pubkey: bdk.Script, network, on_error_return_hex=False
):
    try:
        return bdk.Address.from_script(script_pubkey, network).as_string()
    except:
        if on_error_return_hex:
            return serialized_to_hex(script_pubkey.to_bytes())


if __name__ == "__main__":
    testdict = {}

    def test_hashing(v):
        testdict[v] = v.__hash__()
        print(testdict[v])

    test_hashing(OutPoint("txid", 0))
    test_hashing(AddressInfoMin("ssss", 4, bdk.KeychainKind.EXTERNAL))
