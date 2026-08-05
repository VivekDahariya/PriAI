from sentence_transformers import SentenceTransformer

from app.storage.chroma import ChromaVectorStore
from app.retrieval.graph_retriever import GraphRetriever


class RetrievalService:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        self.graph = GraphRetriever()



    def calculate_vector_score(
        self,
        distance
    ):

        if distance is None:
            return 0

        return max(
            0,
            1 - distance
        )



    def calculate_graph_score(
        self,
        weight,
        confidence
    ):

        if weight is None:
            return 0

        return (
            weight *
            confidence
        )



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

            node_id = result.get(
                "hkr_node_id"
            )

            if node_id:

                node_ids.append(
                    node_id
                )



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



        expanded_node_ids = [

            node["node_id"]

            for node in expanded_nodes

        ]



        graph_chunks = []


        if expanded_node_ids:

            graph_chunks = store.get_by_hkr_nodes(
                expanded_node_ids
            )



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


            vector_score = self.calculate_vector_score(
                result.get("distance")
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

                    "vector_score": vector_score,

                    "retrieval_score": vector_score,

                    "from_graph": False,

                    "graph_context": expanded_nodes

                }

            )



        # -----------------------------
        # Graph Results
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



            graph_score = self.calculate_graph_score(

                graph_metadata.get(
                    "weight"
                ),

                graph_metadata.get(
                    "confidence"
                )

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


                    "graph_relation": graph_metadata.get(
                        "relation"
                    ),

                    "graph_weight": graph_metadata.get(
                        "weight"
                    ),

                    "graph_confidence": graph_metadata.get(
                        "confidence"
                    ),


                    "graph_score": graph_score,


                    "retrieval_score": graph_score,


                    "from_graph": True,

                    "graph_context": expanded_nodes

                }

            )



        # -----------------------------
        # Sort by intelligence score
        # -----------------------------

        retrieved.sort(

            key=lambda x: x.get(
                "retrieval_score",
                0
            ),

            reverse=True

        )


        return retrieved