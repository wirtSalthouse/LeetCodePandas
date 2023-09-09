import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients.apply(lambda x: has_prefix(x.conditions, 'DIAB1'), axis=1)].reset_index(drop=True)


def has_prefix(conditions: str, prefix: str) -> bool:
    cond_list = conditions.split(' ')
    for c in cond_list:
        if c.startswith(prefix):
            return True
    return False
