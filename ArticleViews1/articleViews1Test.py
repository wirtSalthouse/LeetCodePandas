import unittest
import pandas as pd
from TestUtils.testUtils import is_equal_dataframes
from ArticleViews1.articleViews import article_views


class ArticleViews1Tests(unittest.TestCase):
    def test_no_views(self):
        no_views_table = pd.DataFrame({'article_id':[], 'author_id':[], 'viewer_id':[], 'view_date':[]})
        desired_result = pd.DataFrame({'id':[]})
        result = article_views(no_views_table)
        self.assertEqual(is_equal_dataframes(result,desired_result), True)


if __name__ == '__main__':
    unittest.main()
