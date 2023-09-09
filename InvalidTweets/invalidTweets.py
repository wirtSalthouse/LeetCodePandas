import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    char_limit = 15
    if tweets.empty:
        return return_df([])

    tweets.content = tweets.content.astype('str')
    filtered = tweets.loc[tweets.content.apply(lambda x: len(x) > char_limit)]
    return return_df(filtered.tweet_id.tolist())


def return_df(data_list):
    return pd.DataFrame({'tweet_id': data_list})
