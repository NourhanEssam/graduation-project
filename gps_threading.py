import os
from gps import *
from time import *
import time
import threading
import requests
 
gpsd = None
os.system('clear')
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd
    gpsd = gps(mode=WATCH_ENABLE)
    self.current_value = None
    self.running = True
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next()
 
if __name__ == '__main__':
  gpsp = GpsPoller()
  try:
    gpsp.start()
    while True:
      os.system('clear')
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
        response = requests.post("http://192.168.1.88/location/", data=payload)
        #print response.text
 
  except (KeyboardInterrupt, SystemExit):
    gpsp.running = False
    gpsp.join()
