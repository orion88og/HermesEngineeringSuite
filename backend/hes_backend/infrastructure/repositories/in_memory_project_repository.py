"""
In-memory ProjectRepository implementation.
"""
from ...domain.ids import ProjectId
from ...domain.project import Project
from ...domain.repositories import ProjectRepository


class InMemoryProjectRepository(ProjectRepository):
    """Stores project aggregates in memory."""

    def __init__(self) -> None:
        self._projects: dict[ProjectId, Project] = {}

    def get(self, project_id: ProjectId) -> Project | None:
        return self._projects.get(project_id)

    def save(self, project: Project) -> None:
        self._projects[project.project_id] = project

    def delete(self, project_id: ProjectId) -> None:
        self._projects.pop(project_id, None)
