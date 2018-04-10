from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import MySQLdb
import string
from stylesheets import *


class Message_widget(QWidget):
    def __init__(self, parent=None):
        super(Message_widget, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)

        self.wrap_layout.addStretch()
        self.label=QLabel()
        self.label.setWordWrap(True)
        self.button=QPushButton("Ok")
        self.button.setMaximumWidth(150)
        self.button.clicked.connect(self.close)
        #self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(signup_stylesheet)
        self.h_layout=QHBoxLayout()
        self.h_layout.addStretch()
        self.h_layout.addWidget(self.label)
        self.h_layout.addStretch()
        #self.wrap_layout.addWidget(self.main_window)
        self.h_layout1=QHBoxLayout()
        self.h_layout1.addStretch()
        self.h_layout1.addWidget(self.button)
        self.h_layout1.addStretch()
        self.setFixedSize(200,200)
        self.wrap_layout.addStretch()
        self.wrap_layout.addLayout(self.h_layout)
        self.wrap_layout.addLayout(self.h_layout1)
        self.wrap_layout.addStretch()

       # self.setMinimumHeight(500)


        self.setLayout(self.wrap_layout)




def getMessageWindow(text):
    widget=Message_widget()
    widget.label.setText(text)
    return widget





