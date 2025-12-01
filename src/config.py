"""Configuration helpers for the X tech scraper."""

import os
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv

load_dotenv()

# TODO: Import os to read environment variables (e.g. X API token).

# TODO: Define simple constants, such as:
#       - BASE_URL for the X API.
#       - DEFAULT_SEARCH_QUERY for tech topics.
#       - OUTPUT_FILE path for where to store scraped data.

BASE_URL = "https://api.twitter.com/2"

DEFAULT_SEARCH_QUERY = "(python OR rust OR typescript OR golang) lang:en -is:retweet"

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "data" / "sample_tweets.json"
MAX_TWEETS_PER_LIVE_CALL = 20

# TODO: Add a helper function (e.g. get_settings()) that:
#       - Reads required environment variables.
#       - Applies any default values.
#       - Returns a simple dict or small object with all settings.


def get_settings() -> Dict[str, Any]:
    """Return configuration settings for the scraper.

    Expects the X_BEARER_TOKEN environment variable to be set.
    """

    bearer_token = os.getenv("X_BEARER_TOKEN")
    if not bearer_token:
        raise RuntimeError(
            "X_BEARER_TOKEN environment variable is required to talk to the X API."
        )

    return {
        "bearer_token": bearer_token,
        "base_url": BASE_URL,
        "default_search_query": DEFAULT_SEARCH_QUERY,
        "output_file": str(OUTPUT_FILE),
        "max_tweets_per_live_call": MAX_TWEETS_PER_LIVE_CALL,
    }


# TODO: Add basic validation and clear error messages if required
#       configuration values are missing.
