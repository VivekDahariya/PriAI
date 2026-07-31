from app.generation.templates import SYSTEM_TEMPLATE


class PromptBuilder:

    def build(self, question: str, contexts: list[dict]) -> str:

        prompt = SYSTEM_TEMPLATE.strip()

        prompt += "\n\n"

        prompt += "===== CONTEXT =====\n\n"

        for i, context in enumerate(contexts, start=1):

            prompt += f"[{i}]\n"

            prompt += context["text"]

            prompt += "\n\n"

        prompt += "===== QUESTION =====\n\n"

        prompt += question

        prompt += "\n\n"

        prompt += "===== ANSWER =====\n"

        return prompt