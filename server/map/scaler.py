#  playground map
#  -------top--------
#  |                |
#  |                |
# left            right
#  |                |
#  |                |
#  ------bottom------


def scale(lat, lon):
    if 30.063700 <= lat <= 30.064300 and 31.278300 <= lon <= 31.279900:  # top
        new_lat = mapping(lat, 30.066401, 30.065393, 30.064289, 30.063754)
        new_lon = mapping(lon, 31.279903, 31.276954, 31.279833, 31.278349)
        print "scaled lat:", new_lat
        print "scaled lon:", new_lon

    elif 30.063600 <= lat <= 30.064300 and 31.279800 <= lon <= 31.280150:  # right
        new_lat = mapping(lat, 30.066401, 30.063582, 30.064289, 30.063685)
        new_lon = mapping(lon, 31.279903, 31.281198, 31.279833, 31.280112)
        print "scaled lat:", new_lat
        print "scaled lon:", new_lon

    elif 30.063100 <= lat <= 30.063700 and 31.278600 <= lon <= 31.280150:  # bottom
        new_lat = mapping(lat, 30.063582, 30.062512, 30.063685, 30.063151)
        new_lon = mapping(lon, 31.281198, 31.278189, 31.280112, 31.278628)
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
