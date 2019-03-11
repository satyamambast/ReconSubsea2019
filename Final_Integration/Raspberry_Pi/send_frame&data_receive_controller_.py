import socket
import pickle
import _thread as t
import time
import struct
import io
import cv2

host = ('192.168.1.167',5002)
global conn,addr
print("xxxxx")
sock2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock2.bind(host)
sock2.listen(5)
conn,addr=sock2.accept()

def receive_controller_data():
    sock1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock1.connect(('192.168.1.168',5001))
    while True:
        msg=sock1.recv(1024)
        msg1 = pickle.loads(msg)
        print("aman : ",msg1)
        time.sleep(.01)


def send_sensor_values():    
    while True:
        list1 = ['a','v','c','r',5.6,7,2]
        s = str(list1).strip('[]')
        data = pickle.dumps(s)
        conn.send(data)
        time.sleep(.01)


def send_frame():
    client_socket = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
    client_socket.connect(('192.168.1.168', 5003))

    cam = cv2.VideoCapture(1)
    cam.seet(3,320)
    cam.set(4, 240)
    img_counter = 0
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    while True:
        ret, frame = cam.read()
        result, frame = cv2.inencode('.jpg', frame, encode_param)
        size = len(data)

        print("{}: {}".format(img_counter, size))
        client_socket.sendall(struct.pack(">L",size) + data)
        img_counter += 1
    cam.release()
    
    
t.start_new_thread(receive_controller_data,())
t.start_new_thread(send_sensor_value,())
t.start_new_thread(send_frame,())
