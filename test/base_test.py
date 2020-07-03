import unittest
from domain import TownHall, Unit, UnitLocation
import datetime


class BaseTest(unittest.TestCase):

    def mock_towns(self):
        return [
            TownHall(id=1, name='Raphael'),
            TownHall(id=2, name="Donatello")
        ]

    def mock_units(self):
        return [
            Unit(id=1, vehicle_id="1", label="1"),
            Unit(id=2, vehicle_id="2", label="2")
        ]

    def mock_units_of_town(self, town_id):
        if town_id == 2:
            return []
        return [
            Unit(id=1, vehicle_id="1", label="1"),
            Unit(id=2, vehicle_id="2", label="2")
        ]

    def mock_locations(self, unit_id):
        if unit_id == 2:
            return []
        return [
            [
                UnitLocation(id=1, latitude=1, longitude=1, town_hall_id=1, unit_id=1, date_updated=datetime.datetime.now()),
                Unit(id=1, vehicle_id="1", label="1"),
                TownHall(id=1, name='Raphael'),
            ]
        ]
