import pandas as pd


def describe_general(serie: pd.Series) -> dict:
    describe_dict = {
        "name": str(serie.name),
        "size": str(serie.size),
        "type": str(serie.dtype),
        "nan_count": int(serie.isnull().sum())
    }
    return describe_dict