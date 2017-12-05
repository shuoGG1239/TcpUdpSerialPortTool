import json
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from ui_dialoghelp import Ui_DialogHelpShortcut
import global_const

class DialogHelp(QDialog):
    def __init__(self):
        super(DialogHelp, self).__init__()
        self.widgetui = Ui_DialogHelpShortcut()
        self.widgetui.setupUi(self)
        self.setWindowTitle('HELP')
        self.setWindowIcon(QIcon(global_const.ICON_PATH))
        self.setFixedSize(global_const.WIDTH_DialogHelp, global_const.HEIGHT_DialogHelp)




