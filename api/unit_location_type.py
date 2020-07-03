from graphene import ObjectType, DateTime, Int, Field, Float
from .unit_type import UnitType
from .town_hall_type import TownHallType


class UnitLocationType(ObjectType):
    """
    Graphql definition type
    type UnitLocation {
        id: Int
        latitude: Float
        longitude: Float
        unit: Unit
        townHall: TownHall
        date: DateTime
    }
    """
    id = Int()
    latitude = Float()
    longitude = Float()
    unit = Field(UnitType)
    town_hall = Field(TownHallType)
    date = DateTime()

