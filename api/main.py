import fastapi
import api.v1.routes

app = fastapi.FastAPI(title='Data Ingestion Api',
                      docs_url='/docs',
                      redoc_url='/redoc',
                      openapi_url='/openapi.json',
                      root_path='/api')

app.include_router(api.v1.routes.router, prefix='/v1/summaries', tags=['v1'])
