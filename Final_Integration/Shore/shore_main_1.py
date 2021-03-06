import cv2
import numpy as np
import time 
from math import sqrt
#import Image_Recognisation.crackmeasurement as cr
from statistics import mode,mean
import threading
import os
import serial
import socket
import io
import serial
import struct
import pickle
import socket
import threading
import pygame
import sys
from Task_Crack_Detection.crackmeasurement import crack
from Task_Shape_Detection.Shape_Detection import shape
#from Task_Text_Detection.text_detect import *
bor=0
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
msg1=[0,0]
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
i2=0
num2=0
database=[]
shapesdict={'circle':0,'line':0,'triangle':0,'square':0}
from PyQt5 import QtCore, QtGui, QtWidgets
class MultiCam:
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    def __init__(self):
        self.frame1=None
        self.frame2=None
        self.frame3=None
        self.frame4=None
        self.ret1=False
        self.ret2=False
        self.ret3=False
        self.ret4=False
    def encodepossible(self,cam1,cam2,cam3,cam4):
        self.ret1, frame1 = cam1.read()
        self.ret2, frame2 = cam2.read()
        self.ret3, frame3 = cam3.read()
        self.ret4, frame4 = cam4.read()
        if ret1:
            result, self.frame1 = cv2.imencode('.jpg', frame1, encode_param)            
        elif ret2:
            result, self.frame2 = cv2.imencode('.jpg', frame2, encode_param)            
        elif ret3:
            result, self.frame3 = cv2.imencode('.jpg', frame3, encode_param)            
        elif ret3:
            result, self.frame4 = cv2.imencode('.jpg', frame4, encode_param)            

    def displayallfeeds(self):
        if self.ret1:	
            cv2.imshow('cam1',self.decode(self.frame1))
        if self.ret2:
            cv2.imshow('cam2',self.decode(self.frame2))
        if self.ret3:
            cv2.imshow('cam3',self.decode(self.frame3))
        if self.ret4:
            cv2.imshow('cam4',self.decode(self.frame4))
        cv2.waitKey(1)
    def decode(self,frame):
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        h,w = frame.shape[:2]
        framea=cv2.resize(frame,(2*w,2*h), interpolation = cv2.INTER_LINEAR)
        return framea
