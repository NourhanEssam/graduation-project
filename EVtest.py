import socket

TCP_IP = '127.0.0.1'
TCP_IP =  'DESKTOP-55DJIJS'
TCP_PORT = 12346
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send('1')
i=0
while 1:
    s.send('2')
    i = i+1
    if i==4 :
        break;
s.close()

