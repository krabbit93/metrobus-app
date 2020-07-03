from graphene import ObjectType, List, Int
from .vehicle_type import VehicleType
from .vehicle_location_type import VehicleLocationType
from .town_hall_type import TownHallType
from . import resolvers


class Query(ObjectType):
    """
    Graphql root query definition
    type Query{
        availableVehicles: [Vehicle]
        vehicleLocationHistory(vehicleId: Int!): [VehicleLocation]
        availableTownHalls: [TownHall]
        vehiclesInTownHall(townHallId: Int!): [Vehicle]
    }
    """
    available_vehicles = List(VehicleType)
    vehicle_location_history = List(VehicleLocationType, vehicle_id=Int())
    available_town_halls = List(TownHallType)
    vehicles_in_town_hall = List(VehicleType, town_hall_id=Int())

    def resolve_available_vehicles(self, type):
        return resolvers.available_vehicles()

    def resolve_vehicle_location_history(self, type, vehicle_id):
        return resolvers.vehicle_location_history(vehicle_id)

    def resolve_available_town_halls(self, type):
        return resolvers.available_town_halls()

    def resolve_vehicles_in_town_hall(self, type, town_hall_id):
        return resolvers.vehicles_in_town_hall(town_hall_id)