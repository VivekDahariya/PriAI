from app.generation.generator import Generator
from app.generation.prompt_builder import PromptBuilder

from app.services.retrieval_service import RetrievalService
from app.services.context_service import ContextService


class ChatService:


    def __init__(self):

        self.retriever = RetrievalService()

        self.context_service = ContextService()

        self.prompt_builder = PromptBuilder()

        self.generator = Generator()



    def ask(
        self,
        ai_id: str,
        question: str
    ):


        retrieved = self.retriever.retrieve(

            ai_id=ai_id,

            question=question

        )


        context = self.context_service.build_context(

            retrieved

        )


        prompt = self.prompt_builder.build(

            question=question,

            contexts=context

        )


        answer = self.generator.generate(

            prompt

        )


        return {

            "answer": answer,

            "sources": retrieved

        }