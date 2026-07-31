from dataclasses import dataclass
from typing import Optional


@dataclass
class KnowledgeChunk:
    id: str
    text: str
    source: str
    chunk_index: int
    embedding: Optional[list[float]] = None