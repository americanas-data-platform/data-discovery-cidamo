import fastapi
from fastapi.encoders import jsonable_encoder
from api.v1.database import add_summary, retrieve_summaries, retrieve_summary, delete_summaries


router = fastapi.APIRouter()

@router.post('/')
async def post_summary(payload: dict):
    summary = jsonable_encoder(payload)
    new_summary = await add_summary(summary)
    return new_summary

@router.get("/")
async def get_all_summaries():
    summaries = await retrieve_summaries()
    if summaries:
        return summaries
    return {"detail": "Not found."}

@router.get("/{id}")
async def get_summary_by_id(id):
    summary = await retrieve_summary(id)
    if summary:
        return summary
    return {"detail": "Not found."}


@router.put("/delete-all")
async def delete_all_summaries():
    await delete_summaries()
    return {"detail": "No content."}
