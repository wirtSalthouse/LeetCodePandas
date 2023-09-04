import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """
    returns a pandas DataFrame containing only "big countries",
    table entries which have a area greater than 3,000,000 or population greater than 25,000,000
    :param world:
    :return:new dataframe with schema of name, population and area
    """

    min_area = 3000000
    min_population = 25000000

    query_string = f'(area >= {min_area}) | (population >= {min_population})'
    output_schema = ['name', 'population', 'area']
    output_data = world.query(query_string)[output_schema].values.tolist()
    #whole new df to match indexing for test cases
    return pd.DataFrame(output_data, columns=output_schema)
