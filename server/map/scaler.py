#  playground map
#  -------top--------
#  |                |
#  |                |
# left            right
#  |                |
#  |                |
#  ------bottom------


# def scale(lat, lon):
#     if 30.063700 <= lat <= 30.064000 and 31.278300 <= lon <= 31.278900:  # top
#         new_lat = mapping(lat, 30.066401, 30.065393, 30.063930, 30.063754)
#         new_lon = mapping(lon, 31.279903, 31.276954, 31.278853, 31.278349)
#         new_lat, new_lon = avoid_indoors(new_lat, new_lon)
#         print "scaled lat:", new_lat
#         print "scaled lon:", new_lon
#
#     elif 30.063300 <= lat <= 30.064000 and 31.278800 <= lon <= 31.279500:  # right
#         new_lat = mapping(lat, 30.066401, 30.063582, 30.063930, 30.063306)
#         new_lon = mapping(lon, 31.279903, 31.281198, 31.278853, 31.279169)
#         new_lat, new_lon = avoid_indoors(new_lat, new_lon)
#         print "scaled lat:", new_lat
#         print "scaled lon:", new_lon
#
#     elif 30.063100 <= lat <= 30.063350 and 31.278600 <= lon <= 31.279500:  # bottom
#         new_lat = mapping(lat, 30.063582, 30.062512, 30.063306, 30.063151)
#         new_lon = mapping(lon, 31.281198, 31.278189, 31.279169, 31.278628)
#         new_lat, new_lon = avoid_indoors(new_lat, new_lon)
#         print "scaled lat:", new_lat
#         print "scaled lon:", new_lon
#
#     elif 30.063100 <= lat <= 30.063800 and 31.278300 <= lon <= 31.278700:  # left
#         new_lat = mapping(lat, 30.065393, 30.062512, 30.063754, 30.063151)
#         new_lon = mapping(lon, 31.276954, 31.278189, 31.278349, 31.278628)
#         new_lat, new_lon = avoid_indoors(new_lat, new_lon)
#         print "scaled lat:", new_lat
#         print "scaled lon:", new_lon
#
#     else:
#         return lat, lon
#
#     return new_lat, new_lon

I1 = {'lat': 30.063780, 'lon': 31.278302}
I2 = {'lat': 30.063984, 'lon': 31.278881}
I3 = {'lat': 30.063302, 'lon': 31.279198}
I4 = {'lat': 30.063116, 'lon': 31.278640}

OI1 = {'lat': 30.062531, 'lon': 31.278146}
OI2 = {'lat': 30.063590, 'lon': 31.281129}
OI3 = {'lat': 30.062819, 'lon': 31.281547}
OI4 = {'lat': 30.061737, 'lon': 31.278505}


def scale(lat, lon):
    if I1['lat'] <= lat <= I2['lat'] and I1['lon'] <= lon <= I2['lon']:  # top
        new_lat = mapping(lat, OI1['lat'], OI2['lat'], I1['lat'], I2['lat'])
        new_lon = mapping(lon, OI1['lon'], OI2['lon'], I1['lon'], I2['lon'])
        print "scaled lat:", new_lat
        print "scaled lon:", new_lon

    elif I3['lat'] <= lat <= I2['lat'] and I2['lon'] <= lon <= I3['lon']:  # right
        new_lat = mapping(lat, OI2['lat'], OI3['lat'], I2['lat'], I3['lat'])
        new_lon = mapping(lon, OI2['lon'], OI3['lon'], I2['lon'], I3['lon'])
        print "scaled lat:", new_lat
        print "scaled lon:", new_lon

    elif I4['lat'] <= lat <= I3['lat'] and I4['lon'] <= lon <= I3['lon']:  # bottom
        new_lat = mapping(lat, OI3['lat'], OI4['lat'], I3['lat'], I4['lat'])
        new_lon = mapping(lon, OI3['lon'], OI4['lon'], I3['lon'], I4['lon'])
        print "scaled lat:", new_lat
        print "scaled lon:", new_lon

    elif I4['lat'] <= lat <= I1['lat'] and I1['lon'] <= lon <= I4['lon']:  # left
        new_lat = mapping(lat, OI4['lat'], OI1['lat'], I4['lat'], I1['lat'])
        new_lon = mapping(lon, OI4['lon'], OI1['lon'], I4['lon'], I1['lon'])
        print "scaled lat:", new_lat
        print "scaled lon:", new_lon

    else:
        return lat, lon

    return new_lat, new_lon

def rotate(directions):
    for i in range(len(directions)):
        if directions[i] == 'NE':
            directions[i] = 'E'
        elif directions[i] == 'SE':
            directions[i] = 'S'
        elif directions[i] == 'SW':
            directions[i] = 'W'
        elif directions[i] == 'NW':
            directions[i] = 'N'

    return directions


def mapping(input_coord, Street_P1, Street_P2, Playground_P1, PlaygroundP2):
    Street_diff = Street_P1 - Street_P2
    Playground_diff = Playground_P1 - PlaygroundP2
    slope = Street_diff / Playground_diff
    return slope * (input_coord - PlaygroundP2) + Street_P2


def avoid_indoors(lat, lon):
    if 30.065846 <= lat <= 30.065911 and 31.278203 <= lon <= 31.278353:  # gate 1
        return 30.065906, 31.278367
    elif 30.064555 <= lat <= 30.064671 and 31.277281 <= lon <= 31.277302:  # gate 2
        return 30.064685, 31.277257
    elif 30.063831 <= lat <= 30.063970 and 31.277550 <= lon <= 31.277614:  # gate 3
        return 30.063961, 31.277560
    elif 30.063214 <= lat <= 30.063335 and 31.280350 <= lon <= 31.280436:  # gate 4
        return 30.063246, 31.280290
    elif 30.064820 <= lat <= 30.064950 and 31.280491 <= lon <= 31.280523: # gate 5
        return 30.064987, 31.280470
    else:
        return lat, lon


