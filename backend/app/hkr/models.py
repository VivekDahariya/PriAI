from dataclasses import dataclass, field


@dataclass
class MetadataNode:

    id: str

    level: str

    metadata: dict = field(default_factory=dict)

    parent_id: str | None = None

    children: list[str] = field(default_factory=list)



@dataclass
class KnowledgeDocument:

    id: str

    name: str

    root_node: str
