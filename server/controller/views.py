from gettrafficlights.models import TrafficLight, CentralNode, Intersection

import re
import socket
import utilities
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('login:logout')

    if 'TrafficLights' in request.session:
        TLs_IDs = request.session['TrafficLights']

    #Testing
    TLs_IDs = [1,2]
    Passed = False

    for tl_id in TLs_IDs:
        # Get intersection and direction
        Queryset = TrafficLight.objects.filter(TL_ID=tl_id).values('Intersection_ID', 'Direction').first()
        TL_Intersection_ID = Queryset['Intersection_ID']
        TL_Direction = Queryset['Direction']

        # Get TL location from database
        TLLocation = TrafficLight.objects.filter(TL_ID=tl_id).values('Longitude', 'Latitude').first()
        TLLocation['lon'] = TLLocation.pop('Longitude')
        TLLocation['lat'] = TLLocation.pop('Latitude')

        # Get Central node Intersection number
        Intersection_Number_Central_Node = Intersection.objects.values('Intersection_Number_Central_Node').filter(Intersection_ID=TL_Intersection_ID).first()['Intersection_Number_Central_Node']

        # Get ip and port number
        tl_ip = CentralNode.objects.values('CentralNode_IP').filter(CentralNode_ID__in=Intersection.objects.values('CentralNode_ID').filter(Intersection_ID=TL_Intersection_ID)).first()['CentralNode_IP']
        tl_port = 12348
        #Testing
        tl_ip = 'LAPTOP-S9D924P3'
        # opening a socket
        tlsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tlsocket.connect((tl_ip, tl_port))
        # Sending to central node ip
        tlsocket.send(Intersection_Number_Central_Node + TL_Direction)
        print 'Sending ', Intersection_Number_Central_Node, TL_Direction
        # check if EV passed the current TL
        while Passed == False:
            if request.method == 'POST' and request.is_ajax():
                data = request.POST
                EVlocation = {}
                EVlocation['lon'] = data['currentPosLng']
                EVlocation['lat'] = data['currentPosLat']
                EVlocation = {key: float(value) for (key, value) in EVlocation.items()}
                Passed = utilities.passed_tl(EVlocation, TLLocation, TL_Direction)

        # reset TLs
        tlsocket.send("P" + Intersection_Number_Central_Node + TL_Direction)
        tlsocket.close()

    return redirect('map:map')