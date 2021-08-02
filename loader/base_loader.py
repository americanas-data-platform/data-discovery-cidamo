import abc


class BaseLoader:

    @abc.abstractmethod
    def init(self, conf: ConfigTree) -> None:
        pass

    @abc.abstractmethod
    def load(self, record: Any) -> None:
        """
            A loader loads to the destination or to the staging area
        """
        pass
