from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ProjectName:
    value:str
    def __post_init__(self):
        if not self.value.strip():
            raise ValueError("Project name cannot be empty.")

@dataclass(frozen=True, slots=True)
class Description:
    value:str
