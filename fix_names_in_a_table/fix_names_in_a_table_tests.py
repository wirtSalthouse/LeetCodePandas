import unittest
import pandas as pd
from TestUtils.testUtils import is_equal_dataframes
from fix_names_in_a_table import fix_names


class fixNamesInATableTests(unittest.TestCase):
    def make_table(self, data):
        table = pd.DataFrame(data, columns=['user_id', 'name'])
        return table

    def test_given_example(self):
        table_input = self.make_table([[1, 'aLice'], [2, 'bOB']])
        desired_output = self.make_table([[1, 'Alice'], [2, 'Bob']])
        result = fix_names(table_input)
        self.assertEqual(is_equal_dataframes(result, desired_output), True)


if __name__ == '__main__':
    unittest.main()
