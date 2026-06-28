"""
Project application use cases.

These wrappers expose explicit application entry points while delegating
implementation to ProjectApplicationService.
"""

from ...application.services import ProjectApplicationService
from ...domain.ids import ProjectId
from ...domain.project import Project


class GetProjectUseCase:
    def __init__(self, service: ProjectApplicationService) -> None:
        self._service = service

    def execute(self, project_id: ProjectId) -> Project | None:
        return self._service.get_project(project_id)


class SaveProjectUseCase:
    def __init__(self, service: ProjectApplicationService) -> None:
        self._service = service

    def execute(self, project: Project) -> None:
        self._service.save_project(project)


class DeleteProjectUseCase:
    def __init__(self, service: ProjectApplicationService) -> None:
        self._service = service

    def execute(self, project_id: ProjectId) -> None:
        self._service.delete_project(project_id)
