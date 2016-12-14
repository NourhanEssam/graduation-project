from django.shortcuts import render
from __future__ import unicode_literals
import codecs,re,math
import simplejson as json
from django.apps import AppConfig
from compassbearing import calculate_initial_compass_bearing
# Create your views here.



def ParserFn():
    #Read JSON response from a file, can be modified to be called with an input instead.
    response = codecs.open("JSON Response.txt","r",encoding='utf-8',errors='ignore').read()

    Output = []

    JSON = json.loads(response)

    for STEP in JSON['routes'][0]['legs'][0]['steps']:

        HTML_Response = STEP['html_instructions']

        #if these keywords wasn't found, then no street names in this step, skip!
        if (not re.findall(r"( on )|( onto )|( to )|( toward )|( the )(<b>)",HTML_Response)):
            continue
        #as long as these keywords exists, keep extracting the street names.
        while (re.findall(r"( on )|( onto )|( to )|( toward )|( the )(<b>)",HTML_Response)):
            #index of each keyword
            on = HTML_Response.find(' on <b>')
            onto = HTML_Response.find(' onto <b>')
            to = HTML_Response.find(' to <b>')
            toward = HTML_Response.find(' toward <b>')

            #if not found make it 999 ( biggest)
            if (on<0):
                on = 999
            if(onto<0):
                onto = 999
            if(to<0):
                to = 999
            if(toward<0):
                toward = 999

            #start extracting with the first occurance of keywords ( minimal index )
            #remove characters from html response, from the beginning till the first occurance
            HTML_Response=HTML_Response[min(on,onto,to,toward)+2:]
            #Concatinate street name to output, after the occurance of <b> till the occurance of </b>
            Output += [   HTML_Response[ HTML_Response.find('<b>')+3  :  HTML_Response.find('</b>') ]        ]
            #remove the street name from the html response to loop for the next street name
            HTML_Response = HTML_Response[HTML_Response.find('</b>')+4:]

        #calculating the direction (E,N,W,S,NE,NW,SE,SW)
        end_loc = STEP['end_location']
        start_loc = STEP['start_location']
        #calculating the Bearing between the two points ( Bearing is the angel from the south CW )
        Bearing = calculate_initial_compass_bearing((end_loc['lat'],end_loc['lng']),(start_loc['lat'],start_loc['lng']))
        #Assigning the direction based on the bearing
        if(0<Bearing<22.5):Output+=['N']
        elif(22.5<=Bearing<67.5):Output+=['NE']
        elif(67.5<=Bearing<112.5):Output+=['E']
        elif(112.5<=Bearing<157.5):Output+=['SE']
        elif(157.5<=Bearing<202.5):Output+=['S']
        elif(202.5<=Bearing<247.5):Output+=['SW']
        elif(247.5<=Bearing<292.5):Output+=['W']
        elif(292.5<=Bearing<337.5):Output+=['NW']
        elif(337.5<=Bearing<382.5):Output+=['N']

    #removing empty lines which I have no Idea why the occur, and the 2nd element as it's redundant.
    Output.pop(1)
    Output.remove("")


    #print the output to test it, will be deleted later to return it or write it in a file.
    for STEP in Output:
        print STEP

    return Output


#Running the function ( for testing )
ParserFn()