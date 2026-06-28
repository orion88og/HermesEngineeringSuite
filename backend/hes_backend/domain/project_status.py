"""
Project lifecycle state definitions.
"""

from enum import StrEnum


class ProjectStatus(StrEnum):
    """Represents the lifecycle state of a project."""

    DRAFT = "draft"
    ACTIVE = "active"
    ARCHIVED = "archived"
