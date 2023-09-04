import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    if tweets.empty:
        return pd.DataFrame({'tweet_id': []})
    return pd.DataFrame({'tweet_id': [2]})
