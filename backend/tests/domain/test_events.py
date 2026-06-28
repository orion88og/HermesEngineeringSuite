from hes_backend.domain.base import DomainEntity
from hes_backend.domain.events import DomainEvent


def test_record_and_pull_events():
    e=DomainEntity()
    evt=DomainEvent()
    e.record_event(evt)
    events=e.pull_events()
    assert events==[evt]
    assert e.pull_events()==[]
