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


if __name__ == '__main__':
    unittest.main()
