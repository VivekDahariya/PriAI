from dataclasses import dataclass


@dataclass
class KnowledgeChunk:

    id: str

    text: str

    source: str

    chunk_index: int

    embedding: list[float]

    hkr_node_id: str | None = None