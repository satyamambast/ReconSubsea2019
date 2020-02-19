import cv2
import io
import socket
import struct
import time
import pickle
class MultiCam:
	def __init__(self,frame1,frame2,ret1,ret2):
		self.frame1=frame1
		self.frame2=frame2
		#self.frame3=frame3
		self.ret1=ret1
		self.ret2=ret2
		#self.ret3=ret3
	def displayallfeeds(self):
		cv2.imshow('cam1',frame1)
		cv2.imshow('cam2',frame2)
		#cv2.imshow('cam2',frame3)
		
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.2.4', 5003))
connection = client_socket.makefile('wb')


cam = cv2.VideoCapture(0)
cam1 = cv2.VideoCapture(1)
#cam2 = cv2.VideoCapture(2)

cam.set(3, 320)
cam.set(4, 240)

cam1.set(3, 320)
cam1.set(4, 240)

img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)

    ret1, frame1 = cam1.read()
    result1, frame1 = cv2.imencode('.jpg', frame1, encode_param)

    #ret2, frame2 = cam2.read()
    #result2, frame2 = cv2.imencode('.jpg', frame2, encode_param)

    obj=MultiCam(frame,frame1,ret,ret1)
    data=pickle.dumps(obj,1)
    size=len(data)

    #print("{}: {}: {}".format(img_counter, size,size1))
    client_socket.send(struct.pack(">L", size) + data)
    #client_socket.sendall(struct.pack(">L", size1) + data1)
    img_counter += 1
    print(img_counter)


cam.release()
cam1.release()
cam2.release()
