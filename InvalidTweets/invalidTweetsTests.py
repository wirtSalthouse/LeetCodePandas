import unittest
import pandas as pd

from InvalidTweets.invalidTweets import invalid_tweets
from TestUtils.testUtils import is_equal_dataframes


class MyTestCase(unittest.TestCase):
    def input_df(self, data):
        return pd.DataFrame(data, columns=['tweet_id', 'content'])

    def output_df(self, data):
        return pd.DataFrame({'tweet_id': data})

    def test_empty_input(self):
        input_table = self.input_df([])
        desired_output = self.output_df([])
        result = invalid_tweets(input_table)
        self.assertEqual(is_equal_dataframes(result, desired_output), True)

    def test_supplied_test_case(self):
        input_table = self.input_df([[1, 'Vote for Biden'], [2, 'Let us make America great again!']])
        desired_output = self.output_df([2])
        result = invalid_tweets(input_table)
        self.assertEqual(is_equal_dataframes(result, desired_output), True)

    def test_supplied_test_case_reordered(self):
        input_table = self.input_df([[2, 'Vote for Biden'], [1, 'Let us make America great again!']])
        desired_output = self.output_df([1])
        result = invalid_tweets(input_table)
        self.assertEqual(is_equal_dataframes(result, desired_output), True)


if __name__ == '__main__':
    unittest.main()
