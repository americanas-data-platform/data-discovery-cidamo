import abc


class BaseExtractor:

    @abc.abstractmethod
    def __init__(self, param_dict: dict) -> None:
        pass

    @abc.abstractmethod
    def extract(self):
        """
        Extract data from provided datasource
        :return: Pandas dataframe to be transformed in later operations
        """
        pass
