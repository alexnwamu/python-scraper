"""Data model(s) for representing tweets and related information."""

# TODO: Import dataclasses and define a simple Tweet dataclass with fields like:
#       - id: str
#       - text: str
#       - author: str
#       - created_at: str or datetime
#       - maybe extra fields (like like_count, retweet_count).
# TODO: Add a classmethod or helper function (e.g. from_json) that creates
#       a Tweet instance from a raw JSON dictionary.

# TODO: Optionally implement a __str__ or __repr__ method to display tweets
#       nicely when printed.


class Tweet:
    def __init__(
        self,
        id: str,
        text: str,
        author: str,
        created_at: str,
        like_count: int,
        retweet_count: int,
    ):
        self.id = id
        self.text = text
        self.author = author
        self.created_at = created_at
        self.like_count = like_count
        self.retweet_count = retweet_count
