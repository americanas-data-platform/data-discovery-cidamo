from src.extractor.csv_extractor import CsvExtractor
from src.transformer.general_transformer import GeneralTransformer
from src.loader.general_loader import GeneralLoader

class Task:
    def __init__(self, param_dict: dict) -> None:
        self.param_dict = param_dict

    def run(self):
        df = CsvExtractor(self.param_dict).extract()
        transformer = GeneralTransformer(df)
        metadata_dict = transformer.transform()
        loader = GeneralLoader(param_dict=self.param_dict, metadata_dict=metadata_dict)
        response = loader.load()
        return response
