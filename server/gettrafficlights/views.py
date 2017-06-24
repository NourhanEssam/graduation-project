from .models import TrafficLight
from .models import IntersectionsStreets
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('login:logout')

    if 'directions' in request.session:
        lines = request.session['directions']
        tls = []
        print lines
        i = 0
        while i < len(lines)-2:
            street1 = lines[i]
            direct = lines[i + 1]
            street2 = lines[i + 2]

            Queryset = IntersectionsStreets.objects.filter(Street_ID=street1).values('Intersection_ID')
            Queryset2 = IntersectionsStreets.objects.filter(Street_ID=street2, Intersection_ID__in=Queryset).values('Intersection_ID')
            Queryset3 = TrafficLight.objects.filter(Intersection_ID=Queryset2, Direction=direct).values('TL_ID')
            for element in Queryset3:
                tls.append(element['TL_ID'])
            i += 2

        print tls
        request.session['TrafficLights'] = tls
        # testing
        # request.session['TrafficLights'] = [1, 2]
        return redirect('controller:controller')

    return redirect('map:map')


