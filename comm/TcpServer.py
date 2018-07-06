from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtNetwork import QTcpServer, QHostAddress

from comm.TcpSocketClient import TcpSocketClient


class TcpServer(QTcpServer):
    sglOneClientConnected = pyqtSignal(str)
    sglOneClientDisconnected = pyqtSignal(str)
    sglDataRec = pyqtSignal(str)

    def __init__(self, parent):
        super(TcpServer, self).__init__(parent)
        self.mapClientId2Client = dict()
        self.mapIpFull2Client = dict()

    def incomingConnection(self, handle):
        serverClient = TcpSocketClient(self)
        serverClient.setTcpClientID(handle)
        serverClient.setSocketDescriptor(handle)  # 核心连接句
        serverClient.setPeerFullAddrStr(self.toFullAddrStr(serverClient.getPeerIp(), serverClient.getPeerPort()))
        serverClient.connectRecWithClientID(self.dataReceived)
        serverClient.connectDisconnectWithClientID(self.oneClientDisconnected)
        # 存储新连接
        self.mapClientId2Client[int(handle)] = serverClient
        self.mapIpFull2Client[serverClient.getPeerFullAddrStr()] = serverClient
        self.sglOneClientConnected.emit(serverClient.getPeerFullAddrStr())

    def toFullAddrStr(self, ip, port):
        return ip + ':' + str(port)

    def setCurClient(self, clientIpPortString):
        self.curClient = self.mapIpFull2Client.get(clientIpPortString)
        self.curClientID = self.curClient.getTcpClientID()

    def createConnection(self, localPort):
        isOK = self.listen(QHostAddress.Any, localPort)
        return isOK

    def connectRec(self, slotRec):
        self.sglDataRec.connect(slotRec)

    def connectClientConnected(self, slotRec):
        self.sglOneClientConnected.connect(slotRec)

    def connectClientDisconnected(self, slotRec):
        self.sglOneClientDisconnected.connect(slotRec)

    def send(self, data, dstIp='', dstPort=0):
        """
        发送
        :param data: str or bytearray
        :param dstIp:
        :param dstPort:
        :return:
        """
        if dstIp == '':
            self.curClient.send(data)
            return
        fullIpPort = self.toFullAddrStr(dstIp, dstPort)
        client = self.mapIpFull2Client.get(fullIpPort)
        if client is not None:
            client.send(data)

    def read(self):
        return self.curClient.read()

    @pyqtSlot(int)
    def dataReceived(self, clientID):
        client = self.mapClientId2Client.get(clientID)
        peerFullAddrStr = client.getPeerFullAddrStr()
        self.sglDataRec.emit(peerFullAddrStr)

    @pyqtSlot(int)
    def oneClientDisconnected(self, clientID):
        client = self.mapClientId2Client.get(clientID)
        del self.mapClientId2Client[clientID]
        peerFullAddrStr = client.getPeerFullAddrStr()
        del self.mapIpFull2Client[peerFullAddrStr]
        self.sglOneClientDisconnected.emit(peerFullAddrStr)
