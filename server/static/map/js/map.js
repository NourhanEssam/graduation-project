/**
 * Created by Eslam on 2016-11-27.
 */
var directionsDisplay;
var directionsService;
var geoMarker;
var geoCircle;
var currentPos;
var Location = null;
var map;

var searchMarker;

var timer = null;
var timerNoGeo = null;
var TestMode = true;

var TestTimer1 = null;
var TestTimer2 = null;
var TestTimer3 = null;

var time = 5000;

// initial function called by the google maps api
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 30.0444, lng: 31.2357}, // TODO set default map center
        zoom: 18
    });

    navigateToCurrentLocation();

    var card = document.getElementById('pac-card');
    var input = document.getElementById('pac-input');

    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

    var autocomplete = new google.maps.places.Autocomplete(input);

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
            map.setZoom(17);
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

}

// center the map at the current location
function navigateToCurrentLocation() {
    directionsService = new google.maps.DirectionsService();
    directionsDisplay = new google.maps.DirectionsRenderer();

    if (TestMode) {
        testSystem();
    }
    else {
        // map onclick event handler
        map.addListener("click", function (event) {
            searchMarker.setVisible(false);
            Location = event.latLng;
            calcRoute();
        });

        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                map.setCenter(position);
            });
            navigator.geolocation.watchPosition(function (position) {
                currentPos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                drawLocationCenter(currentPos.lat(), currentPos.lng(), currentPos.accuracy);

            }, function () {
                handleMissingGeolocation();
            });
        } else {
            // Browser doesn't support Geolocation
            handleMissingGeolocation();
        }
    }
}

// display directions on the Map and send the coordinates to the map view
function calcRoute() {
    var request = {
        origin: currentPos,
        destination: Location,
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
            targetLat: Location.lat(),
            targetLng: Location.lng()
        },
        success: function () {
            console.log("success calcRoute");
            if (timer) {
                clearInterval(timer);
            }
            // schedule the first invocation:
            timer = setInterval(detectLocationPeriodically, 10000);
        },
        // what to do when there is an error
        error: function (xhr, textStatus, thrownError) {
            console.log(textStatus);
            console.log(thrownError);
        }
    });

}

// --------------------- no GeoLocation Service --------------------

function handleMissingGeolocation() {
    $.ajax({
        url: "/location/?key=driver",
        type: "GET",
        dataType: "text",
        crossDomain: true,
        success: function (response) {
            var context = JSON.parse(response);
            console.log('lon: ' + context.lon + ' lat: ' + context.lat + ' error: ' + context.err + 'm');
            drawLocationCenter(context.lat, context.lon, parseFloat(context.err));
            map.setCenter(new google.maps.LatLng(context.lat, context.lon));
            if (timerNoGeo) {
                clearInterval(timerNoGeo);
            }
            timerNoGeo = setInterval(getLocationPeriodically, 500);
        },
        error: function (xhr, textStatus, thrownError) {
            handleLocationError();
            console.log(textStatus);
            console.log(thrownError);
        }
    });
}

