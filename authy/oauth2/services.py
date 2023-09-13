import secrets
from urllib.parse import urlencode

from django.conf import settings

from oauth2 import queries
from oauth2.errors import OAuth2Error
from oauth2.models import OAuth2
from oauth2.utils import generate_unique_username
from users.models import User
from users.selectors import user_get_by_email
from users.services import user_create


def oauth2_authorize(provider_name: str) -> OAuth2:
    provider = settings.OAUTH2_PROVIDERS.get(provider_name)
    if provider is None:
        error = 'Unsupported provider.'
        raise OAuth2Error(error)
    
    oauth2_state = secrets.token_urlsafe(16)
    qs = urlencode({
        'client_id': provider['client_id'],
        'redirect_uri': settings.BACKEND_OAUTH2_URL + '/' + provider_name,
        'response_type': 'code',
        'scope': ' '.join(provider['scopes']),
        'state': oauth2_state,
    })

    return OAuth2(
        state=oauth2_state,
        url=provider['authorize_url'] + '?' + qs,
    )


def oauth2_callback(
    provider_name: str,
    code: str,
    state: str,
    session_state: str
) -> User:
    provider = settings.OAUTH2_PROVIDERS.get(provider_name)
    if provider is None:
        error = 'Unsupported provider.'
        raise OAuth2Error(error)
    if state != session_state:
        error = 'OAuth2 state is incorrect.'
        raise OAuth2Error(error)
    if code is None:
        error = 'OAuth2 code was empty.'
        raise OAuth2Error(error)
    
    oauth2_token = queries.get_access_token(
        provider, provider_name, code
    )
    if oauth2_token is None:
        error = 'Failed to get access token.'
        raise OAuth2Error(error)
    
    email = queries.get_user_info(provider, oauth2_token)
    if email is None:
        error = 'Failed to get user info.'
        raise OAuth2Error(error)
    
    user = user_get_by_email(email)
    if user is not None:
        return user
    return user_create(
        email=email,
        username=generate_unique_username(email.split('@')[0]),
        password=secrets.token_urlsafe(16),
    )
