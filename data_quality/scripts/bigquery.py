import os
from pathlib import Path
from data_quality.src.task.task import Task, NewTask
from data_quality.src.extractor.bigquery_extractor import BigQueryExtractor


DATASETS_PATH = Path(__file__).resolve().parent.parent

param_dict = {
    "filepath": 'bigquery-public-data.stackoverflow.posts_questions',
    "publisher_api_url": "http://localhost/api/v1/summaries"
}

task = NewTask(param_dict, BigQueryExtractor)
response = task.run()
print(response)
