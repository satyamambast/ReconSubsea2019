import socket
import threading
s=socket.socket()
host=socket.gethostname()
port=9999
s.connect((host,port))

def recv():
    while True:
        data=s.recv(1024)
        data=data.decode('utf-8')
        print("Recieved : " + data)
    
    
def send():
    while True:
        data=input()
        #data="Recieved : " + data
        data=data.encode('utf-8')
        s.sendall(data)

t1 =threading.Thread(target=send)
t2 =threading.Thread(target=recv)
t1.start()
t2.start()


#while True:
    
t1.join()
t2.join()
s.close()
