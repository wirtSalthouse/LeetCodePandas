import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    area = 3000000
    pop = 25000000
    query_string = f'(area >= {area}) | (population >= {pop})'
    schema = ['name', 'population', 'area']
    selection = world.query(query_string)[schema]
    return selection.reset_index(drop=True)
