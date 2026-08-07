from dataclasses import dataclass, field
from typing import List, Optional
import uuid


@dataclass
class KnowledgeHierarchyNode:

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    name: str = ""

    node_type: str = ""

    parent_id: Optional[str] = None

    children: List[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

