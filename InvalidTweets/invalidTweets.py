import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    if tweets.empty:
        return pd.DataFrame({'tweet_id': []})

    tweets.content = tweets.content.astype('str')
    applied_mask = tweets.content.apply(lambda x: len(x) > 15)
    filtered = tweets.loc[applied_mask]
    return pd.DataFrame({'tweet_id': filtered['tweet_id'].values.tolist()})
