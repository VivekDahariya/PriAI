from app.generation.templates import SYSTEM_TEMPLATE


class PromptBuilder:


    def build(
        self,
        question: str,
        contexts: str
    ) -> str:


        prompt = SYSTEM_TEMPLATE.strip()


        prompt += "\n\n"


        prompt += contexts


        prompt += "\n\n===== QUESTION =====\n"

        prompt += question


        prompt += "\n\n===== ANSWER =====\n"


        return prompt