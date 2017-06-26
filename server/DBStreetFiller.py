import urllib2,xmltodict,os

street_list = []
Kolleya_Origin_lat=30.064410
Kolleya_Origin_lng=31.278965

def Write_model(StreetName,StartLng,StartLat,EndLng,EndLat):
    outputfile.write("\n  {\n    \"model\": \"gettrafficlights.street\",\n    \"pk\": \"")
    outputfile.write(StreetName+"\",\n    \"fields\":\n    {\n      \"Start_Longitude\": ")
    outputfile.write(StartLng+",\n      \"Start_Latitude\": ")
    outputfile.write(StartLat+",\n      \"End_Longitude\": ")
    outputfile.write(EndLng+  ",\n      \"End_Latitude\": ")
    outputfile.write(EndLat+"\n    }\n  },")

def Get_Streets(lat=30.064410,lng=31.278965,username="micheltls"):

    service_url = "http://api.geonames.org/findNearbyStreetsOSM?lat=" + str(lat) +\
                  "&lng=" + str(lng) + "&username=" + username + "&radius=1"
    print "Getting all street names ..."
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
            reverse_url = "https://maps.googleapis.com/maps/api/geocode/xml?&latlng="+str(lat)+","+str(lng)+ \
                "&key=AIzaSyCjYtjT-xGAZ-sdjDeQTAMULD_deVuW20k"
            try:
                print "Reversing ..."
                reverse_response = urllib2.urlopen(reverse_url)
                print "Reversed"
            except urllib2.URLError:
                continue
            xml_response = xmltodict.parse(reverse_response.read())
            try :
                street_name = xml_response['GeocodeResponse']['result'][0]['formatted_address'].split(",")[0]
            except KeyError:
                print xml_response['GeocodeResponse']
                continue
            while street_name[0].isdigit():
                street_name = street_name[street_name.find(" ")+1:]
            if (street_list.count(street_name) == 0 ):
                street_list.append(street_name)
                geocode_service_url="https://maps.googleapis.com/maps/api/geocode/xml?address="+\
                    xml_response['GeocodeResponse']['result'][0]['formatted_address'].replace(" ","%20")+\
                    "&key=AIzaSyCjYtjT-xGAZ-sdjDeQTAMULD_deVuW20k"
                print "Geocoding ..."
                try:
                    geocode_response = urllib2.urlopen(geocode_service_url).read()
                except urllib2.URLError:
                    print "ERR Geocoding"
                except UnicodeEncodeError:
                    print "ERR Geocoding"
                print "Geocoded"
                try:
                    bounds =  xmltodict.parse(geocode_response)['GeocodeResponse']['result']['geometry']['bounds']
                except TypeError:
                    print xmltodict.parse(geocode_response)['GeocodeResponse']['result']
                except KeyError:
                    print xmltodict.parse(geocode_response)['GeocodeResponse']['result']
                start = bounds['northeast']
                end =   bounds['southwest']
                Write_model(street_name,start['lng'],start['lat'],end['lng'],end['lat'])
            else:
                print "Again?"




outputfile = open("gettrafficlights/fixtures/data2.json",mode='w')
outputfile.write("[")

Get_Streets(lat=Kolleya_Origin_lat,lng=Kolleya_Origin_lng)
print 1*1000
Get_Streets(lat=Kolleya_Origin_lat+0.005,lng=Kolleya_Origin_lng+0.005)
print 2*1000
Get_Streets(lat=Kolleya_Origin_lat+0.005,lng=Kolleya_Origin_lng)
print 3*1000
Get_Streets(lat=Kolleya_Origin_lat,lng=Kolleya_Origin_lng+0.005)
print 4*1000
Get_Streets(lat=Kolleya_Origin_lat-0.005,lng=Kolleya_Origin_lng)
print 5*1000
Get_Streets(lat=Kolleya_Origin_lat,lng=Kolleya_Origin_lng-0.005)
print 6*1000
Get_Streets(lat=Kolleya_Origin_lat-0.005,lng=Kolleya_Origin_lng+0.005)
print 7*1000
Get_Streets(lat=Kolleya_Origin_lat+0.005,lng=Kolleya_Origin_lng-0.005)
print 8*1000


outputfile.seek(-1,os.SEEK_CUR)
outputfile.write("\n]")
outputfile.close()
