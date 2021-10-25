import os
from data_quality.src.extractor.csv_extractor import CsvExtractor
from pathlib import Path



def test_csv_extractor():
    DATASETS_PATH = Path(__file__).resolve().parent.parent

    param_dict = {
        "filepath": os.path.join(DATASETS_PATH, 'datasets', 'olist_order_items_dataset.csv'),
        "publisher_api_url": "http://localhost/api/v1/summaries"
    }
    csv_extractor = CsvExtractor(param_dict)
    data = csv_extractor.extract()
    assert data.shape == (112650, 7)


