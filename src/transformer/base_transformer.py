import abc
import pandas as pd


class BaseTransformer:

    @abc.abstractmethod
    def __init__(self, dataframe: pd.DataFrame) -> None:
        pass

    @abc.abstractmethod
    def transform(self):
        """
        Perform aggregation and calculate metrics over provided data
        :return: dictionary containing calculated metrics
        """
        pass
