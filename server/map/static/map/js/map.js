/**
 * Created by Eslam on 2016-11-27.
 */
var directionsDisplay;
var directionsService;
var geoMarker;
var geoCircle;
var currentPos;
var map;

var searchMarker;

var timer = null;

// initial function called by the google maps api
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 30.0444, lng: 31.2357}, // TODO set default map center
        zoom: 15
    });

    navigateToCurrentLocation();

    var card = document.getElementById('pac-card');
    var input = document.getElementById('pac-input');

    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

    var autocomplete = new google.maps.places.Autocomplete(input);

    // Bind the map's bounds (viewport) property to the autocomplete object,
    // so that the autocomplete requests use the current map bounds for the
    // bounds option in the request.
    autocomplete.bindTo('bounds', map);

    // Autocomplete types
    autocomplete.setTypes([]);

    var infowindow = new google.maps.InfoWindow();
    var infowindowContent = document.getElementById('infowindow-content');
    infowindow.setContent(infowindowContent);

    // place marker
    searchMarker = new google.maps.Marker({
        map: map,
        anchorPoint: new google.maps.Point(0, -29)
    });

    autocomplete.addListener('place_changed', function () {
        infowindow.close();
        searchMarker.setVisible(false);
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }

        // If the place has a geometry, then present it on a map.
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(15);
        }
        searchMarker.setPosition(place.geometry.location);
        searchMarker.setVisible(true);

        var address = '';
        if (place.address_components) {
            address = [
                (place.address_components[0] && place.address_components[0].short_name || ''),
                (place.address_components[1] && place.address_components[1].short_name || ''),
                (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
        }

        infowindowContent.children['place-icon'].src = place.icon;
        infowindowContent.children['place-name'].textContent = place.name;
        infowindowContent.children['place-address'].textContent = address;
        infowindow.open(map, searchMarker);
    });

    // map onclick event handler
    map.addListener("click", function (event) {
        searchMarker.setVisible(false);
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
            // draw circle around current position
            geoCircle = new google.maps.Circle({
                center: currentPos,
                radius: position.coords.accuracy,
                map: map,
                fillColor: '#0000FF',
                fillOpacity: 0.1,
                strokeWeight: 0
            });
            geoCircle.setMap(map);
            geoMarker = new google.maps.Marker({
                position: currentPos,
                icon: {
                    path: google.maps.SymbolPath.CIRCLE,
                    fillColor: '#0000FF',
                    fillOpacity: 0.5,
                    strokeWeight: 2,
                    strokeColor: '#FFFFFF',
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

// display directions on the Map and send the coordinates to the map view
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
            if(timer)
            {
                clearInterval(timer);
            }
            // schedule the first invocation:
            timer = setInterval(detectLocationPeriodically, 10000);
        },
        // what to do when there is an error
        error: function (xhr, textStatus, thrownError) {
            console.log(xhr);
            console.log(textStatus);
            console.log(thrownError);
        }
    });
}

// Send GPS location to the controller
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

// Cookies for the csrf token
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

// message to be displayed if GPS is not found
function handleLocationError(browserHasGeolocation) {
    var infoWindow = new google.maps.InfoWindow({map: map});
    infoWindow.setPosition(map.getCenter());
    infoWindow.setContent(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');

}