from django.http import HttpResponse
from .models import TrafficLight
from .models import IntersectionsStreets
from django.conf import settings


def index(request):
    path = settings.GETTRAFFICLIGHTS_FOLDER+'myfile.txt'
    lines = open(path,
                 'r').readlines()
    l = file_len(path)
    i = 0
    while i < l:
        street1 = lines[i]
        direct = lines[i + 1]
        street2 = lines[i + 2]
        tls = []
        i += 2
        query = 'SELECT Intersection_ID FROM IntersectionsStreets A B WHERE A.Street_ID = ' + street1 + 'AND B.Street_ID = ' + street2 + 'AND A.Intersection_ID = B.Intersection_ID'
        int_id = IntersectionsStreets.objects.raw(query)

        tls[i] = TrafficLight.objects.get(Direction=direct, Intersection_ID=int_id)
        print('hii')
        print(tls[i])
    open(path, 'w').writelines(tls)

    return HttpResponse("Hello, world. You're at the gettrafficlights index.")


def file_len(fname):
    j = 0
    with open(fname) as f:
        for j, l in enumerate(f):
            pass
    return j + 1


def gettl():
    path = settings.GETTRAFFICLIGHTS_FOLDER + 'myfile.txt'
    lines = open(path,'r').readlines()
    l = file_len(path)
    i = 0
    while i < l:
        street1 = lines[i]
        direct = lines[i + 1]
        street2 = lines[i + 2]
        tls = []
        i += 2
        query = 'SELECT Intersection_ID FROM IntersectionsStreets A B WHERE A.Street_ID = '+street1+ 'AND B.Street_ID = '+street2+ 'AND A.Intersection_ID = B.Intersection_ID'
        int_id = IntersectionsStreets.objects.raw(query)

        tls[i] = TrafficLight.objects.get(Direction=direct, Intersection_ID=int_id)
        print('hii')
        print(tls[i])
    open(path, 'w').writelines(tls)



# Create your views here.
