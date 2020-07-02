from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Unit(Base):
    """
    A vehicle unit
    """
    __tablename__ = 'units'

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(String)
    label = Column(String)
