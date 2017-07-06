#  playground map
#  -------top--------
#  |                |
#  |                |
# left            right
#  |                |
#  |                |
#  ------bottom------


def scale(lat, lon):
    if 30.063700 <= lat <= 30.064000 and 31.278300 <= lon <= 31.278900:  # top
        new_lat = mapping(lat, 30.066401, 30.065393, 30.063930, 30.063754)
        new_lon = mapping(lon, 31.279903, 31.276954, 31.278853, 31.278349)
        print "scaled lat:", new_lat
        print "scaled lon:", new_lon

    elif 30.063300 <= lat <= 30.064000 and 31.278800 <= lon <= 31.279500:  # right
        new_lat = mapping(lat, 30.066401, 30.063582, 30.063930, 30.063306)
        new_lon = mapping(lon, 31.279903, 31.281198, 31.278853, 31.279169)
        print "scaled lat:", new_lat
        print "scaled lon:", new_lon

    elif 30.063100 <= lat <= 30.063350 and 31.278600 <= lon <= 31.279500:  # bottom
        new_lat = mapping(lat, 30.063582, 30.062512, 30.063306, 30.063151)
        new_lon = mapping(lon, 31.281198, 31.278189, 31.279169, 31.278628)
        print "scaled lat:", new_lat
        print "scaled lon:", new_lon

    elif 30.063100 <= lat <= 30.063800 and 31.278300 <= lon <= 31.278700:  # left
        new_lat = mapping(lat, 30.065393, 30.062512, 30.063754, 30.063151)
        new_lon = mapping(lon, 31.276954, 31.278189, 31.278349, 31.278628)
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
