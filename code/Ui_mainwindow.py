# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\nutstore\python_workspace\test_workspace\pyqt5_test\pyqt5_on_eric6\handle_group_info\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 156)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 521, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_create = QtWidgets.QPushButton(self.widget)
        self.pushButton_create.setObjectName("pushButton_create")
        self.horizontalLayout.addWidget(self.pushButton_create)
        self.pushButton_gen_lxb = QtWidgets.QPushButton(self.widget)
        self.pushButton_gen_lxb.setObjectName("pushButton_gen_lxb")
        self.horizontalLayout.addWidget(self.pushButton_gen_lxb)
        self.pushButton_gen_qswj = QtWidgets.QPushButton(self.widget)
        self.pushButton_gen_qswj.setObjectName("pushButton_gen_qswj")
        self.horizontalLayout.addWidget(self.pushButton_gen_qswj)
        self.pushButton_gen_jtpj = QtWidgets.QPushButton(self.widget)
        self.pushButton_gen_jtpj.setObjectName("pushButton_gen_jtpj")
        self.horizontalLayout.addWidget(self.pushButton_gen_jtpj)
        self.label_group_display = QtWidgets.QLabel(self.centralWidget)
        self.label_group_display.setGeometry(QtCore.QRect(10, 40, 521, 91))
        self.label_group_display.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_group_display.setWordWrap(True)
        self.label_group_display.setObjectName("label_group_display")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "团组信息录入"))
        self.pushButton_create.setText(_translate("MainWindow", "新建团组"))
        self.pushButton_gen_lxb.setText(_translate("MainWindow", "生成立项表"))
        self.pushButton_gen_qswj.setText(_translate("MainWindow", "生成请示文件"))
        self.pushButton_gen_jtpj.setText(_translate("MainWindow", "生成集团批件"))
        self.label_group_display.setText(_translate("MainWindow", "团组信息"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

