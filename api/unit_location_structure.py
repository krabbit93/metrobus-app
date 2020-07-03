from graphene import ObjectType, Int, String, Float, Date


class UnitLocationStructure(ObjectType):
    id = Int()
    latitude = Float()
    longitude = Float()
    town_hall_id = Int()
    unit_id = Int()
    date_updated = Date()
    record_id = String()
