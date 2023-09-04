import unittest
import pandas as pd
from TestUtils.testUtils import is_equal_dataframes as equal_dataframes
from CustomersWhoNeverOrder.FindCustomers import find_customers


class FindCustomersTests(unittest.TestCase):
    def test_simplest_case_of_one(self):
        customer_table = pd.DataFrame({'id': [1], 'name': ['Joe']})
        orders_table = pd.DataFrame({'id': [1], 'customer_id': [1]})
        output_table = pd.DataFrame({'Customers': [0]})
        self.assertEqual(equal_dataframes(find_customers(customer_table, orders_table), output_table), True)


if __name__ == '__main__':
    unittest.main()
