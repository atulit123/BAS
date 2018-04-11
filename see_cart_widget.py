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
import sys
with open('stylesheet.txt','r') as f:
    sheet=f.read()




class SeeCart(QWidget):
    def __init__(self, parent=None):
        super(SeeCart, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.login_info=None
        self.setLayout(self.wrap_layout)
        #self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(sheet)
        self.edit_list=[]
        self.login_info=None
        self.login_window=None
        self.layout_list=None
        self.scroll_area=QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.label=QLabel("Your cart")
        self.wrap_layout.addWidget(self.label)
        self.wrap_layout.addWidget(self.scroll_area)
        self.setLayout(self.wrap_layout)
        self.setStyleSheet(sheet)
        self.setMinimumHeight(500)
        self.setMinimumWidth(1000)
        #self.topUI_login()
        #self.wrap_layout.addWidget(self.main_window)

    def make_UI(self):
        self.edit_list=[]
        if not self.login_info:
            self.widget_message=getMessageWindow("Login First")
            self.widget_message.show()
            return None
        self.layout_list=[]
        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")
        cursor=db.cursor()
        search_query="""
            SELECT * FROM cart INNER JOIN book on cart.book_id=book.book_id
            WHERE cart.user_name=%s
        """


        user_name=self.login_info[0][0]
        #user_name="atulit123"
        cursor.execute(search_query,(user_name))
        self.cart_results=list(cursor.fetchall())
        if len(self.cart_results)==0:
            self.label.setText("Your cart is empty")


        self.main_window = QWidget()
        self.main_window_layout=QVBoxLayout()
        for i in range(len(self.cart_results)):
            info=self.cart_results[i]
            self.main_window_layout.addLayout(self.create_layout(info,i))
        self.main_window_layout.addStretch()



       # self.main_window.setMinimumHeight(500)
        #self.main_window.setMinimumWidth(1000)

        #self.main_leftUI()
        #self.main_rightUI()


        #self.main_window_layout.addWidget(book_result)
        self.main_window.setLayout(self.main_window_layout)
        self.scroll_area.setWidget(self.main_window)


    def create_layout(self,info,ind):
        layout=QVBoxLayout()
        layout.addStretch()
        layout.addLayout(self.mainUI(info,ind))
        layout.addLayout(self.bottomUI(info,ind))
        layout.addStretch()
        return layout

    def mainUI(self,info,ind):
        main_layout=QHBoxLayout()
        image_label=QLabel()
        image_label.setPixmap(QPixmap(info[-1]))
        main_right_layout=QVBoxLayout()
        label_details1=QLabel("Title:"+str(info[5]))
        label_details2=QLabel("ISBN:"+str(info[4]))
        label_details3=QLabel("Genre:"+str(info[10]))
        label_details4=QLabel("Authors:"+str(info[6]))
        label_details5=QLabel("Price:"+str(info[8]))
        label_details6=QLabel("Available:"+str(info[9]))
        label_details7=QLabel("Added:"+str(info[2]))

        main_right_layout.addStretch()
        main_right_layout.addWidget(label_details1)
        main_right_layout.addWidget(label_details2)
        main_right_layout.addWidget(label_details3)
        main_right_layout.addWidget(label_details4)
        main_right_layout.addWidget(label_details5)
        main_right_layout.addWidget(label_details6)
        main_right_layout.addWidget(label_details7)
        main_right_layout.addStretch()
        main_layout.addWidget(image_label)
        main_layout.addLayout(main_right_layout)
        main_layout.addStretch()
        return main_layout
    def bottomUI(self,info,ind):
        bottom_layout=QHBoxLayout()
        edit_box=QLineEdit()
        edit_box.setMaximumWidth(200)
        edit_box.setValidator(QIntValidator(1,int(info[9]),self))
        button_update=QPushButton("Update")
        button_delete=QPushButton("Delete")
        self.edit_list.append(edit_box)
        button_delete.clicked.connect(lambda state, x=ind:self.click_delete(x))
        button_update.clicked.connect(lambda state, x=ind:self.click_update(x))
        #self.button_add_cart.clicked.connect(self.add_cart_clicked)
        bottom_layout.addWidget(edit_box)
        bottom_layout.addWidget(button_update)
        bottom_layout.addWidget(button_delete)
        bottom_layout.addStretch()
        return bottom_layout

    def click_update(self,ind):
        print ind
        user_name=self.login_info[0][0]
        #user_name="atulit123"
        book_id=self.cart_results[ind][1]
        amount=int(self.edit_list[ind].text())
        update_query="""
                UPDATE cart
                SET amount=%s
                WHERE user_name=%s and book_id=%s
            """
        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")
        cursor = db.cursor()
        cursor.execute(update_query,(amount,user_name,book_id))
        db.commit()
        self.make_UI()
        self.widget_message=getMessageWindow("Updated Successfully")
        self.widget_message.show()

    def click_delete(self,ind):
        print ind
        user_name=self.login_info[0][0]
        #user_name="atulit123"
        book_id=self.cart_results[ind][1]
        delete_query="""
            DELETE FROM cart WHERE user_name=%s and book_id=%s
        """
        db = MySQLdb.connect(host="localhost",
                     user="root",
                             passwd="atulit",db="bas")
        cursor = db.cursor()
        cursor.execute(delete_query,(user_name,book_id))
        db.commit()
        self.make_UI()
        self.widget_message=getMessageWindow("Deleted Successfully")
        self.widget_message.show()





def get_see_cart_widget(login_info):
    #login_info=1
    widget=SeeCart()
    widget.login_info=login_info
    widget.make_UI()
    return widget

#app = QApplication(sys.argv)
#wind = get_see_cart_widget(None)
#wind.show()
#sys.exit(app.exec_())

