import pandas as pd


# define function here:
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    row = patients.iloc[0]
    condition_string = row['conditions']
    if has_prefix(condition_string, 'DIAB'):
        return patients

    return pd.DataFrame()


def has_prefix(conditions: str, prefix: str) -> bool:
    cond_list = conditions.split(' ')
    for c in cond_list:
        if c.startswith(prefix):
            return True
    return False
