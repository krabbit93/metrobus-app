from domain import data
from domain.config import url_data_units_location
from unit_location_sync import db


def register_unit_locations(town_halls):
    """
    Find all current locations from api and save into database
    :param town_halls: All town halls and his delimiters
    :return:
    """
    unit_locations = data.find(url_data_units_location)
    db.save_unit_locations(town_halls, unit_locations["records"])
