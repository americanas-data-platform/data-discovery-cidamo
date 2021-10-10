import os
from pathlib import Path
from data_quality.src.task.task import Task

DATASETS_PATH = Path(__file__).resolve().parent.parent

param_dict = {
    "filepath": 'https://leofernanndes-datasets.s3.amazonaws.com/airbnb-rio-complete.csv',
    "publisher_api_url": "http://localhost/api/v1/summaries"
}

task = Task(param_dict)
response = task.run()
