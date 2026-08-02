from dataclasses import dataclass, field

from .task import Task

@dataclass
class ExecutionPlan:

    tasks: list[Task] = field(default_factory=list)

    approved: bool = False