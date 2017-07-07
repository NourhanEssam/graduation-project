import math


# approximate radius of earth in km
R = 6371000.0

# tolerance
tol = 3


def get_distance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    diff_lon = lon1 - lon2
    diff_lat = lat1 - lat2

    # Haversine formula
    a = math.sin(diff_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(diff_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def passed_tl(EVLocation, TLLocation, direction):
    diff = {
        'lon': EVLocation['lon'] - TLLocation['lon'],
        'lat': EVLocation['lat'] - TLLocation['lat']
    }

    distance = get_distance(EVLocation['lat'], EVLocation['lon'], TLLocation['lat'], TLLocation['lon'])

    if distance > tol:
        if direction == "N":
            if diff['lat'] > 0:
                return True

        elif direction == "E":
            if diff['lon'] > 0:
                return True

        elif direction == "S":
            if diff['lat'] < 0:
                return True

        elif direction == "W":
            if diff['lon'] < 0:
                return True

        elif direction == "NE":
            if diff['lat'] > 0 and diff['lon'] > 0:
                return True

        elif direction == "NW":
            if diff['lat'] > 0 and diff['lon'] < 0:
                return True

        elif direction == "SE":
            if diff['lat'] < 0 and diff['lon'] > 0:
                return True

        elif direction == "SW":
            if diff['lat'] < 0 and diff['lon'] < 0:
                return True

    return False
