from PyQt5.QtNetwork import QHostInfo, QAbstractSocket


class ICommunicateTCPIP:
    """
        Java风,移植锅
    """

    def __init__(self):
        self.localIp = str()
        self.dstIp = str()
        self.recSrcIp = str()
        self.localPort = 0
        self.dstPort = 0
        self.recSrcPort = 0

    @staticmethod
    def getLocalIpList():
        """
        返回本地网卡的ip列表
        :return: strlist
        """
        myHostInfo = QHostInfo.fromName(QHostInfo.localHostName())
        ipv4_addrs = list(
            filter(lambda myaddr: myaddr.protocol() == QAbstractSocket.IPv4Protocol, myHostInfo.addresses()))
        ipv4_straddrs = list(map(lambda myaddr: myaddr.toString(), ipv4_addrs))
        return ipv4_straddrs

    def setLocalIp(self, ip):
        self.localIp = ip

    def setDstIp(self, ip):
        self.dstIp = ip

    def setRecSrcIp(self, ip):
        self.recSrcIp = ip

    def setLocalPort(self, port):
        self.localPort = port

    def setDstPort(self, port):
        self.dstPort = port

    def setRecSrcPort(self, port):
        self.recSrcPort = port

    def getLocalIp(self):
        return self.localIp

    def getDstIp(self):
        return self.dstIp

    def getRecSrcIp(self):
        return self.recSrcIp

    def getLocalPort(self):
        return self.localPort

    def getDstPort(self):
        return self.dstPort

    def getRecSrcPort(self):
        return self.recSrcPort
