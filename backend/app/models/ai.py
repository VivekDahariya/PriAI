from dataclasses import dataclass


@dataclass
class AIWorkspace:
    id: str
    name: str
    subject: str
    description: str