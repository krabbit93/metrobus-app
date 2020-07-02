from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TownHall(Base):
    __tablename__ = 'town_halls'

    id = Column(Integer, primary_key=True)
    name = Column(String)
