from dataclasses import dataclass, field

from app.hkr.models import MetadataNode
from app.hkr.models import KnowledgeDocument

from app.compiler.concept_models import (
    ConceptNode,
    ConceptRelation
)


@dataclass
class KnowledgeUnit:

    id: str

    text: str

    hkr_node_id: str

    parent_id: str | None = None

    level: str = "chunk"

    metadata: dict = field(
        default_factory=dict
    )

    concepts: list[str] = field(
        default_factory=list
    )

    entities: list[str] = field(
        default_factory=list
    )

    embedding: list[float] | None = None


@dataclass
class MetadataDictionary:

    word_to_id: dict = field(
        default_factory=dict
    )

    id_to_word: dict = field(
        default_factory=dict
    )


@dataclass
class KnowledgeRelation:

    source: str

    relation: str

    target: str

    weight: float = 1.0

    confidence: float = 1.0

    source_type: str = "node"

    target_type: str = "node"


@dataclass
class CompiledKnowledge:

    document: KnowledgeDocument

    hierarchy: dict[str, MetadataNode]

    dictionary: MetadataDictionary

    units: list[KnowledgeUnit]

    relations: list[KnowledgeRelation] = field(
        default_factory=list
    )

    concepts: list[ConceptNode] = field(
        default_factory=list
    )

    concept_relations: list[ConceptRelation] = field(
        default_factory=list
    )