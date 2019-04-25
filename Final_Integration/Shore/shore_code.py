import time
import socket
import threading
import pickle
import pygame
#from Task_Crack_Detection.crackmeasurement import crack
#from Task_Shape_Detection.Shape_Detection import shape
#from Task_Text_Detection.text_detect import *
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
        cv2.waitKey(1)`
    def decode(self,frame):
	    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        h,w = frame.shape[:2]
        framea=cv2.resize(frame,(2*w,2*h), interpolation = cv2.INTER_LINEAR)
	return framea

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
    s=out
    data = pickle.dumps(s,1)
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
    sock2.connect(('192.168.2.2',5058))
    
    while True:
        msg=sock2.recv(1024)
        if len(msg)>0 :
            msg1 = pickle.loads(msg,encoding='bytes')
            print("Received:",msg1)
        time.sleep(.01)



def recv_frame():
    HOST='192.168.2.1'
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
        obj.frame1=obj.__dict__[b'frame1']
        obj.frame2=obj.__dict__[b'frame2']
    	obj.frame3=obj.__dict__[b'frame3']
    	obj.frame4=obj.__dict__[b'frame4']
        obj.ret1=obj.__dict__[b'ret1']
        obj.ret2=obj.__dict__[b'ret2']
    	obj.ret3=obj.__dict__[b'ret3']
    	obj.ret4=obj.__dict__[b'ret4']
	obj.displayallfeeds()
send_cont = threading.Thread(target = send_controller_data, args = ())
recv_sense = threading.Thread(target = recv_sensor_values, args = ())
#recv_cam = threading.Thread(target = recv_frame, args = ())

send_cont.start()
recv_sense.start()
#recv_cam.start()
