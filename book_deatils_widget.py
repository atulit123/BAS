from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import MySQLdb
import string
from stylesheets import *
from Message_widget import *

import sys
with open('stylesheet.txt','r') as f:
    sheet=f.read()

class BookDetailsWindow(QWidget):
    def __init__(self, parent=None):
        super(BookDetailsWindow, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.book_details=None
        self.login_info=None
    def mainUI(self):
        self.main_layout=QHBoxLayout()
        self.image_label=QLabel()
        self.image_label.setPixmap(QPixmap(self.book_details[-1]))
        self.main_right_layout=QVBoxLayout()
        self.label_details1=QLabel("Title:"+str(self.book_details[2]))
        self.label_details2=QLabel("ISBN:"+str(self.book_details[1]))
        self.label_details3=QLabel("Genre:"+str(self.book_details[7]))
        self.label_details4=QLabel("Authors:"+str(self.book_details[3]))
        self.label_details5=QLabel("Price:"+str(self.book_details[5]))
        self.label_details6=QLabel("Available:"+str(self.book_details[6]))
        self.main_right_layout.addStretch()
        self.main_right_layout.addWidget(self.label_details1)
        self.main_right_layout.addWidget(self.label_details2)
        self.main_right_layout.addWidget(self.label_details3)
        self.main_right_layout.addWidget(self.label_details4)
        self.main_right_layout.addWidget(self.label_details5)
        self.main_right_layout.addWidget(self.label_details6)
        self.main_right_layout.addStretch()
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addLayout(self.main_right_layout)
        self.main_layout.addStretch()
    def bottomUI(self):
        self.bottom_layout=QHBoxLayout()
        self.edit_box=QLineEdit()
        self.edit_box.setValidator(QIntValidator(1,int(self.book_details[6]),self))
        self.button_add_cart=QPushButton("Add")
        self.button_add_cart.clicked.connect(self.add_cart_clicked)
        self.bottom_layout.addStretch()
        self.bottom_layout.addWidget(self.edit_box)
        self.bottom_layout.addWidget(self.button_add_cart)
        self.bottom_layout.addStretch()
    def makeUI(self):
        self.wrap_layout.addStretch()
        self.wrap_layout.addLayout(self.main_layout)
        self.wrap_layout.addLayout(self.bottom_layout)
        self.wrap_layout.addStretch()
        self.setLayout(self.wrap_layout)
        self.setStyleSheet(sheet)
    def add_cart_clicked(self):
        if not self.login_info:
            self.widget_message=getMessageWindow("Login First")
            self.widget_message.show()
            return None

        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")

        cursor = db.cursor()
        insert_cart="""
        INSERT INTO cart (user_name,book_id,amount
        )
        VALUES (%s,%s,%s)
        """

        user_name=self.login_info[0][0]
        book_id=self.book_details[0]
        amount=self.edit_box.text()
        if len(amount)==0:
            self.widget_message=getMessageWindow("Select a valid amount")
            self.widget_message.show()

        search_query="""
            SELECT * FROM cart WHERE user_name=%s AND book_id=%s
        """
        cursor.execute(search_query,(user_name,book_id))
        amount=int(amount)
        if len(list(cursor.fetchall()))>0:
            update_query="""
                UPDATE cart
                SET amount=%s
                WHERE user_name=%s and book_id=%s
            """
            cursor.execute(update_query,(amount,user_name,book_id))
            self.widget_message=getMessageWindow("Updated Successfully")
            self.widget_message.show()
        else:
            cursor.execute(insert_cart,(user_name,book_id,amount))
            self.widget_message=getMessageWindow("Added Successfully")
            self.widget_message.show()
        db.commit()




def get_show_details_widget(results,login_info):
    window=BookDetailsWindow()
    window.book_details=results
    window.login_info=login_info
    print login_info
    print results
    window.mainUI()
    window.bottomUI()
    window.makeUI()
    return window