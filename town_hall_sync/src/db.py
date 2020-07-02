from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import config
from .models.town_hall import TownHall
from .models.delimiter_point import DelimiterPoint


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
    print(f'Processing {town_hall_fields["nomgeo"]}.')

    town_hall = TownHall(name=town_hall_fields["nomgeo"])
    session.add(town_hall)
    session.flush()

    for coords in town_hall_fields["geo_shape"]["coordinates"]:
        for point in coords:
            session.add(DelimiterPoint(latitude=point[0], longitude=point[1], town_hall_id=town_hall.id))


def get_session():
    """
    :return: A session managed by ORM
    """
    engine = create_engine(config.url_db)
    return sessionmaker(bind=engine)()
