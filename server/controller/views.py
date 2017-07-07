from gettrafficlights.models import TrafficLight, CentralNode, Intersection

import socket
import utilities
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse


@login_required
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('login:logout')

    if 'TrafficLights' in request.session:
        TLs_IDs = request.session['TrafficLights']

        if request.method == 'POST' and request.is_ajax() and TLs_IDs:
            data = request.POST
            EVlocation = {
                'lon': float(data['currentPosLng']),
                'lat': float(data['currentPosLat'])
            }

            # Get intersection and direction
            tl_id = TLs_IDs[0]
            Queryset = TrafficLight.objects.filter(TL_ID=tl_id).values('Intersection_ID', 'Direction').first()
            TL_Intersection_ID = Queryset['Intersection_ID']
            TL_Direction = Queryset['Direction']

            # Get TL location from database
            TLLocation = TrafficLight.objects.filter(TL_ID=tl_id).values('Longitude', 'Latitude').first()
            TLLocation['lon'] = TLLocation.pop('Longitude')
            TLLocation['lat'] = TLLocation.pop('Latitude')

            # check if EV passed the current TL
            Passed = utilities.passed_tl(EVlocation, TLLocation, TL_Direction)

            if request.session['Send'] or Passed:
                # Get Central node Intersection number
                Intersection_Number_Central_Node = Intersection.objects.values('Intersection_Number_Central_Node').filter(Intersection_ID=TL_Intersection_ID).first()['Intersection_Number_Central_Node']

                # Get ip and port number
                tl_ip = CentralNode.objects.values('CentralNode_IP').filter(CentralNode_ID__in=Intersection.objects.values('CentralNode_ID').filter(Intersection_ID=TL_Intersection_ID)).first()['CentralNode_IP']
                tl_port = 12348
                #Testing
                #tl_ip = '127.0.0.1'
                # opening a socket
                tlsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tlsocket.connect((tl_ip, tl_port))

                if request.session['Send']:
                    # Sending to central node ip
                    tlsocket.send(TL_Direction + Intersection_Number_Central_Node)
                    print 'Sending ', TL_Direction, Intersection_Number_Central_Node
                    request.session['Send'] = False

                if Passed:
                    # reset TLs
                    tlsocket.send("P" + Intersection_Number_Central_Node)
                    request.session['Send'] = True
                    request.session['TrafficLights'].pop(0)
                    request.session.modified = True

                    print request.session['TrafficLights']
                    print "passed"

                tlsocket.close()

    return HttpResponse()
