"""Milestone domain entity."""

from dataclasses import dataclass, field

from .base import DomainEntity
from .ids import MilestoneId

@dataclass(slots=True)
class Milestone(DomainEntity):
    milestone_id: MilestoneId = field(default_factory=lambda: MilestoneId(""))
    name: str = ""
    achieved: bool = False

    def achieve(self) -> None:
        self.achieved = True
        self.touch()
