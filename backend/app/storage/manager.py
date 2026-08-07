from .chroma import ChromaVectorStore


class StorageManager:


    def get_store(
        self,
        ai_id
    ):

        return ChromaVectorStore(
            ai_id
        )