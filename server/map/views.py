from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
import parser
import urllib

from map.scaler import scale, rotate


@never_cache
@login_required
@ensure_csrf_cookie
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('login:logout')
    if request.method == 'POST' and request.is_ajax():
        data = request.POST

        # this url displays the directions between the origin and destination as a json string
        directions_url = 'https://maps.googleapis.com/maps/api/directions/json?sensor=false&origin={},{}&destination={},{}&key={}&mode={}'
        # start
        originLat = float(data.get('currentPosLat'))
        originLong = float(data.get('currentPosLng'))
        #originLat, originLong = 30.063444, 31.278494

        # destination
        destinationLat = float(data.get('targetLat'))
        destinationLong = float(data.get('targetLng'))
        #destinationLat, destinationLong = 30.063936, 31.280017

        # google api key (from my account)
        key = "AIzaSyCwI32R7w5UyY3nvL8Pv-sJqBvUiGCTzOc"
        # directions mode
        mode = "driving"

        # scale for prototype
        originLat, originLong = scale(originLat, originLong)
        destinationLat, destinationLong = scale(destinationLat, destinationLong)

        pars = (originLat, originLong, destinationLat, destinationLong, key, mode)
        # replace the {} in the directions_url with the previous parameters
        request_url = directions_url.format(*pars)
        # call the url and store the json result in a string
        result_string = urllib.urlopen(request_url).read()
        # pass the json string to the parser which michel implemented
        directions = parser.parse_directions(result_string)

        # testing prototype
        directions = rotate(directions)

        request.session['directions'] = directions
        # for testing
        print request_url, "\n\n"
        print result_string, "\n\n"
        print directions, "\n\n"

        return redirect('gettrafficlights:gettrafficlights')

    return render(request, 'map/index.html')

