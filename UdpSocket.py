from PyQt5.QtCore import QObject, QByteArray
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from ICommunicateTCPIP import ICommunicateTCPIP


class UdpSocket(QObject, ICommunicateTCPIP):
    def __init__(self, parent):
        super(UdpSocket, self).__init__()
        self.udpSocket = QUdpSocket(parent)

    def createConnection(self, localIP, localPort):
        localaddr = QHostAddress()
        localaddr.setAddress(localIP)
        self.setLocalIp(localIP)
        self.setLocalPort(localPort)
        isOK = self.udpSocket.bind(localaddr, localPort)
        return isOK

    def send(self, data):
        """
        udp-发送
        :param data: str or bytearray
        :return:
        """
        self.send(data, self.getDstIp(), self.getDstPort())

    def send(self, data, dstIp, dstPort):
        """
        udp-发送
        :param data: str or bytearray
        :param dstIp:
        :param dstPort:
        :return:
        """
        dstAddress = QHostAddress()
        dstAddress.setAddress(dstIp)
        if isinstance(data, str):
            self.udpSocket.writeDatagram(data, dstAddress, dstPort)
        elif isinstance(data, bytearray):
            self.udpSocket.writeDatagram(QByteArray(data), dstAddress, dstPort)
        else:
            print('unexpected input type!')

    def connectRec(self, slotRec):
        self.udpSocket.readyRead.connect(slotRec)

    def read(self):
        """
        读数据
        :return: bytearray
        """
        data = bytearray()
        while self.udpSocket.hasPendingDatagrams():
            datagram, senderAddress, senderPort = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())
            data.extend(datagram)
            self.setRecSrcIp(senderAddress.toString())
            self.setRecSrcPort(senderPort)
        return data

    def close(self):
        self.udpSocket.close()
