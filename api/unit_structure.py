from graphene import ObjectType, Int, String


class UnitStructure(ObjectType):
    id = Int()
    vehicle_id = Int()
    label = String()
