import numpy as np
import pandas as pd


def describe_continuous(serie: pd.Series) -> dict:
    describe_dict = {
        "name": serie.name,
        "size": serie.size,
        "type": serie.dtype,
        "nan_count": serie.isnull().sum(),
        "min": serie.min(),
        "quantile 25": np.quantile(serie, 0.25),
        "quantile 50": np.median(serie),
        "quantile 75": np.quantile(serie, 0.75),
        "max": serie.max()
    }
    return describe_dict
