"""
Hermes Engineering Suite (HES)

Module:
    Domain

File:
    base.py

Purpose:
    Defines the base entity used throughout the HES domain model.

Design Notes:
    Domain entities own their lifecycle metadata and maintain a private
    collection of domain events. Events are recorded by the entity and
    exposed as a copy so callers cannot mutate internal state.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4

from .events import DomainEvent


@dataclass(slots=True)
class DomainEntity:
    """Base class for all HES domain entities."""

    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    _events: list[DomainEvent] = field(default_factory=list, init=False, repr=False)

    def touch(self) -> None:
        """Update the modification timestamp."""
        self.updated_at = datetime.now(UTC)

    def record_event(self, event: DomainEvent) -> None:
        """Record a domain event raised by this entity."""
        self._events.append(event)

    def pull_events(self) -> list[DomainEvent]:
        """Return recorded events and clear the internal queue."""
        events = self._events.copy()
        self._events.clear()
        return events
