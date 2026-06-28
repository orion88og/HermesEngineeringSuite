"""
PATCH INSTRUCTIONS

Update project.py:

1. Import:
    from .project_events import (
        MilestoneAddedEvent,
        TaskAddedEvent,
    )

2. In add_task():
    self.record_event(
        TaskAddedEvent(
            project_id=self.project_id,
            task_id=task.task_id,
        )
    )

3. In add_milestone():
    self.record_event(
        MilestoneAddedEvent(
            project_id=self.project_id,
            milestone_id=milestone.milestone_id,
        )
    )

No other behavior changes are required.
