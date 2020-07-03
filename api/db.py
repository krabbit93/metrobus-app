from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain import config, Unit, UnitLocation, TownHall


def find_units():
    """
    All units registered
    """
    session = get_session()
    return session.query(Unit).all()


def find_locations_of_unit(unit_id):
    """
    All locations that unit_id has been inside
    """
    session = get_session()
    return session.query(UnitLocation, Unit, TownHall).join(
        Unit, UnitLocation.unit_id == Unit.id
    ).join(
        TownHall, UnitLocation.town_hall_id == TownHall.id, isouter=True
    ).filter(UnitLocation.unit_id == unit_id).all()


def find_town_halls():
    """
    All town halls registered
    """
    session = get_session()
    return session.query(TownHall).all()


def find_units_has_been_town_hall(town_hall_id):
    """
    All units that has been inside a town hall
    """
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
