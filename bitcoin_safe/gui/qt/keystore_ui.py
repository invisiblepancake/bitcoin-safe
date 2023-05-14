from curses import keyname
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qtrangeslider import QRangeSlider
from PySide2.QtSvg import QSvgWidget
from .util import  icon_path, center_in_widget, qresize, add_tab_to_tabs, read_QIcon
from ...wallet import AddressTypes, get_default_address_type, Wallet, generate_bdk_descriptors
from ...keystore import KeyStoreTypes, KeyStoreType, KeyStore
from ...signals import Signals, QTWalletSignals,  Signal
from ...util import compare_dictionaries
from typing import List
from .keystore_ui_tabs import KeyStoreUIDefault, KeyStoreUIWalletType
from .block_change_signals import BlockChangesSignals
import bdkpython as bdk


class KeyStoreUI:
    def __init__(self, keystore:KeyStore, tabs:QTabWidget, network:bdk.Network) -> None:
        self.keystore = keystore
        self.tabs = tabs
        
        self.keystore_ui_default = KeyStoreUIDefault(tabs, network)
        self.keystore_ui_wallet_type = KeyStoreUIWalletType(network)
        
        self.block_change_signals = BlockChangesSignals(
                sub_instances=[self.keystore_ui_default.block_change_signals]
        )
        
                
        add_tab_to_tabs(self.tabs, self.keystore_ui_wallet_type.tab, self.icon_for_label(keystore.label), keystore.label, keystore.label,   focus=True)
        self.set_ui_from_keystore(self.keystore)            
        self.keystore_ui_wallet_type.signal_click_watch_only.connect(self.onclick_button_watch_only)    

    def icon_for_label(self, label):
        return read_QIcon("key-gray.png") if label.startswith('Recovery') else read_QIcon("key.png")
        
    def remove_tab(self):
        self.tabs.removeTab(self.tabs.indexOf(self.keystore_ui_default.tab))
        self.tabs.removeTab(self.tabs.indexOf(self.keystore_ui_wallet_type.tab))
                
    def set_keystore_from_ui_values(self, keystore:KeyStore):
        ui_keystore = self.keystore_ui_default.get_ui_values_as_keystore()
        if not keystore:
            keystore = self.keystore
        keystore.from_other_keystore(ui_keystore)

    def changed_ui_values(self) -> KeyStore:
        return compare_dictionaries(self.keystore, self.keystore_ui_default.get_ui_values_as_keystore()                        )

    def set_ui_from_keystore(self, keystore:KeyStore):        
        for tab in [self.keystore_ui_default.tab, self.keystore_ui_wallet_type.tab]:
            index = self.tabs.indexOf(tab)
            if index>=0:
                self.tabs.setTabText(index,  keystore.label)
                self.tabs.setTabIcon(index,  self.icon_for_label(keystore.label))
                
        self.keystore_ui_default.set_ui_from_keystore(keystore)
    

    
    def onclick_button_watch_only(self):
        index = self.tabs.indexOf(self.keystore_ui_wallet_type.tab)
        self.tabs.removeTab(index)
                        
        self.keystore.set_type(KeyStoreTypes.watch_only)
        add_tab_to_tabs(self.tabs, self.keystore_ui_default.tab, read_QIcon("key.png"), self.keystore.label, self.keystore.label, position=index, focus=True)
        self.set_ui_from_keystore(self.keystore)

