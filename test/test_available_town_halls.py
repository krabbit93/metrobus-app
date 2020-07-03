from api import resolvers
from api import db
from test.base_test import BaseTest


class TestAvailableTownHalls(BaseTest):

    def setUp(self):
        db.find_town_halls = super().mock_towns

    def test_should_find_when_exists(self):
        self.assertTrue(
            any(x for x in resolvers.available_town_halls() if x.id == 1 and x.name == "Raphael")
        )

    def test_fail_when_not_exist(self):
        self.assertFalse(
            any(x for x in resolvers.available_town_halls() if x.id == 3 and x.name == "Leonardo")
        )
