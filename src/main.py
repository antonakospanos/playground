from fastapi import FastAPI

from api.v1 import api_v1_router

app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

app.include_router(
    api_v1_router,
    dependencies=[],
)

def start() -> None:
    """Starts the web server programmatically. Used to define a helper in the project's scripts"""
    import uvicorn

    uvicorn.run(app)
 