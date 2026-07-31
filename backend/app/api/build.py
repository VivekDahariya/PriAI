from fastapi import APIRouter
from pydantic import BaseModel

from app.services.build_service import BuildService

router = APIRouter()

builder = BuildService()


class BuildRequest(BaseModel):
    ai_name: str


@router.post("/build")
def build_ai(request: BuildRequest):

    builder.build(

        ai_name=request.ai_name,

        files=["sample.pdf"]

    )

    return {
        "status": "success",
        "ai_name": request.ai_name,
        "message": "Knowledge Base Built Successfully"
    }