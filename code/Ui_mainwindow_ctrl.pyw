# coding=utf-8
import os
import sys
import winreg

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_mainwindow import Ui_MainWindow
from Ui_dialog_create_group_ctrl import Ui_dialog_create_group_ctrl

from generate_li_xiang_biao import Handle_lxb
from generate_qing_shi_wen_jian import Handle_qswj
from generate_ji_tuan_pi_jian import Handle_jtpj
from handle_staff_info import Handle_staff_data
from handle_group_info import Handle_group_info
from msg_box import Msg_box

folder_path = os.path.abspath(os.path.dirname(os.getcwd()))
lxb_template_address = str(folder_path + "/templates/").replace("\\", "/")
lxb_address = str(folder_path + "/立项表/").replace("\\", "/")
qswj_template_address = str(folder_path + "/templates/").replace("\\", "/")
qswj_address = str(folder_path + "/请示文件/").replace("\\", "/")
jtpj_template_address = str(folder_path + "/templates/").replace("\\", "/")
jtpj_address = str(folder_path + "/集团批件/").replace("\\", "/")
staff_info_address = str(folder_path + "/database/" + "staff_info.xls").replace("\\", "/")
group_info_address = str(folder_path + "/database/" + "group_info.xls").replace("\\", "/")
reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
desk_path = winreg.QueryValueEx(reg_key, "Desktop")[0]  # 返回的是Unicode类型数据


class Ui_mainwindow_ctrl(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Ui_mainwindow_ctrl, self).__init__(parent)
        self.setupUi(self)
        self.dialog_create_group = Ui_dialog_create_group_ctrl()

        self.msg_box = Msg_box()
        self.pushButton_gen_lxb.released.connect(lambda: self.msg_box.msg_box_note('提示', '立项表创建成功！'))
        self.pushButton_gen_qswj.released.connect(lambda: self.msg_box.msg_box_note('提示', '请示文件创建成功！'))
        self.pushButton_gen_jtpj.released.connect(lambda: self.msg_box.msg_box_note('提示', '集团批件创建成功！'))
        # self.dialog_create_group.group_info_signal.connect(self.label_group_display.setText)  #信号与槽

    @pyqtSlot()
    def on_pushButton_create_clicked(self):
        self.dialog_create_group.exec_()
        self.group_info_input = self.dialog_create_group.dialog_get_group_info()
        self.label_group_display.setText(str(self.group_info_input))
        self.staff_databases_input = Handle_staff_data(staff_info_address).get_group_info(
            self.group_info_input['group_members'])

    def on_pushButton_gen_lxb_clicked(self):
        lxb = Handle_lxb(self.group_info_input, self.staff_databases_input, lxb_template_address, lxb_address,
                         desk_path)
        lxb.fill_lxb()

    def on_pushButton_gen_qswj_clicked(self):
        qswj = Handle_qswj(self.group_info_input, self.staff_databases_input, qswj_template_address, qswj_address,
                           desk_path)
        qswj.fill_qswj()

    def on_pushButton_gen_jtpj_clicked(self):
        jtpj = Handle_jtpj(self.group_info_input, self.staff_databases_input, jtpj_template_address,
                           jtpj_address, desk_path)
        jtpj.fill_jtpj()

    # todo
    def on_pushButton_gen_lxb_released(self):
        Handle_group_info(group_info_address).write_group_info(self.group_info_input)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fasys = Ui_mainwindow_ctrl()
    fasys.show()
    sys.exit(app.exec_())
