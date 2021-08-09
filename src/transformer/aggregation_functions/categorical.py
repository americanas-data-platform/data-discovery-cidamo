import pandas as pd
from src.transformer.aggregation_functions.general import describe_general


def describe_categorical(serie: pd.Series) -> dict:
    describe_dict = describe_general(serie)
    # describe_dict["unique_values"] = list(serie.unique())
    return describe_dict

