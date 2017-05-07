from _socket import socket
from gettrafficlights.models import TrafficLight, CentralNode, Intersection
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

    tls = []
    for tl_id in TLs_IDs:
        Queryset = TrafficLight.objects.filter(TL_ID=tl_id).values('Intersection_ID','Direction')
        for e in Queryset:
            tls.append(e['Intersection_ID']+e['Direction'])
    print 'here'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 12347))
    s.listen(1)
    (EVconnection, EVaddress) = s.accept()

    if EVconnection.recv(20) == '1':  # EV is Ready
        for tl in tls:
            print tl
            Queryset = TrafficLight.objects.filter(Intersection_ID=str(re.split('(\d+)', tl)[1]))
            for element in Queryset:
                CentralNodeID = Intersection.objects.values('CentralNode_ID').filter(Intersection_ID=str(re.split('(\d+)', tl)[1]))
                CentralNodeIP = CentralNode.objects.values('CentralNode_IP').filter(CentralNode_ID__in=CentralNodeID).first()
                tl_ip = CentralNodeIP['CentralNode_IP']

                #tl_ip_raw = TrafficLight.objects.values('TL_ID').filter(Intersection_ID=str(re.split('(\d+)', tl)[1])).filter(Direction=str(re.split('(\d+)', tl)[2]))
                #tl_ip = tl_ip_raw['TL_ID']
                tl_port = 12348
                #Testing
                tl_ip = 'LAPTOP-S9D924P3'
                tlsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tlsocket.connect((tl_ip, tl_port))

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