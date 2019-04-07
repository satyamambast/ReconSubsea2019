import cv2
import numpy as np
import time 
from math import sqrt
from statistics import mode,mean
import threading
import os
import serial
import socket
import pytesseract
from Task_Character_Detection.detect2 import *
from shape_detect.shapedetector import ShapeDetector
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
MIN_CONTOUR_AREA = 100
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30
k=1.5
k1=0
k2=0
i=0
k3=0
cnte=0
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(119, 190, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(144, 20, 91, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(74, 48, 611, 401))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 20, 91, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(534, 20, 91, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.feed)
        self.pushButton_2.clicked.connect(self.y)
        self.pushButton_3.clicked.connect(self.z)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Text Detection"))
        self.pushButton_2.setText(_translate("MainWindow", "Shape Detection"))
        self.pushButton_3.setText(_translate("MainWindow", "Crack Detection"))
    def text_detection(self,ret,frame):
        global config
        print(ret)
        text = pytesseract.image_to_string(frame, config=config)
        cv2.imshow('frame',frame)
        print(text)
    def feed(self):
        global i
        global k2
        i=0
        k2=1000000000000000
        k3=1000000000000000
        print('k2 ',k2)
        print('k3 ',k3)
        print('i ',i)
        global k1
        global cnt
        cap = cv2.VideoCapture(0)
        k1=1
        print(k1)
        if k1==1:
            while i<1000000000000000:
                        ret,frame = cap.read()
                        self.text_detection(ret,frame)
##                        print('a')
##                        print(ret)
##                        print('b')
##                        text = pytesseract.image_to_string(frame, config=config)
##                        print(text)
##                        #detect(frame)
                        cv2.imwrite('C:/python/camera1/framea%d.jpg' % cnt,frame)
                        self.label.setPixmap(QtGui.QPixmap('C:/python/camera1/framea%d.jpg' % cnt))
                        os.remove('C:/python/camera1/framea%d.jpg' % cnt)
                        cnt=cnt+1
                        time.sleep(.01)
                        k=cv2.waitKey(5)
                        i=i+1
                        print(i)
                        if k==5:
                           break
            cap.release()
            cv2.destroyAllWindows()  
    def y(self):
        global i
        global k2
        k2=0
        i=1000000000000000
        k3=1000000000000000
        print('i ',i)
        print('k3 ',k3)
        print('k2 ',k2)
        global k1
        k1=2
        print(k1)
        global count
        cap1 = cv2.VideoCapture(1)
        if k1==2:
            while k2<1000000000000000:
                    ret,frame = cap1.read()
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
                    cv2.imwrite('C:/python/camera0/frame%d.jpg' % count,frame)
                    self.label.setPixmap(QtGui.QPixmap('C:/python/camera0/frame%d.jpg' % count))
                    os.remove('C:/python/camera0/frame%d.jpg' % count)
                    count=count+1
                    time.sleep(.01)
                    k=cv2.waitKey(5)
                    k2=k2+1
                    print(k2)
                    if k==5:
                        break
            cv2.destroyAllWindows()
            cap1.release()
    def distanceformula(x1,y1,x2,y2):
             return(sqrt((x1-x2)**2 + (y1-y2)**2))
    def z(self):
            global i
            global kernelOpen
            global kernelClose
            global k2
            global k3
            global cnte
            global k
            global dataset
            k3=0
            k2=1000000000000000
            i=1000000000000000
            global k1
            k1=3
            print(k1)
            global crack_length
            cap = cv2.VideoCapture(2)
            if k1==3:
                while k3<1000000000000000:
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
                    cv2.imwrite('C:/python/crack/frame%d.jpg' % cnte,frame)
                    self.label.setPixmap(QtGui.QPixmap('C:/python/crack/frame%d.jpg' % cnte))
                    os.remove('C:/python/crack/frame%d.jpg' % cnte)
                    cnte=cnte+1
                    k=cv2.waitKey(5)
                    k3=k3+1
                    if k==5:
                        break
                cv2.destroyAllWindows()
                cap.release()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

