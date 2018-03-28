# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialogAOP.ui'
#
# Created: Wed Mar 28 20:20:11 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAOP(object):
    def setupUi(self, DialogAOP):
        DialogAOP.setObjectName("DialogAOP")
        DialogAOP.resize(739, 325)
        self.pushButtonSave = QtWidgets.QPushButton(DialogAOP)
        self.pushButtonSave.setGeometry(QtCore.QRect(270, 288, 161, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.tabWidget = QtWidgets.QTabWidget(DialogAOP)
        self.tabWidget.setGeometry(QtCore.QRect(3, 2, 721, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEditSend = QtWidgets.QTextEdit(self.tab)
        self.textEditSend.setGeometry(QtCore.QRect(7, 8, 701, 231))
        self.textEditSend.setObjectName("textEditSend")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEditRec = QtWidgets.QTextEdit(self.tab_2)
        self.textEditRec.setGeometry(QtCore.QRect(7, 8, 701, 231))
        self.textEditRec.setObjectName("textEditRec")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(DialogAOP)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DialogAOP)

    def retranslateUi(self, DialogAOP):
        _translate = QtCore.QCoreApplication.translate
        DialogAOP.setWindowTitle(_translate("DialogAOP", "Dialog"))
        self.pushButtonSave.setText(_translate("DialogAOP", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DialogAOP", "PreSend"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DialogAOP", "PostRecieve"))

