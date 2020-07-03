from . import db
from .unit_type import UnitType
from .unit_location_type import UnitLocationType
from .town_hall_type import TownHallType


def available_units():
    """
    Obtain a list of units that have been within a town hall
    """
    return [
        UnitType(id=it.id, vehicle_id=it.vehicle_id, label=it.label)
        for it in db.find_units()
    ]


def unit_location_history(unit_id):
    """
    Get the history of locations/dates of a units
    """
    location = 0
    unit = 1
    town_hall = 2
    return [
        UnitLocationType(
            id=it[location].id,
            latitude=it[location].latitude,
            longitude=it[location].longitude,
            unit=UnitType(id=it[unit].id, label=it[unit].label, vehicle_id=it[unit].vehicle_id),
            town_hall=TownHallType(id=it[town_hall].id, name=it[town_hall].name) if it[town_hall] else None,
            date=it[location].date_updated
        )
        for it in db.find_locations_of_unit(unit_id)
    ]


def available_town_halls():
    """
    Get a list of available town halls
    """
    return [
        TownHallType(id=it.id, name=it.name)
        for it in db.find_town_halls()
    ]


def units_in_town_hall(town_hall_id):
    """
    Get all the units that were in a town hall
    """
    return [
        UnitType(id=it.id, label=it.label, vehicle_id=it.vehicle_id)
        for it in db.find_units_has_been_town_hall(town_hall_id)
    ]
