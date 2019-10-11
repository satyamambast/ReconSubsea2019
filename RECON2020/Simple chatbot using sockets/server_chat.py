import socket
import threading

def send():
    while True:
        data=input()
        #data="Recieved : " + data
        conn.send(data.encode('utf-8'))
    
def recv():
    while True:
        data=conn.recv(1024)
        print("Recieved : " + data.decode('utf-8'))

    

s=socket.socket()
host=socket.gethostname()
port=9999
s.bind((host,port))
s.listen()
print("Waiting for client...")
conn,addr=s.accept()
print("connected by ",addr)



    
    
t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)

t1.start()
t2.start()


    
t1.join()
t2.join()
conn.close()
    
