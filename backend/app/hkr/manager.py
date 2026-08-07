import uuid

from .models import MetadataNode, KnowledgeDocument
from .storage import HKRStorage
from .metadata_resolver import MetadataResolver


class HKRManager:


    def __init__(self):

        self.storage = HKRStorage()

        # Load existing memory
        self.nodes = self.storage.load_nodes()

        self.documents = self.storage.load_documents()
        self.metadata_resolver = MetadataResolver(self)


    def create_document(self, name):

        root_id = str(uuid.uuid4())


        root = MetadataNode(

            id=root_id,

            level="book",

            metadata={
                "name": name
            }

        )


        self.nodes[root_id] = root



        document = KnowledgeDocument(

            id=str(uuid.uuid4()),

            name=name,

            root_node=root_id

        )


        self.documents[document.id] = document


        self._persist()


        return document




    def add_child(
        self,
        parent_id,
        level,
        metadata
    ):


        node_id = str(uuid.uuid4())


        node = MetadataNode(

            id=node_id,

            level=level,

            metadata=metadata,

            parent_id=parent_id

        )


        self.nodes[node_id] = node



        if parent_id in self.nodes:

            self.nodes[parent_id].children.append(
                node_id
            )


        self._persist()


        return node




    def resolve_metadata(self,node_id):

        return self.metadata_resolver.resolve(node_id)




    def get_node(self,node_id):

        return self.nodes.get(node_id)




    def get_document(self,document_id):

        return self.documents.get(document_id)




    def _persist(self):

        self.storage.save_nodes(
            self.nodes
        )


        self.storage.save_documents(
            self.documents
        )