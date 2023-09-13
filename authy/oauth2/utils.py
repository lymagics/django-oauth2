from random import randint

from users.selectors import user_get_by_username


def generate_unique_username(username: str) -> str:
    if user_get_by_username(username) is None:
        return username
    random_username = username + str(randint(0, 1000))
    return generate_unique_username(random_username)
