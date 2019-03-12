import time
import pygame
import socket
import _thread as t
import pickle
import io
import cv2
import struct

server_address = ('192.168.1.168', 5001)

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

def send():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(server_address)
    sock1.listen(5)
    conn,addr = sock1.accept()
    while True:    
        conn.send(get())
        time.sleep(.01)
        
def recv():
    sock2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock2.connect(('192.168.1.167',5002))
    while True:
        msg=sock2.recv(1024)
        msg1 = pickle.loads(msg)
        print("Received:",msg1)
        time.sleep(.01)

def camera():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.167', 5003))

    cam = cv2.VideoCapture(0)

    cam.set(3, 320);
    cam.set(4, 240);

    img_counter = 0

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

    while True:
        ret, frame = cam.read()
        result, frame = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(frame, 0)
        size = len(data)


        print("{}: {}".format(img_counter, size))
        client_socket.sendall(struct.pack(">L", size) + data)
        img_counter += 1

    cam.release()

t.start_new_thread(send, ())
t.start_new_thread(recv, ())
t.start_new_thread(camera, ())

