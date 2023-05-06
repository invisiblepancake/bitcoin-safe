from curses import keyname
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qtrangeslider import QRangeSlider
from PySide2.QtSvg import QSvgWidget
from .util import  icon_path, center_in_widget, qresize, add_tab_to_tabs, read_QIcon, create_button
from ...wallet import AddressTypes, get_default_address_type, Wallet, generate_bdk_descriptors
from ...keystore import KeyStoreTypes, KeyStoreType, KeyStore
from ...signals import Signals, QTWalletSignals, Listener, Signal
from typing import List


class KeyStoreUIWalletType:
    def __init__(self) -> None:
        self.signal_click_watch_only = Signal('signal_click_watch_only')
        self.tab = self.create()


    def create(self):
        tab = QWidget()

        # 1. tab with connection setting
        self.horizontalLayout_5 = QHBoxLayout(tab)
        self.widget_7 = QWidget(tab)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        # self.horizontalLayout_7.setContentsMargins(10, 6, 10, 6)
            


        button = create_button(KeyStoreTypes.hwi.description, (KeyStoreTypes.hwi.icon_filename), parent=self.widget_7 , outer_layout= self.horizontalLayout_7)
        button = create_button(KeyStoreTypes.psbt.description, (KeyStoreTypes.psbt.icon_filename), parent=self.widget_7 , outer_layout= self.horizontalLayout_7)
        self.button_xpub = create_button(KeyStoreTypes.watch_only.description, (KeyStoreTypes.watch_only.icon_filename), parent=self.widget_7 , outer_layout= self.horizontalLayout_7)
        self.button_xpub.clicked.connect(self.signal_click_watch_only)


        self.horizontalLayout_5.addWidget(self.widget_7)

        return tab


            
    
    
        


class KeyStoreUIDefault:
    def __init__(self, tabs:QTabWidget) -> None:
        self.tabs = tabs
        
        self.signal_xpub_changed = Signal('xpub_changed')
        self.signal_fingerprint_changed = Signal('signal_fingerprint_changed')
        self.signal_derivation_path_changed = Signal('signal_derivation_path_changed')

        self.tab = self.create()
    
    
    def on_label_change(self):
        self.tabs.setTabText(self.tabs.indexOf(self.tab), self.edit_label.text())   
    
    
    def create(self):
        tab = QWidget()
        self.tabs.setTabText(self.tabs.indexOf(tab), QCoreApplication.translate("tab", u"Signer settings", None))
        
        self.horizontalLayout_6 = QHBoxLayout(tab)
        self.box_left = QWidget(tab)
        label_keystore_type = QLabel(self.box_left)
        
        self.comboBox_keystore_type = QComboBox(self.box_left)                
        label_keystore_label = QLabel(self.box_left)
        self.edit_label = QLineEdit(self.box_left)                
        self.label_6 = QLabel(self.box_left)
        self.edit_fingerprint = QLineEdit(self.box_left)
        label_derivation_path = QLabel(self.box_left)
        self.edit_derivation_path = QLineEdit(self.box_left)
        label_xpub = QLabel(self.box_left)
        self.edit_xpub = QLineEdit(self.box_left)
        

        # put them on the formLayout
        self.formLayout = QFormLayout(self.box_left)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, label_keystore_type)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_keystore_type)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, label_keystore_label)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_label)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edit_fingerprint)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, label_derivation_path)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.edit_derivation_path)
        self.formLayout.setWidget(4, QFormLayout.LabelRole, label_xpub)
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.edit_xpub) 



        self.horizontalLayout_6.addWidget(self.box_left)

        self.widget_8 = QWidget(tab)
        self.verticalLayout_3 = QVBoxLayout(self.widget_8)
        self.widget_6 = QWidget(self.widget_8)
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.label_4 = QLabel(self.widget_6)

        self.verticalLayout_5.addWidget(self.label_4)

        self.textEdit_2 = QTextEdit(self.widget_6)
        self.verticalLayout_5.addWidget(self.textEdit_2)


        self.verticalLayout_3.addWidget(self.widget_6)


        self.horizontalLayout_6.addWidget(self.widget_8)


        
        
        label_keystore_type.setText(QCoreApplication.translate("tab", u"Type", None))
        label_keystore_label.setText(QCoreApplication.translate("tab", u"Label", None))
        self.label_6.setText(QCoreApplication.translate("tab", u"Fingerprint", None))
        label_derivation_path.setText(QCoreApplication.translate("tab", u"Derivation Path", None))
        label_xpub.setText(QCoreApplication.translate("tab", u"xPub", None))
        self.label_4.setText(QCoreApplication.translate("tab", u"Description", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("tab", u"Useful information about signer", None))


        self.edit_xpub.textChanged.connect(self.signal_xpub_changed)
        self.edit_fingerprint.textChanged.connect(self.signal_fingerprint_changed)
        self.edit_derivation_path.textChanged.connect(self.signal_derivation_path_changed)
        self.edit_label.textChanged.connect(self.on_label_change)


        return tab   
    
        
    def set_comboBox_keystore_type(self, keystore_type:KeyStoreType):
        keys = [v.name for k,v in KeyStoreTypes.__dict__.items() if not k.startswith('_')]
        self.comboBox_keystore_type.addItems(keys)
        self.comboBox_keystore_type.setCurrentIndex(keys.index(keystore_type.name))
        

    def get_comboBox_keystore_type(self) -> KeyStoreType:
        keystore_types = [v for k,v in KeyStoreTypes.__dict__.items() if not k.startswith('_')]
        return keystore_types[self.comboBox_keystore_type.currentIndex()]
                            
    def get_ui_values_as_keystore(self) -> KeyStore:
        return KeyStore(self.edit_xpub.text(),
                            self.edit_fingerprint.text(),
                            self.edit_derivation_path.text(),
                            self.edit_label.text(),
                            self.get_comboBox_keystore_type(),
                            None
                            ) 
            
    def set_ui_from_keystore(self, keystore:KeyStore): 
        self.edit_xpub.setText(keystore.xpub if keystore.xpub  else '')
        self.edit_fingerprint.setText(keystore.fingerprint if keystore.fingerprint  else '')
        self.edit_derivation_path.setText(keystore.derivation_path if keystore.derivation_path  else '')
        self.edit_label.setText(keystore.label)
        self.set_comboBox_keystore_type(keystore.type)        


        from ...util import DEVELOPMENT_PREFILLS
        if DEVELOPMENT_PREFILLS:
            if not keystore.xpub:
                self.edit_xpub.setText('tpubDDnGNapGEY6AZAdQbfRJgMg9fvz8pUBrLwvyvUqEgcUfgzM6zc2eVK4vY9x9L5FJWdX8WumXuLEDV5zDZnTfbn87vLe9XceCFwTu9so9Kks')
            if not keystore.fingerprint:
                self.edit_fingerprint.setText('a42c6dd3')
            
                