from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TownHall(Base):
    """
    A town hall catalog
    """
    __tablename__ = 'town_halls'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def register_limits(self, delimiter_points):
        self.delimiter_points = delimiter_points

    def __str__(self):
        return f'({self.id}, {self.name})'
