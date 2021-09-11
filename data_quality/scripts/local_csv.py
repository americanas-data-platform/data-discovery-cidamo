import os
from pathlib import Path
from data_quality.src.task.task import Task

DATASETS_PATH = Path(__file__).resolve().parent.parent

param_dict = {
    "filepath": os.path.join(DATASETS_PATH, 'datasets', 'olist_order_items_dataset.csv'),
    "publisher_api_url": "http://localhost/api/v1/"
}

task = Task(param_dict)
response = task.run()
print(response)
