# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\nutstore\python_workspace\pyqt5_test\pyqt5_on_eric6\handle_group_info\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 510)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 771, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_welcome = QtWidgets.QWidget()
        self.tab_welcome.setObjectName("tab_welcome")
        self.label_group_display = QtWidgets.QLabel(self.tab_welcome)
        self.label_group_display.setGeometry(QtCore.QRect(10, 40, 751, 131))
        self.label_group_display.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_group_display.setWordWrap(True)
        self.label_group_display.setObjectName("label_group_display")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_welcome)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 741, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.tab_welcome)
        self.widget.setGeometry(QtCore.QRect(10, 10, 441, 25))
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
        self.widget1 = QtWidgets.QWidget(self.tab_welcome)
        self.widget1.setGeometry(QtCore.QRect(550, 10, 206, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_2.addWidget(self.lcdNumber_3)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_2.addWidget(self.lcdNumber_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.tabWidget.addTab(self.tab_welcome, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.pushButton_create)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "团组信息录入"))
        self.label_group_display.setText(_translate("MainWindow", "团组信息"))
        self.pushButton_create.setText(_translate("MainWindow", "新建团组"))
        self.pushButton_gen_lxb.setText(_translate("MainWindow", "生成立项表"))
        self.pushButton_gen_qswj.setText(_translate("MainWindow", "生成请示文件"))
        self.pushButton_gen_jtpj.setText(_translate("MainWindow", "生成集团批件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_welcome), _translate("MainWindow", "欢迎"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "所有团组"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

