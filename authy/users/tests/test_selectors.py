from django.test import TestCase

from users import selectors
from users.tests.factories import UserFactory


class TestSelectors(TestCase):
    """
    Test case for user selectors.
    """
    def test_user_get(self):
        new_user = UserFactory()
        user = selectors.user_get(new_user.pk)
        self.assertEqual(user, new_user)
