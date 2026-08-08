from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MetadataNode:

    id: str = None

    name: str = ""

    metadata: dict = field(
        default_factory=dict
    )

    parent: Optional["MetadataNode"] = None

    children: list = field(
        default_factory=list
    )


    def add_child(
        self,
        child
    ):

        child.parent = self

        self.children.append(
            child
        )


    def resolve_metadata(
        self
    ):

        result = {}


        if self.parent:

            result.update(
                self.parent.resolve_metadata()
            )


        result.update(
            self.metadata
        )


        return result


@dataclass
class KnowledgeDocument:

    id: str

    name: str

    root_node: str


    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "root_node": self.root_node

        }


    @staticmethod
    def from_dict(data):

        return KnowledgeDocument(

            id=data["id"],

            name=data["name"],

            root_node=data["root_node"]

        )



@dataclass
class HKRNode:

    id: str

    node_type: str = "concept"

    parent_id: Optional[str] = None

    metadata: dict = field(
        default_factory=dict
    )


@dataclass
class HKRChunk:

    id: str

    text: str

    node_type: str = "chunk"

    parent_id: Optional[str] = None

    metadata: dict = field(
        default_factory=dict
    )