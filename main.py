from winrt.windows.devices.geolocation import Geolocator

gl = Geolocator()

pos = gl.get_geoposition_async().get()

print(f"Latitude: {pos.coordinate.latitude:f}")
print(f"Longitude: {pos.coordinate.longitude:f}")

