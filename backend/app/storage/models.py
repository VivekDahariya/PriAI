from dataclasses import dataclass
from typing import Optional


@dataclass
class KnowledgeChunk:

    id: str

    text: str

    source: str

    chunk_index: int

    embedding: list[float]

    knowledge_unit_id: str = ""

    hkr_node_id: Optional[str] = None