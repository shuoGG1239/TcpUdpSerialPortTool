import sys
import TcpUdpSerialportTool
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from qss_ui_theme import qss_setting
from qss_ui_theme import green_theme
from qss_ui_theme import window_titlebar


def run_with_titlebar():
    app = QApplication(sys.argv)
    toolwidget = TcpUdpSerialportTool.TcpUdpSerialPortTool()
    mainWindow = window_titlebar.WindowWithTitleBar(toolwidget, qss_setting.DARKBLUEGREEN, 0)
    mainWindow.setWindowTitle('TcpUdpSerialPort Tool')
    mainWindow.setWindowIcon(QIcon(window_titlebar.imageroot + 'myicon.ico'))
    green_theme.setAppGreenStyle()
    mainWindow.show()
    sys.exit(app.exec_())

def run_normal():
    app = QApplication(sys.argv)
    mainWindow = TcpUdpSerialportTool.TcpUdpSerialPortTool()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_with_titlebar()