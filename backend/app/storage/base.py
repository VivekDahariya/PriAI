from abc import ABC, abstractmethod
from .models import KnowledgeChunk


class BaseVectorStore(ABC):

    @abstractmethod
    def add(self, chunks: list[KnowledgeChunk]):
        pass

    @abstractmethod
    def search(self, query: str, top_k: int = 5):
        pass

    @abstractmethod
    def delete(self):
        pass