"""Requirement domain entity."""
from dataclasses import dataclass
from .base import DomainEntity

@dataclass(slots=True)
class Requirement(DomainEntity):
    identifier: str = ""
    title: str = ""
    satisfied: bool = False
