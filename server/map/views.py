from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from googlemaps import *


@login_required
@ensure_csrf_cookie
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('login:logout')
    if request.method == 'POST' and request.is_ajax():
        data = request.POST
        gmaps = Client(key='AIzaSyCwI32R7w5UyY3nvL8Pv-sJqBvUiGCTzOc')
        directions_result = gmaps.directions((data.get('currentPosLat'), data.get('currentPosLng')),
                                             (data.get('targetLat'), data.get('targetLng')),
                                             mode="driving")
        print (directions_result)
    return render(request, 'map/index.html')

