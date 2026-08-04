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


        # -----------------------------
        # HKR Graph Expansion
        # -----------------------------

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
                ai_id,
                node_ids,
                hops=1
            )


        # -----------------------------
        # Fetch graph connected chunks
        # -----------------------------

        graph_chunks = []

        if expanded_nodes:

            graph_chunks = store.get_by_hkr_nodes(
                expanded_nodes
            )


        print("\n========== GRAPH EXPANSION ==========")

        print(expanded_nodes)

        print("\n========== GRAPH CHUNKS ==========")

        for chunk in graph_chunks:
            print(chunk)

        print("====================================\n")


        retrieved = []


        existing_nodes = set()


        # -----------------------------
        # Vector Results
        # -----------------------------

        for result in results:

            node_id = result.get(
                "hkr_node_id"
            )

            if node_id:
                existing_nodes.add(node_id)


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

                    "hkr_node_id": node_id,

                    "graph_context": expanded_nodes,

                    "from_graph": False

                }

            )


        # -----------------------------
        # HKR Expanded Results
        # -----------------------------

        for chunk in graph_chunks:

            node_id = chunk.get(
                "hkr_node_id"
            )


            if node_id not in existing_nodes:

                retrieved.append(

                    {
                        "text": chunk["text"],

                        "source": chunk["source"],

                        "chunk": chunk["chunk"],

                        "distance": None,

                        "hkr_node_id": node_id,

                        "graph_context": expanded_nodes,

                        "from_graph": True

                    }

                )


        return retrieved