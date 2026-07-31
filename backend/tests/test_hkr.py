from app.hkr.models import HKRNode, HKRChunk
from app.hkr.tree import HKRTree
from app.hkr.metadata import MetadataResolver


tree = HKRTree()


book = HKRNode(
    id="book1",
    node_type="book",
    metadata={
        "language": "English",
        "author": "Vivek"
    }
)


chapter = HKRNode(
    id="chapter1",
    node_type="chapter",
    parent_id="book1",
    metadata={
        "topic": "AI"
    }
)


chunk = HKRChunk(
    id="chunk1",
    node_type="chunk",
    parent_id="chapter1",
    text="Neural networks are..."
)


tree.add_node(book)
tree.add_node(chapter)
tree.add_node(chunk)


resolver = MetadataResolver(tree)


print(
    resolver.resolve(
        "chunk1",
        "author"
    )
)


print(
    resolver.resolve(
        "chunk1",
        "topic"
    )
)