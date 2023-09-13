from users.models import User


def user_get(user_id: int) -> User:
    return User.objects.filter(pk=user_id).first()


def user_get_by_email(email: str) -> User:
    return User.objects.filter(email=email).first()
