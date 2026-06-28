from hes_backend.domain.project import Project
from hes_backend.domain.milestone import Milestone

def test_add_milestone():
    project = Project(name="Demo")
    project.add_milestone(Milestone(name="Phase 1"))
    assert len(project.milestones) == 1
