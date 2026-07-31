from sentence_transformers import SentenceTransformer

from app.storage.chroma import ChromaVectorStore


class RetrievalService:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def retrieve(self, ai_id: str, question: str, top_k: int = 5):

        store = ChromaVectorStore(ai_id)

        query_embedding = self.embedding_model.encode(question).tolist()

        results = store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        print("\n========== DEBUG RESULTS ==========")
        print(results)
        print("===================================\n")

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        retrieved = []

        for document, metadata in zip(documents, metadatas):

            retrieved.append({
                "text": document,
                "source": metadata["source"],
                "chunk": metadata["chunk"]
            })

        return retrieved