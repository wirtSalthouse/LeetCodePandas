import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """
    returns a pandas DataFrame containing only "big countries",
    table entries which have an area greater than 3,000,000 or a population greater than 25,000,000
    :param world: DataFrame with keys including name, population, and area
    :return:new DataFrame with schema of name, population, and area
    """,

    country_parser = CountryParser()
    selection = country_parser.get_selection(world)
    output_data = selection.values.tolist()
    return country_parser.new_dataframe(output_data)


class CountryParser():
    _area = 3000000
    _pop = 25000000
    _schema = ['name', 'population', 'area']

    def get_selection(self, dataframe):
        query_string = f'(area >= {self._area}) | (population >= {self._pop})'
        return dataframe.query(query_string)[self._schema]

    def new_dataframe(self, data):
        return pd.DataFrame(data, columns=self._schema)
