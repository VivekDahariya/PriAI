from app.generation.generator import Generator
from app.generation.prompt_builder import PromptBuilder
from app.services.retrieval_service import RetrievalService
from app.utils.slug import generate_ai_id


class ChatService:

    def __init__(self):

        self.retriever = RetrievalService()

        self.prompt_builder = PromptBuilder()

        self.generator = Generator()

    def ask(self, ai_name: str, question: str):

        ai_id = generate_ai_id(ai_name)

        contexts = self.retriever.retrieve(

            ai_id=ai_id,

            question=question

        )

        prompt = self.prompt_builder.build(

            question=question,

            contexts=contexts

        )

        answer = self.generator.generate(prompt)

        return {

            "answer": answer,

            "sources": contexts

        }