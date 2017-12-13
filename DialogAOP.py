from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
import global_const
from ui_dialogAOP import Ui_DialogAOP


class DialogAOP(QDialog):
    def __init__(self):
        super(DialogAOP, self).__init__()
        self.widgetui = Ui_DialogAOP()
        self.widgetui.setupUi(self)
        self.setWindowTitle('AOP')
        self.setWindowIcon(QIcon(global_const.ICON_PATH))
        self.setFixedSize(global_const.WIDTH_DialogAOP, global_const.HEIGHT_DialogAOP)
        self.__init_read_files()

    def __init_read_files(self):
        with open(global_const.PRE_SEND_FILE_PATH) as f1:
            self.pre_send_text = f1.read()
        self.widgetui.textEditSend.setPlainText(self.pre_send_text)

        with open(global_const.POST_REC_FILE_PATH) as f2:
            self.post_rec_text = f2.read()
        self.widgetui.textEditRec.setPlainText(self.post_rec_text)

    def check_change(self):
        """
        检查下俩文本框是否被修改了
        :return: (bool, bool)
        """
        send_change = (self.widgetui.textEditSend.toPlainText() != self.pre_send_text)
        rec_change = (self.widgetui.textEditRec.toPlainText() != self.post_rec_text)
        return (send_change, rec_change)

    @pyqtSlot()
    def on_pushButtonSave_clicked(self):
        """
        被编辑过则保存
        :return:
        """
        send_change, rec_change = self.check_change()
        if send_change is True:
            with open(global_const.PRE_SEND_FILE_PATH, 'w') as f1:
                f1.write(self.widgetui.textEditSend.toPlainText())
        if rec_change is True:
            with open(global_const.POST_REC_FILE_PATH, 'w') as f2:
                f2.write(self.widgetui.textEditRec.toPlainText())
        if send_change is False and rec_change is False:
            self.reject()
        else:
            self.accept()
