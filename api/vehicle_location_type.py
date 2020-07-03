from graphene import ObjectType, DateTime, Int, Field, Float
from .vehicle_type import VehicleType
from .town_hall_type import TownHallType


class VehicleLocationType(ObjectType):
    """
    Graphql definition type
    type VehicleLocation{
        id: Int
        latitude: Float
        longitude: Float
        vehicle: Vehicle
        townHall: TownHall
        date: DateTime
    }
    """
    id = Int()
    latitude = Float()
    longitude = Float()
    vehicle = Field(VehicleType)
    town_hall = Field(TownHallType)
    date = DateTime()

