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




class ProcessOrder(QWidget):
    def __init__(self, parent=None):
        super(ProcessOrder, self).__init__(parent)
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
        #self.main_window_layout=QVBoxLayout()
        #self.main_leftUI()
        #self.main_rightUI()
    def search_clicked(self):
        #self.main_window_layout=QVBoxLayout()
        user_name=str(self.search_box.text())
        if len(user_name)==0:
            self.widget_message=getMessageWindow("Type Something")
            self.widget_message.show()
            return None
        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")
        cursor=db.cursor()
        search_query="""
            SELECT * FROM customer INNER JOIN cart on cart.user_name=customer.user_name
            WHERE cart.user_name=%s
        """


        cursor.execute(search_query,(user_name))
        self.cart_results=list(cursor.fetchall())
        if len(self.cart_results)==0:
            self.result_window=QWidget()
            self.label_user=QLabel("No cart found")
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


        user_name=self.cart_results[0][0]
        first_name=self.cart_results[0][1]
        last_name=self.cart_results[0][2]
        self.result_window=QWidget()
        self.label_user=QLabel()
        self.button_checkout=QPushButton("Check Out")
        self.button_checkout.clicked.connect(self.checkout_clicked)
        self.label_user.setText(first_name+" "+last_name)
        self.layout=QHBoxLayout()
        self.layout_vert=QVBoxLayout()
        self.layout.addStretch()
        self.layout.addWidget(self.label_user)
        self.layout.addWidget(self.button_checkout)
        self.layout.addStretch()
        self.layout_vert.addLayout(self.layout)
        self.layout_vert.addStretch()
        self.result_window.setLayout(self.layout_vert)
        self.scroll_area.setWidget(self.result_window)

    def checkout_clicked(self):
        search_query="""
            SELECT book.book_id,book.title,cart.amount,book.cost_price,book.stock
             FROM customer INNER JOIN cart on cart.user_name=customer.user_name
            INNER JOIN book on cart.book_id=book.book_id
            WHERE cart.user_name=%s
        """

        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")
        cursor=db.cursor()
        user_name=self.cart_results[0][0]
        cursor.execute(search_query,(user_name))

        self.cart_results_details=list(cursor.fetchall())
        self.getWindow()
        self.main_check_out_window=QWidget()
        self.main_check_out_window_layout=QVBoxLayout()
        self.process_button=QPushButton("Process")
        self.process_button.clicked.connect(self.process_clicked)
        self.amount_label=QLabel()
        total=0
        for res in self.cart_results_details:
            total+=(res[2]*res[3])
        self.amount_label.setText(str(total))
        self.process_layout=QHBoxLayout()
        self.process_layout.addStretch()
        self.process_layout.addWidget(self.amount_label)
        self.process_layout.addWidget(self.process_button)
        self.process_layout.addStretch()
        self.main_check_out_window_layout.addWidget(self.checkout_window)
        self.main_check_out_window_layout.addLayout(self.process_layout)
        self.main_check_out_window.setLayout(self.main_check_out_window_layout)
        self.main_check_out_window.setStyleSheet(sheet)

        self.main_check_out_window.show()
    def getWindow(self):
        self.checkout_window=QWidget()
        self.checkout_layout=QVBoxLayout()
        self.label_widget=QHBoxLayout()
        self.label_widget_id=QVBoxLayout()
        self.label_widget_title=QVBoxLayout()
        self.label_widget_amount=QVBoxLayout()
        self.label_widget_price=QVBoxLayout()
        self.label_widget_id.addWidget(QLabel("Book ID"))
        self.label_widget_title.addWidget(QLabel("Title"))
        self.label_widget_amount.addWidget(QLabel("Amount"))
        self.label_widget_price.addWidget(QLabel("Price"))

        for res in self.cart_results_details:
            #text=str(res[0])+" "+ res[1]+" "+str(res[2])+" "+ str(res[3])
            self.label_widget_id.addWidget(QLabel(str(res[0])))
            self.label_widget_title.addWidget(QLabel(str(res[1])))
            self.label_widget_amount.addWidget(QLabel(str(res[2])))
            self.label_widget_price.addWidget(QLabel(str(res[3])))

        self.label_widget.addStretch()
        self.label_widget.addLayout(self.label_widget_id)
        self.label_widget.addLayout(self.label_widget_title)
        self.label_widget.addLayout(self.label_widget_amount)
        self.label_widget.addLayout(self.label_widget_price)
        self.label_widget.addStretch()
        self.checkout_layout.addStretch()
        self.checkout_layout.addLayout(self.label_widget)
        self.checkout_layout.addStretch()
        self.checkout_window.setLayout(self.checkout_layout)
        self.checkout_window.setStyleSheet(sheet)

    def process_clicked(self):
        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")
        cursor=db.cursor()

        update_inventory_query="""
            UPDATE book SET stock=%s
            WHERE book_id=%s
        """
        user_name=self.cart_results[0][0]
        for res in self.cart_results_details:
            cursor.execute(update_inventory_query,(res[4]-res[2],res[0]))
        delete_cart_query="""
            DELETE FROM cart WHERE user_name=%s

        """

        cursor.execute(delete_cart_query,(user_name))
        db.commit()

        self.widget_message=getMessageWindow("Processed Successfully")
        self.widget_message.show()
        self.main_check_out_window.close()









def get_process_order_widget():
    return ProcessOrder()