obj=MultiCam()
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
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        #self.pushButton_7.setToolTip('This is an example button')
        self.pushButton_7.move(100,670)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        #self.pushButton_7.setToolTip('This is an example button')
        self.pushButton_8.move(500,670)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        #self.pushButton_7.setToolTip('This is an example button')
        self.pushButton_9.move(600,670)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setStyleSheet("background-color: rgb(230, 212, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        #self.pushButton_7.setToolTip('This is an example button')
        self.pushButton_10.move(300,670)
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
        #self.pushButton.clicked.connect(self.tim1)
        self.pushButton_4.clicked.connect(self.m)
        self.pushButton_6.clicked.connect(self.m1)
        self.pushButton_7.clicked.connect(self.dispmode)
        self.pushButton_5.clicked.connect(self.borcam)
        self.pushButton_8.clicked.connect(self.v1)
        self.pushButton_9.clicked.connect(self.v2)
        self.pushButton_10.clicked.connect(self.displayshapes)
        self.checkBox.clicked.connect(self.task2)
        self.checkBox_2.clicked.connect(self.task3)
        self.checkBox_3.clicked.connect(self.task4)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tim1()
        self.fg()

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
        self.pushButton_7.setText(_translate("MainWindow", "DISPLAY CRACK"))
        self.pushButton_8.setText(_translate("MainWindow", "V1"))
        self.pushButton_9.setText(_translate("MainWindow", "V2"))
        self.pushButton_10.setText(_translate("MainWindow", "DISPLAY SHAPES"))

    def borcam(self):
        global bor
        global obj
        bor=1
        time.sleep(3)
        if obj.ret4:
            while True:
                cv2.imshow('borescope',obj.decode(obj.frame4))
                if cv2.waitKey(1) & 0xFF==('q'):
                    bor=0
                    cv2.destroyAllWindows()
                    break
        else:
            print(obj.ret1)
            bor=0
            
    def v1(self):
        global obj
        while obj.ret2:
            cv2.imshow('View 1',obj.decode(obj.frame2))
            if cv2.waitKey(1) & 0xFF==ord('r'):
                cv2.destroyAllWindows()
                break
    def v2(self):
        global obj
        while obj.ret3:
            cv2.imshow('View 2',obj.decode(obj.frame3))
            if cv2.waitKey(1) & 0xFF==ord('r'):
                cv2.destroyAllWindows()
                break
    def putframe(self,frame):
        cv2.imwrite('frame.jpg',frame)
        self.label.setPixmap(QtGui.QPixmap('frame.jpg'))
        os.remove('frame.jpg')
    def dispmode(self):
        global database
        if len(database)!=0:
            crack_l=mode(database)
            print(crack_l)
            self.lcdNumber_7.display(crack_l)
        else:
            self.lcdNumber_7.display('nil')
    def livefeed(self):
        t1 = threading.Thread(target = self.x)
        t1.start()
    def ff(self):
        t2 = threading.Thread(target=self.y)
        t2.start()
    def fg(self):
        t3 = threading.Thread(target = self.sensor)
        t3.start()
    def m(self):
        global obj
        global shapesdict
        if obj.ret2:
            print('loop')
            while True:
                shapesdict,frame=shape(obj.decode(obj.frame2))
                cv2.imshow('shape',frame)
                if cv2.waitKey(1) & 0xFF==ord('r'):
                    cv2.destroyAllWindows()
                    break
    def m1(self):
        global obj
        global database
        while True:
            crack_length,frame=crack(obj.decode(obj.frame2))
            cv2.imshow('crack',frame)
            database.append(round(crack_length,1))
            if cv2.waitKey(1) & 0xFF==ord('r'):
                cv2.destroyAllWindows()
                break
            
    def displayshapes(self):
        global shapesdict
        print(shapesdict)
        img=cv2.imread("shapes.jpg",cv2.IMREAD_COLOR)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,str(shapesdict['circle']),(100,50), font, 1.0,(0,0,255),2,cv2.LINE_AA)
        cv2.putText(img,str(shapesdict['triangle']),(100,150), font, 1.0,(0,0,255),2,cv2.LINE_AA)
        cv2.putText(img,str(shapesdict['line']),(100,250), font, 1.0,(0,0,255),2,cv2.LINE_AA)
        cv2.putText(img,str(shapesdict['square']),(100,350), font, 1.0,(0,0,255),2,cv2.LINE_AA)
        cv2.imshow('img',img)
        cv2.waitKey(0)
        
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
              1
              self.lcdNumber.display(str(num)+":"+str(i))
            
            if i==60:
                num = num+1
                i=0
                self.lcdNumber.display(str(num)+":"+str(i))
            i=i+1
            time.sleep(1)
    def task(self):
        global num1
        global num
        global clk
        global i
        global i1
        clk=clk+1
        if self.checkBox.isChecked() and clk==1:
            self.lcdNumber_4.display(str(num)+":"+str(i))
            num1=num
            i1=i
            self.checkBox.setEnabled(False)
        if self.checkBox_2.isChecked() and clk==1:
            self.lcdNumber_5.display(str(num)+":"+str(i))
            num1=num
            i1=i
            self.checkBox_2.setEnabled(False)
        if self.checkBox_3.isChecked() and clk==1:
            self.lcdNumber_6.display(str(num)+":"+str(i))
            num1=num
            i1=i
            self.checkBox_3.setEnabled(False)
    def task2(self):
        global clk
        global num1
        global i1
        global num2
        global i2
        global num3
        global i3
        clk=clk+1
        print(clk)
        if clk==1:
            self.lcdNumber_4.display(str(num)+":"+str(i))
            num1=num
            i1=i
        if clk==2:
            num2=num-num1
            i2=i-i1
            num3=num
            i3=i
            self.lcdNumber_4.display(str(num2)+":"+str(i2))
            
        if clk==3:
            
            self.lcdNumber_4.display(str(num-num3)+":"+str(i-i3))
        time.sleep(1)
    def task3(self):
        global clk
        global num1
        global i1
        global num2
        global i2
        global num3
        global i3
        clk=clk+1
        print(clk)
        if clk==1:
            self.lcdNumber_5.display(str(num)+":"+str(i))
            num1=num
            i1=i
        if clk==2:
            num2=num-num1
            i2=i-i1
            self.lcdNumber_5.display(str(num2)+":"+str(i2))
            num3=num
            i3=i
        if clk==3:
            self.lcdNumber_5.display(str(num-num3)+":"+str(i-i3))
        time.sleep(1)
    def task4(self):
        global clk
        global num1
        global i1
        global num2
        global i2
        global num3
        global i3
        clk=clk+1
        print(clk)
        if clk==1:
            self.lcdNumber_6.display(str(num)+":"+str(i))
            num1=num
            i1=i
        if clk==2:
            num2=num-num1
            i2=i-i1
            self.lcdNumber_6.display(str(num2)+":"+str(i2))
            num3=num
            i3=i
        if clk==3:
            self.lcdNumber_6.display(str(num-num3)+":"+str(i-i3))
        time.sleep(1)

    def x(self):
        global count
        global obj
        #cap = cv2.VideoCapture(0)
        while True:
            #count=count+1
            #time.sleep(.01)
            self.putframe(obj.decode(obj.frame1))

            #k=cv2.waitKey(1)
            #if k==1:
                #break
        cv2.destroyAllWindows()
        cap.release()
    '''def crack(self):
        cv2.destroyAllWindows()
        global cnt
        cap = cv2.VideoCapture(0)
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
        cap.release()'''
    def distanceformula(x1,y1,x2,y2):
             return(sqrt((x1-x2)**2 + (y1-y2)**2))
    #def mini(self):
    def sensor(self):
        global msg1
        k1=0
        #arduinoData = serial.Serial('com3',9600)
        while True:
            if k1%2==0:
                self.lcdNumber_2.display(msg1[0])
            else:
                self.lcdNumber_3.display(msg1[1])
            k1=k1+1

