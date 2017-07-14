import socket

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 12348))
    s.listen(1)
    (EVconnection, EVaddress) = s.accept()
    print  'done connection'
    EVconnection.send('1')
    data = EVconnection.recv(20)
    print data