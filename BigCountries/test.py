import unittest
import pandas as pd
from bigCountries import big_countries


def input_dataframe(data_list):
    input_schema = ['name', 'continent', 'area', 'population', 'gdp']
    return pd.DataFrame(data_list, columns=input_schema)


def output_dataframe(data_list):
    output_schema = ['name', 'population', 'area']
    return pd.DataFrame(data_list, columns=output_schema)


class BigCountriesTest(unittest.TestCase):

    def test_default_case(self):
        input_data = [['Afghanistan', 'Asia', 652230, 25500100],
                      ['Albania', 'Europe', 28748, 2831741, 12960000000],
                      ['Algeria', 'Africa', 2381741, 37100000, 188681000000],
                      ['Andorra', 'Europe', 468, 78115, 3712000000],
                      ['Angola', 'Africa', 1246700, 20609294, 100990000000]]

        output_data = [['Afghanistan', 25500100, 652230],
                       ['Algeria', 37100000, 2381741]]

        input_df = input_dataframe(input_data)
        output_df = output_dataframe(output_data)
        self.assert_equal_dataframes(big_countries(input_df), output_df)

    def test_case_2(self):
        input_data = [['Afghanistan', 'Asia', 652230, 25500100],
                      ['Albania', 'Europe', 28748, 2831741, 12960000000],
                      ['Andorra', 'Europe', 468, 78115, 3712000000],
                      ['Angola', 'Africa', 1246700, 20609294, 100990000000]]

        output_data = [['Afghanistan', 25500100, 652230]]

        input_df = input_dataframe(input_data)
        output_df = output_dataframe(output_data)
        self.assert_equal_dataframes(big_countries(input_df), output_df)

    def assert_equal_dataframes(self, df1, df2):
        self.assertEqual(df1.equals(df2), True)


if __name__ == '__main__':
    unittest.main()
