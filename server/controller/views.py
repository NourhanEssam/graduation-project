from _socket import socket

from controller.models import TrafficLight
from django.http import HttpResponse
import re
import socket
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def index(request):
  if request.user.is_superuser or request.user.is_staff:
      return redirect('login:logout')

  if 'TrafficLights' in request.session:
    TLs_IDs = request.session['TrafficLights']
    print TLs_IDs
    tls = ['1N', '2W', '6E', '8W', '9N']

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 12346))
    s.listen(1)
    (EVconnection, EVaddress) = s.accept()

    if EVconnection.recv(20) == '1':  # EV is Ready
        for tl in tls:
            Queryset = TrafficLight.objects.filter(Intersection_ID=str(re.split('(\d+)', tl)[1]))
            for element in Queryset:
                tl_ip = TrafficLight.objects.values('TL_ID').filter(Intersection_ID=str(re.split('(\d+)', tl)[1])).filter(Direction=str(re.split('(\d+)', tl)[2]))
                tl_port = 12345
                #Testing
                tl_ip = 'DESKTOP-55DJIJS'
                tlsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tlsocket.connect((tl_ip, tl_port))

                if tlsocket.recv(20) == '1':  # TL confirms the connection
                    if element.Direction == re.split('(\d+)', tl)[2]:
                        tlsocket.send('1'+element.Direction)
                    else:
                        tlsocket.send('0'+element.Direction)

                if EVconnection.recv(20) == '2':
                    tlsocket.send("2")  # reset TLs
                    tlsocket.close()

    if EVconnection.recv(20) == '3':  # end of route
        EVconnection.close()

    return redirect('map:map')

    return HttpResponse("<h1>Hello Controller</h1>");

    ###  Protocol  ###
    # Emergency Vehicle
    # Send 0 --> Reconnect
    # Send 1 --> confirm the connection
    # Send 2 --> moved
    # Send 3 --> End of route
    # Traffic Light
    # Receive 0,dir -->OFF
    # Receive 1,dir -->ON
    # Send 0 --> Reconnect
    # Send 1 --> confirm the connection