"""Client for talking to the X (Twitter) API."""

import tweepy
from typing import Any

from config import get_settings

# TODO: Add a small class (e.g. XClient) that will handle all communication with X.

# TODO: Read API credentials (e.g. bearer token) from config or environment variables.

# TODO: Add a method/function to build the correct request URL and query parameters
#       for searching tech-related posts.

# TODO: Add a method/function to send HTTP requests to X (using requests or httpx)
#       and return the raw JSON response.

# TODO: Add basic error handling for failed requests (network issues, rate limits,
#       invalid credentials) and return clear error information.

# TODO: Add a simple helper to convert the raw JSON into Python dicts or model
#       objects that the rest of the app can work with.


class XClient:
    def __init__(self, bearer_token: str | None = None) -> None:
        settings = get_settings()
        token = bearer_token or settings["bearer_token"]
        self._max_results = settings["max_tweets_per_live_call"]
        self._client = tweepy.Client(bearer_token=token)

    def search_recent(self, query: str, max_results: int) -> Any:
        effective_max = min(max_results, self._max_results)

        response = self._client.search_recent_tweets(
            query=query,
            max_results=effective_max,
            tweet_fields=["created_at", "lang", "public_metrics", "author_id"],
            expansions=["author_id"],
            user_fields=["username"],
        )
        return response
