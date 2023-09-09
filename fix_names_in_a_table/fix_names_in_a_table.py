import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users.name = users.name.apply(lambda x: fix_one_name(x))
    return users.sort_values(by=['user_id']).reset_index(drop=True)


def fix_one_name(name: str) -> str:
    return name.lower().capitalize()
