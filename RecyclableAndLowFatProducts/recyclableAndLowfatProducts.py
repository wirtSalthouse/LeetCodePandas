import pandas as pd


def find_products(df):
    prod_id = 'product_id'

    selection = df.query(f'{is_y("low_fats")} & {is_y("recyclable")}')
    return selection.drop(['low_fats', 'recyclable'], axis=1).reset_index(drop=True)
    return pd.DataFrame({prod_id: selection[prod_id].tolist()})


def is_y(key_string):
    return f"({key_string} == 'Y')"
