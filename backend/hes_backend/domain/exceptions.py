"""Domain exceptions."""

class DomainError(Exception):
    """Base exception for all domain errors."""

class ValidationError(DomainError):
    """Raised when domain validation fails."""

class EntityNotFoundError(DomainError):
    """Raised when a requested entity cannot be found."""
