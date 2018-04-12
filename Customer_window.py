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




class qWindow(QWidget):
    def __init__(self, parent=None):
        super(qWindow, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.top_window = QWidget()
        self.top_window_layout=QHBoxLayout()
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
        print self.top_window_layout.count()
        for i in reversed(range(self.top_window_layout.count())):
            widgetToRemove=self.top_window_layout.itemAt((i))
            if widgetToRemove:
                widgetToRemove=widgetToRemove.widget()
                print widgetToRemove
                self.top_window_layout.removeWidget(widgetToRemove)
                if widgetToRemove:
                    widgetToRemove.setParent(None)
        self.top_window.setObjectName("topwindow")
        self.top_window.setMinimumHeight(100)
        self.search_box=QLineEdit()
        self.search_box.setAlignment(Qt.AlignLeft)
        self.search_box.setFont(QFont("Arial",20))
        self.search_box.setMinimumWidth(300)
        self.button_search=QPushButton("Search")
        self.button_search.setMaximumWidth(200)
        self.button_search.clicked.connect(self.search_clicked)
        self.button_login=QPushButton("Login")
        self.button_login.setMaximumWidth(200)
        self.button_login.clicked.connect(self.login_clicked)
        self.button_signup=QPushButton("Sign up")
        self.button_signup.setMaximumWidth(200)
        self.button_signup.clicked.connect(self.signup_clicked)

        self.top_window_layout.addStretch()
        self.top_window_layout.addWidget(self.search_box)
        self.top_window_layout.addWidget(self.button_search)
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
        self.search_box=QLineEdit()
        self.search_box.setMinimumWidth(300)
        self.search_box.setAlignment(Qt.AlignLeft)
        self.search_box.setFont(QFont("Arial",20))
        self.button_search=QPushButton("Search")
        self.button_see_cart=QPushButton("See Cart")
        self.button_logout=QPushButton("Log out")
        self.button_see_cart.clicked.connect(self.see_cart_clicked)
        self.button_search.setMaximumWidth(200)
        self.button_see_cart.setMaximumWidth(200)
        self.button_search.clicked.connect(self.search_clicked)
        self.button_logout.clicked.connect(self.click_logout)
        self.top_window_layout.addStretch()
        self.top_window_layout.addWidget(self.search_box)
        self.top_window_layout.addWidget(self.button_search)
        self.top_window_layout.addWidget(self.button_see_cart)
        self.top_window_layout.addWidget(self.button_logout)
        self.top_window_layout.addStretch()
        print self.login_info
        name=self.login_info[0][1]+" "+self.login_info[0][2]
        self.top_window_layout.addWidget(QLabel("Welcome "+name))


        self.top_window.setLayout(self.top_window_layout)

    def click_logout(self):
        self.login_info=None
        self.topUI()


    def see_cart_clicked(self):
        self.see_cart_widget=get_see_cart_widget(self.login_info)
        self.see_cart_widget.show()
    def login_clicked(self):
        #self.login_window=LoginWindow()
        #self.login_window.show()
        getLoginWindow(self,"customer")

    def signup_clicked(self):
        self.signup_window=SignupWindow()
        self.signup_window.table="customer"
        self.signup_window.show()

    def details_clicked(self,book_ind):
        print book_ind
        win=get_show_details_widget(self.results[book_ind],self.login_info)
        self.win_details=win
        win.show()

    def search_clicked(self):
        #self.main_window_layout=QVBoxLayout()
        query=str(self.search_box.text())
        if len(query)==0:
            self.widget_message=getMessageWindow("Type Something")
            self.widget_message.show()
            return None
        self.book_result_wid=[]
        for i in reversed(range(self.main_window_layout.count())):
            widgetToRemove=self.main_window_layout.itemAt((i)).widget()
            self.main_window_layout.removeWidget(widgetToRemove)
            if widgetToRemove:
                widgetToRemove.setParent(None)
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
            self.main_window_layout.addWidget(wind_)
        self.main_window_layout.addStretch()
        self.main_window.setLayout(self.main_window_layout)


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
        details_button=QPushButton("See Details")
        details_button.clicked.connect(lambda state, x=book_ind:self.details_clicked(x))
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
