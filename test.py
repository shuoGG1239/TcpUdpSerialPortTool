from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtNetwork import QTcpServer, QHostAddress
from TcpSocketClient import TcpSocketClient

class MyClass(QObject):
    def __init__(self):
        super(MyClass, self).__init__()

    @pyqtSlot()
    def __slot_print(self):
        print(123123123)

    def printa(self, me, you):
        print(123)

    def printa(self, me):
        print(456)


c = MyClass()
c.printa(888,77)




