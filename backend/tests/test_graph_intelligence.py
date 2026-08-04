from app.retrieval.graph_retriever import GraphRetriever
from app.compiler.relation_store import RelationStore


store = RelationStore()

graph = GraphRetriever()


relations = store.load(
    "computer_science"
)


start_node = "9e249280-49c7-4af4-aba3-d03a70fa3836"


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

print()


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

    print(
        f"Weight: {node['weight']}"
    )

    print(
        f"Confidence: {node['confidence']}"
    )

    print()