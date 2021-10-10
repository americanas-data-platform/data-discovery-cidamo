import pandas as pd
from data_quality.src.transformer.aggregation_functions.general import describe_general

def describe_categorical(serie: pd.Series) -> dict:
    describe_dict = describe_general(serie)
    describe_dict["mode"] = [list(serie.mode())[0]]
    return describe_dict