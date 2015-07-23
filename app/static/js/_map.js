'use strict';

var map = (function(L, $) {
    var ACCESS_TOKEN = 'pk.eyJ1IjoibWFwYm94IiwiYSI6IjZjNmRjNzk3ZmE2MTcwOTEwMGY0MzU3YjUzOWFmNWZhIn0.Y8bhBaUMqFiPrDRW9hieoQ',
        MB_ATTR = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
                '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        MB_URL = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + ACCESS_TOKEN,
        OSM_URL = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        OSM_ATTRIB = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        _map,
        pointLayer,
        userLocationShown = false,
        popup=L.popup(),
        userLat=Number.NaN,
        userLng=Number.NaN;

    var CustomIcon = L.Icon.extend({
        options: {
            shadowUrl: '/static/images/leaflet/marker-shadow.png',
            shadowAnchor: [1, 41],
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
        }
    });

    var blackIcon = new CustomIcon({iconUrl: '/static/images/leaflet/marker-black.png'}),
        redIcon = new CustomIcon({iconUrl: '/static/images/leaflet/marker-red.png'}),
        yellowIcon = new CustomIcon({iconUrl: '/static/images/leaflet/marker-yellow.png'}),
        blueIcon = new CustomIcon({iconUrl: '/static/images/leaflet/marker-blue.png'}),
        userIcon = new CustomIcon({iconUrl: '/static/images/leaflet/marker-user.png'});


    // TEST ONLY
    var points = [
        {id: 1, lat: 50.05346, lng: 19.8535, priority: 1, name: 'Name of the task, bla bla', dateDue: '30.07.2015'},
        {id: 2, lat: 50.03597, lng: 20.04627, priority: 2, name: 'Name of the task, bla bla', dateDue: '30.07.2015'},
        {id: 3, lat: 50.04762, lng: 19.94637, priority: 3, name: 'Name of the task, bla bla', dateDue: '30.07.2015'},
        {id: 4, lat: 50.04773, lng: 19.90963, priority: 1, name: 'Name of the task', dateDue: '30.07.2015'},
        {id: 5, lat: 50.05346, lng: 19.8535, priority: 2, name: 'Name of the task, bla bla', dateDue: '30.07.2015'},
        {id: 6, lat: 50.07285, lng: 19.94688, priority: 3, name: 'Name of the task', dateDue: '30.07.2015'}
    ];
    // END TEST

    function __centerMap(return_center) {
        var maxLat=Number.NEGATIVE_INFINITY,
            maxLng=Number.NEGATIVE_INFINITY,
            minLat=Number.POSITIVE_INFINITY,
            minLng=Number.POSITIVE_INFINITY;

        for(var i=0; i<points.length; i++) {
            if(points[i].lat > maxLat) maxLat = points[i].lat;
            if(points[i].lng > maxLng) maxLng = points[i].lng;
            if(points[i].lat < minLat) minLat = points[i].lat;
            if(points[i].lng < minLng) minLng = points[i].lng;
        }

        if(return_center) {
            return [(maxLat+minLat)/2, (maxLng+minLng/2)];
        } else {
            _map.fitBounds(new L.latLngBounds(
                new L.latLng(minLat, minLng),
                new L.latLng(maxLat, maxLng)
            ));
        }
    }

    function onMapClick(e) {
        popup
            .setLatLng(e.latlng)
            .setContent("You clicked the map at " + e.latlng.toString())
            .openOn(_map);
    }

    function panToTask(task_id) {
        var task;

        for(var layer in _map._layers){
            if(_map._layers[layer].task_id == task_id){
                _map._layers[layer].openPopup();
                break;
            }
        }

        for(var i=0; i<points.length; i++)
            if(points[i].id == task_id){
                task = points[i];
                break;
            }

        try {
            _map.panTo([task.lat, task.lng]);
        } catch(e){
            console.log('[MAP] panToTask ERROR :<');
        }
    }



    function __geoSuccess(p) {
        userLat = p.coords.latitude.toFixed(6);
        userLng = p.coords.longitude.toFixed(6);
        console.log([userLat, userLng]);

        L.marker([userLat, userLng], {icon: userIcon}).bindPopup("Oh,<br/>Here you are.").addTo(_map).openPopup();
    }

    function __geoError() {
        console.log('[error] getting coordinates :< USER, WHY U NO ACCEPT.')
    }

    function init(geo) {

        // async
        if(geo && geoPosition.init()){
            geoPosition.getCurrentPosition(__geoSuccess, __geoError);
        }
        _map = L.map('map').setView(__centerMap(true), 13);

        L.tileLayer(MB_URL, {
            attribution: OSM_ATTRIB,
            id: 'mapbox.streets',
            maxZoom: 15
        }).addTo(_map);

        //_map.on('click', onMapClick);

        repopulateClassic();
    }

    function userCheckLocation(){
        return userLat && userLng;
    }

    function userLocation(){
        if(userCheckLocation()) {
            _map.panTo([userLat, userLng]);
        }
    }

    function __preparePopup(id, title, dateDue) {
        return '<b>Due: ' + dateDue + '</b><br/><hr class="thin"><span>' + Utils.cutToLength(title, 16) + '</span><br/><a class="place-left" href="#map" onclick="showTask(' + id + ')">&raquo; more</a> ';
    }

    function __repopulate(urgent, priority){
        if(_map){
            var group = [];

            if(pointLayer){
                try {
                    _map.removeLayer(pointLayer);
                }catch(e){
                    console.log('[MAP] repopulate ERROR :<');
                }
            }

            if(priority) {
                for(var i=0; i<points.length;i++) {

                    switch(points[i].priority) {

                        case 1:
                            var marker = L.marker([points[i].lat, points[i].lng], {icon: yellowIcon}).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                            marker.task_id = points[i].id;
                            group.push(marker);
                            break;

                        case 2:
                            var marker = L.marker([points[i].lat, points[i].lng], {icon: redIcon}).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                            marker.task_id = points[i].id;
                            group.push(marker);
                            break;

                        case 3:
                            var marker = L.marker([points[i].lat, points[i].lng], {icon: blackIcon}).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                            marker.task_id = points[i].id;
                            group.push(marker);
                            break;

                        default:
                            var marker = L.marker([points[i].lat, points[i].lng]).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                            marker.task_id = points[i].id;
                            group.push(marker);
                            break;
                    }

                }
            } else if (urgent) {
                for(var i=0; i<points.length;i++)
                    if(points[i].priority == 2) {
                        var marker = L.marker([points[i].lat, points[i].lng], {icon: redIcon}).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                        marker.task_id = points[i].id;
                        group.push(marker);
                    }
            } else {
                for (var i = 0; i < points.length; i++) {
                    var marker = L.marker([points[i].lat, points[i].lng]).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                    marker.task_id = points[i].id;
                    group.push(marker);
                }
            }

            pointLayer = L.layerGroup(group).addTo(_map);


            __centerMap();
        }
    }


    /* /-------------------------------------------------------------------------------------------------------------------------------------\
                                                            Public functions
       \-------------------------------------------------------------------------------------------------------------------------------------/ */

    function repopulateUrgent() {
        __repopulate(true, false);
    }

    function repopulatePriority() {
        __repopulate(false, true);
    }

    function repopulateClassic() {
        __repopulate(false, false);
    }

    function center() {
        __centerMap(false);
    }

    return {
        init: init,
        repopulate: repopulateClassic,
        repopulatePriority: repopulatePriority,
        repopulateUrgent: repopulateUrgent,
        center: center,
        panToTask: panToTask,
        userLocation: userLocation,
        userCheckLocation: userCheckLocation,
        DEBUG: function(){return _map}
    }


})(L, jQuery);