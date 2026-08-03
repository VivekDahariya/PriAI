from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.registry import router as registry_router

from app.api.build import router as build_router

app = FastAPI(
    title="PriAI",
    version="0.1"
)

app.include_router(build_router)
app.include_router(chat_router)
app.include_router(registry_router)

