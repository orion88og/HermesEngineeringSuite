"""Project aggregate root."""

from dataclasses import dataclass, field

from .base import DomainEntity
from .decision import Decision
from .document import Document
from .enums import ProjectStatus
from .ids import ProjectId
from .milestone import Milestone
from .requirement import Requirement
from .risk import Risk
from .task import Task

@dataclass(slots=True)
class Project(DomainEntity):
    project_id: ProjectId = field(default_factory=lambda: ProjectId(""))
    name: str = ""
    description: str = ""
    status: ProjectStatus = ProjectStatus.PLANNING

    tasks: list[Task] = field(default_factory=list)
    milestones: list[Milestone] = field(default_factory=list)
    requirements: list[Requirement] = field(default_factory=list)
    risks: list[Risk] = field(default_factory=list)
    decisions: list[Decision] = field(default_factory=list)
    documents: list[Document] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        self.touch()

    def add_milestone(self, milestone: Milestone) -> None:
        self.milestones.append(milestone)
        self.touch()

    def activate(self) -> None:
        self.status = ProjectStatus.ACTIVE
        self.touch()

    def archive(self) -> None:
        self.status = ProjectStatus.ARCHIVED
        self.touch()
