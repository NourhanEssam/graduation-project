import requests
import time
import sys

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
    elif sequence == 2:
        print "Sequence Number 2"
        sequence_lat = [30.063421, 30.063364, 30.063308, 30.063252, 30.063187, 30.063178, 30.063178, 30.063206,
                        30.063234, 30.063262, 30.063276, 30.063313, 30.063387, 30.063461, 30.063535]
        sequence_lon = [31.278541, 31.278557, 31.278578, 31.278599, 31.278626, 31.278690, 31.278754, 31.278840,
                        31.278915, 31.278990, 31.279054, 31.279140, 31.279097, 31.279118, 31.279054]
    elif sequence == 3:
        print "Sequence Number 3"
        sequence_lat = [30.063209, 30.063183, 30.063171, 30.063166, 30.063182, 30.063221, 30.063260]
        sequence_lon = [31.278869, 31.278805, 31.278751, 31.278692, 31.278636, 31.278609, 31.278590]
    elif sequence == 4:
        print "Sequence Number 4"
        sequence_lat = [30.063803, 30.063791, 30.063751, 30.063698, 30.063654]
        sequence_lon = [31.278520, 31.278472, 31.278378, 31.278383, 31.278407]
    elif sequence == 5:
        print "Sequence Number 5"
        sequence_lat = [30.063876, 30.063902, 30.063921, 30.063937, 30.063893, 30.063816, 30.063728, 30.063649, 30.063579, 30.063498, 30.063417, 30.063357, 30.063280, 30.063254]
        sequence_lon = [31.278690, 31.278762, 31.278816, 31.278872, 31.278896, 31.278939, 31.278971, 31.279006, 31.279036, 31.279068, 31.279114, 31.279144, 31.279128, 31.279048]

    elif sequence == 6:
        print "Sequence Number 6"
    	sequence_lat = [30.063876, 30.063881, 30.063890, 30.063896, 30.063908, 30.063924, 30.063933, 30.063928, 30.063907, 30.063888, 30.063865, 30.063844, 30.063825, 30.063802, 30.063769, 30.063739, 30.063718, 30.063697, 30.063674, 30.063653, 30.063630, 30.063607, 30.063586, 30.063565, 30.063542, 30.063521, 30.063500, 30.063479, 30.063458, 30.063442, 30.063421, 30.063402, 30.063376, 30.063348, 30.063325, 30.063297, 30.063283, 30.063274, 30.063267, 30.063253]
    	sequence_lon = [31.278690, 31.278709, 31.278730, 31.278754, 31.278784, 31.278808, 31.278823, 31.278861, 31.278872, 31.278888, 31.278896, 31.278904, 31.278912, 31.278920, 31.278928, 31.278949, 31.278960, 31.278968, 31.278973, 31.278994, 31.279010, 31.279015, 31.279026, 31.279037, 31.279045, 31.279053, 31.279058, 31.279069, 31.279080, 31.279088, 31.279096, 31.279120, 31.279133, 31.279138, 31.279143, 31.279122, 31.279084, 31.279049, 31.279014, 31.278984]
    elif sequence == 7:
        sequence_lat = [30.063253, 30.063267, 30.063274, 30.063283, 30.063297, 30.063325, 30.063348, 30.063376, 30.063402, 30.063421, 30.063442, 30.063458, 30.063479, 30.0635, 30.063521, 30.063542, 30.063565, 30.063586, 30.063607, 30.06363, 30.063653, 30.063674, 30.063697, 30.063718, 30.063739, 30.063769, 30.063802, 30.063825, 30.063844, 30.063865, 30.063888, 30.063907, 30.063928, 30.063933, 30.063924, 30.063908, 30.063896, 30.06389, 30.063881, 30.063876]
        sequence_lon = [31.278984, 31.279014, 31.279049, 31.279084, 31.279122, 31.279143, 31.279138, 31.279133, 31.27912, 31.279096, 31.279088, 31.27908, 31.279069, 31.279058, 31.279053, 31.279045, 31.279037, 31.279026, 31.279015, 31.27901, 31.278994, 31.278973, 31.278968, 31.27896, 31.278949, 31.278928, 31.27892, 31.278912, 31.278904, 31.278896, 31.278888, 31.278872, 31.278861, 31.278823, 31.278808, 31.278784, 31.278754, 31.27873, 31.278709, 31.27869]

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

