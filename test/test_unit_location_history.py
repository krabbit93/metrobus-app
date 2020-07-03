from api import db
from api import resolvers
from test.base_test import BaseTest


class TestUnitLocationHistory(BaseTest):

    def setUp(self):
        db.find_locations_of_unit = super().mock_locations

    def test_should_find_when_exists(self):
        self.assertTrue(
            any(x for x in resolvers.unit_location_history(1)
                if x.id == 1 and x.unit.id == 1 and x.town_hall.id == 1)
        )

    def test_fail_when_not_exist(self):
        self.assertFalse(
            any(x for x in resolvers.unit_location_history(2)
                if x.id == 2 and x.unit.id == 2 and x.town_hall.id == 2)
        )
