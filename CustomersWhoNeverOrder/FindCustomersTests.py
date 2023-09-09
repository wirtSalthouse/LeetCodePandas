import unittest
import pandas as pd
from TestUtils.testUtils import is_equal_dataframes as equal_dataframes
from CustomersWhoNeverOrder.FindCustomers import find_customers


class FindCustomersTests(unittest.TestCase):
    def test_no_orders_existing_customer(self):
        #The only customer is Joe, and he doesn't order anything
        customer_table = pd.DataFrame({'id': [1], 'name': ['Joe']})
        orders_table = pd.DataFrame({'id': [], 'customer_id': []})
        output_table = pd.DataFrame({'Customers': ['Joe']})
        result = find_customers(customer_table, orders_table)
        self.assertEqual(equal_dataframes(result, output_table), True)

    def test_no_orders_existing_customers(self):
        #There are customers, but none of them ordered anything
        customer_table = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Harry', 'Sally', 'Jess', 'Marie']})
        orders_table = pd.DataFrame({'id': [], 'customer_id': []})
        output_table = pd.DataFrame({'Customers': ['Harry', 'Sally', 'Jess', 'Marie']})
        self.assertEqual(equal_dataframes(find_customers(customer_table, orders_table), output_table), True)

    def test_no_orders_no_customers(self):
        #there are not customers, so none of them can order anything
        customer_table = pd.DataFrame({'id': [], 'name': []})
        orders_table = pd.DataFrame({'id': [], 'customer_id': []})
        output_table = pd.DataFrame({'Customers': []})
        self.assertEqual(equal_dataframes(find_customers(customer_table, orders_table), output_table), True)

    def test_existing_orders_no_customers(self):
        # assumes orders are always a subset of customers, so will throw for now
        error_customer_table = pd.DataFrame({'id': [], 'name': []})
        error_orders_table = pd.DataFrame({'id': [1], 'customer_id': [1]})

        with self.assertRaises(Exception):
            find_customers(error_customer_table,error_orders_table)

    def test_simple_intersection(self):
        #harry ordered something, but Jess did not
        customer_table = pd.DataFrame({'id': [1, 2], 'name': ['Harry',  'Jess']})
        orders_table = pd.DataFrame({'id': [1], 'customer_id': [1]})
        output_table = pd.DataFrame({'Customers': ['Jess']})
        result = find_customers(customer_table, orders_table)
        self.assertEqual(equal_dataframes(result, output_table), True)

    def test_simple_intersection_different_data(self):
        #Jess ordered something, but Harry did not
        customer_table = pd.DataFrame({'id': [1, 2], 'name': ['Harry',  'Jess']})
        orders_table = pd.DataFrame({'id': [1], 'customer_id': [2]})
        output_table = pd.DataFrame({'Customers': ['Harry']})
        result = find_customers(customer_table, orders_table)
        self.assertEqual(equal_dataframes(result, output_table), True)



if __name__ == '__main__':
    unittest.main()
