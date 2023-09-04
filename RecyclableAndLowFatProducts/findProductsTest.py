import unittest
import pandas as pd
from RecyclableAndLowFatProducts.recyclableAndLowfatProducts import find_products

from TestUtils.testUtils import is_equal_dataframes


class MyTestCase(unittest.TestCase):
    def test_given_case(self):
        input = pd.DataFrame({'product_id': [0, 1, 2, 3, 4], 'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
                              'recyclable': ['N', 'Y', 'Y', 'Y', 'N']})
        result = find_products(input)
        expected = pd.DataFrame({'product_id': [1, 3]})
        self.assertEqual(is_equal_dataframes(result, expected), True)

    def test_different_data(self):
        input = pd.DataFrame({'product_id': [0, 1, 2, 3, 4], 'low_fats': ['Y', 'N', 'N', 'Y', 'Y'],
                              'recyclable': ['Y', 'Y', 'Y', 'N', 'Y']})
        result = find_products(input)
        expected = pd.DataFrame({'product_id': [0, 4]})
        self.assertEqual(is_equal_dataframes(result, expected), True)

    def test_single_entry_true(self):
        input = pd.DataFrame({'product_id': [0], 'low_fats': ['Y'],
                              'recyclable': ['Y']})
        result = find_products(input)
        expected = pd.DataFrame({'product_id': [0]})
        self.assertEqual(is_equal_dataframes(result, expected), True)

    def test_single_entry_false_1(self):
        input = pd.DataFrame({'product_id': [0], 'low_fats': ['N'],
                              'recyclable': ['N']})
        result = find_products(input)
        expected = pd.DataFrame({'product_id': []})
        self.assertEqual(is_equal_dataframes(result, expected), True)

    def test_single_entry_false_2(self):
        input = pd.DataFrame({'product_id': [0], 'low_fats': ['N'],
                              'recyclable': ['Y']})
        result = find_products(input)
        expected = pd.DataFrame({'product_id': []})
        self.assertEqual(is_equal_dataframes(result, expected), True)

    def test_single_entry_false_3(self):
        input = pd.DataFrame({'product_id': [0], 'low_fats': ['Y'],
                              'recyclable': ['N']})
        result = find_products(input)
        expected = pd.DataFrame({'product_id': []})
        self.assertEqual(is_equal_dataframes(result, expected), True)

    def test_single_entry_true(self):
        input = pd.DataFrame({'product_id': [0], 'low_fats': ['Y'],
                              'recyclable': ['Y']})
        result = find_products(input)
        expected = pd.DataFrame({'product_id': [0]})
        self.assertEqual(is_equal_dataframes(result, expected), True)
if __name__ == '__main__':
    unittest.main()
