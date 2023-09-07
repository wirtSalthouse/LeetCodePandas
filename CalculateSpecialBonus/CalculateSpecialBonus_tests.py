import unittest
import pandas as pd

from CalculateSpecialBonus.CalculateSpecialBonus import calculate_special_bonus
from TestUtils.testUtils import is_equal_dataframes


# Remember to import the function to test

class CalculateSpecialBonusTests(unittest.TestCase):
    def test_something(self):
        employees = pd.DataFrame(
            [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]],
            columns=['employee_id', 'name', 'salary'])
        bonus = calculate_special_bonus(employees)
        desired_bonus = pd.DataFrame([[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]], columns=['employee_id', 'bonus'])
        self.assertEqual(is_equal_dataframes(bonus, desired_bonus), True)


if __name__ == '__main__':
    unittest.main()
