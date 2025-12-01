"""High-level functions for fetching tech content from X."""

from __future__ import annotations

from pathlib import Path
from typing import List
import json

from scraper.client import XClient
from config import get_settings
from models.tweet import Tweet

# TODO: Import any parser helpers from scraper.parse.


def _ensure_parent_dir(path: str) -> None:
    parent = Path(path).parent
    parent.mkdir(parents=True, exist_ok=True)


def _tweets_from_dicts(items: list[dict]) -> List[Tweet]:
    tweets: List[Tweet] = []
    for item in items:
        tweets.append(
            Tweet(
                id=str(item.get("id", "")),
                text=item.get("text", ""),
                author=item.get("author", ""),
                created_at=item.get("created_at", ""),
                like_count=int(item.get("like_count", 0)),
                retweet_count=int(item.get("retweet_count", 0)),
            )
        )
    return tweets


def fetch_tech_tweets(
    query: str | None = None,
    limit: int = 20,
    use_live: bool = False,
) -> List[Tweet]:
    """Fetch tech-related tweets either from the X API or from a local cache.

    When use_live is True, a small number of tweets are fetched from the X API
    (within the configured per-call limit) and written to the cache file. When
    use_live is False, tweets are loaded from the cache file instead.
    """

    settings = get_settings()
    effective_query = query or settings["default_search_query"]
    output_file = settings["output_file"]

    if use_live:
        client = XClient()
        response = client.search_recent(effective_query, max_results=limit)

        raw_tweets = []

        if response.data is not None:
            users_by_id = {}
            includes = getattr(response, "includes", None) or {}
            users = includes.get("users", []) if isinstance(includes, dict) else []
            for user in users:
                # tweepy User object: id and username attributes
                users_by_id[str(getattr(user, "id", ""))] = getattr(
                    user, "username", ""
                )

            for tweet in response.data:
                metrics = getattr(tweet, "public_metrics", {}) or {}
                author_id = str(getattr(tweet, "author_id", ""))
                author_name = users_by_id.get(author_id, "")
                raw_tweets.append(
                    {
                        "id": str(getattr(tweet, "id", "")),
                        "text": getattr(tweet, "text", ""),
                        "author": author_name,
                        "created_at": str(getattr(tweet, "created_at", "")),
                        "like_count": int(metrics.get("like_count", 0)),
                        "retweet_count": int(metrics.get("retweet_count", 0)),
                    }
                )

        _ensure_parent_dir(output_file)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(raw_tweets, f, ensure_ascii=False, indent=2)

        return _tweets_from_dicts(raw_tweets)

    # Offline mode: load from cache.
    cache_path = Path(output_file)
    if not cache_path.exists():
        return []

    with cache_path.open("r", encoding="utf-8") as f:
        items = json.load(f)

    # Respect the requested limit in offline mode as well.
    if isinstance(items, list) and limit < len(items):
        items = items[:limit]

    return _tweets_from_dicts(items)


# TODO: Optionally add small helper functions for:
#       - Fetching multiple pages of results.
#       - Printing simple progress messages to the console.
