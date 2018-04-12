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




class ManageStaffWidget(QWidget):
    def __init__(self, parent=None):
        super(ManageStaffWidget, self).__init__(parent)
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
        user_name=str(self.search_box.text())
        if len(user_name)==0:
            self.widget_message=getMessageWindow("Type Something")
            self.widget_message.show()
            return
        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")
        cursor=db.cursor()
        search_query="""
            SELECT * FROM staff WHERE user_name=%s
        """


        cursor.execute(search_query,(user_name))
        self.staff_results=list(cursor.fetchall())
        if len(self.staff_results)==0:
            self.result_window=QWidget()
            self.label_user=QLabel("No Staff Found")
            self.layout=QHBoxLayout()
            self.layout_vert=QVBoxLayout()
            self.layout.addStretch()
            self.layout.addWidget(self.label_user)
            self.layout.addStretch()
            self.layout_vert.addLayout(self.layout)
            self.layout_vert.addStretch()
            self.result_window.setLayout(self.layout_vert)
            self.scroll_area.setWidget(self.result_window)
            return


        user_name=self.staff_results[0][0]
        first_name=self.staff_results[0][1]
        last_name=self.staff_results[0][2]
        self.result_window=QWidget()
        self.label_user=QLabel()
        self.button_remove=QPushButton("Remove")
        self.button_remove.clicked.connect(self.remove_clicked)
        #self.button_checkout.clicked.connect(self.checkout_clicked)
        self.label_user.setText(first_name+" "+last_name)
        self.layout=QHBoxLayout()
        self.layout_vert=QVBoxLayout()
        self.layout.addStretch()
        self.layout.addWidget(self.label_user)
        self.layout.addWidget(self.button_remove)
        self.layout.addStretch()
        self.layout_vert.addLayout(self.layout)
        self.layout_vert.addStretch()
        self.result_window.setLayout(self.layout_vert)
        self.scroll_area.setWidget(self.result_window)

    def remove_clicked(self):
        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")
        cursor=db.cursor()
        user_name=self.staff_results[0][0]
        delete_query="""
            DELETE  FROM staff WHERE user_name=%s
        """
        cursor.execute(delete_query,(user_name))
        db.commit()
        self.scroll_area.setWidget(QWidget())
        self.widget_message=getMessageWindow("Deleted Successfully")
        self.widget_message.show()


def get_manage_staff_widget():
    return ManageStaffWidget()