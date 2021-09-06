# Data Discovery

Data Discovery project in partnership with the CiDAMO-UFPR group.
## Objective

Build an application that summarize a dataset, showing basic statistics (for e.g. max, min and percentage of missing values), histograms, correlations, data quality report, and other relevant metrics.

## Architecture overview

The following diagram shows the overall architecture for the project.

The project is composed by a data quality job package written in python responsible for gettin a summary of datasets
features, an api written using Fast api and a Mongo db for persistence.

![Architecture](data_quality/images/architecture.png)

## Data

This project is based on a Brazilian ecommerce public dataset of orders made at Olist Store. It is available on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

## Dependencies

Docker version 20.10.8 \
Docker-compose version 1.29.2 \
FastAPI version 0.68.0 \
Uvicorn version 0.15.0 \
Motor version 2.5.1 

To check a complete list of project's dependencies check requirements.txt

## Installation

1. Clone dev branch locally ```git clone -b develop https://github.com/americanas-data-platform/data-discovery-cidamo.git```
2. Check if there is any process running on TCP 80
3. We are using docker to package and deliver the source code, so in order to launch a local server you must use ``` docker-compose up --build```

To use and use test scripts like those described in data_quality/scripts, go to the root of the project and call ```python -m data_quality.scripts.{SCRIPT_NAME}``` like ```python -m data_quality.scripts.local_csv```

## License

[MIT License.](./LICENSE)
