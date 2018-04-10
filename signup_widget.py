from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import MySQLdb
import string
from stylesheets import *
from Message_widget import *

import sys
with open('stylesheet.txt','r') as f:
    sheet=f.read()

class SignupWindow(QWidget):
    def __init__(self, parent=None):
        super(SignupWindow, self).__init__(parent)
        self.wrap_layout = QHBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.mainUI()

        self.wrap_layout.addStretch()
        self.wrap_layout.addWidget(self.label_widget)
        self.wrap_layout.addWidget(self.form_widget)
        self.wrap_layout.addStretch()
        self.wrap_layout2=QVBoxLayout()
        self.wrap_layout2.addStretch()
        self.wrap_layout2.addLayout(self.wrap_layout)
        self.signup_button_layout=QHBoxLayout()
        self.signup_button_layout.addStretch()
        self.signup_button=QPushButton("Signup")
        self.signup_button.clicked.connect(self.signup_clicked)
        self.signup_button_layout.addWidget(self.signup_button)
        self.signup_button_layout.addStretch()
        self.signup_button.setMinimumWidth(200)
        self.signup_button.setMaximumWidth(200)
        self.wrap_layout2.addLayout(self.signup_button_layout)
        self.wrap_layout2.addStretch()
        self.setLayout(self.wrap_layout2)
        #self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(signup_stylesheet)
        #self.wrap_layout.addWidget(self.main_window)
        self.setMinimumHeight(300)
        self.setMinimumWidth(800)
       # self.setMinimumHeight(500)

    def mainUI(self):
        self.label_widget=QWidget()
        self.label_layout=QVBoxLayout()
        self.label_layout.addWidget(QLabel("First Name"))
        self.label_layout.addWidget(QLabel("Last Name"))
        self.label_layout.addWidget(QLabel("Email"))
        self.label_layout.addWidget(QLabel("User Name"))
        self.label_layout.addWidget(QLabel("Phone"))
        self.label_layout.addWidget(QLabel("Password"))
        self.label_layout.addWidget(QLabel("Address"))
        self.label_widget.setLayout(self.label_layout)

        self.form_widget=QWidget()
        self.form_layout=QVBoxLayout()
        self.edit_box_widget=[]
        for i in range(7):
            wid=QLineEdit()
            self.form_layout.addWidget(wid)
            self.edit_box_widget.append(wid)

        self.form_widget.setLayout(self.form_layout)

    def signup_clicked(self):
        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")

        cursor = db.cursor()
        ##creating table book
        insert_customer="""
        INSERT INTO customer (user_name,first_name,last_name,email,phone,password,address
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        search_query="""
            SELECT * FROM customer WHERE user_name=%s
        """
        user_name=self.edit_box_widget[3].text()
        first_name=self.edit_box_widget[0].text()
        last_name=self.edit_box_widget[1].text()
        email=self.edit_box_widget[2].text()
        phone=self.edit_box_widget[4].text()
        password=self.edit_box_widget[5].text()
        address=self.edit_box_widget[6].text()
        cursor.execute(search_query,str(self.edit_box_widget[3].text()))
        lst=list(cursor.fetchall())
        if len(lst)==0:
            print "correct info"
            cursor.execute(insert_customer,
                           (user_name,first_name,last_name,email,phone,password,address)
                           )
            db.commit()
            self.widget_message=getMessageWindow("Successfull")
            self.widget_message.show()
            self.close()
        else:
            self.widget_message=getMessageWindow("Username already exists choose another")
            self.widget_message.show()





