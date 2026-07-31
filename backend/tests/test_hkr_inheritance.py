from app.hkr.hierarchy import KnowledgeHierarchy
from app.hkr.resolver import resolve_node_metadata



hkr = KnowledgeHierarchy()


book = hkr.create_book(
    "Deep Learning Book",
    {
        "author": "Ian Goodfellow",
        "language": "English"
    }
)


chapter = hkr.add_chapter(
    "Neural Networks",
    {
        "topic": "AI"
    }
)


page = hkr.add_page(
    chapter,
    "Page 10",
    {
        "page_number":10
    }
)



metadata = resolve_node_metadata(page)


print(metadata)