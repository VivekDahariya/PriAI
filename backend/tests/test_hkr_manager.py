from app.hkr.manager import HKRManager



hkr = HKRManager()



book = hkr.create_document(
    "Machine Learning Book"
)


chapter = hkr.add_child(

    book.root_node,

    "chapter",

    {
        "chapter":"Neural Networks"
    }

)


page = hkr.add_child(

    chapter.id,

    "page",

    {
        "page":10
    }

)



print(
    hkr.resolve_metadata(page.id)
)