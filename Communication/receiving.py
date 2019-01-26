import socket
import pickle
import _thread as t
import time
import struct
import io
import cv2
host = ('192.168.1.168',5002)

global conn,addr
print("xxxxx")
sock2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock2.bind(host)
sock2.listen(5)
conn,addr=sock2.accept()
#print("a")
def receive():
    #print("b")
    sock1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock1.connect(('192.168.1.167',5001))
    while True:
        msg=sock1.recv(1024)
        msg1 = pickle.loads(msg)
        print("aman : ",msg1)
        time.sleep(.01)
def send():    
    while True:
        list1 = ['a','v','c','r',5.6,7,2]
        s = str(list1).strip('[]')
        data = pickle.dumps(s)
        conn.send(data)
        time.sleep(.01)
def recv():
    HOST='192.168.1.168'
    PORT=5003
    
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #print('Socket created')
    s.bind((HOST,PORT))
    #print('Socket bind complete')
    s.listen(10)
    #print('Socket now listening')
    conn,addr=s.accept()
    data = b""
    payload_size = struct.calcsize(">L")
    #print("payload_size: {}".format(payload_size))
    while True:
        while len(data) < payload_size:
            #print("Recv: {}".format(len(data)))
            data += conn.recv(4096)
        #print("Done Recv: {}".format(len(data)))
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        h,w = frame.shape[:2]
        frame1=cv2.resize(frame,(2*w,2*h), interpolation = cv2.INTER_LINEAR)   
        cv2.imshow('ImageWindow',frame1)
        cv2.waitKey(1)
t.start_new_thread(receive,())
t.start_new_thread(send,())
t.start_new_thread(recv,())
