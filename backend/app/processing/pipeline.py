from app.processing.cleaner import clean_text
from app.processing.chunker import chunk_text


def process_document(text: str):

    cleaned = clean_text(text)

    chunks = chunk_text(cleaned)

    return chunks