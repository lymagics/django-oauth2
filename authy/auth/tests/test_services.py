from django.test import TestCase

from auth import services
from auth.errors import InvalidCredentials
from users.tests.factories import UserFactory


class TestServices(TestCase):
    """
    Test case for auth services.
    """
    def test_login(self):
        new_user = UserFactory()
        user = services.login(
            new_user.username, 'testpass123'
        )
        self.assertEqual(user, new_user)

    def test_login_fail(self):
        with self.assertRaises(InvalidCredentials):
            services.login('bob', 'testpass123')
