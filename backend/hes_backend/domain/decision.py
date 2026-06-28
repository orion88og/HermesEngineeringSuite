"""Decision domain entity."""
from dataclasses import dataclass
from .base import DomainEntity

@dataclass(slots=True)
class Decision(DomainEntity):
    title: str = ""
    rationale: str = ""
