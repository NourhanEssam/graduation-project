/**
 * Created by Eslam on 2016-11-27.
 */
var marker, geoMarker;
var geoCircle;
var currentPos;
var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644}, // TODO set default map center
        zoom: 15
    });

    navigateToCurrentLocation();

    map.addListener("click", function (event) {
        addMarker(event.latLng, map);
    });
}

// center the map at the current location
function navigateToCurrentLocation() {
    var infoWindow = new google.maps.InfoWindow({map: map});
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(function (position) {
            currentPos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            map.setCenter(currentPos);

            if (geoCircle != null)
            {
                geoCircle.setMap(null);
            }
            if (geoMarker != null) {
                geoMarker.setMap(null);
            }
            geoCircle = new google.maps.Circle({
                center: currentPos,
                radius: position.coords.accuracy,
                map: map,
                fillColor: '#0000FF',
                fillOpacity: 0.2,
                strokeColor: '#0000FF',
                strokeOpacity: 0.5,
                strokeWeight: 0.8
            });
            geoCircle.setMap(map);
            geoMarker = new google.maps.Marker({
                position: currentPos,
                icon: {
                    path: google.maps.SymbolPath.CIRCLE,
                    fillColor: '#0000FF',
                    fillOpacity: 0.5,
                    strokeWeight: 0,
                    scale: 8
                },
                map: map,
                title: 'Current Location'
            });
            geoMarker.setMap(map);
            console.log('Source: ' + currentPos.lat() + ', ' + currentPos.lng());

        }, function () {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
}

// adds destination marker on click event
function addMarker(location) {
    if (marker != null)
    {
        marker.setMap(null);
    }
    marker = new google.maps.Marker({
        position: location,
        map: map,
        title: 'Destination'
    });
    marker.setMap(map);
    console.log('Destination: ' + location.lat() + ', ' + location.lng());
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');
}