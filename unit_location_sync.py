from town_hall_sync import find_data
from unit_location_sync import register_unit_locations

if __name__ == "__main__":
    """
    Get data from database that will be use for own API ans process the
    location of units for verify to the town hall that the locations indicates
    """
    town_halls = find_data()
    register_unit_locations(town_halls)
