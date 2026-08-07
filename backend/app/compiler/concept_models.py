from dataclasses import dataclass, field
from pydantic import BaseModel


@dataclass
class ConceptNode:

    id: str

    name: str

    aliases: list[str] = field(default_factory=list)

    chunk_ids: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)


class ConceptRelation(BaseModel):

    source: str

    target: str

    relation: str

    weight: float

    confidence: float