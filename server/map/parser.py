import math
import re
import simplejson as json


def calculate_initial_compass_bearing(pointA, pointB):
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180 to + 180 which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


def parse_directions(directions):
    Output = []
    Head_Flag = True
    JSON = json.loads(directions)

    for STEP in JSON['routes'][0]['legs'][0]['steps']:

        HTML_Response = STEP['html_instructions']

        # if these keywords wasn't found, then no street names in this step, skip!
        if not re.findall(r"( on )|( onto )|( to )|( toward )|( the )(<b>)", HTML_Response):
            continue
        # as long as these keywords exists, keep extracting the street names.
        while re.findall(r"( on )|( onto )|( to )|( toward )|( the )(<b>)", HTML_Response):
            # index of each keyword
            on = HTML_Response.find(' on <b>')
            onto = HTML_Response.find(' onto <b>')
            to = HTML_Response.find(' to <b>')
            toward = HTML_Response.find(' toward <b>')

            # if not found make it 999 ( biggest)
            if on < 0:
                on = 999
            if onto < 0:
                onto = 999
            if to < 0:
                to = 999
            if toward < 0:
                toward = 999

            # start extracting with the first occurrence of keywords ( minimal index )
            # remove characters from html response, from the beginning till the first occurance
            HTML_Response = HTML_Response[min(on, onto, to, toward) + 2:]
            # Concatenate street name to output, after the occurance of <b> till the occurance of </b>
            Output += [HTML_Response[HTML_Response.find('<b>') + 3:  HTML_Response.find('</b>')]]
            # remove the street name from the html response to loop for the next street name
            HTML_Response = HTML_Response[HTML_Response.find('</b>') + 4:]

        # calculating the direction (E,N,W,S,NE,NW,SE,SW)
        end_loc = STEP['end_location']
        start_loc = STEP['start_location']
        # calculating the Bearing between the two points ( Bearing is the angel from the south CW )
        Bearing = calculate_initial_compass_bearing((end_loc['lat'], end_loc['lng']),
                                                    (start_loc['lat'], start_loc['lng']))
        # Assigning the direction based on the bearing
        if 0 < Bearing < 22.5:
            Output += ['S']
        elif 22.5 <= Bearing < 67.5:
            Output += ['SW']
        elif 67.5 <= Bearing < 112.5:
            Output += ['W']
        elif 112.5 <= Bearing < 157.5:
            Output += ['NW']
        elif 157.5 <= Bearing < 202.5:
            Output += ['N']
        elif 202.5 <= Bearing < 247.5:
            Output += ['NE']
        elif 247.5 <= Bearing < 292.5:
            Output += ['E']
        elif 292.5 <= Bearing < 337.5:
            Output += ['SE']
        elif 337.5 <= Bearing < 382.5:
            Output += ['S']

    if (Output[1] not in ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]):
        Output.pop(1)
    if (Output.count("")):
        Output.remove("")

    return Output
