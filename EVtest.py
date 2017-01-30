import socket

TCP_IP = 'LAPTOP-S9D924P3'
TCP_PORT = 12347
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send('1')
i=0
while 1:
	s.send(raw_input("2-Move"))
    #s.send('2')
    #i = i+1
    #if i==4 :
    #   break;22
s.close()

