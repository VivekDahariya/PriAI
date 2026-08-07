from app.generation.templates import SYSTEM_TEMPLATE


class PromptBuilder:


    def build(
        self,
        question: str,
        contexts
    ) -> str:


        prompt = SYSTEM_TEMPLATE.strip()


        prompt += "\n\n"


        prompt += (
            "===== KNOWLEDGE CONTEXT =====\n"
        )


        if isinstance(contexts, list):

            for index, context in enumerate(
                contexts,
                start=1
            ):

                prompt += (
                    f"\nKnowledge Chunk {index}\n"
                )

                prompt += (
                    context.get(
                        "text",
                        ""
                    )
                )

                prompt += "\n"


        else:

            prompt += contexts



        prompt += (
            "\n\n===== USER QUESTION =====\n"
        )


        prompt += question


        prompt += (
            "\n\n===== RESPONSE RULES =====\n"
        )


        prompt += (
            """
Answer only using the provided knowledge context.

If the answer is not available in the context,
clearly state that the information is not available.

Do not invent facts.

Prefer concise and accurate answers.
"""
        )


        prompt += (
            "\n\n===== ANSWER =====\n"
        )


        return prompt