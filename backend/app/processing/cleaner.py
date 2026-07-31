import re


def clean_text(text: str) -> str:
    """
    Clean extracted document text.
    """

    text = text.replace("\x00", " ")

    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text