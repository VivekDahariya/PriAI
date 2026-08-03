from pydantic import BaseModel


class Source(BaseModel):

    source: str

    chunk: int


class BuildResponse(BaseModel):

    success: bool

    message: str


class ChatResponse(BaseModel):

    answer: str

    sources: list[Source]


class DeleteResponse(BaseModel):

    success: bool

    message: str