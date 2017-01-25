from django.http import HttpResponse
from .models import TrafficLight
from .models import IntersectionsStreets
from django.conf import settings
from django.shortcuts import render


def index(request):
    path = settings.GETTRAFFICLIGHTS_FOLDER+'myfile.txt'
    lines = open(path, 'r').read().replace('\n', '')
    l = file_len(path)
    i = 0
    tls = []
    print path
    print l
    while i < l-2:
        street1 = lines[i]
        direct = lines[i + 1]
        street2 = lines[i + 2]

        Queryset = IntersectionsStreets.objects.filter(Street_ID=street1).values('Intersection_ID')
        Queryset2 = IntersectionsStreets.objects.filter(Street_ID=street2, Intersection_ID__in=Queryset).values('Intersection_ID')
        Queryset3 = TrafficLight.objects.filter(Intersection_ID=Queryset2, Direction=direct).values('TL_ID')
        for element in Queryset3:
            tls.append(element['TL_ID'])
        open(path, 'a').writelines(element['TL_ID'])
        i += 2
    return render(request, 'map/index.html')
   # return HttpResponse("Hello, world. You're at the gettrafficlights index.")


def file_len(fname):
    j = 0
    with open(fname) as f:
        for j, l in enumerate(f):
            pass
    return j + 1







# Create your views here.
