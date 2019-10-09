# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton_addition = QtWidgets.QPushButton(Dialog)
        self.pushButton_addition.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.pushButton_addition.setObjectName("pushButton_addition")
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setGeometry(QtCore.QRect(50, 210, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.lineEdit_firstNum = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_firstNum.setGeometry(QtCore.QRect(240, 40, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_firstNum.setFont(font)
        self.lineEdit_firstNum.setObjectName("lineEdit_firstNum")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_secondNum = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_secondNum.setGeometry(QtCore.QRect(240, 70, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_secondNum.setFont(font)
        self.lineEdit_secondNum.setObjectName("lineEdit_secondNum")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_addition.setText(_translate("Dialog", "ADD"))
        self.label_result.setText(_translate("Dialog", "Result Status"))
        self.label_2.setText(_translate("Dialog", "Enter 1st Number"))
        self.label_3.setText(_translate("Dialog", "Enter 2nd Number"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
