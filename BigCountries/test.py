import unittest
import pandas as pd
from bigCountries import big_countries


class BigCountriesTest(unittest.TestCase):
    def test_default_case(self):
        input_schema = ['name', 'continent', 'area', 'population', 'gdp']
        input_data = [['Afghanistan', 'Asia', 652230, 25500100],
                      ['Albania', 'Europe', 28748, 2831741, 12960000000],
                      ['Algeria', 'Africa', 2381741, 37100000, 188681000000],
                      ['Andorra', 'Europe', 468, 78115, 3712000000],
                      ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
        input_df = pd.DataFrame(input_data, columns=input_schema)
        output_data = [['Afghanistan', 25500100, 652230],
                       ['Algeria', 37100000, 2381741]]

        # Create a DataFrame
        output_schema = ['name', 'population', 'area']
        output_df = pd.DataFrame(output_data, columns=output_schema)

        self.assertEqual(big_countries(input_df).equals(output_df), True)


if __name__ == '__main__':
    unittest.main()
