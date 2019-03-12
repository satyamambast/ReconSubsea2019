import time
import socket
import _thread as t
import pickle
import pygame
from Task_Crack_Detection.crackmeasurement import crack
from Task_Shape_Detection.Shape_Detection import shape
#from Task_Text_Detection.text_detect import *


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

def send_controller_data():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(server_address)
    sock1.listen(5)
    conn,addr = sock1.accept()
    while True:    
        conn.send(get())
        time.sleep(.01)
        
def recv_sensor_values():
    sock2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock2.connect(('192.168.1.167',5002))
    
    while True:
        msg=sock2.recv(1024)
        msg1 = pickle.loads(msg)
        print("Received:",msg1)
        time.sleep(.01)



def recv_frame():
    HOST='192.168.1.168'
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
        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        h,w = frame.shape[:2]
        frame1=cv2.resize(frame,(2*w,2*h), interpolation = cv2.INTER_LINEAR)   
        #cv2.imshow('ImageWindow',frame1)
        crack(frame)
        '''shape(frame)'''
        cv2.waitKey(1)
    

t.start_new_thread(send_controller_data, ())
t.start_new_thread(recv_sensor_values, ())
t.start_new_thread(recv_frame, ())
