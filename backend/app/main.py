from fastapi import FastAPI

from app.api.build import router as build_router

app = FastAPI(
    title="PriAI",
    version="0.1"
)

app.include_router(build_router)