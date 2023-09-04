import unittest
import pandas as pd
from TestUtils.testUtils import is_equal_dataframes
from nth_highest_salary import nth_highest_salary


class nthHighestSalaryTests(unittest.TestCase):
    def input_table(self, data):
        return pd.DataFrame(data, columns=['id', 'salary'])

    def test_null_case_1(self):
        table_input = self.input_table([[1, 100]])
        desired_result = pd.DataFrame({'getNthHighestSalary(2)': [None]})
        result = nth_highest_salary(table_input, 2)
        self.assertEqual(is_equal_dataframes(result, desired_result), True)

    def test_example_case(self):
        table_input = self.input_table([[1, 100], [2, 200], [3, 300]])
        desired_result = pd.DataFrame({'getNthHighestSalary(2)': [200]})
        result = nth_highest_salary(table_input, 2)
        self.assertEqual(is_equal_dataframes(result, desired_result), True)

    def test_first_highest_paid(self):
        table_input = self.input_table([[1, 100], [2, 200], [3, 300]])
        desired_result = pd.DataFrame({'getNthHighestSalary(1)': [300]})
        result = nth_highest_salary(table_input, 1)
        self.assertEqual(is_equal_dataframes(result, desired_result), True)

if __name__ == '__main__':
    unittest.main()
