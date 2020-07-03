from graphene import ObjectType, Int, String


class UnitType(ObjectType):
    """
    Graphql definition type
    type Unit{
        id: Int
        label: String
        vehicleId: Int
    }
    """
    id = Int()
    label = String()
    vehicle_id = Int()
