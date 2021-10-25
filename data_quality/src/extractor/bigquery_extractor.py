import os
from pathlib import Path
from data_quality.src.extractor.base_extractor import BaseExtractor
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd


CREDENTIALS_PATH = os.path.join(Path(__file__).resolve().parent.parent.parent, 'credentials', 'gcp', 'bq_credentials.json')

class BigQueryExtractor(BaseExtractor):
    def __init__(self, param_dict: dict) -> None:
        self.param_dict = param_dict

    def extract(self) -> pd.DataFrame:
        if not self.param_dict.get('filepath', None):
            raise ValueError("Param dict must contain a filepath")
        try:
            credentials = service_account.Credentials.from_service_account_file(
                CREDENTIALS_PATH, scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
            client = bigquery.Client(credentials=credentials, project=credentials.project_id, )
            # big_query_source = 'bigquery-public-data.stackoverflow.posts_questions'
            query_string = f"SELECT * from { self.param_dict.get('filepath') } LIMIT 1000;"
            data = client.query(query_string).result().to_dataframe()

        except Exception as e:
            raise e
        return data
