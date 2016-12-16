from django.shortcuts import render
from django.http import HttpResponse
from controller.models import TrafficLight
import re
import socket

# Create your views here.
from server.settings import INSTALLED_APPS


def index(request):
    # List of TLs (Hard Coded)
    tls = ['100N', '2S', '3E', '5W', '6N']

    # Open Socket for the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 12345))
    s.listen(1)
    # Accept the EV
    EVconnection, EVaddress = s.accept()

    data = EVconnection.recv(20)
    if data == "1":  # Ready to receive
        # Get List of Directions and Intersections
        for tl in tls:
            Queryset = TrafficLight.objects.filter(Intersection_ID=str(re.split('(\d+)', tl)[1]))
            for element in Queryset:
                tl_ip = TrafficLight.objects.values('TL_ID').filter(Intersection_ID=str(re.split('(\d+)', tl)[1])).filter(Direction=str(re.split('(\d+)', tl)[2])) # Get IP
                tl_port = 12345
                tlsocket = socket(AF_INET, SOCK_STREAM)
                tlsocket.connect((tl_ip, tl_port))
                if element.Direction == re.split('(\d+)', tl)[2]:       # ON
                    tlsocket.send("1")
                    #data = tlsocket.recv(20)

                else:   # OFF
                    tlsocket.send("0")
                    #data = tlsocket.recv(20)

                # Receive from EV
                data = EVconnection.recv(20)
                if data == "1":
                    #reset TLs
                    #close sockets
                    tlsocket.close()
        # if end of route break
        data = EVconnection.recv(20)
        if data == "1": #end of route
            EVconnection.close()
    return HttpResponse("<h1>Hello Controller</h1>");