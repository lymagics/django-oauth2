from django.contrib.auth.models import AbstractUser
from django.db import models

from core.jwt import jwt_encode


class User(AbstractUser):
    """
    User entity.
    """
    email = models.EmailField(unique=True)

    @property
    def jwt_token(self) -> str:
        payload = {'id': self.pk}
        return jwt_encode(payload)
