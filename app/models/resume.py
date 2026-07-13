from dataclasses import dataclass


@dataclass(slots=True)
class Resume:
    id: int
    name: str
    description: str