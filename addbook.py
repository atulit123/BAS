# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addbook.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(506, 436)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(10)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.iSBNLabel = QtGui.QLabel(Form)
        self.iSBNLabel.setObjectName(_fromUtf8("iSBNLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.iSBNLabel)
        self.iSBNLineEdit = QtGui.QLineEdit(Form)
        self.iSBNLineEdit.setObjectName(_fromUtf8("iSBNLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.iSBNLineEdit)
        self.bookNameLabel = QtGui.QLabel(Form)
        self.bookNameLabel.setObjectName(_fromUtf8("bookNameLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.bookNameLabel)
        self.bookNameLineEdit = QtGui.QLineEdit(Form)
        self.bookNameLineEdit.setObjectName(_fromUtf8("bookNameLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.bookNameLineEdit)
        self.genreLabel = QtGui.QLabel(Form)
        self.genreLabel.setObjectName(_fromUtf8("genreLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.genreLabel)
        self.genreLineEdit = QtGui.QLineEdit(Form)
        self.genreLineEdit.setObjectName(_fromUtf8("genreLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.genreLineEdit)
        self.authorLabel = QtGui.QLabel(Form)
        self.authorLabel.setObjectName(_fromUtf8("authorLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.authorLabel)
        self.authorLineEdit = QtGui.QLineEdit(Form)
        self.authorLineEdit.setObjectName(_fromUtf8("authorLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.authorLineEdit)
        self.publicationLabel = QtGui.QLabel(Form)
        self.publicationLabel.setObjectName(_fromUtf8("publicationLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.publicationLabel)
        self.publicationLineEdit = QtGui.QLineEdit(Form)
        self.publicationLineEdit.setObjectName(_fromUtf8("publicationLineEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.publicationLineEdit)
        self.priceLabel = QtGui.QLabel(Form)
        self.priceLabel.setObjectName(_fromUtf8("priceLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.priceLabel)
        self.priceLineEdit = QtGui.QLineEdit(Form)
        self.priceLineEdit.setObjectName(_fromUtf8("priceLineEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.priceLineEdit)
        self.quantityLabel = QtGui.QLabel(Form)
        self.quantityLabel.setObjectName(_fromUtf8("quantityLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.quantityLabel)
        self.quantityLineEdit = QtGui.QLineEdit(Form)
        self.quantityLineEdit.setObjectName(_fromUtf8("quantityLineEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.quantityLineEdit)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(20, 10, 20, 10)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setMaximumSize(QtCore.QSize(500, 30))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.iSBNLabel.setText(_translate("Form", "ISBN", None))
        self.bookNameLabel.setText(_translate("Form", "Book Name", None))
        self.genreLabel.setText(_translate("Form", "Genre", None))
        self.authorLabel.setText(_translate("Form", "Author", None))
        self.publicationLabel.setText(_translate("Form", "Publication", None))
        self.priceLabel.setText(_translate("Form", "Price", None))
        self.quantityLabel.setText(_translate("Form", "Quantity", None))
        self.pushButton_2.setText(_translate("Form", "Exit", None))
        self.pushButton.setText(_translate("Form", "Submit", None))
        self.label_8.setText(_translate("Form", "Add Book", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

