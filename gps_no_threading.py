import os
from gps import *
from time import *
import time
import requests

gpsd = None
os.system('clear')
gpsd = gps(mode=WATCH_ENABLE)

while True:
      gpsd.next()
      lon = gpsd.fix.longitude
      lat = gpsd.fix.latitude
      epx = gpsd.fix.epx
      epy = gpsd.fix.epy
      print 'latitude    ' , lon
      print 'longitude   ' , lat
      print 'time utc    ' , gpsd.utc, gpsd.fix.time
      print 'altitude    ' , gpsd.fix.altitude
      print 'epx         ' , epx
      print 'epy         ' , epy
      
      if lon != 0.0 and lat != 0.0:
            err = (epx + epy) / 4
            print 'error       ' , err
            payload = {'key': 'driver', 'lon': lon, 'lat': lat, 'err': err}
            response = requests.post("http://192.168.1.88:8000/location/", data=payload)
      time.sleep(2)
