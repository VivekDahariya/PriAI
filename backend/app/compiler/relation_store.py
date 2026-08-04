import json
from pathlib import Path

from app.compiler.models import KnowledgeRelation


class RelationStore:

    def __init__(self):

        self.root = Path("database/relations")

        self.root.mkdir(
            parents=True,
            exist_ok=True
        )


    def save(
        self,
        ai_id: str,
        relations: list[KnowledgeRelation]
    ):

        path = self.root / f"{ai_id}.json"


        data = [

            {
                "source": r.source,

                "relation": r.relation,

                "target": r.target,

                "weight": r.weight,

                "confidence": r.confidence,

                "source_type": r.source_type,

                "target_type": r.target_type
            }

            for r in relations

        ]


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