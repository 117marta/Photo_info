// Get geolocation of user
var lat_geolocation;
var lon_geolocation;

if ("geolocation" in navigator) {
navigator.geolocation.getCurrentPosition(
    function (position) {
      console.log('Geolocation has been set successfully!');
      lat_geolocation = position.coords.latitude;
      lon_geolocation = position.coords.longitude;
      console.log('Latitude:', lat_geolocation);
      console.log('Longitude:', lon_geolocation);
      document.cookie = 'lat=' + position.coords.latitude;
      document.cookie = 'lon=' + position.coords.longitude;
  }, function (error) {
      console.log('Geolocation could not be obtained.')
  });
}


// Show map with user's geolocation
const checkbox = document.getElementById('show_user_geolocation');
console.log(checkbox)
const user_map = document.getElementById('user_geolocation_map');
console.log(user_map)
user_map.style.display = 'none';

checkbox.addEventListener('click', function () {
    if (this.checked) {
        user_map.style.display = '';
    } else {
        user_map.style.display = 'none';
    }
});
