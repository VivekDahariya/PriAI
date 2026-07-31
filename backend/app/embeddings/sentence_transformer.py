from .base import BaseEmbeddingModel


class SentenceTransformerEmbedding(BaseEmbeddingModel):

    def embed(self, texts):
        raise NotImplementedError