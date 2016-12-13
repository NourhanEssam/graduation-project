from django.http import HttpResponse
from .models import TrafficLight


def index(request):
    return HttpResponse("Hello, world. You're at the gettrafficlights index.")


def file_len(fname):
    j=0
    with open(fname) as f:
        for j, l in enumerate(f):
            pass
    return j + 1


def gettl():

    lines = open('myfile.txt').readlines()
    l = file_len('myfile.txt')

    i = 0
    while i < l:
        street1 = lines[i]
        dir = lines[i+1]
        street2 = lines[i+2]
        tls = []
        i += 2
        tls[i] = TrafficLight.objects.raw('SELECT TL_ID FROM TrafficLight WHERE Direction=dir AND Intersection_ID in SELECT A.Intersection_ID FROM IntersectionsStreets A B WHERE A.Street_ID=street1 AND B.Street_ID=street2 AND A.Intersection_ID=B.Intersection_ID')
        print(tls[i])
    open('myfile.txt', 'w').writelines(tls)

gettl()


# Create your views here.
