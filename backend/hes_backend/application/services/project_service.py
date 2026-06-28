"""
Hermes Engineering Suite (HES)

Application service for Project use cases.

Current responsibility:
Coordinate repository access without introducing domain behavior that
does not yet exist.
"""

from ...domain.ids import ProjectId
from ...domain.project import Project
from ...domain.repositories import ProjectRepository


class ProjectApplicationService:
    """Coordinates Project application use cases."""

    def __init__(self, repository: ProjectRepository) -> None:
        self._repository = repository

    def get_project(self, project_id: ProjectId) -> Project | None:
        """Retrieve a project by identifier."""
        return self._repository.get(project_id)

    def save_project(self, project: Project) -> None:
        """Persist a project aggregate."""
        self._repository.save(project)

    def delete_project(self, project_id: ProjectId) -> None:
        """Delete a project aggregate."""
        self._repository.delete(project_id)
