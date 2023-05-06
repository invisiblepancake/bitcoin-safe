from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .i18n import _
from .gui.qt.util import read_QIcon
from .gui.qt.balance_dialog import BalanceToolButton


            
            
            
class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.config = {}
        self.setupUi(self)
        


    def setupUi(self, MainWindow:QWidget):            
        # sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        # MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle("Bitcoin Safe")
        MainWindow.setWindowIcon(read_QIcon('logo.svg'))
        w,h = 900, 600
        MainWindow.resize(w,h)
        MainWindow.setMinimumSize(w, h)

        #####
        self.tab_wallets = tabs = QTabWidget(self)
        self.tab_wallets.setTabsClosable(True)
        tabs.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Connect signals to slots
        tabs.tabCloseRequested.connect(self.close_tab)        
        

        # central_widget 
        central_widget = QScrollArea()
        vbox = QVBoxLayout(central_widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(tabs)
        self.setCentralWidget(central_widget)

        self.setMinimumWidth(640)
        self.setMinimumHeight(400)
        if self.config.get("is_maximized"):
            self.showMaximized()

        # self.setWindowIcon(read_QIcon("electrum.png"))
        self.init_menubar()
        ####



        
    def init_menubar(self):
        # menu
        self.menubar = QMenuBar()
        # menu wallet
        self.menu_wallet = self.menubar.addMenu(_("&Wallet"))


        self.menu_wallet.addAction(_("New Wallet"), self.new_wallet).setShortcut(QKeySequence("Ctrl+N"))
        self.menu_wallet.addAction("Open wallet", self.open_wallet).setShortcut(QKeySequence("Ctrl+O"))        
        self.menu_wallet.addAction("Save Current wallet", self.save_current_wallet).setShortcut(QKeySequence("Ctrl+S"))        
        self.menu_wallet.addAction("Find", self.toggle_search).setShortcut(QKeySequence("Ctrl+F"))                
        self.menu_wallet.addSeparator()

        self.menu_wallet.addAction(_("Sync"), self.sync).setShortcut(QKeySequence("F5"))

        # assigne menu bar
        self.setMenuBar(self.menubar)
        


    def new_wallet(self):                   
        pass
    def open_wallet(self):                   
        pass
    def close_tab(self, index):
        pass
    def save_current_wallet(self):
        pass
    def toggle_search(self):
        pass
    def sync(self):
        pass
