# Design Rationale

## Goals
- Make Project the root aggregate for engineering work.
- Keep related records discoverable.
- Support local-first operation and future synchronization.

## Trade-offs
- UUID primary keys for portability.
- Soft-delete for recoverability.
- REST-first API with room for future events.

## Alternatives Considered
- Flat document storage (rejected for reporting limitations).
- Graph-only database (deferred until justified).
