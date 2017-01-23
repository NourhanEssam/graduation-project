from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
import parser
import urllib

@ensure_csrf_cookie
def index(request):
    if request.method == 'POST' and request.is_ajax():
        data = request.POST

        # this url displays the directions between the origin and destination as a json string
        directions_url = 'https://maps.googleapis.com/maps/api/directions/json?sensor=false&origin={},{}&destination={},{}&key={}&mode={}'
        # start
        originLat = float(data.get('currentPosLat'))
        originLong = float(data.get('currentPosLng'))
        # destination
        destinationLat = float(data.get('targetLat'))
        destinationLong = float(data.get('targetLng'))

        # google api key (from my account)
        key = "AIzaSyCwI32R7w5UyY3nvL8Pv-sJqBvUiGCTzOc"
        # directions mode
        mode = "driving"
        pars = (originLat, originLong, destinationLat, destinationLong, key, mode)
        # replace the {} in the directions_url with the previous parameters
        request_url = directions_url.format(*pars)
        # call the url and store the json result in a string
        result_string = urllib.urlopen(request_url).read()
        # pass the json string to the parser which michel implemented
        directions = parser.parse_directions(result_string)

        # for testing
        print request_url, "\n\n"
        print result_string, "\n\n"
        print directions, "\n\n"

    return render(request, 'map/index.html')



