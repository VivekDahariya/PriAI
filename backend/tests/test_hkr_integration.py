from app.hkr.manager import HKRManager


hkr = HKRManager()


document = hkr.create_document(
    "Machine Learning Book"
)


chapter = hkr.add_child(
    document.root_node,
    "chapter",
    {
        "chapter": "Neural Networks"
    }
)


page = hkr.add_child(
    chapter.id,
    "page",
    {
        "page": 10
    }
)


metadata = hkr.resolve_metadata(
    page.id
)


print(metadata)