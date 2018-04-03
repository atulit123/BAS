from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import pandas as pd
import string
import matplotlib.pyplot as plt
from book_details import get_show_details_widget
from stylesheets import *
import sys
with open('stylesheet.txt','r') as f:
    sheet=f.read()




class qWindow(QWidget):
    def __init__(self, parent=None):
        super(qWindow, self).__init__(parent)
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
        #self.wrap_layout.addWidget(self.main_window)

    def topUI(self):
        self.top_window = QWidget()
        self.top_window.setObjectName("topwindow")
        self.top_window.setMinimumHeight(100)
        self.search_box=QLineEdit()
        self.search_box.setAlignment(Qt.AlignLeft)
        self.search_box.setFont(QFont("Arial",20))
        self.button_search=QPushButton("Search")
        self.button_search.setMaximumWidth(200)
        self.button_search.clicked.connect(self.search_clicked)
        self.button_login=QPushButton("Login")
        self.button_login.setMaximumWidth(200)
        #self.button_compare.clicked.connect(self.compare_clicked)
        self.button_signup=QPushButton("Sign up")
        self.button_signup.setMaximumWidth(200)
        #self.button_compare.clicked.connect(self.compare_clicked)
        self.top_window_layout=QHBoxLayout()
        self.top_window_layout.addStretch()
        self.top_window_layout.addWidget(self.search_box)
        self.top_window_layout.addWidget(self.button_search)
        self.top_window_layout.addWidget(self.button_login)
        self.top_window_layout.addWidget(self.button_signup)
        self.top_window_layout.addStretch()
        self.top_window.setLayout(self.top_window_layout)


    def details_clicked(self,book_id):
        win=get_show_details_widget()
        self.wins=win
        win.show()

    def search_clicked(self):
        #self.main_window_layout=QVBoxLayout()
        for i in reversed(range(self.main_window_layout.count())):
            widgetToRemove=self.main_window_layout.itemAt((i)).widget()
            self.main_window_layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
        query=str(self.search_box.text())
        book_result=self.qSearchBookResult("sorce_stone.jpg",query)
        book_result1=self.qSearchBookResult("sorce_stone.jpg",query)
        book_result2=self.qSearchBookResult("sorce_stone.jpg",query)
        book_result3=self.qSearchBookResult("sorce_stone.jpg",query)
        book_result4=self.qSearchBookResult("sorce_stone.jpg",query)
        book_result5=self.qSearchBookResult("sorce_stone.jpg",query)

        self.main_window_layout.addWidget(book_result)
        self.main_window_layout.addWidget(book_result1)
        self.main_window_layout.addWidget(book_result2)
        self.main_window_layout.addWidget(book_result3)
        self.main_window_layout.addWidget(book_result4)
        self.main_window_layout.addStretch()
        self.main_window.setLayout(self.main_window_layout)


    def qSearchBookResult(self,book_path,book_title,book_id=None):
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
        details_button=QPushButton("See Details")
        details_button.clicked.connect(self.details_clicked)
        book_result_layout.addWidget(book_image)
        #book_result_layout.addStretch()
        book_result_layout.addWidget(book_name)

        book_result_layout.addWidget(details_button)
        book_result_layout.addStretch()
        book_result.setLayout(book_result_layout)
        book_result.setStyleSheet(book_result_stylesheet)
        return book_result


    def mainUI(self):
        self.scroll_area=QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.main_window = QWidget()
       # self.main_window.setMinimumHeight(500)
        #self.main_window.setMinimumWidth(1000)
        self.main_window_layout=QVBoxLayout()
        #self.main_leftUI()
        #self.main_rightUI()


        #self.main_window_layout.addWidget(book_result)
        self.main_window.setLayout(self.main_window_layout)
        self.scroll_area.setWidget(self.main_window)
        #self.main_window.setStyleSheet("*{background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #8bf192, stop: 1 #41c34a);}")



   








app = QApplication(sys.argv)
wind = qWindow()
wind.setMinimumHeight(500)
wind.setMinimumWidth(1000)
wind.show()
sys.exit(app.exec_())
