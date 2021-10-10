import os
from pathlib import Path
from data_quality.src.task.task import Task

DATASETS_PATH = Path(__file__).resolve().parent.parent
for dataset in os.listdir(os.path.join(DATASETS_PATH, "datasets")):
    param_dict = {
        "filepath": os.path.join(DATASETS_PATH, 'datasets', dataset),
        "publisher_api_url": "http://localhost/api/v1/summaries"
    }

    task = Task(param_dict)
    response = task.run()
