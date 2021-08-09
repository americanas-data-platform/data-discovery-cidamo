import pandas as pd
from src.transformer.aggregation_functions.general import describe_general


def describe_discrete(serie: pd.Series) -> dict:
    describe_dict = describe_general(serie)
    describe_dict["unique_values"] = [int(value) for value in serie.unique()]
    return describe_dict
