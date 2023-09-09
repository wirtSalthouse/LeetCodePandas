import pandas as pd


def find_customers(customers, orders):
    if customers.empty and (not orders.empty):
        raise Exception("Can't have orders without customers")

    if customers.empty:
        return df_from_list([])

    if orders.empty:
        return df_from_list(customers['name'])

    for id in orders['customer_id']:
        customers = customers.drop(customers[customers['id'] == id].index)

    return df_from_list(customers['name'].tolist())


def df_from_list(id_list):
    return pd.DataFrame({'Customers': id_list})
