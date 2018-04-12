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
import sys
with open('stylesheet.txt','r') as f:
    sheet=f.read()




class AddBook(QWidget):
    def __init__(self, parent=None):
        super(AddBook, self).__init__(parent)
        self.wrap_layout = QHBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.mainUI()
        self.wrap_layout2=QVBoxLayout()
        self.add_button=QPushButton("Add")
        self.button_layout=QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addStretch()
        self.add_button.clicked.connect(self.add_button_click)

        self.wrap_layout.addStretch()
        self.wrap_layout.addWidget(self.label_widget)
        self.wrap_layout.addWidget(self.form_widget)
        self.wrap_layout.addStretch()
        self.wrap_layout2.addLayout(self.wrap_layout)
        self.wrap_layout2.addLayout(self.button_layout)
        #self.wrap_layout.addLayout(self.button_layout)
        self.wrap_layout2.addStretch()
        #self.wrap_layout.addWidget(self.main_window)
        #self.wrap_layout.addStretch()
        self.setLayout(self.wrap_layout2)
        #self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(sheet)
        self.compare_list=[]
        self.login_info=None
        self.login_window=None
        #self.topUI_login()
        #self.wrap_layout.addWidget(self.main_window)
        self.setMinimumHeight(500)
        self.setMinimumWidth(1000)
    def mainUI(self):
        self.label_widget=QWidget()
        self.label_layout=QVBoxLayout()
        #self.label_layout.addStretch()
        self.label_layout.addWidget(QLabel("ISBN"))
        self.label_layout.addWidget(QLabel("Title"))
        self.label_layout.addWidget(QLabel("Genre"))
        self.label_layout.addWidget(QLabel("Author"))

        self.label_layout.addWidget(QLabel("MRP"))
        self.label_layout.addWidget(QLabel("Cost Price"))
        self.label_layout.addWidget(QLabel("Quantity"))
        self.label_layout.addWidget(QLabel("Path"))
        self.label_widget.setLayout(self.label_layout)
        #self.label_layout.addStretch()
        self.form_widget=QWidget()
        self.form_layout=QVBoxLayout()
        #self.form_layout.addStretch()
        self.edit_box_widget=[]
        for i in range(8):
            wid=QLineEdit()
            wid.setMinimumWidth(400)
            self.form_layout.addWidget(wid)
            self.edit_box_widget.append(wid)
        #self.edit_box_widget[5].setEchoMode(QLineEdit.Password)
        #self.form_layout.addStretch()
        self.form_widget.setLayout(self.form_layout)

    def add_button_click(self):
        valid=True
        for wid in self.edit_box_widget:
            if len(wid.text())==0:
                valid=False
        if not valid:
            self.widget_message=getMessageWindow("Type Valid Input")
            self.widget_message.show()
            return None
        insert_book="""
        INSERT INTO book (isbn,author,title,book_id,image_path,mrp,cost_price,genre,stock)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        isbn=self.edit_box_widget[0].text()
        title=self.edit_box_widget[1].text()
        genre=self.edit_box_widget[2].text()
        author=self.edit_box_widget[3].text()
        mrp=float(self.edit_box_widget[4].text())
        cost_price=float(self.edit_box_widget[5].text())
        quantity=int(self.edit_box_widget[6].text())
        path=self.edit_box_widget[7].text()
        db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="atulit",db="bas")

        cursor = db.cursor()
        ##creating table book
        id_query="""
                    SELECT MAX(book_id) FROM book
                """
        cursor.execute(id_query)
        book_id=int(list(cursor.fetchall())[0][0])+1
        cursor.execute(insert_book,(isbn,author,title,book_id,path,mrp,cost_price,genre,quantity))
        db.commit()
        self.widget_message=getMessageWindow("Added Sucessfully")
        self.widget_message.show()








def get_add_book_widget():
    wind=AddBook()
    return wind


if __name__=="__main__":
    app = QApplication(sys.argv)
    wind = AddBook()

    wind.show()
    sys.exit(app.exec_())