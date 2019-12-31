# coding=utf-8
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_dialog_create_group import Ui_Dialog
from handle_group_info import Handle_group_info
from msg_box import Msg_box

import os
import winreg

folder_path = os.path.abspath(os.path.dirname(os.getcwd()))
group_info_address = str(folder_path + "/database/" + "group_info.xls").replace("\\", "/")
leadership = ['王世民', '杨庆利', '张振江', '李超', '金昌范', '张振江', '李玉俊', '朱宏光']
chief_leadership = ['郭宇', '曲爱民']
hazard_country = ['伊拉克']
reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
desk_path = winreg.QueryValueEx(reg_key, "Desktop")[0]  # 返回的是Unicode类型数据


class Ui_dialog_create_group_ctrl(QDialog, Ui_Dialog):

    # group_info_signal = pyqtSignal(str)                                #信号与槽
    def __init__(self, parent=None):
        super(Ui_dialog_create_group_ctrl, self).__init__(parent)
        self.setupUi(self)
        # self.group_info= self.textEdit_group_members.toPlainText()     #信号与槽
        # self.group_info_signal.connect(self.on_buttonBox_accepted())   #信号与槽
        self.msg_box = Msg_box()
        self.group_info = {}

    def dialog_get_group_info(self):

        self.group_info['destination'] = self.lineEdit_destination.text()
        if self.group_info['destination'] in hazard_country:
            self.group_info['hazard_country'] = 1
        else:
            self.group_info['hazard_country'] = 0
        self.group_info['time'] = self.lineEdit_time.text()
        if self.group_info['time'] == '':
            self.buttonBox.accepted.connect(lambda: self.msg_box.msg_box_warning('警告', '请输入停留时间！'))
        elif int(self.group_info['time']) < 180:
            self.group_info['visa_type'] = '多次往返'
        else:
            self.group_info['visa_type'] = '长期'
        self.group_info['departure_date_year'] = self.dateEdit_departure_date.date().toString("yyyy")
        self.group_info['departure_date_month'] = self.dateEdit_departure_date.date().toString("M")
        self.group_info['departure_date_day'] = self.dateEdit_departure_date.date().toString("d")
        self.group_info['departure_date'] = self.dateEdit_departure_date.date().toString("yyyy/M/d")
        self.group_info['job_detail'] = self.lineEdit_job_detail.text()
        self.group_info['inviter'] = self.lineEdit_inviter.text()
        self.group_info['cost_center'] = '派员单位自理'
        self.group_info['combined_in_heg'] = '否'
        self.group_info['group_members'] = self.lineEdit_group_members.text().split(' ')
        self.group_info['group_leader'] = self.group_info['group_members'][0]
        if self.group_info['group_leader'] in chief_leadership:
            self.group_info['group_leader_position'] = 0
        elif self.group_info['group_leader'] in leadership:
            self.group_info['group_leader_position'] = 1
        else:
            self.group_info['group_leader_position'] = 2
        self.group_info['group_members_no'] = len(self.group_info['group_members'])
        self.group_info['tour_rountine'] = self.lineEdit_tour_rountine.text()
        nos = Handle_group_info(group_info_address).get_group_hei_no()
        self.group_info['foreign_affair_doc_no'] = nos[0] + 1
        self.group_info['he_permission_no'] = nos[1] + 1
        self.group_info['group_serial_no'] = nos[2] + 1
        if self.checkBox_tour_rountine.isChecked():
            a = self.lineEdit_tour_rountine.text().split(' ')
            self.group_info['tour_rountine'] = self.lineEdit_tour_rountine.text().split(' ')
            for i in range(len(a) - 1):
                self.group_info['tour_rountine'].append(a[-i - 2])
        else:
            self.group_info['tour_rountine'] = self.lineEdit_tour_rountine.text().split(' ')
        if self.checkBox_passport.isChecked():
            # self.checkBox_he_permission.setChecked(True)
            # self.checkBox_customs_pass.setChecked(True)
            self.group_info['needed_doc'] = ['护照', '路条', '批件']
        elif self.checkBox_customs_pass.isChecked():
            self.group_info['needed_doc'] = ['路条', '批件']
        else:
            self.group_info['needed_doc'] = ['批件']

        # self.group_info['back_date'] = self.dateEdit_departure_date.date() + int(self.lineEdit_time.text()) - 1
        # print(self.group_info['back_date'].toString("yyyy/MM/dd"))
        #
        # self.group_info[''] =
        os.makedirs(str(
            desk_path + "/" + str(self.group_info['foreign_affair_doc_no']) + " - " + self.group_info[
                'group_leader'] + " - " + self.group_info['destination'] + "/"))
        #os.makedirs(str(
            #desk_path + "/" + str(self.group_info['foreign_affair_doc_no']) + " - " + self.group_info[
                #'group_leader'] + " - " + self.group_info['destination'] + "/打印目录/"))
        return self.group_info

    # def on_pushButton_gen_lxb_released(self):


'''
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        #self.group_info_signal.emit(self.group_info)                   #信号与槽
        #return self.group_info
        Ui_dialog_create_group_ctrl().close()

    @pyqtSlot()
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        self.group_info.clear()
        Ui_dialog_create_group_ctrl().close()

    #@pyqtSlot(QAbstractButton)
#    def on_buttonBox_clicked(self, button):
#        """
#        Slot documentation goes here.
#
#        @param button DESCRIPTION
#        @type QAbstractButton
#        """
#        # TODO: not implemented yet
#        #raise NotImplementedError

#    def get_group_info(self):
#        self.group_info_signal.connect(self.on_buttonBox_accepted())
'''
