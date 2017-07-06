# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from location.models import Location
import json

@csrf_exempt
def location(request):
    if request.method == 'POST':
        lon = request.POST['lon']
        lat = request.POST['lat']
        err = request.POST['err']
        key = request.POST['key']

        query = Location.objects.get(Key=key)
        if query:
            query.lon = lon
            query.lat = lat
            query.err = err
            query.save()
        else:
            new_row = Location(pk=key, lon=lon, lat=lat, err=err)
            new_row.save()

        return HttpResponse()

    if request.method == 'GET':
        key = request.GET.get('key', '')
        query = Location.objects.filter(pk=key).values('lon', 'lat', 'err').first()
        if query:
            return HttpResponse(json.dumps({'lon': query['lon'], 'lat': query['lat'], 'err': query['err']}),
                                content_type="application/json")
        else:
            print "no match"
            return HttpResponse()

