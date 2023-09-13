from django.test import SimpleTestCase

from oauth2 import services
from oauth2.errors import OAuth2Error
from oauth2.models import OAuth2


class TestServices(SimpleTestCase):
    """
    Test case for oauth2 services.
    """
    def test_oauth2_authorize(self):
        oauth2 = services.oauth2_authorize('google')
        self.assertIsInstance(oauth2, OAuth2)
        url = oauth2.url
        self.assertIn('client_id', url)
        self.assertIn('redirect_url', url)
        self.assertIn('response_type', url)
        self.assertIn('scope', url)
        self.assertIn('state', url)

    def test_oauth2_authorize_fail(self):
        with self.assertRaises(OAuth2Error):
            services.oauth2_authorize('unsupported')
