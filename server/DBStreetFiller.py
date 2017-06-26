import urllib2
import xmltodict
import time

start_time = time.time()
street_list = []
Kolleya_Origin_lat=30.064410
Kolleya_Origin_lng=31.278965

def Get_Streets(lat=30.064410,lng=31.278965,username="micheltls"):

    service_url = "http://api.geonames.org/findNearbyStreetsOSM?lat=" + str(lat) +\
                  "&lng=" + str(lng) + "&username=" + username + "&radius=1"

    response = urllib2.urlopen(service_url)
    xml_response = response.read()
    i=1
    dict_response = xmltodict.parse(xml_response)
    for line in dict_response['geonames']['streetSegment']:
        for coords in line['line'].split(","):
            print i
            i +=1
            lng=coords.split()[0]
            lat=coords.split()[1]
            reverse_url = "https://maps.googleapis.com/maps/api/geocode/xml?&latlng="+str(lat)+","+str(lng)
            try:
                reverse_response = urllib2.urlopen(reverse_url)
            except urllib2.URLError:
                continue
            xml_response = xmltodict.parse(reverse_response.read())
            try :
                street_name = xml_response['GeocodeResponse']['result'][0]['formatted_address'].split(",")[0]
                while street_name[0].isdigit():
                    street_name = street_name[street_name.find(" ")+1:]
                if (street_list.count(street_name) == 0 ):
                    street_list.append(street_name)
                    print street_name

            except KeyError:
                print xml_response['GeocodeResponse']
                continue


    '''
    #example = dict_response['geonames']['streetSegment'][0]['line'].split(",")[0].split()
    print(example)
    print service_url

    reverse_url = "https://maps.googleapis.com/maps/api/geocode/xml?&latlng="+str(example[1])+","+str(example[0])
    reverse_response = urllib2.urlopen(reverse_url)

    xml_response = xmltodict.parse(reverse_response.read())
    print reverse_url
    print xml_response['GeocodeResponse']['result'][0]['formatted_address']
    '''
Get_Streets(lat=Kolleya_Origin_lat,lng=Kolleya_Origin_lng)
print 1
Get_Streets(lat=Kolleya_Origin_lat+0.005,lng=Kolleya_Origin_lng+0.005)
print 2
Get_Streets(lat=Kolleya_Origin_lat+0.005,lng=Kolleya_Origin_lng)
print 3
Get_Streets(lat=Kolleya_Origin_lat,lng=Kolleya_Origin_lng+0.005)
print 4
Get_Streets(lat=Kolleya_Origin_lat-0.005,lng=Kolleya_Origin_lng)
print 5
Get_Streets(lat=Kolleya_Origin_lat,lng=Kolleya_Origin_lng-0.005)
print 6
Get_Streets(lat=Kolleya_Origin_lat-0.005,lng=Kolleya_Origin_lng+0.005)
print 7
Get_Streets(lat=Kolleya_Origin_lat+0.005,lng=Kolleya_Origin_lng-0.005)
print 8
for i in street_list:
    print i
print("--- %s seconds ---" % (time.time() - start_time))
