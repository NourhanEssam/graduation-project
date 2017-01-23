import socket

TCP_IP = '127.0.0.1'
TCP_IP =  'DESKTOP-55DJIJS'
TCP_PORT = 12346
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Hello1")
s.connect((TCP_IP, TCP_PORT))
print("Hello2")
s.send("1".encode("utf-8"))
print("Hello3")
data = s.recv(BUFFER_SIZE)
print("Hello4")
s.close()
print("Hello5")

print ("received data:", data)