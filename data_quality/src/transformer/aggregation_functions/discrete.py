import pandas as pd
from data_quality.src.transformer.aggregation_functions.general import describe_general


def describe_discrete(serie: pd.Series) -> dict:
    describe_dict = describe_general(serie)
    describe_dict["min"] = int(serie.min())
    describe_dict["max"] = int(serie.max())
    describe_dict["histogram"] = describe_histogram(serie)
    return describe_dict
     