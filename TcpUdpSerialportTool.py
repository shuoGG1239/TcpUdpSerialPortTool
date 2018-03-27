from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QKeySequence
from PyQt5.QtNetwork import QHostInfo
from PyQt5.QtWidgets import QWidget, QMessageBox
import global_const
from ConfigFile import ConfigFile
from DataOperate import *
from DialogAOP import DialogAOP
from DialogHelp import DialogHelp
from ICommunicateTCPIP import ICommunicateTCPIP
from SerialPort import SerialPort, baudList
from TcpServer import TcpServer
from TcpSocketClient import TcpSocketClient
from UdpSocket import UdpSocket
from ui_tcpUdpSerialportTool import Ui_TcpUdpComTool

"""
AOP example:
    self.udpSocket.send('hello', '192.168.75.111', 7777)
    print(self.current_rec_data)

"""


# @装饰器pre_send_decorate
def pre_send_decorate(func):
    def send_new(self, *args, **kwargs):
        try:
            exec(self.pre_send_code)
        except Exception as e:
            print(e)
        func(self, *args, **kwargs)

    return send_new


# @装饰器post_rec_decorate
def post_rec_decorate(func):
    def rec_new(self, *args, **kwargs):
        func(self, *args, **kwargs)
        try:
            exec(self.post_rec_code)
        except Exception as e:
            print(e)

    return rec_new


class ConnectMode(Enum):
    UDP_MODE = 0
    TCP_CLIENT_MODE = 1
    TCP_SERVER_MODE = 2
    SERIAL_PORT_MODE = 3


