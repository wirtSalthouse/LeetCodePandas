import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """
    returns a pandas DataFrame
    :param world:
    :return:new dataframe with schema of name, population and area
    """

    answer = world.query('(area >= 3000000) | (population >= 25000000)')
    output_schema = ['name', 'population', 'area']
    answer = answer[output_schema]
    print(answer)
    return answer
