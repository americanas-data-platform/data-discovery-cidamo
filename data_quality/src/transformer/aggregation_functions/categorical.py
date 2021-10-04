import pandas as pd
from data_quality.src.transformer.aggregation_functions.general import describe_general

def describe_categorical(serie: pd.Series) -> dict:
    describe_dict = describe_general(serie)
    describe_dict["unique_values"] = [value for value in serie.unique()]
    describe_dict["mode"] = serie.mode()
    return describe_dict