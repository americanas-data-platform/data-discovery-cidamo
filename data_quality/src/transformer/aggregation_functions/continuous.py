from data_quality.src.transformer.aggregation_functions.general import describe_general
import pandas as pd

def describe_continuous(serie: pd.Series) -> dict:
    describe_dict = describe_general(serie)
    describe_dict["min"] = float(serie.min())
    describe_dict["quantile_25"] = float(serie.quantile(0.25))
    describe_dict["quantile_50"] = float(serie.quantile(0.5))
    describe_dict["quantile_75"] = float(serie.quantile(0.75))
    describe_dict["max"] = float(serie.max())
    describe_dict["histogram"] = describe_histogram(serie) 
    return describe_dict

def describe_datetime(serie: pd.Series) -> dict:
    describe_dict = describe_general(serie)
    describe_dict["min"] = str(serie.min())
    describe_dict["quantile_25"] = str(serie.quantile(0.25))
    describe_dict["quantile_50"] = str(serie.quantile(0.5))
    describe_dict["quantile_75"] = str(serie.quantile(0.75))
    describe_dict["max"] = str(serie.max())
    describe_dict["histogram"] = describe_histogram(serie) 
    return describe_dict