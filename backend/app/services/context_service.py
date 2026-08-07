class ContextService:


    def __init__(
        self,
        max_chunks: int = 8
    ):

        self.max_chunks = max_chunks



    def build_context(
        self,
        retrieved_chunks: list[dict]
    ):

        if not retrieved_chunks:

            return ""


        selected = retrieved_chunks[:self.max_chunks]


        context_parts = []


        seen = set()


        for chunk in selected:

            text = chunk.get(
                "text",
                ""
            )


            if not text:

                continue


            normalized = text.strip().lower()


            if normalized in seen:

                continue


            seen.add(normalized)


            source = chunk.get(
                "source"
            )


            context_parts.append(

                f"""
Source: {source}

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