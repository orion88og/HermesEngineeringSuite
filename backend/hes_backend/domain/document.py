"""Document domain entity."""
from dataclasses import dataclass
from .base import DomainEntity

@dataclass(slots=True)
class Document(DomainEntity):
    filename: str = ""
    description: str = ""
