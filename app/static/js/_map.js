'use strict';
/*
TODO
1. ADD MAP LEGEND
2. COLORING BUTTON ==> toggle
3. REMAKE DRAGGABLE MARKER TO USE CALLBACK
4. MAYBE DYNAMIC LOCATION ?

 */
var map = (function(L, $) {
    var OpenMapSurfer_Roads = L.tileLayer('http://openmapsurfer.uni-hd.de/tiles/roads/x={x}&y={y}&z={z}', {
	        maxZoom: 16,
	        attribution: 'Imagery from <a href="http://giscience.uni-hd.de/">GIScience Research Group @ University of Heidelberg</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }),
        _map,
        pointLayer,
        movableMarker = undefined,
        singleTask = undefined,
        userLat=Number.NaN,
        userLng=Number.NaN;

    var CustomIcon = L.Icon.extend({
        options: {
            shadowUrl: '/static/images/leaflet/marker-shadow.png',
            shadowAnchor: [13, 41],
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
        }
    }),
        greenIcon = new CustomIcon({iconUrl: '/static/images/leaflet/marker-green.png'}),
        purpleIcon = new CustomIcon({iconUrl: '/static/images/leaflet/marker-purple.png'}),
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



    function __geoSuccess(e) {

        userLat = e.latlng.lat;
        userLng = e.latlng.lng;
        console.log([userLat, userLng]);
        L.marker(e.latlng, {icon: userIcon}).addTo(_map).bindPopup("<b>You are here</b><br/> or " + e.accuracy / 2 + "m away").openPopup();
    }

    function __geoError(e) {
        console.log('[error] getting coordinates :< USER, WHY U NO ACCEPT. ' + e.message);
        alert('USER, WHY U NO ACCEPT :<');
    }

    function __setMarkers(markers){
        points = markers;
    }

    function init() {
        _map = L.map('map');
        _map.on('locationfound', __geoSuccess);
        _map.on('locationerror', __geoError);

        OpenMapSurfer_Roads.addTo(_map);
        _map.locate({setView: true, maxZoom: 14});
    }


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

    function __generateMovableMarker($h_lat, $h_lng, lat, lng){
        return L.marker([lat, lng], {'draggable': true}).bindPopup('Here')
            .on('dragend', function (evt) {
                var coords = evt.target.getLatLng();
                //console.log(coords);
                $($h_lat).val(Utils.roundCoord(coords['lat']));
                $($h_lng).val(Utils.roundCoord(coords['lng']));
                this.openPopup();
            })
            .addTo(_map);
    }

    function __enableCoordChoice($h_lat, $h_lng, lat, lng) {

        if(!movableMarker && lat && lng){
            movableMarker = __generateMovableMarker($h_lat, $h_lng, lat, lng).openPopup();
        }

        _map.on('click', function(e) {
            //popup.setLatLng(e.latlng).setContent("You clicked the map at " + e.latlng.toString()).openOn(_map);
            if (!movableMarker) {
                movableMarker = __generateMovableMarker($h_lat, $h_lng, e.latlng.lat, e.latlng.lng).openPopup();

                $($h_lat).val(Utils.roundCoord(e.latlng['lat']));
                $($h_lng).val(Utils.roundCoord(e.latlng['lng']));
            } else {
                movableMarker.setLatLng(e.latlng).openPopup();
            }
        });
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


    function userCheckLocation(){
        return userLat && userLng;
    }

    function userLocation(){
        if(userCheckLocation()) {
            _map.panTo([userLat, userLng]);
        }
    }

    function __preparePopup(id, title, dateDue, $fnName) {
        //return '<b>Due: ' + dateDue + '</b><br/><hr class="thin"><span>' + Utils.cutToLength(title, 16) + '</span><br/><a class="place-left" href="#map" onclick="showTask(' + id + ')">&raquo; more</a> ';
        return '<b>Due: ' + dateDue + '</b><br/><hr class="thin"><span>' + Utils.cutToLength(title, 16) + '</span><br/><a class="place-left" href="/tasks/' + id + '/">&raquo; more</a> ';
    }

    function __preparePopupLite() {
        return '<b>Your destination</b>';
    }

    function __panToCoordinates(lat, lng) {
        _map.panTo([lat, lng]);
    }

    function __markAndPan(lat, lng){
        if(!singleTask){
            singleTask = L.marker([lat, lng]).bindPopup(__preparePopupLite()).addTo(_map).openPopup();
        }
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

                    var marker;

                    switch(points[i].priority) {

                        case 1:
                            marker = L.marker([points[i].lat, points[i].lng], {icon: greenIcon}).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                            marker.task_id = points[i].id;
                            group.push(marker);
                            break;

                        case 2:
                            marker = L.marker([points[i].lat, points[i].lng], {icon: yellowIcon}).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                            marker.task_id = points[i].id;
                            group.push(marker);
                            break;

                        case 3:
                            marker = L.marker([points[i].lat, points[i].lng], {icon: redIcon}).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                            marker.task_id = points[i].id;
                            group.push(marker);
                            break;

                        default:
                            marker = L.marker([points[i].lat, points[i].lng]).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                            marker.task_id = points[i].id;
                            group.push(marker);
                            break;
                    }

                }
            } else if (urgent) {
                for(var i=0; i<points.length;i++) {
                    if(points[i].priority == 2) {
                        var marker = L.marker([points[i].lat, points[i].lng], {icon: redIcon}).bindPopup(__preparePopup(points[i].id, points[i].name, points[i].dateDue));
                        marker.task_id = points[i].id;
                        group.push(marker);
                    }
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

    function getData(markers){
        __setMarkers(markers);
    }

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

    function panToCoords(lat, lng) {
        __panToCoordinates(lat, lng);
    }

    function addSingleTask(lat, lng){
        __markAndPan(lat, lng);
    }

    function singleTaskLocation() {
        if(singleTask){
            __panToCoordinates(singleTask._latlng.lat, singleTask._latlng.lng);
        }
    }

    function registerCreationEvents($handler_lat, $handler_lng, lat, lng){
        __enableCoordChoice($handler_lat, $handler_lng, lat, lng);
        // and more if needed
    }

    function initMovableMarkerFromLatLng(){
        __setMovableMarker();
    }

    return {
        init: init,
        getData: getData,
        repopulate: repopulateClassic,
        repopulatePriority: repopulatePriority,
        repopulateUrgent: repopulateUrgent,
        center: center,
        panToCoords: panToCoords,
        panToTask: panToTask,
        addSingleTask: addSingleTask,
        singleTaskLocation: singleTaskLocation,
        registerCreationEvents: registerCreationEvents,
        userLocation: userLocation,
        userCheckLocation: userCheckLocation,
        DEBUG: function(){return _map}
    }


})(L, jQuery);