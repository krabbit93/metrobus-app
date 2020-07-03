from graphene import ObjectType, List, Int
from .unit_type import UnitType
from .unit_location_type import UnitLocationType
from .town_hall_type import TownHallType
from . import resolvers


class Query(ObjectType):
    """
    Graphql root query definition
    type Query{
        availableVehicles: [Vehicle]
        vehicleLocationHistory(unitId: Int!): [VehicleLocation]
        availableTownHalls: [TownHall]
        vehiclesInTownHall(townHallId: Int!): [Vehicle]
    }
    """
    available_units = List(UnitType)
    unit_location_history = List(UnitLocationType, unit_id=Int())
    available_town_halls = List(TownHallType)
    units_in_town_hall = List(UnitType, town_hall_id=Int())

    def resolve_available_units(self, type):
        return resolvers.available_units()

    def resolve_unit_location_history(self, type, unit_id):
        return resolvers.unit_location_history(unit_id)

    def resolve_available_town_halls(self, type):
        return resolvers.available_town_halls()

    def resolve_units_in_town_hall(self, type, town_hall_id):
        return resolvers.units_in_town_hall(town_hall_id)