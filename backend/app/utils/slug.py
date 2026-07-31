import re


def generate_ai_id(name: str) -> str:
    """
    Convert a user-facing AI name into a safe internal ID.

    Example:
    Computer Science
        ->
    computer_science
    """

    name = name.lower().strip()

    name = re.sub(r"\s+", "_", name)

    name = re.sub(r"[^a-z0-9_-]", "", name)

    return name