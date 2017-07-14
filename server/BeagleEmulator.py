import socket

# TCP Server Socket
TCP_PORT = 12348
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.88", TCP_PORT))

while True:
    close_conn = False
    s.listen(1)
    conn, addr = s.accept()
    print 'Connection address:', addr

    while True:
        data = conn.recv(BUFFER_SIZE)
        if data:
            print "received data:", data

        if data == 'close':
            close_conn = True
            break

    if close_conn:
        conn.close()
        break
