import Adafruit_BBIO.UART as UART
import serial
import socket

# List or serial ports
serials = []

# UART1 Initialization
UART.setup("UART1")
serials.append(serial.Serial(port = "/dev/ttyO1", baudrate=115200))

# UART2 Initialization
UART.setup("UART2")
serials.append(serial.Serial(port = "/dev/ttyO2", baudrate=115200))

# UART4 Initialization
UART.setup("UART4")
serials.append(serial.Serial(port = "/dev/ttyO4", baudrate=115200))

# UART5 Initialization
UART.setup("UART5")
serials.append(serial.Serial(port = "/dev/ttyO5", baudrate=115200))

# TCP Server Socket
TCP_PORT = 12348
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", TCP_PORT))

while True:
    close_conn = False
    s.listen(1)
    conn, addr = s.accept()
    print 'Connection address:', addr
    
    while True:
        data = conn.recv(BUFFER_SIZE)
        print "received data:", data
        
        if data == 'close':
            close_conn = True
            break
		
        if not data or len(data) != 2 or not data[1].isdigit(): 
            break

        Intersection_Number = int(data[1]) - 1
        
        if 0 <= Intersection_Number <= 3:
            serials[Intersection_Number].write(data)
    
    if close_conn:
        conn.close()
        break
    
for ser in serials:
    ser.close()
