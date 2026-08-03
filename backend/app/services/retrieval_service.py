from sentence_transformers import SentenceTransformer

from app.storage.chroma import ChromaVectorStore
from app.retrieval.graph_retriever import GraphRetriever


class RetrievalService:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        self.graph = GraphRetriever()


    def retrieve(
        self,
        ai_id: str,
        question: str,
        top_k: int = 5
    ):

        store = ChromaVectorStore(ai_id)


        query_embedding = self.embedding_model.encode(
            question
        ).tolist()


        results = store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )


        print("\n========== VECTOR RESULTS ==========")

        for result in results:
            print(result)

        print("====================================\n")


        node_ids = []


        for result in results:

            hkr_node_id = result.get(
                "hkr_node_id"
            )

            if hkr_node_id:

                node_ids.append(
                    hkr_node_id
                )


        expanded_nodes = []


        if node_ids:

            expanded_nodes = self.graph.expand(

                ai_id=ai_id,

                node_ids=node_ids,

                hops=1

            )


        print("\n========== GRAPH EXPANSION ==========")

        print(expanded_nodes)

        print("====================================\n")


        retrieved = []


        for result in results:

            metadata = result.get(
                "metadata",
                {}
            )


            retrieved.append(

                {
                    "text": result["text"],

                    "source": metadata.get(
                        "source"
                    ),

                    "chunk": metadata.get(
                        "chunk"
                    ),

                    "distance": result.get(
                        "distance"
                    ),

                    "hkr_node_id": result.get(
                        "hkr_node_id"
                    ),

                    "graph_context": expanded_nodes

                }

            )


        return retrieved