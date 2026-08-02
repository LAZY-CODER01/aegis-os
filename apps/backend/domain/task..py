from dataclasses import dataclass

@dataclass
class Task:

    id: str

    description: str

    completed: bool = False