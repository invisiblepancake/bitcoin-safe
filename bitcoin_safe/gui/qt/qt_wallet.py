
import imp
from bitcoin_safe.keystore import KeyStore

from bitcoin_safe.wallet import Wallet
from .util import format_amount, read_QIcon
from typing import List
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .balance_dialog import BalanceToolButton
from .balance_dialog import COLOR_FROZEN, COLOR_CONFIRMED, COLOR_FROZEN_LIGHTNING, COLOR_LIGHTNING, COLOR_UNCONFIRMED, COLOR_UNMATURED
from .history_list import HistoryList, HistoryModel
from .address_list import AddressList
from .utxo_list import UTXOList
from .util import add_tab_to_tabs, format_amount_and_units, format_amount

from ...util import start_in_background_thread
from ...signals import Signals, Listener
from ...i18n import _
from .ui_settings import WalletSettingsUI
from ...wallet import AddressTypes, AddressType
from enum import Enum, auto
from .password_question import PasswordQuestion
from threading import Lock
from bitcoin_safe import wallet


class StatusBarButton(QToolButton):
    # note: this class has a custom stylesheet applied in stylesheet_patcher.py
    def __init__(self, icon, tooltip, func, sb_height):
        QToolButton.__init__(self)
        self.setText('')
        self.setIcon(icon)
        self.setToolTip(tooltip)
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.setAutoRaise(True)
        size = max(25, round(0.9 * sb_height))
        self.setMaximumWidth(size)
        self.clicked.connect(self.onPress)
        self.func = func
        self.setIconSize(QSize(size, size))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def onPress(self, checked=False):
        '''Drops the unwanted PySide2 "checked" argument'''
        self.func()

    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Return, Qt.Key_Enter]:
            self.func()
            
            

class Network():
    def __init__(self, wallet):
        self.proxy = None
        self.wallet = wallet
    
    def is_connected(self):
        return bool(self.get_server_height())
        
    def get_server_height(self):
        if self.wallet.blockchain:
            return self.wallet.blockchain.get_height()
        
    def get_local_height(self):
        return self.get_server_height()
        
    def get_blockchains(self):
        return [self.wallet.blockchain] if self.wallet.blockchain else []

class FX():
    def __init__(self):
        pass
    
    def is_enabled(self):
        return False
    
    def can_have_history(self):
        return False
    def has_history(self):
        return False
 
 

