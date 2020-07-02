from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain import config, Unit


def get_unit(session, vehicle_id, vehicle_label):
    """
    Find a vehicle unit, if not exists then insert into the database, then return
    :param session: Current session
    :param vehicle_id: Id to search
    :param vehicle_label: Name of vehicle unit
    :return:
    """
    unit = session.query(Unit).filter_by(vehicle_id=vehicle_id).first()
    if not unit:
        unit = Unit(vehicle_id=vehicle_id, label=vehicle_label)
        session.add(unit)
        session.flush()
    return unit


def get_town_hall(town_halls, latitude, longitude):
    """
    Find the town hall using latitude and longitude
    :see  TownHall.contains
    :param town_halls: All town halls and his delimiters
    :param latitude:
    :param longitude:
    :return: Town hall that contains latutude and longitude
    """
    for town_hall in town_halls:
        if town_hall.contains(latitude, longitude):
            return town_hall
    return


def save_unit_location(session, town_halls, fields):
    """
    Save unit location into the database
    :param session:
    :param town_halls:
    :param fields:
    :return:
    """
    unit = get_unit(session, fields["vehicle_id"], fields["vehicle_label"])
    town_hall = get_town_hall(town_halls, fields["position_latitude"], fields["position_longitude"])
    print (town_hall)


def save_unit_locations(town_halls, records):
    """
    Loop over all records and processing
    :param town_halls:
    :param records:
    :return:
    """
    session = get_session()
    for record in records:
        save_unit_location(session, town_halls, record["fields"])
    session.commit()


def get_session():
    """
    :return: A session managed by ORM
    """
    engine = create_engine(config.url_db)
    return sessionmaker(bind=engine)()
