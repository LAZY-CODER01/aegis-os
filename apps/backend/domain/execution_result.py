from dataclasses import dataclass

@dataclass
class ExecutionResult:

    stdout: str

    stderr: str

    exit_code: int

    duration_ms: float