from api import db
from api import resolvers
from test.base_test import BaseTest


class TestAvailableUnits(BaseTest):

    def setUp(self):
        db.find_units = super().mock_units

    def test_should_find_when_exists(self):
        self.assertTrue(
            any(x for x in resolvers.available_units()
                if x.id == 1 and x.vehicle_id == "1" and x.label == "1")
        )

    def test_fail_when_not_exist(self):
        self.assertFalse(
            any(x for x in resolvers.available_units()
                if x.id == 3 and x.vehicle_id == "3" and x.label == "3")
        )
