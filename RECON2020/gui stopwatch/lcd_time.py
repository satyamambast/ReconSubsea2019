# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lcd_time.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(520, 60, 201, 101))
        self.lcdNumber.setObjectName("lcdNumber")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(50, 120, 141, 41))
        self.start.setObjectName("start")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(70, 400, 131, 51))
        self.quit.setObjectName("quit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 220, 430, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.t1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.t1.setObjectName("t1")
        self.horizontalLayout_2.addWidget(self.t1)
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.horizontalLayout_2.addWidget(self.lcdNumber_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.t2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.t2.setObjectName("t2")
        self.horizontalLayout_3.addWidget(self.t2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_3.addWidget(self.lcdNumber_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.t3.setObjectName("t3")
        self.horizontalLayout.addWidget(self.t3)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout.addWidget(self.lcdNumber_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lcdNumber.raise_()
        self.start.raise_()
        self.quit.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "START"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        self.t1.setText(_translate("MainWindow", "Task 1"))
        self.t2.setText(_translate("MainWindow", "Task 2"))
        self.t3.setText(_translate("MainWindow", "Task 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

