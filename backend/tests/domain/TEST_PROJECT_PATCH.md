Update test_add_task() after Package 04:

- Construct Project with ProjectName and Description if required by current implementation.
- After project.add_task(task), assert len(project.tasks)==1.
- Assert len(project.pull_events())==1.
