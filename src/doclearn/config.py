from os import getenv


class Config:
    """
    App settings.
    """

    tokens = getenv("GITHUB_TOKENS", "").split(",")
    tokens = [token.strip() for token in tokens if token.strip()]
