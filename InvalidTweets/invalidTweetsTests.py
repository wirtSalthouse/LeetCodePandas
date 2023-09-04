import unittest
import pandas as pd

from InvalidTweets.invalidTweets import invalid_tweets
from TestUtils.testUtils import is_equal_dataframes


class MyTestCase(unittest.TestCase):
    def test_empty_input(self):
        input_table = pd.DataFrame({'tweet_id': [], 'content': []})
        desired_output = pd.DataFrame({'tweet_id': []})
        result = invalid_tweets(input_table)
        self.assertEqual(is_equal_dataframes(result, desired_output), True)

    def test_supplied_test_case(self):
        input_schema = ['tweet_id', 'content']
        input_data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
        input_table = pd.DataFrame(input_data, columns=input_schema)
        desired_output = pd.DataFrame({'tweet_id': [2]})
        result = invalid_tweets(input_table)
        self.assertEqual(is_equal_dataframes(result, desired_output), True)


if __name__ == '__main__':
    unittest.main()
