"""
Application tests for the in-memory repository.
"""

from hes_backend.infrastructure.repositories import InMemoryProjectRepository


def test_repository_instantiates() -> None:
    repo = InMemoryProjectRepository()
    assert repo is not None
