from pydantic import BaseModel


class AIRegistryEntry(BaseModel):

    id: str

    name: str

    documents: int

    chunks: int

    created_at: str

    knowledge_density: str

    suggested_top_k: int

    suggested_threshold: float