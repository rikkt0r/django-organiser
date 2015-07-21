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


    // TEST ONLY
    var points = [
        {lat: 50.05346, lng: 19.8535},
        {lat: 50.06657, lng: 19.98894},
        {lat: 50.04762, lng: 19.94637},
        {lat: 50.04773, lng: 19.90963},
        {lat: 50.05346, lng: 19.8535},
        {lat: 50.07285, lng: 19.94688}
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

        if(geo && geoPosition.init()){
            geoPosition.getCurrentPosition(geoSuccess, geoError);
        } else {
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
        center: centerMap
    }


})(L, jQuery);