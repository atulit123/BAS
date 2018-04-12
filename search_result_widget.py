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
from update_book_widget import *
import sys
with open('stylesheet.txt','r') as f:
    sheet=f.read()




class SearchResult(QWidget):
    def __init__(self, parent=None):
        super(SearchResult, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)



        #self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(sheet)
        self.compare_list=[]
        self.login_info=None
        self.login_window=None
        #self.topUI_login()
        #self.wrap_layout.addWidget(self.main_window)

    def makeUI(self,query):
        self.book_result_wid=[]
        db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="atulit",db="bas")

        cursor = db.cursor()

        search_book="""
        SELECT * FROM book WHERE UPPER(title) LIKE UPPER ('%%%s%%') or isbn like '%%%s%%'

        or upper(author) like upper('%%%s%%')

        """

        query="%%".join(query.split())
        cursor.execute(search_book%(query,query,query))

        self.results=list(cursor.fetchall())

        #commit change
        print "done"
        db.commit()


        ## Close the connection
        db.close()

        for i in range(len(self.results)):
            res=self.results[i]
            self.book_result_wid.append(self.qSearchBookResult(res[-1],res[2],i))

        for wind_ in self.book_result_wid:
            self.wrap_layout.addWidget(wind_)
        self.wrap_layout.addStretch()
        self.setLayout(self.wrap_layout)
    def qSearchBookResult(self,book_path,book_title,book_ind):
        print book_ind
        book_result=QWidget()
        book_result.setMaximumHeight(300)
        book_result.setMinimumHeight(300)
        book_result_layout=QHBoxLayout()
        book_image=QLabel()
        book_image.setPixmap(QPixmap(book_path))
        book_image.setMaximumHeight(200)
        book_image.setMaximumWidth(200)
        book_name=QLabel()
        book_name.setMaximumHeight(30)
        book_name.setText(book_title)
        update_button=QPushButton("Update")
        update_button.clicked.connect(lambda state, x=book_ind:self.update_clicked(x))
        book_result_layout.addWidget(book_image)
        #book_result_layout.addStretch()
        book_result_layout.addWidget(book_name)

        book_result_layout.addWidget(update_button)
        book_result_layout.addStretch()
        book_result.setLayout(book_result_layout)
        book_result.setStyleSheet(book_result_stylesheet)
        return book_result

    def update_clicked(self,ind):
        self.update_window=get_update_book_widget(self.results[ind])
        self.update_window.show()

def get_search_result_widget(query):
    #query="harry"
    wid=SearchResult()
    wid.makeUI(query)
    return wid


