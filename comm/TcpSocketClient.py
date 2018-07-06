from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QByteArray
from PyQt5.QtNetwork import QTcpSocket

from comm.ICommunicateTCPIP import ICommunicateTCPIP


class TcpSocketClient(QObject, ICommunicateTCPIP):
    readyReadClientID = pyqtSignal(int)
    disconnectedClientID = pyqtSignal(int)

    def __init__(self, parent=None):
        super(TcpSocketClient, self).__init__()
        self.tcpSocketClient = QTcpSocket(parent)
        self.setIsConnected(False)
        self.setTcpClientID(0)
        self.setPeerFullAddrStr(str())
        self.tcpSocketClient.readyRead.connect(self.dataReceived)
        self.connectClientDisconnect(self.disConnected)

    def createConnection(self, ip, port):
        self.tcpSocketClient.connectToHost(ip, port)  # 向目的ip服务器的端口进行连接
        isOK = self.tcpSocketClient.waitForConnected(2000)  # 等2s, 若还无法连上服务器就算失败
        self.setIsConnected(isOK)
        return isOK

    def send(self, data):
        """
        发送
        :param data: str or bytearray
        :return: int
        """
        if len(data) == 0 or data is None:
            return
        if isinstance(data, str):
            return self.tcpSocketClient.write(QByteArray(bytes(data, 'utf8')))
        else:
            return self.tcpSocketClient.write(QByteArray(data))

    def connectRec(self, slotRec):
        self.tcpSocketClient.readyRead.connect(slotRec)

    def connectClientDisconnect(self, slotRec):
        self.tcpSocketClient.disconnected.connect(slotRec)

    def read(self):
        """
        读取数据
        :return: bytes
        """
        datagram = self.tcpSocketClient.readAll()
        self.setRecSrcIp(self.tcpSocketClient.peerAddress())
        self.setRecSrcPort(self.tcpSocketClient.peerPort())
        return datagram.data()

    def close(self):
        self.tcpSocketClient.close()

    def connectRecWithClientID(self, slotRec):
        self.readyReadClientID.connect(slotRec)

    def connectDisconnectWithClientID(self, slotRec):
        self.disconnectedClientID.connect(slotRec)

    def setSocketDescriptor(self, socketDescriptor):
        return self.tcpSocketClient.setSocketDescriptor(socketDescriptor)

    @pyqtSlot()
    def dataReceived(self):
        self.readyReadClientID.emit(self.getTcpClientID())

    @pyqtSlot()
    def disConnected(self):
        self.disconnectedClientID.emit(self.getTcpClientID())

    def setIsConnected(self, isConnected):
        self.isConnected = isConnected

    def getIsConnected(self):
        return self.isConnected

    def setTcpClientID(self, tcpClientID):
        self.tcpClientID = tcpClientID

    def getTcpClientID(self):
        return self.tcpClientID

    def setPeerFullAddrStr(self, peerFullAddrStr):
        self.peerFullAddrStr = peerFullAddrStr

    def getPeerFullAddrStr(self):
        return self.peerFullAddrStr

    def getPeerIp(self):
        return self.tcpSocketClient.peerAddress().toString()

    def getPeerPort(self):
        return self.tcpSocketClient.peerPort()
