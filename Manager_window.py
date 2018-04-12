#!usr/bin/env python
#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import MySQLdb
import string
import matplotlib.pyplot as plt
from book_deatils_widget import get_show_details_widget
from signup_widget import SignupWindow
from login_form import login_form
from login_widget import *
from stylesheets import *
from see_cart_widget import *
from add_book_widget import *
from update_inventory_widget import *
from process_order_widget import *
from manage_staff_widget import *
import sys
with open('stylesheet.txt','r') as f:
    sheet=f.read()




class qWindow(QWidget):
    def __init__(self, parent=None):
        super(qWindow, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.top_window = QWidget()
        self.top_window_layout=QHBoxLayout()
        self.top_window.setMinimumHeight(100)

        self.tasks=["Add Book","Update Inventory","Process Order","Manage Staff"]
        self.topUI()
        self.mainUI()
        self.wrap_layout.addWidget(self.top_window)
        self.wrap_layout.addWidget(self.main_window)

        #self.wrap_layout.addWidget(self.main_window)
        #self.wrap_layout.addStretch()
        self.setLayout(self.wrap_layout)
        #self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(sheet)
        self.compare_list=[]
        self.login_info=None
        self.login_window=None
        #self.topUI_login()
        #self.wrap_layout.addWidget(self.main_window)
        self.setMinimumHeight(500)
        self.setMinimumWidth(1200)

    def topUI(self):
        print self.top_window_layout.count()
        for i in reversed(range(self.top_window_layout.count())):
            widgetToRemove=self.top_window_layout.itemAt((i))
            if widgetToRemove:
                widgetToRemove=widgetToRemove.widget()
                print widgetToRemove
                self.top_window_layout.removeWidget(widgetToRemove)
                if widgetToRemove:
                    widgetToRemove.setParent(None)
        self.button_login=QPushButton("Login")
        #self.button_login.setMaximumWidth(200)
        self.button_login.clicked.connect(self.login_clicked)
        self.button_signup=QPushButton("Sign up")

        self.button_signup.setMaximumWidth(200)
        self.button_signup.clicked.connect(self.signup_clicked)

        self.top_window_layout.addStretch()
        self.top_window_layout.addWidget(self.button_login)
        self.top_window_layout.addWidget(self.button_signup)
        self.top_window_layout.addStretch()
        self.top_window.setLayout(self.top_window_layout)

    def topUI_login(self):
        #self.search_box=None
        #self.button_search=None
        #self.button_login=None
        #self.button_signup=None
        print self.top_window_layout.count()
        for i in reversed(range(self.top_window_layout.count())):
            widgetToRemove=self.top_window_layout.itemAt((i))
            if widgetToRemove:
                widgetToRemove=widgetToRemove.widget()
                print widgetToRemove
                self.top_window_layout.removeWidget(widgetToRemove)
                if widgetToRemove:
                    widgetToRemove.setParent(None)
        self.label_name=QLabel()
        self.button_logout=QPushButton("Log out")

        self.button_logout.setMaximumWidth(200)
        self.button_logout.clicked.connect(self.click_logout)
        self.top_window_layout.addStretch()
        self.top_window_layout.addWidget(self.label_name)
        self.top_window_layout.addWidget(self.button_logout)
        self.top_window_layout.addStretch()
        print self.login_info
        name=self.login_info[0][1]+" "+self.login_info[0][2]
        #self.top_window_layout.addWidget(QLabel("Welcome "+name))
        self.label_name.setText("Welcome "+name)


        self.top_window.setLayout(self.top_window_layout)

    def click_logout(self):
        self.login_info=None
        self.main_right_widget=QWidget()
        self.scroll_right_main.setWidget(self.main_right_widget)
        self.topUI()

    def mainUI(self):
        self.main_window=QWidget()
        self.main_window_layout=QHBoxLayout()
        self.scroll_left_main=QScrollArea()
        self.scroll_left_main.setWidgetResizable(True)
        self.list_widget=QListWidget()
        self.list_widget.itemClicked.connect(self.list_item_clicked)
        self.list_widget.addItems(self.tasks)
        #self.list_widget.itemClicked.connect(self.Clicked)
        self.scroll_left_main.setMinimumHeight(250)
        self.scroll_left_main.setMaximumWidth(300)
        self.list_widget.setMinimumWidth(250)
        self.list_widget.setMaximumWidth(300)
        self.scroll_left_main.setWidget(self.list_widget)
        self.main_window_layout.addWidget(self.scroll_left_main)
       # self.main_window_layout.addStretch()
        self.main_window.setLayout(self.main_window_layout)

        ###Main Right UI

        self.scroll_right_main=QScrollArea()
        self.scroll_right_main.setMinimumWidth(1000)
        self.scroll_right_main.setWidgetResizable(True)
        self.main_right_widget=None
        self.scroll_right_main.setWidget(self.main_right_widget)
        self.main_window_layout.addWidget(self.scroll_right_main)
        self.main_window_layout.addStretch()

    def list_item_clicked(self,item):
        if not self.login_info:
            self.widget_message=getMessageWindow("Login First")
            self.widget_message.show()
           # return
        if str(item.text())==self.tasks[0]:
            self.main_right_widget=get_add_book_widget()
            self.scroll_right_main.setWidget(self.main_right_widget)
        elif str(item.text())==self.tasks[1]:
            self.main_right_widget=get_update_inventory_widget()
            self.scroll_right_main.setWidget(self.main_right_widget)
        elif str(item.text())==self.tasks[2]:
            self.main_right_widget=get_process_order_widget()
            self.scroll_right_main.setWidget(self.main_right_widget)
        elif str(item.text())==self.tasks[3]:
            self.main_right_widget=get_manage_staff_widget()
            self.scroll_right_main.setWidget(self.main_right_widget)
    def login_clicked(self):
        #self.login_window=LoginWindow()
        #self.login_window.show()
        getLoginWindow(self,"manager")

    def signup_clicked(self):
        self.signup_window=SignupWindow()
        self.signup_window.table="manager"
        self.signup_window.show()

app = QApplication(sys.argv)
wind = qWindow()

wind.show()
sys.exit(app.exec_())