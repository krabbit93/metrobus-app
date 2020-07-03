from graphene import ObjectType, String, List, Int
from .unit_structure import UnitStructure
from .unit_location_structure import UnitLocationStructure
from .town_hall_structure import TownHallStructure
from . import db


class RootQuery(ObjectType):
    available_vehicles = List(UnitStructure)
    location_history = List(UnitLocationStructure, unit_id=Int())
    available_town_halls = List(TownHallStructure)
    vehicles_has_been_town_hall = List(UnitStructure, town_hall_id=Int())

    def resolve_available_vehicles(self, available_vehicles):
        return [
            UnitStructure(id=it.id, vehicle_id=it.vehicle_id, label=it.label)
            for it in db.find_units()
        ]

    def resolve_location_history(self, location_history, unit_id):
        return [
            UnitLocationStructure(
                id=it.id,
                latitude=it.latitude,
                longitude=it.longitude,
                town_hall_id=it.town_hall_id,
                unit_id=it.unit_id,
                date_updated=it.date_updated,
                record_id=it.record_id
            )
            for it in db.find_location_units(unit_id)
        ]

    def resolve_available_town_halls(self, available_town_halls):
        return [
            TownHallStructure(id=it.id, name=it.name)
            for it in db.find_town_halls()
        ]

    def resolve_vehicles_has_been_town_hall(self, vehicles_has_been_town_hall, town_hall_id):
        print(db.find_units_has_been_town_hall(town_hall_id))
        return [
            UnitStructure(id=it.id, vehicle_id=it.vehicle_id, label=it.label)
            for it in db.find_units_has_been_town_hall(town_hall_id)
        ]
