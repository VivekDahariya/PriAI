from .sentence_transformer import SentenceTransformerEmbedding


class EmbeddingManager:

    def __init__(self):
        self.model = SentenceTransformerEmbedding()

    def get_model(self):
        return self.model