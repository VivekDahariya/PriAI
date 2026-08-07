class HybridRanker:


    def __init__(self):

        self.vector_weight = 0.60

        self.graph_weight = 0.30

        self.confidence_weight = 0.10



    def calculate_score(
        self,
        item
    ):


        vector_score = item.get(
            "vector_score",
            0
        )


        graph_score = item.get(
            "graph_score",
            0
        )


        confidence = item.get(
            "graph_confidence",
            1.0
        )



        final_score = (

            self.vector_weight *
            vector_score

            +

            self.graph_weight *
            graph_score

            +

            self.confidence_weight *
            confidence

        )


        return final_score



    def rank(
        self,
        results
    ):


        for item in results:

            item["retrieval_score"] = (
                self.calculate_score(item)
            )


        results.sort(

            key=lambda x:
            x.get(
                "retrieval_score",
                0
            ),

            reverse=True

        )


        return results