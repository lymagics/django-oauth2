from typing import Optional

from django.conf import settings

import jwt


def jwt_encode(payload: dict) -> str:
    return jwt.encode(
        payload=payload,
        key=settings.SECRET_KEY,
        algorithm='HS256',
    )


def jwt_decode(jwt_token: str) -> Optional[dict]:
    try:
        return jwt.decode(
            jwt_token,
            key=settings.SECRET_KEY,
            algorithms=['HS256'],
        )
    except jwt.PyJWKError:
        return None
