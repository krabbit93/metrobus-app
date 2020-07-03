from graphene import ObjectType, Int, String


class TownHallType(ObjectType):
    """
    Graphql definition type
    type TownHall{
        id: Int
        name: String
    }
    """
    id = Int()
    name = String()
