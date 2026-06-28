from hes_backend.domain.project import Project
from hes_backend.domain.task import Task

def test_add_task():
    project = Project(name="Demo")
    task = Task(title="Task")
    project.add_task(task)
    assert len(project.tasks) == 1
