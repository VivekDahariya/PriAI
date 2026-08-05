import json
from pathlib import Path

from app.retrieval.graph_retriever import GraphRetriever


with open(
    "database/relations/computer_science.json",
    "r"
) as f:

    relations = json.load(f)


start_node = relations[0]["source"]


graph = GraphRetriever()


nodes = graph.expand(

    "computer_science",

    [
        start_node
    ],

    hops=1

)


print("\nGRAPH INTELLIGENCE RESULTS")
print("-" * 40)

print("START NODE")
print(start_node)


for node in nodes:

    print()

    print(
        f"Node: {node['node_id']}"
    )

    print(
        f"Distance: {node['distance']}"
    )

    print(
        f"Relation: {node['relation']}"
    )

    print(
        f"Weight: {node['weight']}"
    )

    print(
        f"Confidence: {node['confidence']}"
    )

    print(
        f"Source Type: {node['source_type']}"
    )

    print(
        f"Target Type: {node['target_type']}"
    )