server_address = ('192.168.2.1', 5059)

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
print ('Initialized Joystick : %s' % j.get_name())

"""
1.Left analog x axis
2.Left analog y axis
3.LT +ve RT -ve
4.Right y axis
5.Right x axis
6.A
7.B
8.X
9.Y
10.LB
11.RB
12.BACK
13.START
14.LEFT CLICK
15.RIGHT CLICK
"""

def get():
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    it = 0 #iterator
    pygame.event.pump()
    #Read input from the two joysticks       
    for i in range(0, j.get_numaxes()):
        out[it] = round(j.get_axis(i),1)
        it+=1
    #Read input from buttons
    for i in range(0, j.get_numbuttons()):
        out[it] = j.get_button(i)
        it+=1
    if(abs(out[1])>abs(out[0])):
        out[0]=0.0
    else:
        out[1]=0.0
    if(out[1]==0.1 or out[1]==-0.1):
        out[1]=0.0
    if(out[0]==0.1 or out[0]==-0.1):
        out[0]=0.0
    if(out[3]==0.1 or out[3]==-0.1):
        out[3]=0.0
    if(out[4]==0.1 or out[4]==-0.1):
        out[4]=0.0
    out[1]=out[1]*10
    out[0]=out[0]*10
    out[3]=out[3]*10
    out[4]=out[4]*10
    #s=str(out).strip('[]')
    out.append(bor)
    #print(out)
    data = pickle.dumps(out,1)
    return data


def send_controller_data():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(server_address)
    sock1.listen(5)
    conn,addr = sock1.accept()
    while True:
        #s = get()
        #t = int(input('Enter 0 to 7-->\n'))
        #s = s.append(t)
        #s = str(s).strip('[]')
        #print(s)
        #data = pickle.dumps(s,1)
        conn.send(get())
        time.sleep(.01)
        
def recv_sensor_values():
    sock2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock2.connect(('192.168.2.2',5070))
    global msg1
    while True:
        msg=sock2.recv(1024)
        if len(msg)>0 :
            msg1 = pickle.loads(msg,encoding='bytes')
            #print("Received:",msg1)
        time.sleep(.01)



def recv_frame():
    HOST='192.168.2.1'
    PORT=5004 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(10)
    conn,addr=s.accept()
    data = b""
    payload_size = struct.calcsize(">L")
    global obj
    while True:
        while len(data) < payload_size:
            data += conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        obj=pickle.loads(frame_data,encoding='bytes')
        #print(obj.__dict__)
        obj.frame1=obj.__dict__[b'frame1']
        obj.frame2=obj.__dict__[b'frame2']
        obj.frame3=obj.__dict__[b'frame3']
        obj.frame4=obj.__dict__[b'frame4']
        obj.ret1=obj.__dict__[b'ret1']
        obj.ret2=obj.__dict__[b'ret2']
        obj.ret3=obj.__dict__[b'ret3']
        obj.ret4=obj.__dict__[b'ret4']
        #obj.displayallfeeds()


if __name__=="__main__":
    time.sleep(2)
    send_cont = threading.Thread(target = send_controller_data, args = ())
    recv_sense = threading.Thread(target = recv_sensor_values, args = ())
    recv_cam = threading.Thread(target = recv_frame, args = ())
    send_cont.start()
    recv_sense.start()
    recv_cam.start()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
