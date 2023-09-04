import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:
    value = nth_highest(employee.salary.tolist(), n)
    return pd.DataFrame({f'getNthHighestSalary({n})': [value]})


def nth_highest(salaries: list, ndx: int) -> int | None:
    salaries = list(set(salaries))
    if ndx > len(salaries):
        return None

    salaries.sort(reverse=True)
    return salaries[ndx - 1]
