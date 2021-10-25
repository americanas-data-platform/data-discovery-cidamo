import os
import json
import fastapi
from pathlib import Path
from numpy import histogram
from pydantic import BaseModel
from typing import List
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from api.v1.database import add_summary, retrieve_summaries, retrieve_summary, delete_summaries, update_summary, delete_summary
from data_quality.src.extractor.bigquery_extractor import BigQueryExtractor
from data_quality.src.transformer.general_transformer import GeneralTransformer


class GeneralFeatureSummary(BaseModel):
    name: str
    size: str
    type: str
    na_count: int
    #top10: List[str]
    #down10: List[str]
    count_top10: dict
    count_down10: dict


class CategoricalFeatureSummary(GeneralFeatureSummary):
    mode: List[str]
    

class DiscreteFeatureSummary(GeneralFeatureSummary):
    min: int
    max: int
    histogram: dict


class ContinuousFeatureSummary(GeneralFeatureSummary):
    min: float
    quantile_25: float
    quantile_50: float
    quantile_75: float
    max: float
    histogram: dict


class DateTimeFeatureSummary(GeneralFeatureSummary):
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
    bool_features: List[CategoricalFeatureSummary]
    null_features: List[str]


router = fastapi.APIRouter()

@router.get('/seed')
async def seed_sample_summary():   
    SAMPLE_SUMMARY_PATH = Path(__file__).resolve().parent
    with open(f'{SAMPLE_SUMMARY_PATH}/sample_summary.json') as f:
        data_summary = json.load(f)
        summary = jsonable_encoder(data_summary)
        new_summary = await add_summary(summary)
    return fastapi.responses.JSONResponse({'detail': 'Seed ok'}, status_code=200)


@router.post('/')
async def post_summary(data_summary: DataSummary):
    summary = jsonable_encoder(data_summary)
    new_summary = await add_summary(summary)
    return fastapi.responses.JSONResponse(new_summary, status_code=201)


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
async def update_summary_by_id(id: str, data_summary: DataSummary):
    summary = jsonable_encoder(data_summary)
    updated_summary = await update_summary(id, summary)
    if updated_summary:
        return updated_summary
    return {"detail": "Not found."}


@router.delete("/")
async def delete_all_summaries():
    await delete_summaries()
    return fastapi.responses.Response(status_code=204)


@router.delete("/{id}")
async def delete_summary_by_id(id: str):
    await delete_summary(id)
    return fastapi.responses.Response(status_code=204)
