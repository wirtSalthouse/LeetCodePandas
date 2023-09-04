import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    auth_id = 'author_id'
    selection = views.query(f'({auth_id} == viewer_id)')
    selection = selection.sort_values(auth_id)
    unique_and_sorted_ids = selection[auth_id].drop_duplicates().tolist()
    return pd.DataFrame({'id': unique_and_sorted_ids})
