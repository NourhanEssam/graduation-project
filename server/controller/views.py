from gettrafficlights.models import TrafficLight, CentralNode, Intersection

import re
import socket
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('login:logout')

    if request.method == 'POST' and request.is_ajax():
        data = request.POST
        print "hello data\n"
        print data

        # TODO use passed_tl function

    if 'TrafficLights' in request.session:
        TLs_IDs = request.session['TrafficLights']

    #Testing
    TLs_IDs = [1,2]

    for tl_id in TLs_IDs:
        Queryset = TrafficLight.objects.filter(TL_ID=tl_id).values('Intersection_ID','Direction').first()
        TL_Intersection_ID = Queryset['Intersection_ID']
        TL_Direction = Queryset['Direction']

        Intersection_Number_Central_Node = Intersection.objects.values('Intersection_Number_Central_Node').filter(Intersection_ID=TL_Intersection_ID).first()['Intersection_Number_Central_Node']
        tl_ip = CentralNode.objects.values('CentralNode_IP').filter(CentralNode_ID__in=Intersection.objects.values('CentralNode_ID').filter(Intersection_ID=TL_Intersection_ID)).first()['CentralNode_IP']
        tl_port = 12348

        #Testing
        tl_ip = 'LAPTOP-S9D924P3'

        #tlsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #tlsocket.connect((tl_ip, tl_port))

        print 'Sending ', Intersection_Number_Central_Node, TL_Direction

        #tlsocket.send(Intersection_Number_Central_Node + TL_Direction)

        #if EVconnection.recv(20) == '2':
        #    tlsocket.send("2")  # reset TLs
        #    tlsocket.close()

    return redirect('map:map')

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