import unittest
import pandas as pd

from CalculateSpecialBonus import calculate_special_bonus
from TestUtils.testUtils import is_equal_dataframes

# Remember to import the function to test
EMPLOYEE_COLUMNS = ['employee_id', 'name', 'salary']
BONUS_COLUMNS = ['employee_id', 'bonus']


class CalculateSpecialBonusTests(unittest.TestCase):
    def test_given_example(self):
        employees = pd.DataFrame(
            [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]],
            columns=EMPLOYEE_COLUMNS)
        bonus = calculate_special_bonus(employees)
        desired_bonus = pd.DataFrame([[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]], columns=BONUS_COLUMNS)
        self.assertEqual(is_equal_dataframes(bonus, desired_bonus), True)

    def test_smaller_example(self):
        employees = pd.DataFrame([[7, 'mary', 4200], [1, 'steve', 1800], [4, 'Kirk', 5000]], columns=EMPLOYEE_COLUMNS)
        bonus = calculate_special_bonus(employees)
        desired_bonus = pd.DataFrame([[1, 1800], [4, 0], [7, 0]], columns=BONUS_COLUMNS)
        self.assertEqual(is_equal_dataframes(bonus, desired_bonus), True)


if __name__ == '__main__':
    unittest.main()
