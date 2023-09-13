import secrets
from urllib.parse import urlencode

from django.conf import settings

from oauth2.errors import OAuth2Error
from oauth2.models import OAuth2


def oauth2_authorize(provider_name: str) -> OAuth2:
    provider = settings.OAUTH2_PROVIDERS.get(provider_name)
    if provider is None:
        error = 'Unsupported provider.'
        raise OAuth2Error(error)
    
    oauth2_state = secrets.token_urlsafe(16)
    qs = urlencode({
        'client_id': provider['client_id'],
        'redirect_url': settings.BACKEND_OAUTH2_URL + '/' + provider_name,
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
):
    pass
