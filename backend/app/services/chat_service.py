from app.generation.generator import Generator
from app.generation.prompt_builder import PromptBuilder
from app.services.retrieval_service import RetrievalService


class ChatService:

    def __init__(self):

        self.retriever = RetrievalService()

        self.prompt_builder = PromptBuilder()

        self.generator = Generator()


    def ask(
        self,
        ai_id: str,
        question: str
    ):

        contexts = self.retriever.retrieve(

            ai_id=ai_id,

            question=question

        )


        prompt = self.prompt_builder.build(

            question=question,

            contexts=contexts

        )


        answer = self.generator.generate(
            prompt
        )


        return {

            "answer": answer,

            "sources": contexts

        }