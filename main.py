from winrt.windows.devices.geolocation import Geolocator, PositionAccuracy
from geopy.distance import geodesic
from datetime import timedelta
from time import sleep

#======================================================

records: list[dict] = []


while True:

    gl = Geolocator()
    gl.desired_accuracy = PositionAccuracy.HIGH

    pos = gl.get_geoposition_async_with_age_and_timeout(
        timedelta(seconds=0), # Max Age
        timedelta(seconds=15) # Timeout
    ).get().coordinate

    records += [{
        'coords': [
            pos.latitude,
            pos.longitude
        ],
        'ping': -1
    }]
    
    dist = geodesic(
        records[0]['coords'],
        records[-1]['coords']
    ).meters

    print()
    print(f'{records[0]['coords']=}')
    print(f'{records[-1]['coords']=}')
    print(f"Distance: {dist:f} m")

    sleep(1)
