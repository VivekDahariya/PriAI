class ContextService:

    def __init__(
        self,
        max_chunks: int = 8
    ):

        self.max_chunks = max_chunks


    def _calculate_context_score(
        self,
        chunk: dict
    ):

        retrieval_score = chunk.get(
            "retrieval_score",
            0
        )

        vector_score = chunk.get(
            "vector_score",
            0
        )

        graph_score = chunk.get(
            "graph_score",
            0
        )

        concept_score = chunk.get(
            "concept_score",
            0
        )


        return (

            retrieval_score * 0.5

            +

            vector_score * 0.2

            +

            graph_score * 0.15

            +

            concept_score * 0.15

        )


    def _deduplicate_chunks(
        self,
        chunks: list[dict]
    ):

        unique = []

        seen = set()


        for chunk in chunks:

            text = chunk.get(
                "text",
                ""
            )


            if not text:

                continue


            normalized = (

                text

                .strip()

                .lower()

            )


            if normalized in seen:

                continue


            seen.add(
                normalized
            )


            unique.append(
                chunk
            )


        return unique



    def build_context(
        self,
        retrieved_chunks: list[dict]
    ):

        if not retrieved_chunks:

            return ""


        ranked_chunks = sorted(

            retrieved_chunks,

            key=self._calculate_context_score,

            reverse=True

        )


        selected_chunks = self._deduplicate_chunks(

            ranked_chunks

        )[:self.max_chunks]


        context_parts = []


        for index, chunk in enumerate(

            selected_chunks,

            start=1

        ):


            text = chunk.get(
                "text",
                ""
            )


            source = chunk.get(
                "source",
                "Unknown"
            )


            relation = chunk.get(
                "graph_relation"
            )


            concept_info = chunk.get(
                "matched_concepts"
            )


            metadata = []


            if relation:

                metadata.append(

                    f"Relation: {relation}"

                )


            if concept_info:

                metadata.append(

                    f"Concepts: {', '.join(concept_info)}"

                )


            metadata_text = ""


            if metadata:

                metadata_text = (

                    "\n"

                    +

                    "\n".join(metadata)

                )



            context_parts.append(

                f"""
Knowledge Chunk {index}

Source: {source}
{metadata_text}

{text}
"""

            )


        return "\n\n".join(

            context_parts

        )



    def build_prompt_context(
        self,
        question: str,
        retrieved_chunks: list[dict]
    ):


        context = self.build_context(

            retrieved_chunks

        )


        return {

            "question": question,

            "context": context

        }