function drawLocationCenter(lat, lon, accuracy) {
    currentPos = new google.maps.LatLng(lat, lon);

    if (geoCircle != null) {
        geoCircle.setMap(null);
    }
    if (geoMarker != null) {
        geoMarker.setMap(null);
    }
    // draw circle around current position
    geoCircle = new google.maps.Circle({
        center: currentPos,
        radius: accuracy,
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
    console.log('Source: ' + lat + ', ' + lon);
    directionsDisplay.setMap(map);
}

// ---------------------- Testing Methods ---------------------------
function testSystem() {
    currentPos = new google.maps.LatLng(0.0, 0.0);
    console.log("in testsystem");
    if(TestTimer1 == null)
    {
        TestTimer1 = setInterval(waitForSource, time);
    }
}

function waitForSource() {
    if (TestTimer2 == null) {
        $.ajax({
            url: "/location/?key=driver",
            type: "GET",
            dataType: "text",
            cache: false,
            // what to do when the call is complete ( you can right your clean from code here)
            success: function (response) {
                var context = JSON.parse(response);
                if (context.lon != 0.0 && context.lat != 0.0) {
                    console.log("Source: " + context.lat + ", " + context.lon);
                    currentPos = new google.maps.LatLng(context.lat, context.lon);
                    map.setCenter(currentPos);
                    clearInterval(TestTimer1);
                    drawLocationCenter(context.lat, context.lon, parseFloat(context.err));
                    TestTimer2 = setInterval(waitForDestination, time);
                }
            },
            // what to do when there is an error
            error: function (xhr, textStatus, thrownError) {
                console.log(textStatus);
                console.log(thrownError);
            }
        });
    }
}

function waitForDestination() {
    if(TestTimer3 == null) {
        $.ajax({
            url: "/location/?key=driver",
            type: "GET",
            dataType: "text",
            cache: false,
            // what to do when the call is complete ( you can right your clean from code here)
            success: function (response) {
                var context = JSON.parse(response);
                Location = new google.maps.LatLng(context.lat, context.lon);
                if (Location.lng() != currentPos.lng() && Location.lat() != currentPos.lat()) {
                    console.log("Destination: " + context.lat + ", " + context.lon);
                    clearInterval(TestTimer2);
                    calcRoute();
                    TestTimer3 = setInterval(waitForSteps, 10000);
                }
            },
            // what to do when there is an error
            error: function (xhr, textStatus, thrownError) {
                console.log(textStatus);
                console.log(thrownError);
            }
        });
    }
}

function waitForSteps() {
    $.ajax({
        url: "/location/?key=driver",
        type: "GET",
        dataType: "text",
        cache: false,
        // what to do when the call is complete ( you can right your clean from code here)
        success: function (response) {
            var context = JSON.parse(response);
            var pos = new google.maps.LatLng(context.lat, context.lon);
            if (pos.lng() != currentPos.lng() && pos.lat() != currentPos.lat()) {
                console.log("Step: " + context.lat + ", " + context.lon);
                pos = new google.maps.LatLng(context.lat, context.lon);
                currentPos = pos;
                drawLocationCenter(context.lat, context.lon, parseFloat(context.err));
            }
        },
        // what to do when there is an error
        error: function (xhr, textStatus, thrownError) {
            console.log(textStatus);
            console.log(thrownError);
        }
    });
}

// ---------------------- periodic functions ----------------------------

// Send GPS location to the controller
function detectLocationPeriodically() {
    console.log("called");
    $.ajax({
        url: '/controller/',
        type: 'POST',
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        cache: false,
        data: {
            currentPosLat: currentPos.lat(),
            currentPosLng: currentPos.lng()
        },
        // what to do when the call is complete ( you can right your clean from code here)
        success: function () {
            console.log("send to controller");
        },
        // what to do when there is an error
        error: function (xhr, textStatus, thrownError) {
            console.log(textStatus);
            console.log(thrownError);
        }
    });
}

function getLocationPeriodically() {
    $.ajax({
        url: "/location/?key=driver",
        type: "GET",
        dataType: "text",
        crossDomain: true,
        cache: false,
        success: function (response) {
            var context = JSON.parse(response);
            console.log('lon: ' + context.lon + ' lat: ' + context.lat + ' error: ' + context.err + 'm');
            drawLocationCenter(context.lat, context.lon, parseFloat(context.err));
            currentPos = new google.maps.LatLng(context.lat, context.lon);
        },
        error: function (xhr, textStatus, thrownError) {
            handleLocationError();
            console.log(textStatus);
            console.log(thrownError);
        }
    });
}

// -------------------------- utilities ------------------------------

// message to be displayed if GPS is not found
function handleLocationError() {
    var infoWindow = new google.maps.InfoWindow({map: map});
    infoWindow.setPosition(map.getCenter());
    infoWindow.setContent('Error: The Geolocation service failed.');
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