
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .util import  read_QIcon, add_tab_to_tabs
from bdkpython import Network
from PySide2.QtSvg import QSvgWidget
from .util import  icon_path, resize, qresize
from .ui_explainer0 import Ui_Form as Ui_Explainer0
from .ui_explainer1 import Ui_Form as Ui_Explainer1

class NewWalletWelcomeScreen():    
    def __init__(self, main_tabs, network:Network) -> None:
        super().__init__()
        self.main_tabs = main_tabs
        
        self.name = 'New wallet tab'
        self.network = network
        
        self.create_ui()
        self.create_ui_explainer0()
        self.create_ui_explainer1()
        
    
    def add_new_wallet_welcome_tab(self):
        add_tab_to_tabs(self.main_tabs, self.tab,  read_QIcon("file.png"), 'Create new wallet', 'Create new wallet')

    
    def create_ui_explainer0(self):
        self.ui_explainer0 = Ui_Explainer0(self.main_tabs)
        self.ui_explainer0.setupUi()

    def create_ui_explainer1(self):
        self.ui_explainer1 = Ui_Explainer1(self.main_tabs)
        self.ui_explainer1.setupUi()


    def create_ui(self):
        self.tab = QWidget()
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.groupBox_singlesig = QGroupBox(self.tab)
        self.verticalLayout = QVBoxLayout(self.groupBox_singlesig)
        self.label_singlesig = QLabel(self.groupBox_singlesig)
        # font = QFont()
        # font.setPointSize(11)
        # self.label_singlesig.setFont(font)
        self.label_singlesig.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_singlesig)

        self.groupBox_1signingdevice = QGroupBox(self.groupBox_singlesig)
        self.groupBox_1signingdevice.setEnabled(True)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_1signingdevice)
        



        self.svg_widget = QSvgWidget(icon_path("coldcard-only.svg")) 
        self.svg_widget.setMinimumSize(qresize(self.svg_widget.sizeHint(), (60,80)))
        self.svg_widget.setMaximumSize(qresize(self.svg_widget.sizeHint(), (60,80)))
        self.horizontalLayout_4.addWidget(self.svg_widget)


        # set size of groupbox according to svg
        self.groupBox_1signingdevice.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.verticalLayout.addWidget(self.groupBox_1signingdevice)

        self.pushButton_singlesig = QPushButton(self.groupBox_singlesig)

        self.verticalLayout.addWidget(self.pushButton_singlesig)


        self.horizontalLayout_2.addWidget(self.groupBox_singlesig)

        self.groupBox_multisig = QGroupBox(self.tab)
        self.verticalLayout_multisig = QVBoxLayout(self.groupBox_multisig)
        self.label_multisig = QLabel(self.groupBox_multisig)
        # font1 = QFont()
        # font1.setFamily(u"Noto Sans")
        # # font1.setPointSize(11)
        # font1.setBold(False)
        # font1.setItalic(False)
        # font1.setWeight(50)
        # self.label_multisig.setFont(font1)
        self.label_multisig.setWordWrap(True)

        self.verticalLayout_multisig.addWidget(self.label_multisig)

        self.groupBox_3signingdevices = QGroupBox(self.groupBox_multisig)
        self.groupBox_3signingdevices.setEnabled(True)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3signingdevices)

        for i in range(3):
            svg_widget = QSvgWidget(icon_path("coldcard-only.svg")) 
            svg_widget.setMinimumSize(qresize(svg_widget.sizeHint(), (60,80)))
            svg_widget.setMaximumSize(qresize(svg_widget.sizeHint(), (60,80))) 
            self.horizontalLayout_3.addWidget(svg_widget)

        self.verticalLayout_multisig.addWidget(self.groupBox_3signingdevices)
        # set size of groupbox according to svg
        self.groupBox_3signingdevices.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)



        self.pushButton_multisig = QPushButton(self.groupBox_multisig)

        self.verticalLayout_multisig.addWidget(self.pushButton_multisig)


        self.horizontalLayout_2.addWidget(self.groupBox_multisig)

        self.groupBox_3 = QGroupBox(self.tab)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.label_custom = QLabel(self.groupBox_3)
        # self.label_custom.setFont(font)
        self.label_custom.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_custom)

        self.pushButton_custom_wallet = QPushButton(self.groupBox_3)

        self.verticalLayout_2.addWidget(self.pushButton_custom_wallet)


        self.horizontalLayout_2.addWidget(self.groupBox_3)




        # self.groupBox_singlesig.setTitle(QCoreApplication.translate("Form", u"Single Signature Wallet", None))
        self.label_singlesig.setAlignment(Qt.AlignTop)
        self.label_singlesig.setText(QCoreApplication.translate("Form", u"""<h1>Single Signature Wallet</h1>
<p>For large funds (but not life savings)</p>
<p>Pros:</p>
<ul>
<li>1 seed (24 secret words) is all you need to access your funds</li>
<li>1 secure location to store the seed backup (on paper or steel) is needed</li>
</ul>
<p>Cons:</p>
<ul>
<li>If you get tricked into giving hackers your seed, your Bitcoin will be stolen immediately</li>
</ul>""", None))
        self.groupBox_1signingdevice.setTitle(QCoreApplication.translate("Form", u"1 signing devices", None))
        self.pushButton_singlesig.setText(QCoreApplication.translate("Form", u"Choose Single Signature", None))
        # self.groupBox_multisig.setTitle(QCoreApplication.translate("Form", u"2 of 3 Multi-Signature Wallet", None))
        self.label_multisig.setAlignment(Qt.AlignTop)
        self.label_multisig.setText(QCoreApplication.translate("Form", u"""<h1>2 of 3 Multi-Signature Wallet</h1>
<p>For life savings</p>
<p>Pros:</p>
<ul>
<li>If 1 seed was lost or stolen, all the funds can be transferred to a new wallet with the 2 remaining seeds + all (master) public keys</li>
</ul>
<p>Cons:</p>
<ul>
<li>3 secure locations to store the seed backups (on paper or steel) + wallet descriptor are needed</li>
<li>Backing up the wallet file (or descriptor) is required to recreate wallet</li>
</ul>
""", None))
        self.groupBox_3signingdevices.setTitle(QCoreApplication.translate("Form", u"3 signing devices", None))
        self.pushButton_multisig.setText(QCoreApplication.translate("Form", u"Choose Multi-Signature", None))
        # self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Custom", None))
        self.label_custom.setAlignment(Qt.AlignTop)
        self.label_custom.setText(QCoreApplication.translate("Form", u"<html><head/><body><h1>Custom Wallet</h1><p>Pros:</p><p>Customize the wallet to your needs</p><p>Cons:</p><p>Less support material online in case of recovery</p></body></html>", None))
        self.pushButton_custom_wallet.setText(QCoreApplication.translate("Form", u"Create custom wallet", None))
    
    def remove_tab(self):
        index = self.main_tabs.indexOf(self.tab)
        if index>=0:
            self.main_tabs.removeTab(index)
        
    
    def set_onclick_multisig_signature(self, f):
        def wrapped_f():
            self.remove_tab()
            f()        
        self.pushButton_multisig.clicked.connect(wrapped_f)
    def set_onclick_single_signature(self, f):
        def wrapped_f():
            self.remove_tab()
            f()        
        self.pushButton_singlesig.clicked.connect(wrapped_f)
    def set_onclick_custom_signature(self, f):
        def wrapped_f():
            self.remove_tab()
            f()        
        self.pushButton_custom_wallet.clicked.connect(wrapped_f)
