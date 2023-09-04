import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    selection = views.query('(author_id == viewer_id)')
    return pd.DataFrame({'id': remove_duplicates(selection['author_id'])})


def remove_duplicates(author_ids):
    return list(set(author_ids))
