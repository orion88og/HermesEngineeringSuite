"""
Application service smoke tests.
"""

from hes_backend.application.services import ProjectApplicationService
from hes_backend.infrastructure.repositories import InMemoryProjectRepository


def test_service_instantiates() -> None:
    repo = InMemoryProjectRepository()
    service = ProjectApplicationService(repo)
    assert service is not None
