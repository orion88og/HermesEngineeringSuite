"""
Hermes Engineering Suite (HES)

Application Commands - Projects

Commands capture user intent. They are immutable request objects
passed into application services.
"""

from dataclasses import dataclass

from hes_backend.domain.ids import ProjectId


@dataclass(frozen=True, slots=True)
class CreateProjectCommand:
    """Request to create a new project."""
    name: str
    description: str = ""


@dataclass(frozen=True, slots=True)
class UpdateProjectCommand:
    """Request to update an existing project."""
    project_id: ProjectId
    name: str
    description: str


@dataclass(frozen=True, slots=True)
class ArchiveProjectCommand:
    """Request to archive an existing project."""
    project_id: ProjectId
