from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain import config, Unit, UnitLocation, TownHall


def find_units():
    session = get_session()
    return session.query(Unit).all()


def find_location_units(unit_id):
    session = get_session()
    return session.query(UnitLocation).filter_by(unit_id=unit_id).all()


def find_town_halls():
    session = get_session()
    return session.query(TownHall).all()

def find_units_has_been_town_hall(town_hall_id):
    session = get_session()
    return session.query(Unit).filter(
        UnitLocation.unit_id == Unit.id
    ).filter(
        UnitLocation.town_hall_id == town_hall_id
    ).group_by(UnitLocation.unit_id).all()

def get_session():
    """
    :return: A session managed by ORM
    """
    engine = create_engine(config.url_db)
    return sessionmaker(bind=engine)()