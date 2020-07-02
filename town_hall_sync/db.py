from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain import TownHall, DelimiterPoint, config


def save_town_halls(records):
    """
    Save record to the database
    :param records: Records to save
    :return:
    """
    session = get_session()
    for record in records:
        save_town_hall(session, record["fields"])
    session.commit()


def save_town_hall(session, town_hall_fields: dict):
    """
    Process a record, save self and save his coordinates
    :param session: Current database session
    :param town_hall_fields: Field's record
    :return:
    """
    town_hall = TownHall(name=town_hall_fields["nomgeo"])
    session.add(town_hall)
    session.flush()

    for coords in town_hall_fields["geo_shape"]["coordinates"]:
        for point in coords:
            session.add(DelimiterPoint(latitude=point[1], longitude=point[0], town_hall_id=town_hall.id))


def get_session():
    """
    :return: A session managed by ORM
    """
    engine = create_engine(config.url_db)
    return sessionmaker(bind=engine)()


def contains_info():
    """
    Simple counter to verify if town halls are loaded
    :return: A boolean that indicate if table contains data
    """
    session = get_session()
    total = session.query(TownHall).count()
    return total > 0


def find_town_halls():
    """
    Recover all town halls and his delimiters point
    :return:
    """
    session = get_session()
    town_halls = session.query(TownHall).all()
    for town_hall in town_halls:
        town_hall.register_limits(session.query(DelimiterPoint).filter_by(town_hall_id=town_hall.id).all())
    return town_halls
