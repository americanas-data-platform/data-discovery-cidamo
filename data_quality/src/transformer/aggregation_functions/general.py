import pandas as pd

def describe_list10(serie: pd.Series, choose: str, count: bool) -> dict:
    if serie.dtype == "datetime64[ns]":
        serie = serie.astype("string")

    if choose == "top":
        describe_dict = serie.value_counts(dropna=True).head(10).to_dict()
    elif choose == "down":
        describe_dict = serie.value_counts(dropna=True).tail(10).to_dict()

    if count == False:
        return list(describe_dict.keys())
    else:    
        return describe_dict

def describe_general(serie: pd.Series) -> dict:
    describe_dict = {
        "name": str(serie.name),
        "size": str(serie.size),
        "type": str(serie.dtype),
        "nan_count": int(serie.isnull().sum()),
        "top10": describe_list10(serie, 'top', False),
        "down10": describe_list10(serie, 'down', False),
        "count_top10": describe_list10(serie, 'top', True),
        "count_down10": describe_list10(serie, 'down', True)
    }
    return describe_dict