import socket
import sys
import cv2
import pickle
import numpy as np
import struct
import threading 
class MultiCam:
	def __init__(self,frame1,frame2):
		self.frame1=frame1
		self.frame2=frame2
	def displayallfeeds(self):
		cv2.imshow('cam1',self.decode(self.frame1))
		cv2.imshow('cam2',self.decode(self.frame2))
		cv2.waitKey(1)
	def decode(self,frame):
		frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
		h,w = frame.shape[:2]
		frame1=cv2.resize(frame,(2*w,2*h), interpolation = cv2.INTER_LINEAR) 
		return frame1
HOST=''
PORT=8489
obj=MultiCam(None,None)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
def getimage(conn,data):
    global obj
    while len(data) < payload_size:
        #print("Recv: {}".format(len(data)))
        data += conn.recv(4096)
    print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    print("msg_size: {}".format(msg_size))
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    #obj = MultiCam(None,None)
    obj=pickle.loads(frame_data,encoding='bytes')
    obj.frame1=obj.__dict__[b'frame1']
    obj.frame2=obj.__dict__[b'frame2']
    obj.displayallfeeds()
def disp(obj):
	while True:
		obj.displayallfeeds()
	
t1 = threading.Thread(target=disp, args=(obj,))       
data=b""
t1.start()
while True:
	getimage(conn,data)
t1.join()	

	
