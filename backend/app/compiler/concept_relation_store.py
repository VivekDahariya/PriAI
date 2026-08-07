import json
import os

from app.compiler.concept_models import ConceptRelation


class ConceptRelationStore:

    def __init__(self):

        self.folder = "database/concept_relations"

        os.makedirs(

            self.folder,

            exist_ok=True

        )

    def _path(

        self,

        ai_id: str

    ):

        return os.path.join(

            self.folder,

            f"{ai_id}.json"

        )

    def save(

        self,

        ai_id: str,

        relations: list[ConceptRelation]

    ):

        path = self._path(

            ai_id

        )

        with open(

            path,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                [

                    relation.model_dump()

                    for relation in relations

                ],

                f,

                indent=4,

                ensure_ascii=False

            )

    def load(

        self,

        ai_id: str

    ) -> list[ConceptRelation]:

        path = self._path(

            ai_id

        )

        if not os.path.exists(

            path

        ):

            return []

        with open(

            path,

            "r",

            encoding="utf-8"

        ) as f:

            data = json.load(f)

        return [

            ConceptRelation(**item)

            for item in data

        ]