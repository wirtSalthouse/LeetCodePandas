import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """
    returns a pandas DataFrame
    :param world:
    :return:
    """
    output_data = [['Afghanistan', 25500100, 652230],
                   ['Algeria', 37100000, 2381741]]

    # Create a DataFrame
    output_schema = ['name', 'population', 'area']
    output_df = pd.DataFrame(output_data, columns=output_schema)
    return output_df
