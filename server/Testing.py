import requests
import time
import sys

print len(sys.argv)
if len(sys.argv) == 4:
    # first command line argument is the ip or the hostname of the server
    url = "http://" + sys.argv[1] + "/location/"
    sequence = int(sys.argv[2])
    payload = {'key': sys.argv[3], 'err': 5}

    sequence_lat = []
    sequence_lon = []
    if sequence == 1:
        print "Sequence Number 1"
        sequence_lat = [30.063609, 30.063690, 30.063769, 30.063797, 30.063831, 30.063850, 30.063866, 30.063889,
                        30.063919, 30.063935, 30.063902, 30.063860, 30.063814]
        sequence_lon = [31.278422, 31.278385, 31.278396, 31.278463, 31.278557, 31.278605, 31.278659, 31.278715,
                        31.278790, 31.278854, 31.278878, 31.278899, 31.278923]

    if len(sequence_lat) > 3:
        # reset
        payload['lat'], payload['lon'] = 0.0, 0.0
        requests.post(url, data=payload)

        raw_input("Open Map and press Enter to continue...")

        # send source
        payload['lat'], payload['lon'] = sequence_lat[0], sequence_lon[0]
        print 'Initial Position: latitude = ' + str(payload['lat']) + ', longitude = ' + str(payload['lon'])
        requests.post(url, data=payload)
        time.sleep(2)

        # send destination
        payload['lat'], payload['lon'] = sequence_lat[len(sequence_lat) - 1], sequence_lon[len(sequence_lat) - 1]
        print 'Destination Position: latitude = ' + str(payload['lat']) + ', longitude = ' + str(payload['lon'])
        requests.post(url, data=payload)

        # send sequence
        for i in range(1, len(sequence_lat)):
            time.sleep(2)
            payload['lat'], payload['lon'] = sequence_lat[i], sequence_lon[i]
            print 'Step ' + str(i) + ': latitude = ' + str(payload['lat']) + ', longitude = ' + str(payload['lon'])
            requests.post(url, data=payload)

        print "Sequence Executed"

