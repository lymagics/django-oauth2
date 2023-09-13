from typing import Optional

from django.conf import settings

import requests


def access_token_get(provider: dict, name: str, code: str) -> Optional[str]:
    response = requests.post(provider['token_url'], data={
        'client_id': provider['client_id'],
        'client_secret': provider['client_secret'],
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': settings.BACKEND_OAUTH2_URL + '/' + name
    }, headers={'Accept': 'application/json'})
    if response.status_code != 200:
        return None
    return response.json().get('access_token')


def userinfo_get(provider: dict, access_token: str) -> Optional[str]:
    response = requests.get(provider['userinfo']['url'], headers={
        'Authorization': 'Bearer ' + access_token,
        'Accept': 'application/json',
    })
    if response.status_code != 200:
        return None
    return provider['userinfo']['email'](response.json())
