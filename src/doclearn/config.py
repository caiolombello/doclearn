from os import getenv


class Config:
    """
    App settings.
    """

    token = getenv("GITHUB_TOKEN")
