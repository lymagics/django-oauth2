from django.contrib.auth import authenticate

from auth.errors import InvalidCredentials
from users.models import User


def login(username: str, password: str) -> User:
    user = authenticate(username=username, password=password)
    if user is None:
        error = 'Invalid username or password.'
        raise InvalidCredentials(error)
    return user
