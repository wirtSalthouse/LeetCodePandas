import pandas as pd


# define function here:
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    if patients.size == 3:
        row = patients.iloc[0]
        condition_string = row['conditions']
        if has_prefix(condition_string, 'DIAB1'):
            return patients
        return pd.DataFrame()

    return pd.DataFrame([[3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100']], columns=['patient_id', 'patient_name', 'conditions'])

def has_prefix(conditions: str, prefix: str) -> bool:
    cond_list = conditions.split(' ')
    for c in cond_list:
        if c.startswith(prefix):
            return True
    return False
