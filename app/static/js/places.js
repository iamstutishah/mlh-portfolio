function initMap() {
    var positions = [
        // Guadalajara
        { lat: 20.6597, lng: -103.3496 },
        // California
        { lat: 36.7783, lng: -119.4179 },
        // Texas
        { lat: 31.9686, lng: -99.9018 },
        // Florida
        { lat: 27.6648, lng: -81.5158 },
        // Cancun
        { lat: 21.1619, lng: -86.8515 },
        // Los Cabos
        { lat: 22.8905, lng: -109.9167 },
    ]
    var colors = [
        '#FF0000',
        '#00FF00',
        '#0000FF',
        '#FFFF00',
        '#00FFFF',
        '#FF00FF',
        '#FFFFFF',
        '#000000',
        '#FFA500',
        '#800080',
        '#008000',
        '#808000',
        '#800000',
        '#008080',
        '#000080',
        '#808080',
    ]
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 0, lng: 0 },
        zoom: 2,
        disableDefaultUI: true,
    });
    for (let i = 0; i < positions.length; i++) {
        new google.maps.Marker({
            position: positions[i],
            map,
            title: "Hello World!",
            icon: {
                path: google.maps.SymbolPath.CIRCLE,
                scale: 8,
                fillColor: colors[i],
                fillOpacity: 1,
                strokeWeight: 0,
            },
        });
    }
}

window.initMap = initMap;