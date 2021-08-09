import pandas as pd
from src.transformer.base_transformer import BaseTransformer
from src.transformer.aggregation_functions.categorical import describe_categorical
from src.transformer.aggregation_functions.continuous import describe_continuous, describe_datetime
from src.transformer.aggregation_functions.discrete import describe_discrete


class GeneralTransformer(BaseTransformer):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    def transform(self) -> dict:
        metadata_dict = dict()
        for feature in self.dataframe.columns:
            if self.dataframe[feature].dtype in ('object',):
                try:
                    datetime_serie = pd.to_datetime(self.dataframe[feature])
                    metadata_dict[feature] = describe_datetime(datetime_serie)
                except Exception as e:
                    metadata_dict[feature] = describe_categorical(self.dataframe[feature])
            if self.dataframe[feature].dtype in ('float', 'float32', 'float64'):
                metadata_dict[feature] = describe_continuous(self.dataframe[feature])
            if self.dataframe[feature].dtype in ('int', 'int32', 'int64'):
                metadata_dict[feature] = describe_discrete(self.dataframe[feature])
        return metadata_dict
