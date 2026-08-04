from app.retrieval.graph_retriever import GraphRetriever


graph = GraphRetriever()


nodes = graph.expand(

    "computer_science",

    [
        "9e4da266-0fb4-40c8-a40e-d3cf9d2b0691"
    ],

    hops=1

)


print("\nGRAPH INTELLIGENCE RESULTS")
print("-" * 40)

for node in nodes:

    print(
        f"Node: {node['node_id']}"
    )

    print(
        f"Distance: {node['distance']}"
    )

    print(
        f"Relation: {node['relation']}"
    )

    print()