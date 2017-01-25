import socket

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 12345))
    s.listen(1)
    (EVconnection, EVaddress) = s.accept()
    EVconnection.send('1')
    data = EVconnection.recv(20)
    print data