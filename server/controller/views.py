from django.shortcuts import render
from django.http import HttpResponse
from controller.models import TrafficLight
import re

# Create your views here.
from server.settings import INSTALLED_APPS


def index(request):
    # List of TLs (Hard Coded)
    tls = ['100N', '2S', '3E', '5W', '6N']

    # Get List of Directions and Intersections
    for tl in tls:
        Queryset = TrafficLight.objects.filter(Intersection_ID=str(re.split('(\d+)', tl)[1]))
        for element in Queryset:
            if element.Direction == re.split('(\d+)', tl)[2]:
                # open socket for ON
            else:
                # open socket for OFF

    return HttpResponse("<h1>Hello Controller</h1>");