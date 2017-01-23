from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from googlemaps import *
import parser
import urllib

@ensure_csrf_cookie
def index(request):
    if request.method == 'POST' and request.is_ajax():
        data = request.POST

        directions_url = 'https://maps.googleapis.com/maps/api/directions/json?sensor=false&origin={},{}&destination={},{}&key={}&mode={}'
        originLat = float(data.get('currentPosLat'))
        originLong = float(data.get('currentPosLng'))
        destinationLat = float(data.get('targetLat'))
        destinationLong = float(data.get('targetLng'))
        key = "AIzaSyCwI32R7w5UyY3nvL8Pv-sJqBvUiGCTzOc"
        mode = "driving"
        pars = (originLat, originLong, destinationLat, destinationLong, key, mode)
        request_url = directions_url.format(*pars)
        result_string = urllib.urlopen(request_url).read()

        directions = parser.parse_directions(result_string)

        # for testing
        print request_url, "\n\n"
        print result_string, "\n\n"
        print directions, "\n\n"
    return render(request, 'map/index.html')



