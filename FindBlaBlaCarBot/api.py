import hug
from TripManager import TripManager
import json

trip_manager = TripManager()

@hug.get('/')
def status():
    return { "status": "OK" }

@hug.get('/trips/{src}/{dest}')
def get_trips(src: str, dest: str):
    trip_manager.setTrips(src, dest)
    return trip_manager.getTrips()

@hug.get('/trips/{src}')
def get_trips_no_dest(src: str):
    trip_manager.setTrips(src, "")
    return trip_manager.getTrips()
