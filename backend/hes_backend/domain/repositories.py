"""
Hermes Engineering Suite (HES)

Module:
    Domain Repository Contracts

Purpose:
    Defines persistence contracts for aggregate roots.

Design Notes:
    Repository interfaces are expressed as Protocols so the domain remains
    independent of any specific database or storage technology.
"""

from typing import Protocol

from .ids import ProjectId
from .project import Project


class ProjectRepository(Protocol):
    """Persistence contract for Project aggregates."""

    def get(self, project_id: ProjectId) -> Project | None:
        """Return a project by identifier or None if it does not exist."""
        ...

    def save(self, project: Project) -> None:
        """Persist a project aggregate."""
        ...

    def delete(self, project_id: ProjectId) -> None:
        """Delete a project aggregate."""
        ...
