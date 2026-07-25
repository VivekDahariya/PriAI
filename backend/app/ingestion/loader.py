from pathlib import Path

from .extractor import extract_text_from_pdf


def load_document(file_path: str) -> str:

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    raise ValueError(
        f"Unsupported file type: {extension}"
    )