import unittest
import pandas as pd
from TestUtils.testUtils import is_equal_dataframes

from find_patients import find_patients


class find_patientsTests(unittest.TestCase):
	def test_single_entry_no_change(self):
		input_table = pd.DataFrame([['3', 'Don', 'DIAB007']], columns=['patient_id', 'patient_name', 'conditions'])
		filtered_table = find_patients(input_table)
		self.assertEqual(is_equal_dataframes(input_table, filtered_table), True)

	def test_single_entry_no_matches(self):
		input_table = pd.DataFrame([['5', 'Tim', 'ACNE']], columns=['patient_id', 'patient_name', 'conditions'])
		filtered_table = find_patients(input_table)
		self.assertEqual(filtered_table.empty,  True)

	def test_single_entry_no_change_comma_data(self):
		input_table = pd.DataFrame([['3', 'Don', 'COUGH DIAB007']], columns=['patient_id', 'patient_name', 'conditions'])
		filtered_table = find_patients(input_table)
		self.assertEqual(is_equal_dataframes(input_table, filtered_table), True)

if __name__ == '__main__':
	unittest.main()