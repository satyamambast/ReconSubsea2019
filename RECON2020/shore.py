import cv2
import numpy as np
import time 
import struct
import pickle
import socket
import threading
import sys
import pygame

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
    s=str(out).strip('[]')
    data = pickle.dumps(s)
    return data

class MultiCam:
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    def __init__(self):
        self.frame1=None
        self.frame2=None
        #self.frame3=None
        #self.frame4=None
        self.ret1=False
        self.ret2=False
        #self.ret3=False
        #self.ret4=False
    def encodepossible(self,cam1,cam2):#,cam3,cam4):
        self.ret1, frame1 = cam1.read()
        self.ret2, frame2 = cam2.read()
        #self.ret3, frame3 = cam3.read()
        #self.ret4, frame4 = cam4.read()
        if ret1:
            result, self.frame1 = cv2.imencode('.jpg', frame1, encode_param)            
        elif ret2:
            result, self.frame2 = cv2.imencode('.jpg', frame2, encode_param)            
        '''elif ret3:
            result, self.frame3 = cv2.imencode('.jpg', frame3, encode_param)            
        elif ret3:
            result, self.frame4 = cv2.imencode('.jpg', frame4, encode_param)'''            

    def displayallfeeds(self):
        if self.ret1:	
            cv2.imshow('cam1',self.decode(self.frame1))
        if self.ret2:
            cv2.imshow('cam2',self.decode(self.frame2))
        '''if self.ret3:
            cv2.imshow('cam3',self.decode(self.frame3))
        if self.ret4:
            cv2.imshow('cam4',self.decode(self.frame4))'''
        cv2.waitKey(1)
    def decode(self,frame):
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        h,w = frame.shape[:2]
        framea=cv2.resize(frame,(2*w,2*h), interpolation = cv2.INTER_LINEAR)
        return framea

def recv_frame():
    HOST='192.168.20.4'
    PORT=5003    
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(5)
    conn,addr=s.accept()
    data = b""
    payload_size = struct.calcsize(">L")
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
        obj.frame1=obj.__dict__['frame1']
        obj.frame2=obj.__dict__['frame2']
        #obj.frame3=obj.__dict__['frame3']
        #obj.frame4=obj.__dict__[b'frame4']
        obj.ret1=obj.__dict__['ret1']
        obj.ret2=obj.__dict__['ret2']
        #obj.ret3=obj.__dict__['ret3']
        #obj.ret4=obj.__dict__[b'ret4']
        obj.displayallfeeds()

def send_data():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(('192.168.20.3',5004))
    while True:
        #x = str(get())
        '''data = list(x[1:len(x)-1].split(","))
        #print(data)
        controller_data = ''
        for i in range(0,len(data)):
            n=int(data[i]) +107
            controller_data = controller_data+chr(n)
        d = pickle.dumps(controller_data)'''
        client_socket.send(get()) 
        msg = client_socket.recv(1024).decode()  #acknowledgement from rov
        print(msg)
    client_socket.close()    


print("3")
recv = threading.Thread(target=recv_frame)
send = threading.Thread(target=send_data)
recv.start()
send.start()
recv.join()
send.join()
