from .chroma import ChromaVectorStore


class StorageManager:

    def __init__(self):
        self.store = ChromaVectorStore()

    def get_store(self):
        return self.store