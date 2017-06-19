/**
 * Created by Eslam on 2016-11-27.
 */
var directionsDisplay;
var directionsService;
var geoMarker;
var geoCircle;
var currentPos;
var map;

var timer = null;

// initial function called by the google maps api
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644}, // TODO set default map center
        zoom: 15
    });

    navigateToCurrentLocation();

    map.addListener("click", function (event) {
        calcRoute(event.latLng);
    });
}

// center the map at the current location
function navigateToCurrentLocation() {
    directionsService = new google.maps.DirectionsService();
    directionsDisplay = new google.maps.DirectionsRenderer();

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

            directionsDisplay.setMap(map);

        }, function () {
            handleLocationError(true);
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false);
    }
}

function calcRoute(location) {
    var request = {
        origin: currentPos,
        destination: location,
        travelMode: 'DRIVING'
    };
    directionsService.route(request, function (result, status) {
        if (status == 'OK') {
            console.log(result);
            directionsDisplay.setDirections(result);
        }
        else {
            console.log(status);
        }
    });

    $.ajax({
        // points to the url where your data will be posted
        url: '',
        // post for security reason
        type: "POST",
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        // data that you will like to return
        data: {
            currentPosLat: currentPos.lat(),
            currentPosLng: currentPos.lng(),
            targetLat: location.lat(),
            targetLng: location.lng()
        },
        complete: function () {
            console.log("complete calcRoute");
            if(timer != null)
            {
                clearTimeout(timer);
            }
            // schedule the first invocation:
            timer = setTimeout(detectLocationPeriodically, 10000);
        },
        // what to do when there is an error
        error: function (xhr, textStatus, thrownError) {
            console.log(xhr);
            console.log(textStatus);
            console.log(thrownError);
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function handleLocationError(browserHasGeolocation) {
    var infoWindow = new google.maps.InfoWindow({map: map});
    infoWindow.setPosition(map.getCenter());
    infoWindow.setContent(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');

}

function detectLocationPeriodically() {
    console.log("called");
    $.ajax({
        url: '/controller/',
        type: 'POST',
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        data: {
            currentPosLat: currentPos.lat(),
            currentPosLng: currentPos.lng()
        },
        // what to do when the call is complete ( you can right your clean from code here)
        complete: function () {
            console.log("complete");
            setTimeout(detectLocationPeriodically, 10000);
        },
        // what to do when there is an error
        error: function (xhr, textStatus, thrownError) {
            console.log("error");
            console.log(xhr);
            console.log(textStatus);
            console.log(thrownError);
        }
    });
}