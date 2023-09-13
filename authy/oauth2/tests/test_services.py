from unittest.mock import patch, Mock

from django.test import TestCase

from oauth2 import services
from oauth2.errors import OAuth2Error
from oauth2.models import OAuth2
from users.tests.factories import UserFactory


class TestServices(TestCase):
    """
    Test case for oauth2 services.
    """
    def test_oauth2_authorize(self):
        oauth2 = services.oauth2_authorize('google')
        self.assertIsInstance(oauth2, OAuth2)
        url = oauth2.url
        self.assertIn('client_id', url)
        self.assertIn('redirect_uri', url)
        self.assertIn('response_type', url)
        self.assertIn('scope', url)
        self.assertIn('state', url)

    def test_oauth2_authorize_fail(self):
        with self.assertRaises(OAuth2Error):
            services.oauth2_authorize('unsupported')

    @patch('oauth2.services.queries.get_access_token')
    @patch('oauth2.services.queries.get_user_info')
    @patch('oauth2.services.user_get_by_email')
    def test_oauth2_callback(
        self,
        user_get_by_email_mock: Mock,
        get_user_info_mock: Mock,
        get_access_token_mock: Mock,
    ):
        new_user = UserFactory()
        user_get_by_email_mock.return_value = new_user
        get_user_info_mock.return_value = '123@example.com'
        get_access_token_mock.return_value = '123'
        user = services.oauth2_callback('google', '123', 'abc', 'abc')
        self.assertEqual(user, new_user)

    def test_oauth2_callback_fail_unsupported_provider(self):
        with self.assertRaises(OAuth2Error):
            services.oauth2_callback('unsupported', '123', 'abc', 'abc')

    def test_oauth2_callback_fail_no_code(self):
        with self.assertRaises(OAuth2Error):
            services.oauth2_callback('unsupported', None, 'abc', 'abc')

    def test_oauth2_callback_fail_invalid_state(self):
        with self.assertRaises(OAuth2Error):
            services.oauth2_callback('unsupported', '123', 'abc', 'cba')
