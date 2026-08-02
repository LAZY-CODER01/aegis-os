from dataclasses import dataclass, field

@dataclass
class Command:

    executable: str

    arguments: list[str] = field(default_factory=list)

    sudo: bool = False

    risk_score: int = 0

    explanation: str = ""

    def shell(self):

        if self.sudo:
            return "sudo " + self.executable + " " + " ".join(self.arguments)

        return self.executable + " " + " ".join(self.arguments)