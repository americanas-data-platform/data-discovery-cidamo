from data_quality.src.transformer.aggregation_functions.general import describe_general
import pandas as pd

def describe_histogram(serie: pd.Series) -> dict:
    df_temp = serie.value_counts(bins=15, sort = False).to_frame().reset_index()
    df_temp.columns = ['value', 'value_counts']
    df_temp['LeftEnd'] = df_temp['value'].apply(lambda x: x.left)
    df_temp = df_temp[['LeftEnd', 'value_counts']]
    if df_temp.LeftEnd.dtype == 'datetime64[ns]':
        df_temp.LeftEnd = df_temp.LeftEnd.astype('string')

    describe_dict = df_temp.set_index('LeftEnd').to_dict()
    return describe_dict

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