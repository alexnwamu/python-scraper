"""Main entry point for the X tech scraper project."""

import argparse

from scraper.fetch import fetch_tech_tweets
from config import get_settings


def main() -> None:
    parser = argparse.ArgumentParser(description="X tech scraper")
    parser.add_argument(
        "--query",
        type=str,
        default=None,
        help="Search query for tech tweets (defaults to configured query)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of tweets to fetch or load",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="Fetch from the live X API instead of using the local cache",
    )

    args = parser.parse_args()

    tweets = fetch_tech_tweets(query=args.query, limit=args.limit, use_live=args.live)

    settings = get_settings()
    output_file = settings["output_file"]

    print(f"Fetched {len(tweets)} tweets (live={args.live}).")
    print(f"Cache file: {output_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="X tech scraper")
    parser.add_argument(
        "--query",
        type=str,
        default=None,
        help="Search query for tech tweets (defaults to configured query)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of tweets to fetch or load",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="Fetch from the live X API instead of using the local cache",
    )

    args = parser.parse_args()

    tweets = fetch_tech_tweets(query=args.query, limit=args.limit, use_live=args.live)

    settings = get_settings()
    output_file = settings["output_file"]

    print(f"Fetched {len(tweets)} tweets (live={args.live}).")
    print(f"Cache file: {output_file}")


if __name__ == "__main__":
    main()
