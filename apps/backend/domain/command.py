from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Command:
    executable: str
    arguments: List[str]
    requires_sudo: bool = False
    risk_score: int = 0

    def to_shell(self) -> str:
        return " ".join(
            [self.executable, *self.arguments]
        )