from PyQt5.QtCore import QObject, QIODevice, QByteArray
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

baudList = ('1200', '4800', '9600', '14400', '19200', '38400', '57600', '115200')


class SerialPort(QObject):
    def __init__(self):
        super(SerialPort, self).__init__()
        self.serialPort = QSerialPort(self)

    @staticmethod
    def getSerialPortList():
        """
        当前所连接的串口列表
        :return: list-of-QSerialPortInfo
        """
        portlist = list(map(lambda port: port.portName(), QSerialPortInfo.availablePorts()))
        return portlist

    def connectRec(self, slotRec):
        self.serialPort.readyRead.connect(slotRec)

    def openPort(self, portName, baudRate):
        self.serialPort.setPortName(portName)
        isOpenSuccess = (self.serialPort.open(QIODevice.ReadWrite)
                         and self.serialPort.setBaudRate(baudRate)
                         and self.serialPort.setDataBits(QSerialPort.Data8)
                         and self.serialPort.setDataErrorPolicy(QSerialPort.IgnorePolicy)
                         and self.serialPort.setFlowControl(QSerialPort.NoFlowControl)
                         and self.serialPort.setParity(QSerialPort.NoParity)
                         and self.serialPort.setStopBits(QSerialPort.OneStop))
        return isOpenSuccess

    def send(self, data):
        if len(data) == 0 or data is None:
            return
        if isinstance(data, str):
            return self.serialPort.write(QByteArray(bytes(data)))
        else:
            return self.serialPort.write(QByteArray(data))

    def read(self):
        """
        读取串口收到的数据
        :return: bytes
        """
        return self.serialPort.readAll().data()

    def getCurPortName(self):
        return self.serialPort.portName()

    def close(self):
        self.serialPort.close()
