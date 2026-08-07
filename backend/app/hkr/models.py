from dataclasses import dataclass, field
from typing import Optional



@dataclass
class MetadataNode:

    id: str

    level: str

    metadata: dict = field(
        default_factory=dict
    )

    parent_id: Optional[str] = None

    children: list[str] = field(
        default_factory=list
    )


    def to_dict(self):

        return {

            "id": self.id,

            "level": self.level,

            "metadata": self.metadata,

            "parent_id": self.parent_id,

            "children": self.children

        }



    @staticmethod
    def from_dict(data):

        return MetadataNode(

            id=data["id"],

            level=data["level"],

            metadata=data.get(
                "metadata",
                {}
            ),

            parent_id=data.get(
                "parent_id"
            ),

            children=data.get(
                "children",
                []
            )

        )




@dataclass
class KnowledgeDocument:

    id: str

    name: str

    root_node: str



    def to_dict(self):

        return {

            "id":self.id,

            "name":self.name,

            "root_node":self.root_node

        }



    @staticmethod
    def from_dict(data):

        return KnowledgeDocument(

            id=data["id"],

            name=data["name"],

            root_node=data["root_node"]

        )