from domain import data
from domain.config import url_data_units_location
from unit_location_sync import db


def register_unit_locations(town_halls):
    unit_ubications = data.find(url_data_units_location)
    db.save_unit_locations(town_halls, unit_ubications["records"])
