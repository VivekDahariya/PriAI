class ContextBuilder:


    def build(
        self,
        contexts: list[dict]
    ) -> str:


        output = []

        output.append(
            "===== KNOWLEDGE CONTEXT =====\n"
        )


        for index, context in enumerate(
            contexts,
            start=1
        ):

            block = []

            block.append(
                f"Knowledge Unit {index}:"
            )


            block.append(
                context.get(
                    "text",
                    ""
                )
            )


            if context.get("from_graph"):

                block.append(
                    "\nConnection Information:"
                )


                block.append(

                    f"Relation: "
                    f"{context.get('graph_relation')}"

                )


                block.append(

                    f"Relation Strength: "
                    f"{context.get('graph_weight')}"

                )


                block.append(

                    f"Confidence: "
                    f"{context.get('graph_confidence')}"

                )


            output.append(

                "\n".join(block)

            )

            output.append(
                "\n"
            )


        return "\n".join(output)