"""
Hermes Engineering Suite (HES)

Immutable domain event base class.
"""
from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4

@dataclass(frozen=True, slots=True, kw_only=True)
class DomainEvent:
    """Immutable base class for all domain events."""
    event_id: str = field(default_factory=lambda: str(uuid4()))
    occurred_at: datetime = field(default_factory=lambda: datetime.now(UTC))
