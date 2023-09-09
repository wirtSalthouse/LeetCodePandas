import unittest
import pandas as pd
from TestUtils.testUtils import is_equal_dataframes
from ArticleViews1.articleViews import article_views


class ArticleViews1Tests(unittest.TestCase):
    def test_no_views(self):
        no_views_table = pd.DataFrame({'article_id': [], 'author_id': [], 'viewer_id': [], 'view_date': []})
        desired_result = pd.DataFrame({'id': []})
        result = article_views(no_views_table)
        self.assertEqual(is_equal_dataframes(result, desired_result), True)

    def test_one_author_viewed_twice(self):
        input_table = pd.DataFrame(
            {'article_id': [3], 'author_id': [4], 'viewer_id': [4], 'view_date': ['2019-07-21']})
        desired_result = pd.DataFrame({'id': [4]})
        result = article_views(input_table)
        self.assertEqual(is_equal_dataframes(result, desired_result), True)

    def test_one_author_did_not_self_view(self):
        input_table = pd.DataFrame(
            {'article_id': [3, 3], 'author_id': [4, 4], 'viewer_id': [4, 5], 'view_date': ['2019-07-21', '2019-07-22']})
        desired_result = pd.DataFrame({'id': [4]})
        result = article_views(input_table)
        self.assertEqual(is_equal_dataframes(result, desired_result), True)

    def test_prompt_example(self):
        input_schema = ['article_id', 'author_id', 'viewer_id', 'view_date']
        input_data = [
            [1, 3, 5, '2019-08-0'],
            [1, 3, 6, '2019-08-02'],
            [2, 7, 7, '2019-08-01'],
            [2, 7, 6, '2019-08-02'],
            [4, 7, 1, '2019-07-22'],
            [3, 4, 4, '2019-07-21'],
            [3, 4, 4, '2019-07-21']
        ]
        input_table = pd.DataFrame(input_data, columns=input_schema)
        desired_result = pd.DataFrame({'id': [4, 7]})
        result = article_views(input_table)
        self.assertEqual(is_equal_dataframes(result, desired_result), True)


if __name__ == '__main__':
    unittest.main()
