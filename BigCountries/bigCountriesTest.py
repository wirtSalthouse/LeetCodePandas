import unittest
import pandas as pd
from BigCountries.bigCountries import big_countries
from TestUtils.testUtils import is_equal_dataframes


def df_from_schema_and_data(schema, data):
    return pd.DataFrame(data, columns=schema)


def input_dataframe(data_list):
    return df_from_schema_and_data(['name', 'continent', 'area', 'population', 'gdp'], data_list)


def output_dataframe(data_list):
    return df_from_schema_and_data(['name', 'population', 'area'], data_list)


class BigCountriesTest(unittest.TestCase):

    def test_default_case(self):
        input_data = [['Afghanistan', 'Asia', 652230, 25500100],
                      ['Albania', 'Europe', 28748, 2831741, 12960000000],
                      ['Algeria', 'Africa', 2381741, 37100000, 188681000000],
                      ['Andorra', 'Europe', 468, 78115, 3712000000],
                      ['Angola', 'Africa', 1246700, 20609294, 100990000000]]

        desired_output_data = [['Afghanistan', 25500100, 652230],
                               ['Algeria', 37100000, 2381741]]

        input_df = input_dataframe(input_data)

        result = big_countries(input_df)

        desired_result = output_dataframe(desired_output_data)
        self.assertEqual(is_equal_dataframes(result, desired_result), True)

    def test_case_2(self):
        input_data = [['Afghanistan', 'Asia', 652230, 25500100],
                      ['Albania', 'Europe', 28748, 2831741, 12960000000],
                      ['Andorra', 'Europe', 468, 78115, 3712000000],
                      ['Angola', 'Africa', 1246700, 20609294, 100990000000]]

        desired_output_data = [['Afghanistan', 25500100, 652230]]

        input_df = input_dataframe(input_data)

        result = big_countries(input_df)

        desired_result = output_dataframe(desired_output_data)
        self.assertEqual(is_equal_dataframes(result, desired_result), True)

    def test_single_entry_different_data(self):
        input_data = [['Latveria', 'Europe', 600, 1000000],
                      ['Wakanda', 'Africa', 28748, 25000000, 1897900000],
                      ['Duckburg', 'Calisota', 10000, 78115, 261200000000000000000]]

        desired_output_data = [['Wakanda', 25000000, 28748]]

        input_df = input_dataframe(input_data)
        desired_df = output_dataframe(desired_output_data)

        result = big_countries(input_df)

        self.assertEqual(is_equal_dataframes(result, desired_df), True)

    def test_no_matches(self):
        input_data = [['Latveria', 'Europe', 600, 1000000],
                      ['Wakanda', 'Africa', 28748, 25000, 1897900000],
                      ['Duckburg', 'Calisota', 10000, 78115, 261200000000000000000]]

        input_df = input_dataframe(input_data)

        result = big_countries(input_df)
        self.assertEqual(result.empty, True)


if __name__ == '__main__':
    unittest.main()
