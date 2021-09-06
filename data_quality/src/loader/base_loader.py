import abc


class BaseLoader:

    @abc.abstractmethod
    def __init__(self, param_dict: dict, metadata_dict: dict) -> None:
        pass

    @abc.abstractmethod
    def load(self) -> None:
        """
            A loader loads to the destination or to the staging area
        """
        pass
