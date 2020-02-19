import cv2
import numpy as np
import time 
import struct
import pickle
import socket
import threading
import sys

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
    HOST='192.168.2.3'
    PORT=5003    
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(10)
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


recv_frame()
