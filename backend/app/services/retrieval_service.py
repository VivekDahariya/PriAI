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
        # Extract HKR nodes
        # -----------------------------

        node_ids = []

        for result in results:

            node_id = result.get(
                "hkr_node_id"
            )

            if node_id:

                node_ids.append(
                    node_id
                )


        # -----------------------------
        # Weighted HKR Expansion
        # -----------------------------

        expanded_nodes = []


        if node_ids:

            expanded_nodes = self.graph.expand(
                ai_id,
                node_ids,
                hops=1
            )


        print("\n========== GRAPH EXPANSION ==========")

        for node in expanded_nodes:
            print(node)

        print("====================================\n")


        # -----------------------------
        # Convert graph results
        # into Chroma lookup IDs
        # -----------------------------

        expanded_node_ids = [

            node["node_id"]

            for node in expanded_nodes

        ]


        graph_chunks = []


        if expanded_node_ids:

            graph_chunks = store.get_by_hkr_nodes(
                expanded_node_ids
            )


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

                existing_nodes.add(
                    node_id
                )


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

                    "from_graph": False,

                    "graph_context": expanded_nodes

                }

            )



        # -----------------------------
        # Graph Expanded Chunks
        # -----------------------------

        for chunk in graph_chunks:


            node_id = chunk.get(
                "hkr_node_id"
            )


            if node_id in existing_nodes:

                continue



            graph_metadata = next(

                (
                    node
                    for node in expanded_nodes
                    if node["node_id"] == node_id
                ),

                {}

            )


            retrieved.append(

                {

                    "text": chunk["text"],

                    "source": chunk.get(
                        "source"
                    ),

                    "chunk": chunk.get(
                        "chunk"
                    ),

                    "distance": None,

                    "hkr_node_id": node_id,

                    "from_graph": True,

                    "graph_relation": graph_metadata.get(
                        "relation"
                    ),

                    "graph_weight": graph_metadata.get(
                        "weight"
                    ),

                    "graph_confidence": graph_metadata.get(
                        "confidence"
                    ),

                    "graph_context": expanded_nodes

                }

            )


        return retrieved