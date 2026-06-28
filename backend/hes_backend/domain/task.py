"""Task domain entity."""

from dataclasses import dataclass, field

from .base import DomainEntity
from .ids import TaskId

@dataclass(slots=True)
class Task(DomainEntity):
    task_id: TaskId = field(default_factory=lambda: TaskId(""))
    title: str = ""
    description: str = ""
    completed: bool = False

    def complete(self) -> None:
        self.completed = True
        self.touch()
