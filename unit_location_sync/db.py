from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain import config, Unit, UnitLocation
from matplotlib import path


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
        polygon = path.Path(town_hall.delimiter_points)
        if polygon.contains_point((latitude, longitude)):
            return town_hall
    return


def save_unit_location(session, town_halls, record_id, fields):
    """
    Save unit location into the database
    :param session:
    :param town_halls:
    :param fields:
    :return:
    """
    unit = get_unit(session, fields["vehicle_id"], fields["vehicle_label"])
    latitude = fields["position_latitude"]
    longitude = fields["position_longitude"]
    town_hall = get_town_hall(town_halls, latitude, longitude)
    session.add(UnitLocation(
        latitude=latitude,
        longitude=longitude,
        town_hall_id=town_hall.id if town_hall else None,
        unit_id=unit.id,
        date_updated=fields["date_updated"],
        record_id=record_id
    ))


def has_been_processed(session, record_id):
    """
    Check if recordid of this unit has been processed before
    :param session:
    :param record_id:
    :return:
    """
    return session.query(UnitLocation).filter_by(record_id=record_id.__str__()).count() > 0


def save_unit_locations(town_halls, records):
    """
    Loop over all records and processing if not has been processed
    :param town_halls:
    :param records:
    :return:
    """
    session = get_session()
    for record in records:
        if not has_been_processed(session, record["recordid"]):
            save_unit_location(session, town_halls, record["recordid"], record["fields"])
    session.commit()


def get_session():
    """
    :return: A session managed by ORM
    """
    engine = create_engine(config.url_db)
    return sessionmaker(bind=engine)()