class QTWallet():
    def __init__(self, wallet, config, signals:Signals):    
        self.wallet = wallet
        self.password = None
        self.wallet_settings_tab = None
        self.config = config
        self.fx = FX()
        self.ui_password_question = PasswordQuestion()
        self.password = None
        self.signals = signals
        
        
        self.history_tab, self.history_list, self.history_model = None, None, None
        self.addresses_tab, self.address_list = None, None
        self.utxo_tab, self.utxo_list = None, None
        
        self._create_wallet_tab_and_subtabs()
    
    def __repr__(self) -> str:
        return f'QTWallet({self.__dict__})'    
    
    def save(self): 
        self.password = self.ui_password_question.ask_for_password()  if not self.password else self.password
        self.wallet.save(self.password, self.wallet.basename())
    
                
        
    def cancel_setting_changes(self):
        self.wallet_settings_ui.set_ui_from_wallet(self.wallet)
        
        
    def apply_setting_changes(self):
        self.wallet_settings_ui.set_wallet_from_ui()
        self.wallet.recrate_bdk_wallet() # this must be after set_wallet_from_ui, but before create_wallet_tabs
        
        self.sync()
        self.refresh_caches_and_ui_lists()


    def refresh_caches_and_ui_lists(self):
        # before the wallet UI updates, we have to refresh the wallet caches to make the UI update faster
        print('start refresh cashe')
        self.wallet.reset_cache()
        
        def threaded():
            self.wallet.fill_commonly_used_caches()
            
        def on_finished():
            # now do the UI
            print('start refresh ui')
            
            if self.history_tab:
                self.address_list.update()
                self.utxo_list.update()
                self.history_list.update()
            else:
                self.create_wallet_tabs()
            
        start_in_background_thread(threaded, name='Update wallet UI', on_finished=on_finished)
            
    
    
    def _create_wallet_tab_and_subtabs(self):
        "Create a tab, and layout, that other UI components can fit inside"
        # create UI part
        self.tab = QWidget()
        self.tab.setObjectName(self.wallet.id)
            
        self.outer_layout = QVBoxLayout(self.tab)
        # add the tab_widget for  history, utx, send tabs
        self.tabs = QTabWidget(self.tab)
        self.outer_layout.addWidget(self.tabs)
    
    def create_and_add_settings_tab(self):
        "Create a wallet settings tab, such that one can create a wallet (e.g. with xpub)"
        wallet_settings_ui = WalletSettingsUI(wallet=self.wallet)
        add_tab_to_tabs(self.tabs, wallet_settings_ui.tab, read_QIcon("preferences.png"), "Settings", "settings")

        self.listener_apply_setting_changes =  Listener(self.apply_setting_changes, 
                                                connect_to_signals=[wallet_settings_ui.signal_qtwallet_apply_setting_changes]) 
        self.listener_cancel_setting_changes =  Listener(self.cancel_setting_changes, 
                                                connect_to_signals=[wallet_settings_ui.signal_qtwallet_cancel_setting_changes]) 

        return wallet_settings_ui.tab, wallet_settings_ui   

    def create_pre_wallet_tab(self ):
        "Create a wallet settings tab, such that one can create a wallet (e.g. with xpub)"        
        self.wallet_settings_tab, self.wallet_settings_ui = self.create_and_add_settings_tab()        

    def set_wallet(self, wallet:Wallet):
        self.wallet = wallet        

    def create_wallet_tabs(self):
        "Create tabs.  set_wallet be called first"
        assert bool(self.wallet)
        self.network =  Network(self.wallet)
                
        self.history_tab, self.history_list, self.history_model = self._create_hist_tab(self.tabs)
        self.addresses_tab, self.address_list = self._create_addresses_tab(self.tabs)        
        self.utxo_tab, self.utxo_list = self._create_utxo_tab(self.tabs)        
        if not self.wallet_settings_tab:
            self.settings_tab, self.wallet_settings_ui = self.create_and_add_settings_tab()
        
        self.create_status_bar(self.tab, self.outer_layout)

        self.update_status()
        self.tabs.setCurrentIndex(0)



    def create_status_bar(self, tab, outer_layout):
        sb = QStatusBar()
        self.balance_label = BalanceToolButton()
        self.balance_label.setText("Loading wallet...")
        self.balance_label.setAutoRaise(True)
        # self.balance_label.clicked.connect(self.show_balance_dialog)
        sb.addWidget(self.balance_label)

        font_height = QFontMetrics(self.balance_label.font()).height()
        sb_height = max(35, int(2 * font_height))
        sb.setFixedHeight(sb_height)

        # remove border of all items in status bar
        tab.setStyleSheet("QStatusBar::item { border: 0px;} ")

        self.search_box = QLineEdit()
        self.search_box.textChanged.connect(self.do_search)
        self.search_box.hide()
        sb.addPermanentWidget(self.search_box)

        # self.update_check_button = QPushButton("")
        # self.update_check_button.setFlat(True)
        # self.update_check_button.setCursor(QCursor(Qt.PointingHandCursor))
        # self.update_check_button.setIcon(read_QIcon("update.png"))
        # self.update_check_button.hide()
        # sb.addPermanentWidget(self.update_check_button)

        # self.tasks_label = QLabel('')
        # sb.addPermanentWidget(self.tasks_label)

        # self.password_button = StatusBarButton(QIcon(), _("Password"), self.change_password_dialog, sb_height)
        # sb.addPermanentWidget(self.password_button)

        # sb.addPermanentWidget(StatusBarButton(read_QIcon("preferences.png"), _("Preferences"), self.settings_dialog, sb_height))
        # self.seed_button = StatusBarButton(read_QIcon("seed.png"), _("Seed"), self.show_seed_dialog, sb_height)
        # sb.addPermanentWidget(self.seed_button)
        # self.lightning_button = StatusBarButton(read_QIcon("lightning.png"), _("Lightning Network"), self.gui_object.show_lightning_dialog, sb_height)
        # sb.addPermanentWidget(self.lightning_button)
        # self.update_lightning_icon()
        self.status_button = None
        if self.network:
            self.status_button = StatusBarButton(read_QIcon("status_disconnected.png"), _("Network"), self.show_network_dialog, sb_height)
            sb.addPermanentWidget(self.status_button)
        # run_hook('create_status_bar', sb)
        outer_layout.addWidget(sb)
        
        
    def show_network_dialog(self):
        pass
        

    def toggle_search(self):
        self.search_box.setHidden(not self.search_box.isHidden())
        if not self.search_box.isHidden():
            self.search_box.setFocus()
        else:
            self.do_search('')

    def do_search(self, t):
        tab = self.tabs.currentWidget()
        if hasattr(tab, 'searchable_list'):
            tab.searchable_list.filter(t)        
            
            
            
        

    def update_status(self):
        if not self.wallet:
            return

        network_text = ""
        balance_text = ""

        if self.network is None:
            network_text = _("Offline")
            icon = read_QIcon("status_disconnected.png")

        elif self.network.is_connected():
            server_height = self.network.get_server_height()
            server_lag = self.network.get_local_height() - server_height
            fork_str = "_fork" if len(self.network.get_blockchains())>1 else ""
            # Server height can be 0 after switching to a new server
            # until we get a headers subscription request response.
            # Display the synchronizing message in that case.
            if not self.wallet.is_up_to_date() or server_height == 0:
                num_sent, num_answered = self.wallet.get_history_sync_state_details()
                network_text = ("{} ({}/{})"
                                .format(_("Synchronizing..."), num_answered, num_sent))
                icon = read_QIcon("status_waiting.png")
            elif server_lag > 1:
                network_text = _("Server is lagging ({} blocks)").format(server_lag)
                icon = read_QIcon("status_lagging%s.png"%fork_str)
            else:
                network_text = _("Connected")
                confirmed, unconfirmed, unmatured, frozen = self.wallet.get_balances_for_piechart()
                self.balance_label.update_list([
                    (_('Frozen'), COLOR_FROZEN, frozen),
                    (_('Unmatured'), COLOR_UNMATURED, unmatured),
                    (_('Unconfirmed'), COLOR_UNCONFIRMED, unconfirmed),
                    (_('On-chain'), COLOR_CONFIRMED, confirmed), 
                ])
                balance = confirmed + unconfirmed + unmatured + frozen  
                balance_text =  _("Balance") + ": %s "%(format_amount_and_units(balance))
                # append fiat balance and price
                if self.fx.is_enabled():
                    balance_text += self.fx.get_fiat_status_text(balance,
                        self.base_unit(), self.get_decimal_point()) or ''
                if not self.network.proxy:
                    icon = read_QIcon("status_connected%s.png"%fork_str)
                else:
                    icon = read_QIcon("status_connected_proxy%s.png"%fork_str)
        else:
            if self.network.proxy:
                network_text = "{} ({})".format(_("Not connected"), _("proxy enabled"))
            else:
                network_text = _("Not connected")
            icon = read_QIcon("status_disconnected.png")

        # if self.tray:
        #     # note: don't include balance in systray tooltip, as some OSes persist tooltips,
        #     #       hence "leaking" the wallet balance (see #5665)
        #     name_and_version = self.get_app_name_and_version_str()
        #     self.tray.setToolTip(f"{name_and_version} ({network_text})")
        self.balance_label.setText(balance_text or network_text)
        if self.status_button:
            self.status_button.setIcon(icon)

        # num_tasks = self.num_tasks()
        # if num_tasks == 0:
        #     name = ''
        # elif num_tasks == 1:
        #     with self._coroutines_scheduled_lock:
        #         name = list(self._coroutines_scheduled.values())[0]  + '...'
        # else:
        #     name = "%d"%num_tasks + _('tasks')  + '...'
        # self.tasks_label.setText(name)
        # self.tasks_label.setVisible(num_tasks > 0)



    def get_tabs(self, tab_widget):
        return  [tab_widget.widget(i) for i in range(tab_widget.count())] 

    def create_list_tab(self, l:HistoryList):
        w = QWidget()
        w.searchable_list = l
        vbox = QVBoxLayout()
        w.setLayout(vbox)
        #vbox.setContentsMargins(0, 0, 0, 0)
        #vbox.setSpacing(0)
        toolbar = l.create_toolbar(self.config)
        if toolbar:
            vbox.addLayout(toolbar)
        vbox.addWidget(l)
        return w
    
    def _create_hist_tab(self, tabs): 
        hm = HistoryModel(self.tab, self.fx, self.config, self.wallet, self.signals)
        l = HistoryList(self.fx, self.config, self.signals,  self.wallet, hm)
        hm.set_view(l)
        l.searchable_list = l
        tab =  self.create_list_tab(l)

        add_tab_to_tabs(tabs, tab, read_QIcon("tab_history.png"), "History", "history", position=0)
        
        
        
        return tab, l, hm
                
     


    def _create_addresses_tab(self, tabs):
        l = AddressList(self.fx, self.config, self.wallet, self.signals)
        tab =  self.create_list_tab(l)

        add_tab_to_tabs(tabs, tab, read_QIcon("tab_addresses.png"), "Addresses", "addresses", position=1)
        return tab, l        



    def _create_utxo_tab(self, tabs):
        l = UTXOList(self.config, self.wallet, self.signals)
        tab =  self.create_list_tab(l)

        add_tab_to_tabs(tabs, tab, read_QIcon("tab_coins.png"), "Coins", "utxo", position=2)
        return tab, l        


    def update_tabs(self, wallet=None):
        if wallet is None:
            wallet = self.wallet
        if wallet != self.wallet:
            return
        self.history_model.refresh('update_tabs')
        # self.receive_tab.request_list.update()
        # self.receive_tab.update_current_request()
        # self.send_tab.invoice_list.update()
        self.address_list.update()
        self.utxo_list.update()
        # self.contact_list.update()
        # self.channels_list.update_rows.emit(wallet)
        # self.update_completions()

    def refresh_tabs(self, wallet=None):
        self.history_model.refresh('refresh_tabs')
        # self.receive_tab.request_list.refresh_all()
        # self.send_tab.invoice_list.refresh_all()
        self.address_list.refresh_all()
        self.utxo_list.refresh_all()
        # self.contact_list.refresh_all()
        # self.channels_list.update_rows.emit(self.wallet)

        
    def sync(self, threaded=True):
        def do_sync():            
            self.wallet.sync()
            print('finished sync')
        def on_finished():
            self.refresh_caches_and_ui_lists()
            # self.update_tabs()
            # self.update_status()
        if threaded:
            future = start_in_background_thread(do_sync, on_finished=on_finished)
        else:
            do_sync()
            on_finished()
        print(future)
                    
        
        