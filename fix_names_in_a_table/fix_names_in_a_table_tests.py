import unittest
import pandas as pd
from TestUtils.testUtils import is_equal_dataframes
import fix_names_in_a_table as names


class FixNamesInATableTests(unittest.TestCase):
    def make_table(self, data):
        table = pd.DataFrame(data, columns=['user_id', 'name'])
        return table

    def test_given_example(self):
        table_input = self.make_table([[1, 'aLice'], [2, 'bOB']])
        desired_output = self.make_table([[1, 'Alice'], [2, 'Bob']])
        result = names.fix_names(table_input)
        self.assertEqual(is_equal_dataframes(result, desired_output), True)

    def test_different_example(self):
        table_input = self.make_table([[1, 'KIRK'], [2, 'Bones'], [3, 'spock']])
        desired_output = self.make_table([[1, 'Kirk'], [2, 'Bones'], [3, 'Spock']])
        result = names.fix_names(table_input)
        self.assertEqual(is_equal_dataframes(result, desired_output), True)

    def test_must_be_sorted(self):
        table_input = self.make_table([[593, 'DAlia'], [944, 'FREIda'],[222, 'refAEL']])
        desired_output = self.make_table([[222, 'Refael'],[593, 'Dalia'],[944, 'Freida']])
        result = names.fix_names(table_input)
        self.assertEqual(is_equal_dataframes(result, desired_output), True)


    def test_component_function(self):
        self.assertEqual(names.fix_one_name('aLice'), 'Alice')

    def test_component_function_different_data(self):
        self.assertEqual(names.fix_one_name('bOB'), 'Bob')


if __name__ == '__main__':
    unittest.main()
