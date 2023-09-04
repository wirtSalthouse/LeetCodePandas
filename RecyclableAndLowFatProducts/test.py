import unittest
import pandas as pd


def find_products():
    return -1


class MyTestCase(unittest.TestCase):
    def test_given_case(self):
        input = pd.DataFrame({'product_id': [0, 1, 2, 3, 4], 'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
                              'recyclable': ['N', 'Y', 'Y', 'Y', 'N']})
        result = find_products(input)
        expected = pd.DataFrame({'product_id': [1, 3]})
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
