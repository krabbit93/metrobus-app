from town_hall_sync import db
from domain import data, config


def find_data():
    """
    Checks if database contains data of townhall, if not exist,
    Get data to the public API of 'Límites de alcaldías' and process records
    to save into database, then return from database
    """
    if not db.contains_info():
        town_halls = data.find(config.url_data_town_hall)
        db.save_town_halls(town_halls["records"])
    return db.find_townhalls()
