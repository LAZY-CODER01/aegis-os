import subprocess
import time

from domain.execution_result import ExecutionResult


class Executor:

    def run(self, command: list[str]) -> ExecutionResult:

        start = time.perf_counter()

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30
        )

        duration = (time.perf_counter() - start) * 1000

        return ExecutionResult(
            stdout=result.stdout,
            stderr=result.stderr,
            exit_code=result.returncode,
            duration_ms=duration
        )