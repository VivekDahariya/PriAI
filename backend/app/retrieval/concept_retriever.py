from app.compiler.concept_store import ConceptStore
from app.compiler.concept_relation_store import ConceptRelationStore


class ConceptRetriever:

    def __init__(self):

        self.concepts = ConceptStore()

        self.relations = ConceptRelationStore()


    def retrieve(
        self,
        ai_id: str,
        query_concepts: list[str]
    ):

        concepts = self.concepts.load(
            ai_id
        )

        relations = self.relations.load(
            ai_id
        )


        # -----------------------------------
        # Normalize Stored Concepts
        # -----------------------------------

        concept_map = {}

        concept_id_map = {}


        for concept in concepts:

            if isinstance(concept, dict):

                concept_id = concept.get(
                    "id"
                )

                name = concept.get(
                    "name"
                )

                chunk_ids = concept.get(
                    "chunk_ids",
                    []
                )

            else:

                concept_id = concept.id

                name = concept.name

                chunk_ids = concept.chunk_ids


            if not concept_id or not name:

                continue


            normalized = {

                "id": concept_id,

                "name": name,

                "chunk_ids": chunk_ids

            }


            concept_map[name.lower()] = normalized

            concept_id_map[concept_id] = normalized



        # -----------------------------------
        # Direct Concept Matching
        # -----------------------------------

        matched_concepts = set()

        matched_scores = {}



        for query in query_concepts:

            query_lower = query.lower()


            for name, concept in concept_map.items():

                score = 0


                if name == query_lower:

                    score = 1.0


                elif query_lower in name:

                    score = 0.8


                elif name in query_lower:

                    score = 0.7



                if score > 0:

                    concept_id = concept["id"]


                    matched_concepts.add(

                        concept_id

                    )


                    matched_scores[concept_id] = max(

                        matched_scores.get(
                            concept_id,
                            0
                        ),

                        score

                    )



        # -----------------------------------
        # Relation Expansion
        # -----------------------------------

        expanded_concepts = set(

            matched_concepts

        )


        relation_scores = {}



        for relation in relations:


            if isinstance(relation, dict):

                source = relation.get(
                    "source"
                )

                target = relation.get(
                    "target"
                )

                weight = relation.get(
                    "weight",
                    1.0
                )

                confidence = relation.get(
                    "confidence",
                    1.0
                )

            else:

                source = relation.source

                target = relation.target

                weight = relation.weight

                confidence = relation.confidence



            relation_strength = (

                weight *

                confidence

            )



            if source in matched_concepts:


                expanded_concepts.add(

                    target

                )


                relation_scores[target] = max(

                    relation_scores.get(
                        target,
                        0
                    ),

                    relation_strength

                )


            elif target in matched_concepts:


                expanded_concepts.add(

                    source

                )


                relation_scores[source] = max(

                    relation_scores.get(
                        source,
                        0
                    ),

                    relation_strength

                )



        # -----------------------------------
        # Collect Knowledge Units
        # -----------------------------------

        results = []

        seen_chunks = set()



        for concept_id in expanded_concepts:


            concept = concept_id_map.get(

                concept_id

            )


            if concept is None:

                continue



            concept_score = max(

                matched_scores.get(

                    concept_id,

                    0

                ),

                relation_scores.get(

                    concept_id,

                    0

                )

            )


            for chunk_id in concept["chunk_ids"]:


                if chunk_id in seen_chunks:

                    continue


                seen_chunks.add(

                    chunk_id

                )


                results.append(

                    {

                        "knowledge_unit_id":
                            chunk_id,

                        "concept_score":
                            concept_score,

                        "matched_concepts":
                            [
                                concept["name"]
                            ]

                    }

                )



        return results