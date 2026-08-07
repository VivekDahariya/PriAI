import json
from pathlib import Path

from app.compiler.models import ConceptNode


class ConceptStore:

    def __init__(self):

        self.root = Path("database/concepts")

        self.root.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(
        self,
        ai_id: str,
        concepts: list[ConceptNode]
    ):

        path = self.root / f"{ai_id}.json"

        data = []

        for concept in concepts:

            data.append(

                {

                    "id": concept.id,

                    "name": concept.name,

                    "chunk_ids": concept.chunk_ids

                }

            )

        with path.open(
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

    def load(
        self,
        ai_id: str
    ):

        path = self.root / f"{ai_id}.json"

        if not path.exists():

            return []

        with path.open(
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)