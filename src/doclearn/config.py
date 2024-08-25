from os import getenv


class Config:
    """
    App settings.
    """

    # export GITHUB_TOKENS="token1,token2,token3"
    tokens = getenv("GITHUB_TOKENS", "").split(",")
    tokens = [token.strip() for token in tokens if token.strip()]

    google_search_enabled = False
    google_api_key = getenv("GOOGLE_API_KEY")
    google_search_engine_id = getenv("GOOGLE_SEARCH_ENGINE_ID")
