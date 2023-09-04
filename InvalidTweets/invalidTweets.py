import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    if tweets.empty:
        return pd.DataFrame({'tweet_id': []})
    filtered = tweets.query('content == \'Let us make America great again!\'')
    return pd.DataFrame({'tweet_id': filtered['tweet_id'].values.tolist()})
