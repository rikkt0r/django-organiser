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
        popup=L.popup(),
        userLat=Number.NaN,
        userLng=Number.NaN;

    var CustomIcon = L.Icon.extend({
        options: {
            shadowUrl: 'marker-shadow.png',
            shadowAnchor: [1, 41],
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
        }
    });

    var blackIcon = new CustomIcon({iconUrl: 'marker-black.png'}),
        redIcon = new LeafIcon({iconUrl: 'marker-red.png'}),
        yellowIcon = new LeafIcon({iconUrl: 'marker-yellow.png'}),
        blueIcon = new LeafIcon({iconUrl: 'blue-yellow.png'});


    // TEST ONLY
    var points = [
        {id: 1, lat: 50.05346, lng: 19.8535, priority: 1},
        {id: 2, lat: 50.03597, lng: 20.04627, priority: 2},
        {id: 3, lat: 50.04762, lng: 19.94637, priority: 3},
        {id: 4, lat: 50.04773, lng: 19.90963, priority: 1},
        {id: 5, lat: 50.05346, lng: 19.8535, priority: 2},
        {id: 6, lat: 50.07285, lng: 19.94688, priority: 3}
    ];
    // END TEST

    function centerMap() {
        var maxLat=Number.NEGATIVE_INFINITY,
            maxLng=Number.NEGATIVE_INFINITY,
            minLat=Number.POSITIVE_INFINITY,
            minLng=Number.POSITIVE_INFINITY;

        for(var i=0;i<points.length;i++){
            if(points[i].lat > maxLat) maxLat = points[i].lat;
            if(points[i].lng > maxLng) maxLng = points[i].lng;
            if(points[i].lat < minLat) minLat = points[i].lat;
            if(points[i].lng < minLng) minLng = points[i].lng;
        }

        _map.fitBounds(new L.latLngBounds(
            new L.latLng(minLat, minLng),
            new L.latLng(maxLat, maxLng)
        ));
    }

    function onMapClick(e) {
        popup
            .setLatLng(e.latlng)
            .setContent("You clicked the map at " + e.latlng.toString())
            .openOn(_map);
    }

    function panToTask(task_id) {
        var task;

        console.log(task_id);

        for(var i=0; i<points.length; i++)
            if(points[i].id == task_id)
                task = points[i];

        console.log(task);
        try {
            _map.panTo([task.lat, task.lng]);
        } catch(e){
            console.log('[MAP] panToTask ERROR :<');
        }
    }



    function geoSuccess(p) {
        userLat = p.coords.latitude.toFixed(6);
        userLng = p.coords.longitude.toFixed(6);
        console.log([userLat, userLng]);
        _map = L.map('map').setView([userLat, userLng], 13);

        L.tileLayer(MB_URL, {
            attribution: OSM_ATTRIB,
            id: 'mapbox.streets',
            maxZoom: 15
        }).addTo(_map);

        setTimeout(centerMap, 2000);
        _map.on('click', onMapClick);

        repopulate();
    }

    function geoError() {
        alert("Could not find you!");
    }

    function init(geo) {

        // async
        if(geo && geoPosition.init()){
            geoPosition.getCurrentPosition(geoSuccess, geoError);
        }
        // sync
        else {
            _map = L.map('map').setView([50.07733, 19.91306], 13);

            L.tileLayer(MB_URL, {
                attribution: OSM_ATTRIB,
                id: 'mapbox.streets',
                maxZoom: 15
            }).addTo(_map);

            setTimeout(centerMap, 2000);
            _map.on('click', onMapClick);

            repopulate();
        }
    }

    function userCheckLocation(){
        return userLat && userLng;
    }

    function userLocation(){
        if(userCheckLocation())
            _map.panTo([userLat, userLng]);
    }

    function repopulate(){
        if(_map){
            var group = [];

            if(pointLayer){
                try {
                    _map.removeLayer(pointLayer);
                }catch(e){
                    //nothing
                }
            }

            for(var i=0; i<points.length;i++)
                group.push(L.marker([points[i].lat, points[i].lng]).bindPopup("Something to do here")); // .openPopup();

            pointLayer = L.layerGroup(group).addTo(_map);
        }
    }

    return {
        init: init,
        repopulate: repopulate,
        center: centerMap,
        panToTask: panToTask,
        userLocation: userLocation,
        userCheckLocation: userCheckLocation
    }


})(L, jQuery);