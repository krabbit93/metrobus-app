from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from matplotlib import path

Base = declarative_base()


class TownHall(Base):
    """
    A town hall catalog
    """
    __tablename__ = 'town_halls'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def register_limits(self, delimiter_points):
        self.path = path.Path([(it.latitude, it.longitude) for it in delimiter_points])

    def contains(self, latitude, longitude):
        return self.path.contains_point((latitude, longitude))

    def __str__(self):
        return f'({self.id}, {self.name})'
