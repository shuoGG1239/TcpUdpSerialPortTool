import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

import TcpUdpSerialportTool


def run_with_titlebar():
    app = QApplication(sys.argv)
    toolwidget = TcpUdpSerialportTool.TcpUdpSerialPortTool()
    toolwidget.setWindowTitle('TcpUdpSerialPort Tool')
    toolwidget.setWindowIcon(QIcon('myicon.ico'))
    toolwidget.show()
    sys.exit(app.exec_())


def run_normal():
    app = QApplication(sys.argv)
    mainWindow = TcpUdpSerialportTool.TcpUdpSerialPortTool()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_with_titlebar()
