from enum import Enum

class IntentType(Enum):

    FILESYSTEM = "filesystem"

    PROCESS = "process"

    NETWORK = "network"

    PACKAGE = "package"

    DIAGNOSTICS = "diagnostics"

    UNKNOWN = "unknown"