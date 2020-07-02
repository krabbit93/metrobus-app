from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UnitLocation(Base):
    """
    Location of a vehicle unit and the town hall that his belongs
    """
    __tablename__ = "unit_locations"

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    town_hall_id = Column(Integer)
    unit_id = Column(Integer)
    date_updated = Column(Date)
