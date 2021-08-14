import fastapi
import v1.main

app = fastapi.FastAPI()
app.include_router(v1.main.router, prefix='/v1', tags=['v1'])
