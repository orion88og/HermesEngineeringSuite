Update project.py:

1. Import:
   from .project_status import ProjectStatus

2. Add a status field initialized to:
   ProjectStatus.DRAFT

3. Add methods:

   activate() -> set status to ACTIVE
   archive() -> set status to ARCHIVED

Each method should call touch() and record the appropriate domain event
when those events are introduced in a later package.
