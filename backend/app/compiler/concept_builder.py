from app.compiler.models import ConceptNode


class ConceptBuilder:

    def __init__(self):

        self.concepts = {}

    def add_concepts(

        self,

        chunk_id: str,

        concepts: list[str]

    ):

        for concept in concepts:

            key = concept.strip().lower()

            if not key:
                continue

            if key not in self.concepts:

                self.concepts[key] = ConceptNode(

                    id=f"C{len(self.concepts)+1}",

                    name=concept.strip(),

                    chunk_ids=[]

                )

            self.concepts[key].chunk_ids.append(
                chunk_id
            )

    def build(self):

        return list(
            self.concepts.values()
        )