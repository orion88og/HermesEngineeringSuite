"""Base domain abstractions."""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4

@dataclass(slots=True)
class DomainEntity:
    """Base entity for all domain objects."""
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def touch(self) -> None:
        self.updated_at = datetime.now(UTC)
