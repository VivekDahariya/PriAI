from abc import ABC, abstractmethod


class BaseEmbeddingModel(ABC):

    @abstractmethod
    def embed(self, texts: list[str]) -> list[list[float]]:
        pass