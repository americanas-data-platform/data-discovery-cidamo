import pandas as pd


def describe_categorical(serie: pd.Series) -> dict:
    describe_dict = {
        "name": serie.name,
        "size": serie.size,
        "chave": "test",
        "type": serie.dtype,
        "unique_count": len(serie.unique()),
        "unique_values": serie.unique(),
        "nan_count": serie.isnull().sum()
    }
    return describe_dict

