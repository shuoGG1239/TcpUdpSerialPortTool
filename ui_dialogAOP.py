# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialogAOP.ui'
#
# Created: Tue Dec  5 20:01:23 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAOP(object):
    def setupUi(self, DialogAOP):
        DialogAOP.setObjectName("DialogAOP")
        DialogAOP.resize(609, 365)
        self.textEditSend = QtWidgets.QTextEdit(DialogAOP)
        self.textEditSend.setGeometry(QtCore.QRect(10, 30, 291, 291))
        self.textEditSend.setObjectName("textEditSend")
        self.textEditRec = QtWidgets.QTextEdit(DialogAOP)
        self.textEditRec.setGeometry(QtCore.QRect(307, 30, 291, 291))
        self.textEditRec.setObjectName("textEditRec")
        self.label = QtWidgets.QLabel(DialogAOP)
        self.label.setGeometry(QtCore.QRect(12, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogAOP)
        self.label_2.setGeometry(QtCore.QRect(309, 10, 54, 12))
        self.label_2.setObjectName("label_2")
        self.pushButtonSave = QtWidgets.QPushButton(DialogAOP)
        self.pushButtonSave.setGeometry(QtCore.QRect(224, 330, 161, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")

        self.retranslateUi(DialogAOP)
        QtCore.QMetaObject.connectSlotsByName(DialogAOP)

    def retranslateUi(self, DialogAOP):
        _translate = QtCore.QCoreApplication.translate
        DialogAOP.setWindowTitle(_translate("DialogAOP", "Dialog"))
        self.label.setText(_translate("DialogAOP", "Send:"))
        self.label_2.setText(_translate("DialogAOP", "Receive:"))
        self.pushButtonSave.setText(_translate("DialogAOP", "Save"))

