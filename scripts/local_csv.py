import sys
import pathlib
ROOT = pathlib.Path(__file__).parent.parent.resolve()
sys.path.append(str(ROOT))

from src.task.task import Task


param_dict = {
    "filepath": "/home/leofernanndes/dev/geral/data-discovery-cidamo/data/olist_order_items_dataset.csv",
    "publisher_api_url": "http://localhost:8000/v1/"
}

task = Task(param_dict)
response = task.run()
print(response)
