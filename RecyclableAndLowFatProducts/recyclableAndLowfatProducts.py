import pandas as pd


def find_products(df):
    ans = df.query('(low_fats == \'Y\') & (recyclable == \'Y\')')
    return pd.DataFrame({'product_id': ans['product_id'].tolist()})
