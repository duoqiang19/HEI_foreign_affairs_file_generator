import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Msg_box(QWidget):
    def __init__(self, parent=None):
        super(Msg_box, self).__init__(parent)

    def test(self):
        self.setWindowTitle('QMessageBox例子')
        self.resize(300, 100)
        self.mybutton = QPushButton(self)
        self.mybutton.move(5, 5)
        self.mybutton.setText('点击消息弹出消息框')
        self.mybutton.clicked.connect(lambda: self.msg_box_note('hello', 'test'))

    def msg_box_test(self):
        # 弹出消息对话框
        reply = QMessageBox.information(self, '标题', '消息对话框正文', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply1 = QMessageBox.question(self, "标题", "提问框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply2 = QMessageBox.warning(self, "标题", "警告框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply3 = QMessageBox.critical(self, "标题", "严重错误对话框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply4 = QMessageBox.about(self, "标题", "关于对话框消息正文")

    def msg_box_note(self, note_msg_title, note_msg):
        reply = QMessageBox.information(self, note_msg_title, note_msg)

    def msg_box_warning(self, note_msg_title, note_msg):
        reply = QMessageBox.warning(self, note_msg_title, note_msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = Msg_box()
    myshow.test()
    myshow.show()
    sys.exit(app.exec_())
