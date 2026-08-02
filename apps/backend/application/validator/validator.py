class Validator:

    BLOCKED_EXECUTABLES = {
        "mkfs",
        "shutdown",
        "reboot",
    }

    HIGH_RISK_EXECUTABLES = {
        "rm",
        "dd",
    }

    def validate(self, command: list[str]) -> bool:

        if not command:
            return False

        executable = command[0]

        if executable in self.BLOCKED_EXECUTABLES:
            return False

        if executable in self.HIGH_RISK_EXECUTABLES:
            return False

        return True