from graphene import ObjectType, Int, String


class TownHallStructure(ObjectType):
    id = Int()
    name = String()
