from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import MySQLdb
import string
import sys
from stylesheets import *
from Message_widget import *


class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.wrap_layout = QHBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.parent=None
        self.mainUI()

        self.wrap_layout.addStretch()
        self.wrap_layout.addWidget(self.label_widget)
        self.wrap_layout.addWidget(self.form_widget)
        self.wrap_layout.addStretch()
        self.wrap_layout2=QVBoxLayout()
        self.wrap_layout2.addStretch()
        self.wrap_layout2.addLayout(self.wrap_layout)
        self.login_button_layout=QHBoxLayout()
        self.login_button_layout.addStretch()
        self.login_button=QPushButton("Login")
        self.login_button.clicked.connect(self.login_clicked)
        self.login_button_layout.addWidget(self.login_button)
        self.login_button_layout.addStretch()
        self.login_button.setMinimumWidth(200)
        self.login_button.setMaximumWidth(200)
        self.wrap_layout2.addLayout(self.login_button_layout)
        self.wrap_layout2.addStretch()
        self.setLayout(self.wrap_layout2)
        #self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(signup_stylesheet)
        #self.wrap_layout.addWidget(self.main_window)
        self.setMinimumHeight(300)
        self.setMinimumWidth(300)
       # self.setMinimumHeight(500)

    def mainUI(self):
        self.label_widget=QWidget()
        self.label_layout=QVBoxLayout()
        self.label_layout.addWidget(QLabel("User Name"))
        self.label_layout.addWidget(QLabel("Password"))
        self.label_widget.setLayout(self.label_layout)

        self.form_widget=QWidget()
        self.form_layout=QVBoxLayout()
        self.edit_box_widget=[]
        for i in range(2):
            wid=QLineEdit()
            self.form_layout.addWidget(wid)
            self.edit_box_widget.append(wid)
        self.edit_box_widget[1].setEchoMode(QLineEdit.Password)

        self.form_widget.setLayout(self.form_layout)

    def login_clicked(self):
        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")

        cursor = db.cursor()
        user_name=self.edit_box_widget[0].text()
        password=self.edit_box_widget[1].text()

        if len(user_name)==0 or len(password)==0:
            self.widget_message=getMessageWindow("Type Valid input")
            self.widget_message.show()
            return None

        search_query="""
            SELECT * FROM customer WHERE user_name=%s
            AND password=%s
        """
        cursor.execute(search_query,(user_name,password))
        results=list(cursor.fetchall())
        if len(results)==0:
            self.widget_message=getMessageWindow("Wrong Username or password")
            self.widget_message.show()
        else:
            self.widget_message=getMessageWindow("Successfull")
            self.parent.login_info=results
            self.parent.topUI_login()
            self.widget_message.show()
            self.close()


def getLoginWindow(window):
    window.login_window=LoginWindow()
    window.login_window.parent=window
    window.login_window.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    wind = LoginWindow()

    wind.show()
    sys.exit(app.exec_())



