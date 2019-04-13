import cv2
import numpy as np
import time 
from math import sqrt
import pytesseract
from Task_Character_Detection.detect2 import *
from shape_detect.shapedetector import ShapeDetector
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
config = ('-l eng --oem 1 --psm 3')
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))
crack_length=0
k=1.5
k1=0
MIN_CONTOUR_AREA = 100
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30
dataset=[]
from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 0, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../python/sensorimg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 380, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(556, 380, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 0, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../python/webcamimg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 611, 321))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 120, 75, 23))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 170, 75, 23))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.livefeed)
        self.pushButton_3.clicked.connect(self.shapesdetect)
        self.pushButton_5.clicked.connect(self.textdetect)
        self.pushButton_6.clicked.connect(self.crack)
        self.pushButton_4.clicked.connect(self.sensor)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "  °C"))
        self.label_4.setText(_translate("MainWindow", "   pH"))
        self.label_5.setText(_translate("MainWindow", "        © Saransh Gupta"))
        self.pushButton_4.setText(_translate("MainWindow", "SENSORS"))
        self.label_6.setText(_translate("MainWindow", "  TEMPERATURE SENSOR"))
        self.label_7.setText(_translate("MainWindow", "         PH SENSOR"))
        self.pushButton.setText(_translate("MainWindow", "Live Feed"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_3.setText(_translate("MainWindow", "Shape Detection"))
        self.pushButton_5.setText(_translate("MainWindow", "Text Detection"))
        self.pushButton_6.setText(_translate("MainWindow", "Crack Detection"))
    def openwin(self):
        print('c')
        self.window = QtWidgets.QMainWindow()
        print('d')
        self.ui = Ui_MainWindow1()
        print('e')
        self.ui.setupUi(self.window)
        print('f')
        self.window.show()
    def livefeed(self): 
        t1 = threading.Thread(target = self.x)
        t1.start()
    def ff(self):
        t2 = threading.Thread(target=self.y)
        t2.start()
    def fg(self):
        t3 = threading.Thread(target = self.sen)
        t3.start()
    def m(self):
        t4 = threading.Thread(target = self.shapesdetect)
        t4.start()
    def m1(self):
        t5 = threading.Thread(target=self.crack)
        t5.start()
    def text_detection(self,ret,frame):
        global config
        print(ret)
        text = pytesseract.image_to_string(frame, config=config)
        #cv2.imshow('frame',frame)
        print(text)
    def shapesdetect(self):
        cv2.destroyAllWindows()
        cap = cv2.VideoCapture(1)
        while True:
                    ret,frame = cap.read()
                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    lower = np.array([0,0,0])
                    upper = np.array([180,255,30])
                    mask = cv2.inRange(hsv, lower, upper)
                    res = cv2.bitwise_and(frame,frame, mask= mask)
                    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
                    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
                    maskFinal=maskClose
                    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                    cv2.drawContours(frame,conts,-1,(230,0,0),3)
                    sd = ShapeDetector()
                    shapesf=dict()
                    for c in conts:
                      shape = sd.detect(c)
                      if shape in shapesf:
                         shapesf[shape]+=1
                      else:
                         shapesf[shape]=1
                    print(shapesf)      
                    cv2.imshow('shape',frame)
                    if cv2.waitKey(1) & 0xFF==ord('r'):
                        break
        cv2.destroyAllWindows()
        cap.release()
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
                k=cv2.waitKey(1)
                if k==1:
                    break
        cv2.destroyAllWindows()
        cap.release()
    def crack(self):
        cv2.destroyAllWindows()
        global cnt
        cap = cv2.VideoCapture(2)
        while True:
                    ret,frame = cap.read()
                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    lower = np.array([80,100,100])
                    upper = np.array([120,250,250])
                    mask = cv2.inRange(hsv, lower, upper)
                    res = cv2.bitwise_and(frame,frame, mask= mask)
                    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
                    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
                    maskFinal=maskClose
                    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                    print(len(conts))
                    if len(conts)!=0:
                        c=max(conts,key=cv2.contourArea)
                        cv2.drawContours(frame,c,-1,(0,0,0),3)
                        rect =cv2.minAreaRect(c)
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)
                        cv2.drawContours(frame,[box],0,(0,0,255),2)
                        l=sqrt((box[0][0]-box[1][0])**2+(box[0][1]-box[1][1])**2)
                        b=sqrt((box[1][0]-box[2][0])**2+(box[1][1]-box[2][1])**2)
                        if l>b:
                            crack1=((l/b)*k)
                        else:
                            crack1=((b/l)*k)
                        print('crack1=',crack1)
                    cv2.imshow('crack',frame)
                    if cv2.waitKey(1) & 0xFF==ord('r'):
                        break
        cv2.destroyAllWindows()
        cap.release()
    def distanceformula(x1,y1,x2,y2):
             return(sqrt((x1-x2)**2 + (y1-y2)**2))
    def textdetect(self):
            '''global kernelOpen
            global kernelClose
            global dataset
            global crack_length
            cap = cv2.VideoCapture(3)
            while True:
                    ret,frame = cap.read()
                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    lower = np.array([80,100,100])
                    upper = np.array([120,250,250])
                    mask = cv2.inRange(hsv, lower, upper)
                    res = cv2.bitwise_and(frame,frame, mask= mask)
                    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
                    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
                    maskFinal=maskClose
                    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                    print(len(conts))
                    if len(conts)!=0:
                        c=max(conts,key=cv2.contourArea)
                        cv2.drawContours(frame,c,-1,(0,0,0),3)
                        rect =cv2.minAreaRect(c)
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)
                        cv2.drawContours(frame,[box],0,(0,0,255),2)
                        l=sqrt((box[0][0]-box[1][0])**2+(box[0][1]-box[1][1])**2)
                        b=sqrt((box[1][0]-box[2][0])**2+(box[1][1]-box[2][1])**2)
                        if l>b:
                            crack1=((l/b)*k)
                        else:
                            crack1=((b/l)*k)
                        print('crack1=',crack1)
                    self.imshow('text',frame)
                    if cv2.waitKey(1) & 0xFF==ord('r'):
                        break
            cv2.destroyAllWindows()
            cap.release()'''
    def sensor(self):
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
