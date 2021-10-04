import fastapi
from pydantic import BaseModel
from typing import List
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from api.v1.database import add_summary, retrieve_summaries, retrieve_summary, delete_summaries, update_summary


class CategoricalFeatureSummary(BaseModel):
    name: str
    size: str
    nan_count: int
    top10: List[str]
    down10: List[str]
    count_top10: dict
    count_down10: dict


class DiscreteFeatureSummary(CategoricalFeatureSummary):
    unique_values: List[int]


class ContinuousFeatureSummary(CategoricalFeatureSummary):
    min: float
    quantile_25: float
    quantile_50: float
    quantile_75: float
    max: float
    histogram: dict


class DateTimeFeatureSummary(CategoricalFeatureSummary):
    min: str
    quantile_25: str
    quantile_50: str
    quantile_75: str
    max: str
    histogram: dict


class DataSummary(BaseModel):
    filename: str
    categorical_features: List[CategoricalFeatureSummary]
    discrete_features: List[DiscreteFeatureSummary]
    continuous_features: List[ContinuousFeatureSummary]
    datetime_features: List[DateTimeFeatureSummary]


def validate_objectid(id):
    try:
        ObjectId(id)
    except:
        raise fastapi.HTTPException(detail="Id is not a valid ObjectId.", status_code=422)


router = fastapi.APIRouter()

@router.post('/')
async def post_summary(data_summary: DataSummary):
    summary = jsonable_encoder(data_summary)
    new_summary = await add_summary(summary)
    return new_summary

@router.get("/")
async def get_all_summaries():
    summaries = await retrieve_summaries()
    if summaries:
        return summaries
    raise fastapi.HTTPException(detail="Not found.", status_code=404)

@router.get("/{id}")
async def get_summary_by_id(id):
    summary = await retrieve_summary(id)
    if summary:
        return summary
    raise fastapi.HTTPException(detail="Not found.", status_code=404)

@router.put("/{id}")
async def update_summary_data(id: str, data_summary: DataSummary):
    summary = jsonable_encoder(data_summary)
    updated_summary = await update_summary(id, summary)
    if updated_summary:
        return updated_summary
    return {"detail": "Not found."}

@router.post("/delete-all")
async def delete_all_summaries():
    await delete_summaries()
    raise fastapi.HTTPException(detail="Not found.", status_code=404)
