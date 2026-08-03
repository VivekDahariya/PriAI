from pathlib import Path
import shutil
import uuid

from fastapi import UploadFile

UPLOAD_DIR = Path("database/uploads")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def save_upload(file: UploadFile):

    filename = f"{uuid.uuid4()}_{file.filename}"

    path = UPLOAD_DIR / filename

    with path.open("wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return str(path)