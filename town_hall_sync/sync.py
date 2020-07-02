from src import config, data, db

if __name__ == "__main__":
    """
    Get data to the public API of 'Límites de alcaldías' and process records
    to save into database that will be use for own API
    """
    town_halls = data.find(config.url_data)
    db.save_town_halls(town_halls["records"])
