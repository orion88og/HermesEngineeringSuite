"""Project domain events."""
from dataclasses import dataclass
from .events import DomainEvent
from .ids import MilestoneId, ProjectId, TaskId

@dataclass(frozen=True, slots=True, kw_only=True)
class TaskAddedEvent(DomainEvent):
    project_id: ProjectId
    task_id: TaskId

@dataclass(frozen=True, slots=True, kw_only=True)
class MilestoneAddedEvent(DomainEvent):
    project_id: ProjectId
    milestone_id: MilestoneId
