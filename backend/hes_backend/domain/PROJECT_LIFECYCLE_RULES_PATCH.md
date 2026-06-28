Add lifecycle methods to Project using the existing ProjectStatus enum:

activate(): PLANNING -> ACTIVE
place_on_hold(): ACTIVE -> ON_HOLD
resume(): ON_HOLD -> ACTIVE
complete(): ACTIVE -> COMPLETED
archive(): COMPLETED -> ARCHIVED

Each successful transition should:
- update status
- call touch()

Raise ValueError for invalid transitions.
