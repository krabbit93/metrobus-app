from graphene import ObjectType, Int, String


class VehicleType(ObjectType):
    """
    Graphql definition type
    type Vehicle{
        id: Int
        label: String
        vehicleId: Int
    }
    """
    id = Int()
    label = String()
    vehicle_id = Int()
