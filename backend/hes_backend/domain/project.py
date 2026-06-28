"""
Hermes Engineering Suite (HES)

Module:
    Projects Domain

File:
    project.py

Purpose:
    Defines the Project aggregate root.

Design Notes:
    Child collections are private. All modifications should occur
    through aggregate methods so future business rules, authorization,
    auditing, and domain events are enforced in one place.
"""

from dataclasses import dataclass, field
from typing import Tuple

from .base import DomainEntity
from .decision import Decision
from .document import Document
from .enums import ProjectStatus
from .ids import ProjectId
from .milestone import Milestone
from .requirement import Requirement
from .risk import Risk
from .task import Task
from .value_objects import Description, ProjectName

@dataclass(slots=True)
class Project(DomainEntity):
    """Aggregate root representing an engineering project."""

    project_id: ProjectId = field(default_factory=lambda: ProjectId(""))
    name: ProjectName = field(default_factory=lambda: ProjectName("New Project"))
    description: Description = field(default_factory=lambda: Description(""))
    status: ProjectStatus = ProjectStatus.PLANNING

    _tasks: list[Task] = field(default_factory=list, repr=False)
    _milestones: list[Milestone] = field(default_factory=list, repr=False)
    requirements: list[Requirement] = field(default_factory=list)
    risks: list[Risk] = field(default_factory=list)
    decisions: list[Decision] = field(default_factory=list)
    documents: list[Document] = field(default_factory=list)

    @property
    def tasks(self) -> Tuple[Task, ...]:
        """Read-only view of project tasks."""
        return tuple(self._tasks)

    @property
    def milestones(self) -> Tuple[Milestone, ...]:
        """Read-only view of project milestones."""
        return tuple(self._milestones)

    def add_task(self, task: Task) -> None:
        """Add a task through the aggregate."""
        self._tasks.append(task)
        self.touch()

    def add_milestone(self, milestone: Milestone) -> None:
        """Add a milestone through the aggregate."""
        self._milestones.append(milestone)
        self.touch()
