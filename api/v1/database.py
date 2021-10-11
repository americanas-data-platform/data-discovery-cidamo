import motor.motor_asyncio
import fastapi
from decouple import config

MONGODB_USER = config('MONGO_INITDB_ROOT_USERNAME')
MONGODB_PASSWORD = config('MONGO_INITDB_ROOT_PASSWORD')
MONGODB_PORT = config('MONGO_INITDB_PORT')

MONGO_DETAILS = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@mongo:{MONGODB_PORT}/"

COLLECTION_NAME = 'data_quality'
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.dataquality
data_quality_collection = database.get_collection(COLLECTION_NAME)


def summary_helper(summary) -> dict:
    parsed_summary = {}
    for key in summary.keys():
        if key == "_id":
            value = str(summary['_id'])
        else:
            value = summary[key]
        parsed_summary[key] = value
    return parsed_summary


async def add_summary(summary_data: dict) -> dict:
    older_summary = await data_quality_collection.find_one({"filename": summary_data['filename']})
    if older_summary:
        raise fastapi.HTTPException(detail="Filemane already exists.", status_code=400)
    await data_quality_collection.insert_one(summary_data)
    new_summary = await data_quality_collection.find_one({"filename": summary_data['filename']})
    return summary_helper(new_summary)


async def retrieve_summaries() -> list:
    summaries = []
    async for summary in data_quality_collection.find():
        summaries.append(summary_helper(summary))
    return summaries


async def retrieve_summary(id: str) -> dict:
    summary = await data_quality_collection.find_one({"filename": id})
    if summary:
        return summary_helper(summary)


async def update_summary(id: str, summary_data: dict) -> dict:
    summary_data['filename'] = id
    await data_quality_collection.replace_one({"filename": id}, summary_data)
    updated_summary = await data_quality_collection.find_one({"filename": id})
    if not updated_summary:
        raise fastapi.HTTPException(detail="Not found.", status_code=404)
    return summary_helper(updated_summary)


async def delete_summaries():
    await data_quality_collection.drop()
    return None


async def delete_summary(id: str):
    summary = await data_quality_collection.find_one({"filename": id})
    if summary:
        await data_quality_collection.delete_one({"filename": id})
        return None
    raise fastapi.HTTPException(detail="Not found.", status_code=404)
