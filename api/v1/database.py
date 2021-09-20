import motor.motor_asyncio
import fastapi


MONGO_DETAILS = "mongodb://root:example@mongo:27017/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.dataquality
data_quality_collection = database.get_collection("data_quality")


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
    summary_data['_id'] = summary_data['filename']
    try:
        await data_quality_collection.insert_one(summary_data)
        new_summary = await data_quality_collection.find_one({"_id": summary_data['filename']})
        return summary_helper(new_summary)
    except:
        raise fastapi.HTTPException(detail="Filemane already exists.", status_code=400)


async def retrieve_summaries() -> list:
    summaries = []
    async for summary in data_quality_collection.find():
        summaries.append(summary_helper(summary))
    return summaries


async def retrieve_summary(id: str) -> dict:
    summary = await data_quality_collection.find_one({"_id": id})
    if summary:
        return summary_helper(summary)


async def update_summary(id: str, summary_data: dict) -> dict:
    await data_quality_collection.replace_one({"_id": id}, summary_data)
    updated_summary = await data_quality_collection.find_one({"_id": id})
    if not updated_summary:
        raise fastapi.HTTPException(detail="Not found.", status_code=404)
    return summary_helper(updated_summary)


async def delete_summaries() -> dict:
    await data_quality_collection.drop()
    return None
