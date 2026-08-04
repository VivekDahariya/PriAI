from dataclasses import dataclass, field

from app.hkr.models import MetadataNode
from app.hkr.models import KnowledgeDocument


@dataclass
class KnowledgeUnit:

    id: str

    text: str

    hkr_node_id: str

    metadata: dict = field(default_factory=dict)

    embedding: list[float] | None = None


@dataclass
class MetadataDictionary:

    word_to_id: dict = field(default_factory=dict)

    id_to_word: dict = field(default_factory=dict)


@dataclass
class KnowledgeRelation:

    source: str

    relation: str

    target: str

    # Relationship strength
    weight: float = 1.0

    # Extraction confidence
    confidence: float = 1.0

    # Entity types
    source_type: str = "node"

    target_type: str = "node"


@dataclass
class CompiledKnowledge:

    document: KnowledgeDocument

    hierarchy: dict[str, MetadataNode]

    dictionary: MetadataDictionary

    units: list[KnowledgeUnit]

    relations: list[KnowledgeRelation] = field(default_factory=list)