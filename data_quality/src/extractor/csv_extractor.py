from data_quality.src.extractor.base_extractor import BaseExtractor
import pandas as pd


class CsvExtractor(BaseExtractor):
    def __init__(self, param_dict: dict) -> None:
        self.param_dict = param_dict

    def extract(self) -> pd.DataFrame:
        if not self.param_dict.get('filepath', None):
            raise ValueError("Param dict must contain a filepath")
        try:
            data = pd.read_csv(self.param_dict.get("filepath"), low_memory=False)
        except Exception as e:
            raise e
        return data
