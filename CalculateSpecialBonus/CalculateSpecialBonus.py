import pandas as pd


def get_bonus(em_id, name, salary):
    if name[0].lower() == 'm':
        return 0
    return (em_id % 2) * salary


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    emp_id = 'employee_id'
    n = 'name'
    s = 'salary'
    employees['bonus'] = employees.apply(lambda x: get_bonus(x[emp_id], x[n], x[s]), axis=1)

    return employees.drop([n, s], axis=1).sort_values(emp_id).reset_index(drop=True)
