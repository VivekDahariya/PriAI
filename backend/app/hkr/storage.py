import json
from pathlib import Path



class HKRStorage:


    def __init__(self):

        self.path = Path(
            "database/hkr"
        )

        self.path.mkdir(
            parents=True,
            exist_ok=True
        )


        self.nodes_file = (
            self.path /
            "nodes.json"
        )


        self.documents_file = (
            self.path /
            "documents.json"
        )



    def save_nodes(self,nodes):

        data={}

        for key,node in nodes.items():

            data[key]=node.to_dict()


        with open(
            self.nodes_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )



    def load_nodes(self):

        if not self.nodes_file.exists():

            return {}


        from .models import MetadataNode


        with open(
            self.nodes_file,
            encoding="utf-8"
        ) as f:

            data=json.load(f)



        return {

            key:
            MetadataNode.from_dict(value)

            for key,value in data.items()

        }



    def save_documents(self,documents):

        data={}

        for key,doc in documents.items():

            data[key]=doc.to_dict()


        with open(
            self.documents_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )



    def load_documents(self):

        if not self.documents_file.exists():

            return {}


        from .models import KnowledgeDocument


        with open(
            self.documents_file,
            encoding="utf-8"
        ) as f:

            data=json.load(f)



        return {

            key:
            KnowledgeDocument.from_dict(value)

            for key,value in data.items()

        }