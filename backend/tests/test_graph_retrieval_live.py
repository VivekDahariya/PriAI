from app.retrieval.graph_retriever import GraphRetriever


retriever = GraphRetriever()


nodes = [
    "35e30076-32ef-4dc9-b658-8f1f799860df"
]


expanded = retriever.expand(
    ai_id="computer_science",
    node_ids=nodes,
    hops=1
)


print("EXPANDED NODES")
for node in expanded:
    print(node)