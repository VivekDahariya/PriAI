from .models import MetadataNode



class KnowledgeHierarchy:


    def __init__(self):

        self.root = None



    def create_book(
        self,
        name,
        metadata
    ):

        self.root = MetadataNode(
            name=name,
            metadata=metadata
        )

        return self.root



    def add_chapter(
        self,
        name,
        metadata={}
    ):

        chapter = MetadataNode(
            name=name,
            metadata=metadata
        )

        self.root.add_child(chapter)

        return chapter



    def add_page(
        self,
        chapter,
        name,
        metadata={}
    ):

        page = MetadataNode(
            name=name,
            metadata=metadata
        )

        chapter.add_child(page)

        return page