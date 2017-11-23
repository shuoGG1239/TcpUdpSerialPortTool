import json
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtCore import pyqtSlot
from ui_dialoghelp import Ui_DialogHelpShortcut


class DialogHelp(QDialog):
    def __init__(self):
        super(DialogHelp, self).__init__()
        self.widgetui = Ui_DialogHelpShortcut()
        self.widgetui.setupUi(self)
        self.setWindowTitle('help')
        self.setFixedSize(240, 320)




