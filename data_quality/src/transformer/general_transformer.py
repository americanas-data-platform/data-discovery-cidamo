import pandas as pd
from data_quality.src.transformer.base_transformer import BaseTransformer
from data_quality.src.transformer.aggregation_functions.categorical import describe_categorical
from data_quality.src.transformer.aggregation_functions.continuous import describe_continuous, describe_datetime
from data_quality.src.transformer.aggregation_functions.discrete import describe_discrete


class GeneralTransformer(BaseTransformer):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    def transform(self) -> dict:
        metadata_dict = {}
        metadata_dict['categorical_features'] = []
        metadata_dict['discrete_features'] = []
        metadata_dict['continuous_features'] = []
        metadata_dict['datetime_features'] = []
        metadata_dict['null_features'] = []

        for feature in self.dataframe.columns:
            if self.dataframe[feature].isnull().sum() == len(list(self.dataframe[feature])):
                metadata_dict['null_features'].append(feature)
                continue
            if self.dataframe[feature].dtype in ('object',):
                try:
                    datetime_serie = pd.to_datetime(self.dataframe[feature])
                    metadata_dict['datetime_features'].append(describe_datetime(datetime_serie))
                except Exception as e:
                    metadata_dict['categorical_features'].append(describe_categorical(self.dataframe[feature]))
            if self.dataframe[feature].dtype in ('float', 'float32', 'float64'):
                metadata_dict['continuous_features'].append(describe_continuous(self.dataframe[feature]))
            if self.dataframe[feature].dtype in ('int', 'int32', 'int64'):
                metadata_dict['discrete_features'].append(describe_discrete(self.dataframe[feature]))
        return metadata_dict
