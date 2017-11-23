# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialoghelp.ui'
#
# Created: Tue Nov 21 19:21:24 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogHelpShortcut(object):
    def setupUi(self, DialogHelpShortcut):
        DialogHelpShortcut.setObjectName("DialogHelpShortcut")
        DialogHelpShortcut.resize(240, 320)
        self.label = QtWidgets.QLabel(DialogHelpShortcut)
        self.label.setGeometry(QtCore.QRect(100, 30, 54, 12))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(DialogHelpShortcut)
        self.frame.setGeometry(QtCore.QRect(40, 60, 161, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 105, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 105, 61, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(DialogHelpShortcut)
        QtCore.QMetaObject.connectSlotsByName(DialogHelpShortcut)

    def retranslateUi(self, DialogHelpShortcut):
        _translate = QtCore.QCoreApplication.translate
        DialogHelpShortcut.setWindowTitle(_translate("DialogHelpShortcut", "Dialog"))
        self.label.setText(_translate("DialogHelpShortcut", "快捷键"))
        self.label_4.setText(_translate("DialogHelpShortcut", "双清    : ctrl + ~"))
        self.label_2.setText(_translate("DialogHelpShortcut", "清输出框: ctrl + 1"))
        self.label_3.setText(_translate("DialogHelpShortcut", "清输入框: ctrl + 2"))
        self.label_5.setText(_translate("DialogHelpShortcut", "发送    :"))
        self.label_6.setText(_translate("DialogHelpShortcut", "ctrl +回车"))

