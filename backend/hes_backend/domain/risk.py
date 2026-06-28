"""Risk domain entity."""
from dataclasses import dataclass
from .base import DomainEntity

@dataclass(slots=True)
class Risk(DomainEntity):
    title: str = ""
    probability: int = 0
    impact: int = 0
