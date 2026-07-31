import uuid

from .models import MetadataNode, KnowledgeDocument



class HKRManager:


    def __init__(self):

        self.nodes = {}

        self.documents = {}



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


        self.nodes[parent_id].children.append(
            node_id
        )


        return node



    def resolve_metadata(self,node_id):


        result={}


        current=node_id


        while current:


            node=self.nodes[current]


            result.update(
                node.metadata
            )


            current=node.parent_id


        return result