import pandas as pd
from transformer.base_transformer import BaseTransformer

from transformer.aggregation_functions.categorical import describe_categorical
from transformer.aggregation_functions.continuous import describe_continuous


class GeneralTransformer(BaseTransformer):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    def transform(self) -> dict:
        metadata_dict = dict()
        for feature in self.dataframe.columns:
            if self.dataframe[feature].dtype in ('object',):
                metadata_dict[feature] = describe_categorical(self.dataframe[feature])
            if self.dataframe[feature].dtype in ('float', 'float32', 'float64'):
                metadata_dict[feature] = describe_continuous(self.dataframe[feature])
        return metadata_dict
