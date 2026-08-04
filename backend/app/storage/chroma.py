import chromadb

from .base import BaseVectorStore
from .models import KnowledgeChunk


class ChromaVectorStore(BaseVectorStore):

    def __init__(self, collection_name: str):

        self.client = chromadb.PersistentClient(
            path="./database"
        )

        self.collection_name = collection_name

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add(self, chunks: list[KnowledgeChunk]):

        self.collection.add(

            ids=[c.id for c in chunks],

            documents=[c.text for c in chunks],

            metadatas=[
                {
                    "source": c.source,
                    "chunk": c.chunk_index,
                    **(
                        {"hkr_node": c.hkr_node_id}
                        if c.hkr_node_id is not None
                        else {}
                    )
                }
                for c in chunks
            ],

            embeddings=[c.embedding for c in chunks]

        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        result = self.collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k,

            include=[
                "documents",
                "metadatas",
                "distances"
            ]

        )

        chunks = []

        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]

        for doc, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            chunks.append(

                {
                    "text": doc,
                    "metadata": metadata,
                    "distance": distance,
                    "hkr_node_id": metadata.get("hkr_node")
                }

            )

        return chunks

    def delete(self):

        self.client.delete_collection(
            self.collection_name
        )

    def get_by_hkr_nodes(self, node_ids: list[str]):

        if not node_ids:
            return []

        result = self.collection.get(
            where={
                "hkr_node": {
                    "$in": node_ids
                }
            },
            include=[
                "documents",
                "metadatas"
            ]
        )

        chunks = []

        documents = result.get("documents", [])
        metadatas = result.get("metadatas", [])

        for doc, metadata in zip(
            documents,
            metadatas
        ):

            chunks.append(
                {
                    "text": doc,
                    "source": metadata.get("source"),
                    "chunk": metadata.get("chunk"),
                    "hkr_node_id": metadata.get("hkr_node")
                }
            )

        return chunks