class TcpUdpSerialPortTool(QWidget):
    WIN_WIDTH = 655
    WIN_HEIGHT = 486

    ClientReadData = pyqtSignal(int, str, int, bytearray)
    ClientDisConnect = pyqtSignal(int, str, int)
    send_data = None
    pre_send_code = str()
    post_rec_code = str()

    def __init__(self):
        super(TcpUdpSerialPortTool, self).__init__()
        self.widgetui = Ui_TcpUdpComTool()
        self.widgetui.setupUi(self)
        self.setFixedSize(self.WIN_WIDTH, self.WIN_HEIGHT)
        self.myconfig = ConfigFile("condat.json")
        self.comboboxInit()
        self.configDataInit()
        self.__init_aop_files()
        self.widgetui.pushButtonSend.setEnabled(False)
        self.widgetui.pushButtonSend.setShortcut(QKeySequence("Ctrl+Return"))  # 快捷键, 也可以在QtDesign直接填
        self.setFocusPolicy(Qt.ClickFocus)  # 随便点击便聚焦
        self.current_rec_data = ''

    def __del__(self):
        self.configDataSave()

    def __init_aop_files(self):
        with open(global_const.PRE_SEND_FILE_PATH) as f1:
            self.pre_send_code = f1.read()
        with open(global_const.POST_REC_FILE_PATH) as f2:
            self.post_rec_code = f2.read()

    def configDataInit(self):
        # 发送状态读取
        if int(self.myconfig.getValue('sendStatus') or 0) == HexOrChar.CHAR_STYLE.value:
            self.widgetui.radioButtonString.click()
        else:
            self.widgetui.radioButton16.click()
        if self.myconfig.getValue('recStatus') == HexOrChar.CHAR_STYLE.value:
            self.widgetui.checkBoxHexRec.setChecked(False)
        else:
            self.widgetui.checkBoxHexRec.setChecked(True)
        self.widgetui.comboBoxBaud.setCurrentText(str(self.myconfig.getValue("baudValue")))
        self.oldcomNum = str(self.myconfig.getValue("comNum"))
        self.widgetui.lineEditIpAim.setText(str(self.myconfig.getValue("aimIp")))
        self.widgetui.lineEditPortLocal.setText(str(self.myconfig.getValue("srcPort")))
        self.widgetui.lineEditPortAim.setText(str(self.myconfig.getValue("dstPort")))

    def configDataSave(self):
        self.myconfig.setValue("sendStatus", self.getRadioButtStat().value)
        self.myconfig.setValue("recStatus", self.getCheckBoxStat().value)
        self.myconfig.setValue("baudValue", self.widgetui.comboBoxBaud.currentText())
        self.myconfig.setValue("srcPort", self.widgetui.lineEditPortLocal.text())
        self.myconfig.setValue("dstPort", self.widgetui.lineEditPortAim.text())
        self.myconfig.setValue("aimIp", self.widgetui.lineEditIpAim.text())
        self.myconfig.setValue("hostIp", self.widgetui.comboBoxLocal.currentText())
        if None != self.widgetui.comboComNum.currentText():
            self.myconfig.setValue("comNum", self.widgetui.comboComNum.currentText())

    def comboboxInit(self):
        # 工具选择框combox
        self.widgetui.comboBoxStyle.insertItem(0, "UDP")
        self.widgetui.comboBoxStyle.insertItem(1, "TCP Client")
        self.widgetui.comboBoxStyle.insertItem(2, "TCP Server")
        self.widgetui.comboBoxStyle.insertItem(3, "COM Tool")
        self.connectModeList = list()
        self.connectModeList.append('UDP')
        self.connectModeList.append('TCP Client')
        self.connectModeList.append('TCP Server')
        self.connectModeList.append('COM Tool')
        self.widgetui.comboBoxStyle.activated.connect(self.comboxClicked)
        # 波特率combox
        self.widgetui.comboBoxBaud.insertItems(0, baudList)
        self.widgetui.comboBoxBaud.setCurrentText("9600")
        self.widgetui.comboBoxBaud.hide()
        self.widgetui.comboComNum.hide()
        self.widgetui.comboBoxClientList.hide()  # tcp的server专用的组合框
        # 本地IP combobox
        self.myhostInfo = QHostInfo.fromName(QHostInfo.localHostName())
        hostIpList = ICommunicateTCPIP.getLocalIpList()
        oldHostIp = str(self.myconfig.getValue("hostIp"))
        tempHostIp = str()
        for ip in hostIpList:
            self.widgetui.comboBoxLocal.addItem(ip)
            if oldHostIp == ip:
                tempHostIp = ip
        self.widgetui.comboBoxLocal.setCurrentText((tempHostIp))
        self.myaddress = self.widgetui.comboBoxLocal.currentText()

    def connectUDP(self):
        self.udpSocket = UdpSocket(self)
        self.udpSocket.createConnection(self.myaddress, int(self.widgetui.lineEditPortLocal.text()))
        self.udpSocket.connectRec(self.dataReceivedUDP)
        self.widgetui.pushButtonSend.setEnabled(True)
        self.widgetui.labelStatus.setText('Udp创建OK')

    def connectTCPclient(self):
        self.tcpSocketClient = TcpSocketClient(self)
        self.tcpSocketClient.connectRec(self.dataReceivedTCP_client)
        isConnectOK = self.tcpSocketClient.createConnection(self.widgetui.lineEditIpAim.text(),
                                                            int(self.widgetui.lineEditPortAim.text()))
        if isConnectOK:
            self.widgetui.lineEditIpAim.setEnabled(False)
            self.widgetui.lineEditPortAim.setEnabled(False)
            self.widgetui.labelStatus.setText("TCP客户端创建OK")
        else:
            QMessageBox.information(self, "error", "连接失败")
            return
        self.widgetui.pushButtonSend.setEnabled(True)

    def connectTCPserver(self):
        self.tcpServer = TcpServer(self)
        self.tcpServer.createConnection(int(self.widgetui.lineEditPortLocal.text()))
        # 有TCPclient连接上server时
        self.tcpServer.connectClientConnected(self.updateClientList)
        # 当server收到client的发来的数据时
        self.tcpServer.connectClientDisconnected(self.disconnectTCPlist)
        # 有TCPclient断开连接时
        self.tcpServer.connectRec(self.dataReceivedTCP_server)
        self.widgetui.lineEditIpAim.setEnabled(False)
        self.widgetui.lineEditPortAim.setEnabled(False)
        self.widgetui.pushButtonSend.setEnabled(False)
        self.widgetui.comboBoxClientList.show()
        self.widgetui.labelStatus.setText("TCP服务端创建OK")

    def connectCOM(self):
        self.serialPort = SerialPort()
        self.serialPort.connectRec(self.comReadData)
        isOpenSuccess = self.serialPort.openPort(self.widgetui.comboComNum.currentText(),
                                                 int(self.widgetui.comboBoxBaud.currentText()))
        if isOpenSuccess:
            self.widgetui.labelStatus.setText(self.serialPort.getCurPortName() + " OK")
            self.widgetui.pushButtonStart.setText("断开")
            self.widgetui.pushButtonSend.setEnabled(True)
            self.widgetui.comboComNum.setEnabled(False)
            self.widgetui.comboBoxBaud.setEnabled(False)
        else:
            self.widgetui.labelStatus.setText(self.serialPort.getCurPortName() + " Error")

    def getRadioButtStat(self):
        if self.widgetui.radioButton16.isChecked():
            return HexOrChar.HEX_STYLE
        if self.widgetui.radioButtonString.isChecked():
            return HexOrChar.CHAR_STYLE
        return HexOrChar.CHAR_STYLE

    def getCheckBoxStat(self):
        if self.widgetui.checkBoxHexRec.isChecked():
            return HexOrChar.HEX_STYLE
        else:
            return HexOrChar.CHAR_STYLE

    @pyqtSlot(str)
    def disconnectTCPlist(self, fullAddrStr):
        removeIndex = self.widgetui.comboBoxClientList.findText(fullAddrStr)  # 找出文字对应的index
        self.widgetui.comboBoxClientList.removeItem(removeIndex)  # 根据index移除该项
        if self.widgetui.comboBoxClientList.count() == 0:  # client列表为空时, 不允许发送
            self.widgetui.pushButtonSend.setEnabled(False)

    @pyqtSlot(str)
    def updateClientList(self, fullAddrStr):
        if self.widgetui.comboBoxClientList.count() == 0:
            self.tcpServer.setCurClient(fullAddrStr)
        self.widgetui.comboBoxClientList.addItem(fullAddrStr)
        self.widgetui.pushButtonSend.setEnabled(True)

    @pyqtSlot()
    def dataReceivedUDP(self):
        data = self.udpSocket.read()
        self.recByStyle(data)

    @pyqtSlot()
    def dataReceivedTCP_client(self):
        data = self.tcpSocketClient.read()
        self.recByStyle(data)

    @pyqtSlot(str)
    def dataReceivedTCP_server(self, recFromFullAddr):
        uiCurClientFullAddr = self.widgetui.comboBoxClientList.currentText()
        # tcpServer.setCurClient(uiCurClientFullAddr)
        # 过滤掉其他非comboBoxClientList当前Client的接收数据
        if uiCurClientFullAddr == recFromFullAddr:
            data = self.tcpServer.read()
            self.recByStyle(data)

    @pyqtSlot()
    def comReadData(self):
        data = self.serialPort.read()
        self.recByStyle(data)

    @pyqtSlot()
    def on_pushButtonStart_clicked(self):
        # -------------------连接------------------
        if self.widgetui.pushButtonStart.text() == "连接":
            self.widgetui.pushButtonStart.setText("断开")
            self.widgetui.comboBoxLocal.setEnabled(False)
            self.widgetui.lineEditPortLocal.setEnabled(False)
            self.widgetui.comboBoxStyle.setEnabled(False)
            curMode = self.connectModeList.index(self.widgetui.comboBoxStyle.currentText())
            if curMode == ConnectMode.UDP_MODE.value:
                self.connectUDP()
            elif curMode == ConnectMode.TCP_CLIENT_MODE.value:
                self.connectTCPclient()
            elif curMode == ConnectMode.TCP_SERVER_MODE.value:
                self.connectTCPserver()
            elif curMode == ConnectMode.SERIAL_PORT_MODE.value:
                self.connectCOM()
        # -------------------断开------------------
        elif self.widgetui.pushButtonStart.text() == "断开":
            curMode = self.connectModeList.index(self.widgetui.comboBoxStyle.currentText())
            if curMode == ConnectMode.UDP_MODE.value:
                self.udpSocket.close()
            elif curMode == ConnectMode.TCP_CLIENT_MODE.value:
                self.tcpSocketClient.close()
                self.widgetui.lineEditIpAim.setEnabled(True)
                self.widgetui.lineEditPortAim.setEnabled(True)
            elif curMode == ConnectMode.TCP_SERVER_MODE.value:
                self.tcpServer.close()
                self.widgetui.comboBoxClientList.clear()
                self.widgetui.comboBoxClientList.hide()
                self.widgetui.lineEditIpAim.setEnabled(True)
                self.widgetui.lineEditPortAim.setEnabled(True)
            elif curMode == ConnectMode.SERIAL_PORT_MODE.value:
                self.widgetui.comboComNum.setEnabled(True)
                self.widgetui.comboBoxBaud.setEnabled(True)
                self.serialPort.close()
            self.widgetui.pushButtonSend.setEnabled(False)
            self.widgetui.comboBoxLocal.setEnabled(True)
            self.widgetui.lineEditPortLocal.setEnabled(True)
            self.widgetui.pushButtonStart.setText("连接")
            self.widgetui.comboBoxStyle.setEnabled(True)
            self.widgetui.labelStatus.setText("未连接")

    @pyqtSlot()
    def on_pushButtonSend_clicked(self):
        """
        self.udpSocket.send()
        self.tcpSocketClient.send()
        self.tcpServer.send()
        self.serialPort.send()
        :return:
        """
        msg = self.widgetui.plainTextEditSend.toPlainText()
        aimIP = self.widgetui.lineEditIpAim.text()
        aimPort = int(self.widgetui.lineEditPortAim.text())
        hexORchar = self.getRadioButtStat()
        if hexORchar == HexOrChar.HEX_STYLE:  # 16进制形式
            data = DataOperate.hexStringTochars(msg)
        if hexORchar == HexOrChar.CHAR_STYLE:  # 字符串形式
            data = msg
        curMode = self.connectModeList.index(self.widgetui.comboBoxStyle.currentText())
        self.send_data = data
        self.method_name(aimIP, aimPort, curMode)

    @pre_send_decorate
    def method_name(self, aimIP, aimPort, curMode):
        if curMode == ConnectMode.UDP_MODE.value:
            self.udpSocket.send(self.send_data, aimIP, aimPort)
        elif curMode == ConnectMode.TCP_CLIENT_MODE.value:
            self.tcpSocketClient.send(self.send_data)
        elif curMode == ConnectMode.TCP_SERVER_MODE.value:
            self.tcpServer.setCurClient(self.widgetui.comboBoxClientList.currentText())
            self.tcpServer.send(self.send_data)
        elif curMode == ConnectMode.SERIAL_PORT_MODE.value:
            self.serialPort.send(self.send_data)

    @pyqtSlot()
    def on_toolButtonAOP_clicked(self):
        aopEditWindow = DialogAOP()
        # aop_dialog若accept则表示aop文件修改了: accept:1 reject:0
        exec_status = aopEditWindow.exec()
        if exec_status == 1:
            self.__init_aop_files()

    @pyqtSlot()
    def on_pushButtonClearRec_clicked(self):
        self.widgetui.plainTextEditRec.clear()

    @pyqtSlot()
    def on_toolButtonShortCut_clicked(self):
        shortCutWindow = DialogHelp()
        shortCutWindow.exec()

    @pyqtSlot(int)
    def comboxClicked(self, selectedIndex):
        if "COM Tool" == self.widgetui.comboBoxStyle.itemText(selectedIndex):
            self.widgetui.comboBoxBaud.show()
            self.widgetui.comboComNum.show()
            self.widgetui.comboComNum.clear()
            # 扫描电脑存在连接的串口com并将其portname加入combox
            for portinfo in SerialPort.getSerialPortList():
                self.widgetui.comboComNum.addItem(portinfo)
            if ('' != self.oldcomNum) and (-1 != self.widgetui.comboComNum.findText(self.oldcomNum)):
                self.widgetui.comboComNum.setCurrentText(self.oldcomNum)
            self.widgetui.groupBoxLocal.hide()
            self.widgetui.groupBoxAim.hide()
        else:
            self.widgetui.comboBoxBaud.hide()
            self.widgetui.comboComNum.hide()
            self.widgetui.groupBoxLocal.show()
            self.widgetui.groupBoxAim.show()

    @pyqtSlot(str)
    def on_comboBoxLocal_activated(self, arg1):
        self.myaddress = arg1

    def keyPressEvent(self, e):
        if (e.modifiers() == Qt.ControlModifier) and (e.key() == Qt.Key_1):
            self.widgetui.plainTextEditRec.clear()
        if (e.modifiers() == Qt.ControlModifier) and (e.key() == Qt.Key_2):
            self.widgetui.plainTextEditSend.clear()
        if (e.modifiers() == Qt.ControlModifier) and (e.key() == Qt.Key_QuoteLeft):
            self.widgetui.plainTextEditRec.clear()
            self.widgetui.plainTextEditSend.clear()

    @post_rec_decorate
    def recByStyle(self, bytesData):
        self.current_rec_data = bytesData
        if self.getCheckBoxStat() == HexOrChar.CHAR_STYLE:
            self.widgetui.plainTextEditRec.insertPlainText(bytesData.decode('ascii'))
        elif self.getCheckBoxStat() == HexOrChar.HEX_STYLE:
            self.widgetui.plainTextEditRec.insertPlainText(DataOperate.charsToHexString(bytesData))
