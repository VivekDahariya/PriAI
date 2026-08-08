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
                "source": r.get("source") if isinstance(r, dict) else r.source,

                "target": r.get("target") if isinstance(r, dict) else r.target,

                "relation": r.get("relation") if isinstance(r, dict) else r.relation,

                "weight": r.get("weight", 1.0) if isinstance(r, dict) else r.weight,

                "confidence": r.get("confidence", 1.0) if isinstance(r, dict) else r.confidence,

                "source_type": r.get("source_type", "unknown") if isinstance(r, dict) else r.source_type,

                "target_type": r.get("target_type", "unknown") if isinstance(r, dict) else r.target_type
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