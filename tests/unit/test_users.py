import unittest

import pytest

from users.models import UserAccount


class TestUsersUnit(unittest.TestCase):
    @pytest.mark.django_db
    def test_constructor(self):
        payload = dict(
            first_name="alpha",
            last_name="invest",
            email="alpha@gmail.com",
            password="alpha12645370",
        )

        obj = UserAccount()
        obj.first_name = payload["first_name"]
        obj.last_name = payload["last_name"]
        obj.email = payload["email"]
        obj.password = payload["password"]
        obj.save()
