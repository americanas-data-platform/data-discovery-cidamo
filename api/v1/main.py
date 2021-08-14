import fastapi
from pydantic import BaseModel, Field

router = fastapi.APIRouter()

@router.post('/')
async def post(payload: dict):
    return payload
