from sqlalchemy import Column, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DelimiterPoint(Base):
    """
    Entity that represents a point of boundary zone's town hall
    """
    __tablename__ = "delimiter_points"

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    town_hall_id = Column(Integer)
