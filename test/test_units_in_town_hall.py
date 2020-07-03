from api import db
from api import resolvers
from test.base_test import BaseTest


class TestUnitsInTownHall(BaseTest):

    def setUp(self):
        db.find_units_has_been_town_hall = super().mock_units_of_town

    def test_should_find_when_exists(self):
        self.assertTrue(
            any(x for x in resolvers.units_in_town_hall(1)
                if x.id == 1 and x.vehicle_id == "1" and x.label == "1")
        )

    def test_fail_when_not_exist(self):
        self.assertFalse(
            any(x for x in resolvers.units_in_town_hall(2)
                if x.id == 2 and x.vehicle_id == "2" and x.label == "2")
        )
