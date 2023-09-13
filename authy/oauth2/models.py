from dataclasses import dataclass


@dataclass
class OAuth2:
    """
    OAuth2 parameters.
    """
    state: str
    url: str
