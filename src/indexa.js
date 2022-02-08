// window.initMap = () => {

//     const map = new google.maps.Map(document.getElementById('map'), {
//         center: {lat: 40.0, lng: -100.0},
//         zoom: 5,
//     });
    
// }

window.initMap = () => {

  const map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 40.0, lng: -100.0},
      zoom: 5,        
      styles: [
        {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
        {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
        {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
        {
          featureType: 'administrative.locality',
          elementType: 'labels.text.fill',
          stylers: [{color: '#d59563'}]
        },
        {
          featureType: 'poi',
          elementType: 'labels.text.fill',
          stylers: [{color: '#d59563'}]
        },
        {
          featureType: 'poi.park',
          elementType: 'geometry',
          stylers: [{color: '#263c3f'}]
        },
        {
          featureType: 'poi.park',
          elementType: 'labels.text.fill',
          stylers: [{color: '#6b9a76'}]
        },
        {
          featureType: 'road',
          elementType: 'geometry',
          stylers: [{color: '#38414e'}]
        },
        {
          featureType: 'road',
          elementType: 'geometry.stroke',
          stylers: [{color: '#212a37'}]
        },
        {
          featureType: 'road',
          elementType: 'labels.text.fill',
          stylers: [{color: '#9ca5b3'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'geometry',
          stylers: [{color: '#746855'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'geometry.stroke',
          stylers: [{color: '#1f2835'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'labels.text.fill',
          stylers: [{color: '#f3d19c'}]
        },
        {
          featureType: 'transit',
          elementType: 'geometry',
          stylers: [{color: '#2f3948'}]
        },
        {
          featureType: 'transit.station',
          elementType: 'labels.text.fill',
          stylers: [{color: '#d59563'}]
        },
        {
          featureType: 'water',
          elementType: 'geometry',
          stylers: [{color: '#17263c'}]
        },
        {
          featureType: 'water',
          elementType: 'labels.text.fill',
          stylers: [{color: '#515c6d'}]
        },
        {
          featureType: 'water',
          elementType: 'labels.text.stroke',
          stylers: [{color: '#17263c'}]
        }
      ],
  });

  const overlay = new GoogleMapsOverlay({
      layers: [
          scatterplot(),
          heatmap(),
          hexagon()
      ],
  });

  
  overlay.setMap(map);
  
}

import { GoogleMapsOverlay } from '@deck.gl/google-maps';
import { HexagonLayer } from '@deck.gl/aggregation-layers';
import { ScatterplotLayer } from '@deck.gl/layers';
import { HeatmapLayer } from '@deck.gl/aggregation-layers';
//test
//test2
const sourceData = './covid_dailies_final.json';
//

const scatterplot = () => new ScatterplotLayer({
  id: 'scatter',
  data: sourceData,
  opacity: 0.8,
  filled: true,
  radiusMinPixels: 2,
  radiusMaxPixels: 5,
  getPosition: d => [d.longitude, d.latitude],
  getFillColor: d => d.n_killed > 0 ? [200, 0, 40, 150] : [255, 140, 0, 100],
  pickable: true,
  onHover: ({object, x, y}) => {
      const el = document.getElementById('tooltip');
      if (object) {
        const { n_killed, incident_id } = object;
        el.innerHTML = `<h1>${deaths}'a', ${cases}</h1>`
        el.style.display = 'block';
        el.style.opacity = 0.9;
        el.style.left = x + 'px';
        el.style.top = y + 'px';
      } else {
        el.style.opacity = 0.0;
      }
  },

  onClick: ({object, x, y}) => {
    window.open(`https://www.gunviolencearchive.org/incident/${object.incident_id}`)
  },
   

});

const heatmap = () => new HeatmapLayer({
  id: 'heat',
  data: sourceData,
  getPosition: d => [d.longitude, d.latitude],
  getWeight: d => d.deaths + (d.cases * 0.5),
  radiusPixels: 60,
});

// const hexagon = () => new HexagonLayer({
//   id: 'hex',
//   data: sourceData,
//   getPosition: d => [d.longitude, d.latitude],
//   getElevationWeight: d => (d.deaths * 2) + d.cases,
//   elevationScale: 100,
//   extruded: true,
//   radius: 2000,         
//   opacity: 0.6,        
//   coverage: 0.88,
//   lowerPercentile: 50
// });