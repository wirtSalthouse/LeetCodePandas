import unittest
import pandas as pd
from TestUtils.testUtils import is_equal_dataframes

from find_patients import find_patients

COLUMN_ROWS = ['patient_id', 'patient_name', 'conditions']


class FindPatientsTests(unittest.TestCase):
    def test_single_entry_no_change(self):
        input_table = pd.DataFrame([['3', 'Don', 'DIAB1007']], columns=COLUMN_ROWS)
        filtered_table = find_patients(input_table)
        self.assertEqual(is_equal_dataframes(input_table, filtered_table), True)

    def test_single_entry_no_matches(self):
        input_table = pd.DataFrame([['5', 'Tim', 'ACNE']], columns=COLUMN_ROWS)
        filtered_table = find_patients(input_table)
        self.assertEqual(filtered_table.empty, True)

    def test_single_entry_no_change_comma_data(self):
        input_table = pd.DataFrame([[3, 'Don', 'COUGH DIAB1007']], columns=COLUMN_ROWS)
        filtered_table = find_patients(input_table)
        self.assertEqual(is_equal_dataframes(input_table, filtered_table), True)

    def test_given_case(self):
        input_data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'],
                      [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
        input_table = pd.DataFrame(input_data, columns=COLUMN_ROWS)
        filtered_table = find_patients(input_table)
        output_table = pd.DataFrame([[3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100']], columns=COLUMN_ROWS)
        self.assertEqual(is_equal_dataframes(filtered_table, output_table), True)


if __name__ == '__main__':
    unittest.main()
