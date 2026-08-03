from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import ChatService

router = APIRouter()

chat = ChatService()


class ChatRequest(BaseModel):
    ai_id: str
    question: str


@router.post("/chat")
def ask_ai(request: ChatRequest):

    response = chat.ask(
        ai_id=request.ai_id,
        question=request.question
    )

    return response