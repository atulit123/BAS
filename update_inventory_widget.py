#!usr/bin/env python
#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import MySQLdb
import string
import matplotlib.pyplot as plt
from book_deatils_widget import get_show_details_widget
from search_result_widget import *
from stylesheets import *
from see_cart_widget import *
import sys
with open('stylesheet.txt','r') as f:
    sheet=f.read()




class UpdateInventoryWidget(QWidget):
    def __init__(self, parent=None):
        super(UpdateInventoryWidget, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.topUI()
        self.mainUI()

        self.wrap_layout.addWidget(self.top_window)
        self.wrap_layout.addWidget(self.scroll_area)
        self.setLayout(self.wrap_layout)
        #self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(sheet)
        self.compare_list=[]
        self.login_info=None
        self.login_window=None
        #self.topUI_login()
        #self.wrap_layout.addWidget(self.main_window)

    def topUI(self):
        self.top_window = QWidget()
        self.top_window.setObjectName("topwindow")
        self.top_window.setMinimumHeight(100)
        self.search_box=QLineEdit()
        self.search_box.setAlignment(Qt.AlignLeft)
        self.search_box.setFont(QFont("Arial",20))
        self.search_box.setMinimumWidth(300)
        self.button_search=QPushButton("Search")
        self.button_search.setMaximumWidth(200)
        self.button_search.clicked.connect(self.search_clicked)
        #self.button_search.clicked.connect(self.search_clicked)

        self.top_window_layout=QHBoxLayout()
        self.top_window_layout.addStretch()
        self.top_window_layout.addWidget(self.search_box)
        self.top_window_layout.addWidget(self.button_search)
        self.top_window_layout.addStretch()
        self.top_window.setLayout(self.top_window_layout)
    def mainUI(self):
        self.scroll_area=QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.main_window = QWidget()
       # self.main_window.setMinimumHeight(500)
        #self.main_window.setMinimumWidth(1000)
        self.main_window_layout=QVBoxLayout()
        #self.main_leftUI()
        #self.main_rightUI()
    def search_clicked(self):
        #self.main_window_layout=QVBoxLayout()
        query=str(self.search_box.text())
        if len(query)==0:
            self.widget_message=getMessageWindow("Type Something")
            self.widget_message.show()
            return None
        self.main_window=get_search_result_widget(query)
        self.scroll_area.setWidget(self.main_window)


        #self.main_window_layout.addWidget(book_result)
        self.main_window.setLayout(self.main_window_layout)
        self.scroll_area.setWidget(self.main_window)

def get_update_inventory_widget():
    return UpdateInventoryWidget()