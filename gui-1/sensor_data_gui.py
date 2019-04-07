import cv2
import numpy as np
import time 
from math import sqrt
from statistics import mode,mean
import threading
import os
import serial
import socket
import io
import serial
import struct
import pickle
import numpy as np
count=0
cnt=0
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))
crack_length=0
k=1.5
k1=0
dataset=[]
from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow import Ui_MainWindow1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(150, 430, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(550, 430, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setDigitCount(6)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 430, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(676, 432, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 520, 191, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 430, 111, 71))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../python/sensorimg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(156, 380, 111, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(556, 390, 101, 31))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 0, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../python/webcamimg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 0, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 40, 791, 321))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.xy)
        self.pushButton_2.clicked.connect(self.openwin)
        self.pushButton_4.clicked.connect(self.fg)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "  °C"))
        self.label_4.setText(_translate("MainWindow", "   pH"))
        self.label_5.setText(_translate("MainWindow", "        © Saransh Gupta"))
        self.pushButton_4.setText(_translate("MainWindow", "SENSORS"))
        self.label_6.setText(_translate("MainWindow", "      TEMP SENSOR"))
        self.label_7.setText(_translate("MainWindow", "       pH SENSOR"))
        self.pushButton.setText(_translate("MainWindow", "Live Feed"))
        self.pushButton_2.setText(_translate("MainWindow", "Detections"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
    print('b')
    def openwin(self):
        print('c')
        self.window = QtWidgets.QMainWindow()
        print('d')
        self.ui = Ui_MainWindow1()
        print('e')
        self.ui.setupUi(self.window)
        print('f')
        self.window.show()
    def xy(self): 
        t1 = threading.Thread(target = self.x)
        t1.start()
    def ff(self):
        t2 = threading.Thread(target=self.y)
        t2.start()
    def fg(self):
        t3 = threading.Thread(target = self.sen)
        t3.start()
    def x(self):
        global count
        cap = cv2.VideoCapture(0)
        while True:
                ret,frame = cap.read()
                cv2.imwrite('C:/python/camera0/frame%d.jpg' % count,frame)
                self.label.setPixmap(QtGui.QPixmap('C:/python/camera0/frame%d.jpg' % count))
                os.remove('C:/python/camera0/frame%d.jpg' % count)
                count=count+1
                time.sleep(.01)
                #cv2.imshow('frame0',frame)
                k=cv2.waitKey(5)
                if k==5:
                    break
        cv2.destroyAllWindows()
        cap.release()
    def y(self):
        global cnt
        cap = cv2.VideoCapture(1)
        while True:
                ret,framea = cap.read()
                cv2.imwrite('C:/python/camera1/framea%d.jpg' % cnt,framea)
                self.label_2.setPixmap(QtGui.QPixmap('C:/python/camera1/framea%d.jpg' % cnt))
                os.remove('C:/python/camera1/framea%d.jpg' % cnt)
                cnt=cnt+1
                time.sleep(.01)
                #cv2.imshow('frame1',framea)
                k=cv2.waitKey(5)
                if k==5:
                    break
        cv2.destroyAllWindows()
        cap.release()
        '''HOST='192.168.1.167'
        PORT=5003
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((HOST,PORT))
        s.listen(10)
        conn,addr=s.accept()
        data = b""
        payload_size = struct.calcsize(">L")
        while True:
            while len(data) < payload_size:
                data += conn.recv(1048576)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack(">L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += conn.recv(1048576)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            h,w = frame.shape[:2]
            frame1=cv2.resize(frame,(2*w,2*h), interpolation = cv2.INTER_LINEAR)
            cv2.imwrite('C:/python/crack/frame%d.jpg' % cnt,frame1)
            self.label_2.setPixmap(QtGui.QPixmap('C:/python/crack/frame%d.jpg' % cnt))
            os.remove('C:/python/crack/frame%d.jpg' % cnt)
            cnt=cnt+1
            cv2.waitKey(1)'''
    def sen(self):
        global k1
        sendata = []
        arduinoData = serial.Serial('com3',9600)
        while True:
            s = (arduinoData.readline().strip())
            print(s)
            rt =  s.decode('utf-8')
            sendata.append(rt)
            if k1%2==0:
                self.lcdNumber.display(str(sendata[k1]))
            else:
                self.lcdNumber_2.display(str(sendata[k1]))
            k1=k1+1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

