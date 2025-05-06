import geocoder

location = geocoder.ip('me')
print(location.latlng)  # Your [latitude, longitude]