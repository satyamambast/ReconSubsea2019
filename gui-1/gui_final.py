import cv2
import numpy as np
import time 
from math import sqrt
<<<<<<< HEAD
=======
#import pytesseract
>>>>>>> 1d136c8589abd4c874d27df61c10708339e4fdee
#from Task_Character_Detection.detect2 import *
#from shape_detect.shapedetector import ShapeDetector
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
num=0
i=0
c=0
mi=0
se=0
cb=0
cb1=0
mi1=0
se1=0
clk=0
num1=0
i1=0
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1357, 817)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 10, 671, 51))
        self.pushButton.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(45, 90, 751, 441))
        self.label.setText("")
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(823, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(830, 80, 91, 17))
        self.checkBox.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(830, 170, 91, 17))
        self.checkBox_2.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(830, 260, 91, 17))
        self.checkBox_3.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 370, 251, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(850, 420, 201, 91))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1110, 370, 211, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(1120, 420, 201, 91))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 550, 471, 111))
        self.pushButton_4.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 550, 391, 111))
        self.pushButton_5.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(970, 550, 361, 111))
        self.pushButton_6.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(830, 110, 171, 51))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(820, 200, 191, 51))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(820, 290, 191, 51))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(970, 670, 351, 51))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1060, 100, 261, 231))
        self.label_2.setStyleSheet("background: url(C:/Users/hp/Desktop/recon img.png)\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1357, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.livefeed)
        self.pushButton.clicked.connect(self.tim1)
        self.pushButton_4.clicked.connect(self.m)
        self.pushButton_6.clicked.connect(self.m1)
        self.checkBox.clicked.connect(self.task2)
        self.checkBox_2.clicked.connect(self.task2)
        self.checkBox_3.clicked.connect(self.task2)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LIVE FEED"))
        self.checkBox.setText(_translate("MainWindow", "TASK 1"))
        self.checkBox_2.setText(_translate("MainWindow", "TASK 2"))
        self.checkBox_3.setText(_translate("MainWindow", "TASK 3"))
        self.pushButton_2.setText(_translate("MainWindow", "TEMPERATURE SENSOR (C)"))
        self.pushButton_3.setText(_translate("MainWindow", "METAL DETECTOR"))
        self.pushButton_4.setText(_translate("MainWindow", "SHAPE DETECTION"))
        self.pushButton_5.setText(_translate("MainWindow", "MINI ROV LIVE FEED"))
        self.pushButton_6.setText(_translate("MainWindow", "CRACK DETECTION"))
    def task2(self):
        global num
        global i
        global i1
        global i2
        global num1
        global num2
        global clk
        if self.checkBox.isChecked():
            print('a')
        if clk==1 and (self.checkBox_2.isChecked()==False and self.checkBox_3.isChecked()==False):
            self.lcdNumber_4.display(str(num)+":"+str(i))
            num1=num
            i1=i
        if clk==1 and (self.checkBox_2.isChecked()==False and self.checkBox.isChecked()==False):
            self.lcdNumber_6.display(str(num)+":"+str(i))
            num1=num
            i1=i
        if clk==1 and(self.checkBox_3.isChecked()==False and self.checkBox.isChecked()==False):
            self.lcdNumber_5.display(str(num)+":"+str(i))
            num1=num
            i1=i
        if clk==2 and self.checkBox.isChecked() and self.checkBox_2.isChecked():
            self.lcdNumber_5.display(str(num-num1)+":"+str(i-i1))
        if clk==2 and self.checkBox.isChecked() and self.checkBox_3.isChecked():
            self.lcdNumber_6.display(str(num-num1)+":"+str(i-i1))
        if clk==2 and self.checkBox_2.isChecked() and self.sheckBox.isChecked():
            self.lcdNumber_4.display(str(num-num1)+":"+str(i-i1))
        if clk==2 and self.checkBox_2.isChecked() and self.sheckBox_3.isChecked():
            self.lcdNumber_5.display(str(num-num1)+":"+str(i-i1))
        if clk==2 and self.checkBox_3.isChecked() and self.sheckBox.isChecked():
            self.lcdNumber_5.display(str(num-num1)+":"+str(i-i1))
        if clk==2 and self.checkBox_3.isChecked() and self.sheckBox_2.isChecked():
            self.lcdNumber_4.display(str(num-num1)+":"+str(i-i1))
        
    def task1(self):
        global num
        global i
        global mi
        global se
        global cb
        global mi1
        global se1
        cb=cb+1
        print(cb)
        if cb==1:
            #self.lcdNumber_4.display(str(num)+":"+str(i))
            mi1 = num
            se1 = i
        if cb==1 and cb1==1:
            mi1 = num-mi
            se1 = i-se
            self.lcdNumber_4.display(str(mi1)+":"+str(se1))
    '''def tasks(self):
        clk=clk+1
        if self.checkBox_2.isChecked() and self.checkBox.isChecked()==False and self.checkBox_3.isChecked==False:
            self.lcdNumber_5.display(str(num)+":"+str(i))
        if self.checkBox.isChecked() and self.checkBox_2.isChecked()==False and self.checkBox_3.isChecked()==False:
            self.lcdNumber_4.display(str(num)+":"+str(i))
        if self.checkBox_3.isChecked() and self.checkBox_2.isChecked()==False and self.checkBox.isChecked()==False:
            self.lcdNumber_6.display(str(num)+":"+str(i))
        if self.check'''
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
    def tim1(self):
        t6 = threading.Thread(target = self.tim)
        t6.start()
    def tim(self):
        global i
        global num
        while i<1000000000000000000000:
            if i<10:
                self.lcdNumber.display(str(num)+":0"+str(i))
            else:
                self.lcdNumber.display(str(num)+":"+str(i))
            
            if i==60:
                num = num+1
                i=0
                self.lcdNumber.display(str(num)+":"+str(i))
            i=i+1
            time.sleep(1)
    '''def text_detection(self,ret,frame):
        global config
        print(ret)
        text = pytesseract.image_to_string(frame, config=config)
        #cv2.imshow('frame',frame)
        print(text)'''
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
                '''cv2.imwrite('C:/python/camera0/frame%d.jpg' % count,frame)
                self.label.setPixmap(QtGui.QPixmap('C:/python/camera0/frame%d.jpg' % count))
                os.remove('C:/python/camera0/frame%d.jpg' % count)
                count=count+1
                time.sleep(.01)'''
                cv2.imshow('frame0',frame)
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
                        self.lcdNumber_7.display(crack1)
                        #print('crack1=',crack1)
                    cv2.imshow('crack',frame)
                    if cv2.waitKey(1) & 0xFF==ord('r'):
                        break
        cv2.destroyAllWindows()
        cap.release()
    def distanceformula(x1,y1,x2,y2):
             return(sqrt((x1-x2)**2 + (y1-y2)**2))
    #def mini(self):
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

