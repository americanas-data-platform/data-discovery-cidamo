import motor.motor_asyncio
from bson.objectid import ObjectId


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

async def add_summary(student_data: dict) -> dict:
    student = await data_quality_collection.insert_one(student_data)
    new_student = await data_quality_collection.find_one({"_id": student.inserted_id})
    return summary_helper(new_student)

async def retrieve_summaries() -> list:
    students = []
    async for student in data_quality_collection.find():
        students.append(summary_helper(student))
    return students

async def retrieve_summary(id: str) -> dict:
    student = await data_quality_collection.find_one({"_id": ObjectId(id)})
    if student:
        return summary_helper(student)


async def delete_summaries() -> dict:
    await data_quality_collection.drop()
    return None