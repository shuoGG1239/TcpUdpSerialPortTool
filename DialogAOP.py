from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from ui_dialogAOP import Ui_DialogAOP
import global_const

class DialogAOP(QDialog):
    def __init__(self):
        super(DialogAOP, self).__init__()
        self.widgetui = Ui_DialogAOP()
        self.widgetui.setupUi(self)
        self.setWindowTitle('AOP')
        self.setWindowIcon(QIcon(global_const.ICON_PATH))
        self.setFixedSize(global_const.WIDTH_DialogAOP, global_const.HEIGHT_DialogAOP)

    @pyqtSlot()
    def on_pushButtonSave_clicked(self):
        print(123)
