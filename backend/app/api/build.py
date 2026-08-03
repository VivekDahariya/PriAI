from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

from app.services.build_service import BuildService
from app.utils.file_manager import save_upload

router = APIRouter()

builder = BuildService()


@router.post("/build")
def build_ai(

    ai_name: str = Form(...),

    files: list[UploadFile] = File(...)

):

    paths = []

    for file in files:

        paths.append(
            save_upload(file)
        )

    builder.build(

        ai_name=ai_name,

        files=paths

    )

    return {

        "success": True,

        "message": "AI built successfully."

    }