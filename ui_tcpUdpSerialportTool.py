# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tcpUdpSerialportTool.ui'
#
# Created: Tue Jul 10 21:33:46 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TcpUdpComTool(object):
    def setupUi(self, TcpUdpComTool):
        TcpUdpComTool.setObjectName("TcpUdpComTool")
        TcpUdpComTool.resize(780, 645)
        TcpUdpComTool.setMinimumSize(QtCore.QSize(780, 645))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(TcpUdpComTool)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setContentsMargins(-1, -1, 13, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEditRec = QtWidgets.QPlainTextEdit(TcpUdpComTool)
        self.plainTextEditRec.setMinimumSize(QtCore.QSize(481, 261))
        self.plainTextEditRec.setObjectName("plainTextEditRec")
        self.verticalLayout_2.addWidget(self.plainTextEditRec)
        self.plainTextEditSend = QtWidgets.QPlainTextEdit(TcpUdpComTool)
        self.plainTextEditSend.setMinimumSize(QtCore.QSize(481, 171))
        self.plainTextEditSend.setObjectName("plainTextEditSend")
        self.verticalLayout_2.addWidget(self.plainTextEditSend)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frameStatus = QtWidgets.QFrame(TcpUdpComTool)
        self.frameStatus.setMinimumSize(QtCore.QSize(191, 21))
        self.frameStatus.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameStatus.setObjectName("frameStatus")
        self.labelStatusTag = QtWidgets.QLabel(self.frameStatus)
        self.labelStatusTag.setGeometry(QtCore.QRect(10, 5, 61, 21))
        self.labelStatusTag.setMinimumSize(QtCore.QSize(61, 21))
        self.labelStatusTag.setAutoFillBackground(False)
        self.labelStatusTag.setObjectName("labelStatusTag")
        self.labelStatus = QtWidgets.QLabel(self.frameStatus)
        self.labelStatus.setGeometry(QtCore.QRect(66, 5, 121, 21))
        self.labelStatus.setMinimumSize(QtCore.QSize(121, 21))
        self.labelStatus.setAutoFillBackground(False)
        self.labelStatus.setObjectName("labelStatus")
        self.horizontalLayout_2.addWidget(self.frameStatus)
        self.checkBoxHexRec = QtWidgets.QCheckBox(TcpUdpComTool)
        self.checkBoxHexRec.setMinimumSize(QtCore.QSize(91, 20))
        self.checkBoxHexRec.setObjectName("checkBoxHexRec")
        self.horizontalLayout_2.addWidget(self.checkBoxHexRec)
        self.toolButtonShortCut = QtWidgets.QToolButton(TcpUdpComTool)
        self.toolButtonShortCut.setMinimumSize(QtCore.QSize(71, 31))
        self.toolButtonShortCut.setAutoRaise(True)
        self.toolButtonShortCut.setObjectName("toolButtonShortCut")
        self.horizontalLayout_2.addWidget(self.toolButtonShortCut)
        self.toolButtonAOP = QtWidgets.QToolButton(TcpUdpComTool)
        self.toolButtonAOP.setMinimumSize(QtCore.QSize(71, 31))
        self.toolButtonAOP.setAutoRaise(True)
        self.toolButtonAOP.setObjectName("toolButtonAOP")
        self.horizontalLayout_2.addWidget(self.toolButtonAOP)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 12)
        self.verticalLayout_2.setStretch(1, 7)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBoxStyle = QtWidgets.QComboBox(TcpUdpComTool)
        self.comboBoxStyle.setMinimumSize(QtCore.QSize(141, 31))
        self.comboBoxStyle.setMaximumSize(QtCore.QSize(141, 31))
        self.comboBoxStyle.setObjectName("comboBoxStyle")
        self.verticalLayout.addWidget(self.comboBoxStyle)
        self.pushButtonStart = QtWidgets.QPushButton(TcpUdpComTool)
        self.pushButtonStart.setMinimumSize(QtCore.QSize(141, 31))
        self.pushButtonStart.setMaximumSize(QtCore.QSize(141, 31))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.verticalLayout.addWidget(self.pushButtonStart)
        self.comboBoxClientList = QtWidgets.QComboBox(TcpUdpComTool)
        self.comboBoxClientList.setMinimumSize(QtCore.QSize(141, 22))
        self.comboBoxClientList.setMaximumSize(QtCore.QSize(141, 22))
        self.comboBoxClientList.setObjectName("comboBoxClientList")
        self.verticalLayout.addWidget(self.comboBoxClientList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboComNum = QtWidgets.QComboBox(TcpUdpComTool)
        self.comboComNum.setMinimumSize(QtCore.QSize(65, 22))
        self.comboComNum.setMaximumSize(QtCore.QSize(65, 22))
        self.comboComNum.setObjectName("comboComNum")
        self.horizontalLayout.addWidget(self.comboComNum)
        self.comboBoxBaud = QtWidgets.QComboBox(TcpUdpComTool)
        self.comboBoxBaud.setMinimumSize(QtCore.QSize(65, 22))
        self.comboBoxBaud.setMaximumSize(QtCore.QSize(65, 22))
        self.comboBoxBaud.setObjectName("comboBoxBaud")
        self.horizontalLayout.addWidget(self.comboBoxBaud)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(TcpUdpComTool)
        self.groupBox.setMinimumSize(QtCore.QSize(141, 81))
        self.groupBox.setMaximumSize(QtCore.QSize(141, 81))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton16 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton16.setGeometry(QtCore.QRect(10, 4, 71, 21))
        self.radioButton16.setMinimumSize(QtCore.QSize(71, 21))
        self.radioButton16.setMaximumSize(QtCore.QSize(71, 21))
        self.radioButton16.setObjectName("radioButton16")
        self.radioButtonString = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonString.setGeometry(QtCore.QRect(73, 4, 61, 21))
        self.radioButtonString.setMinimumSize(QtCore.QSize(61, 21))
        self.radioButtonString.setMaximumSize(QtCore.QSize(61, 21))
        self.radioButtonString.setObjectName("radioButtonString")
        self.pushButtonSend = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonSend.setGeometry(QtCore.QRect(10, 30, 121, 41))
        self.pushButtonSend.setMinimumSize(QtCore.QSize(121, 41))
        self.pushButtonSend.setMaximumSize(QtCore.QSize(121, 41))
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.verticalLayout.addWidget(self.groupBox)
        self.pushButtonClearRec = QtWidgets.QPushButton(TcpUdpComTool)
        self.pushButtonClearRec.setMinimumSize(QtCore.QSize(121, 23))
        self.pushButtonClearRec.setMaximumSize(QtCore.QSize(141, 23))
        self.pushButtonClearRec.setObjectName("pushButtonClearRec")
        self.verticalLayout.addWidget(self.pushButtonClearRec)
        self.groupBoxLocal = QtWidgets.QGroupBox(TcpUdpComTool)
        self.groupBoxLocal.setMinimumSize(QtCore.QSize(141, 71))
        self.groupBoxLocal.setMaximumSize(QtCore.QSize(141, 71))
        self.groupBoxLocal.setFlat(False)
        self.groupBoxLocal.setObjectName("groupBoxLocal")
        self.lineEditPortLocal = QtWidgets.QLineEdit(self.groupBoxLocal)
        self.lineEditPortLocal.setGeometry(QtCore.QRect(50, 44, 81, 20))
        self.lineEditPortLocal.setMinimumSize(QtCore.QSize(81, 20))
        self.lineEditPortLocal.setMaximumSize(QtCore.QSize(81, 20))
        self.lineEditPortLocal.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPortLocal.setObjectName("lineEditPortLocal")
        self.comboBoxLocal = QtWidgets.QComboBox(self.groupBoxLocal)
        self.comboBoxLocal.setGeometry(QtCore.QRect(10, 16, 121, 22))
        self.comboBoxLocal.setMinimumSize(QtCore.QSize(121, 22))
        self.comboBoxLocal.setMaximumSize(QtCore.QSize(121, 22))
        self.comboBoxLocal.setObjectName("comboBoxLocal")
        self.verticalLayout.addWidget(self.groupBoxLocal)
        self.groupBoxAim = QtWidgets.QGroupBox(TcpUdpComTool)
        self.groupBoxAim.setMinimumSize(QtCore.QSize(141, 71))
        self.groupBoxAim.setMaximumSize(QtCore.QSize(141, 71))
        self.groupBoxAim.setObjectName("groupBoxAim")
        self.lineEditPortAim = QtWidgets.QLineEdit(self.groupBoxAim)
        self.lineEditPortAim.setGeometry(QtCore.QRect(50, 45, 81, 20))
        self.lineEditPortAim.setMinimumSize(QtCore.QSize(81, 20))
        self.lineEditPortAim.setMaximumSize(QtCore.QSize(81, 20))
        self.lineEditPortAim.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPortAim.setObjectName("lineEditPortAim")
        self.lineEditIpAim = QtWidgets.QLineEdit(self.groupBoxAim)
        self.lineEditIpAim.setGeometry(QtCore.QRect(10, 20, 121, 20))
        self.lineEditIpAim.setMinimumSize(QtCore.QSize(121, 20))
        self.lineEditIpAim.setMaximumSize(QtCore.QSize(121, 20))
        self.lineEditIpAim.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditIpAim.setObjectName("lineEditIpAim")
        self.verticalLayout.addWidget(self.groupBoxAim)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(TcpUdpComTool)
        QtCore.QMetaObject.connectSlotsByName(TcpUdpComTool)

    def retranslateUi(self, TcpUdpComTool):
        _translate = QtCore.QCoreApplication.translate
        TcpUdpComTool.setWindowTitle(_translate("TcpUdpComTool", "Widget"))
        self.labelStatusTag.setText(_translate("TcpUdpComTool", "当前状态:"))
        self.labelStatus.setText(_translate("TcpUdpComTool", "未连接"))
        self.checkBoxHexRec.setText(_translate("TcpUdpComTool", "Hex接收显示"))
        self.toolButtonShortCut.setText(_translate("TcpUdpComTool", "快捷键"))
        self.toolButtonAOP.setText(_translate("TcpUdpComTool", "AOP"))
        self.pushButtonStart.setText(_translate("TcpUdpComTool", "连接"))
        self.radioButton16.setText(_translate("TcpUdpComTool", "16进制"))
        self.radioButtonString.setText(_translate("TcpUdpComTool", "字符串"))
        self.pushButtonSend.setToolTip(_translate("TcpUdpComTool", "ctrl+Enter"))
        self.pushButtonSend.setText(_translate("TcpUdpComTool", "发送"))
        self.pushButtonClearRec.setText(_translate("TcpUdpComTool", "清空接收框"))
        self.groupBoxLocal.setTitle(_translate("TcpUdpComTool", "本地"))
        self.groupBoxAim.setTitle(_translate("TcpUdpComTool", "目的"))

