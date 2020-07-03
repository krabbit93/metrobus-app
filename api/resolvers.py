from . import db
from .vehicle_type import VehicleType
from .vehicle_location_type import VehicleLocationType
from .town_hall_type import TownHallType


def available_vehicles():
    """
    Obtain a list of vehicles that have been within a town hall
    """
    return [
        VehicleType(id=it.id, vehicle_id=it.vehicle_id, label=it.label)
        for it in db.find_units()
    ]


def vehicle_location_history(vehicle_id):
    """
    Get the history of locations/dates of a vehicle
    """
    location = 0
    unit = 1
    town_hall = 2
    return [
        VehicleLocationType(
            id=it[location].id,
            latitude=it[location].latitude,
            longitude=it[location].longitude,
            vehicle=VehicleType(id=it[unit].id, label=it[unit].label, vehicle_id=it[unit].vehicle_id),
            town_hall=TownHallType(id=it[town_hall].id, name=it[town_hall].name),
            date=it[location].date_updated
        )
        for it in db.find_location_units(vehicle_id)
    ]


def available_town_halls():
    """
    Get a list of available town halls
    """
    return [
        TownHallType(id=it.id, name=it.name)
        for it in db.find_town_halls()
    ]


def vehicles_in_town_hall(town_hall_id):
    """
    Get all the vehicles that were in a town hall
    """
    return [
        VehicleType(id=it.id, label=it.label, vehicle_id=it.vehicle_id)
        for it in db.find_units_has_been_town_hall(town_hall_id)
    ]
