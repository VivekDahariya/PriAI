from app.hkr.manager import HKRManager


hkr = HKRManager()


document = hkr.create_document(
    "Machine Learning"
)


page = hkr.add_child(

    document.root_node,

    "page",

    {
        "page":3
    }

)


chunk = hkr.add_child(

    page.id,

    "chunk",

    {
        "text":
        "Gradient Descent requires learning rate"
    }

)



print(
    hkr.resolve_metadata(
        chunk.id
    )
)