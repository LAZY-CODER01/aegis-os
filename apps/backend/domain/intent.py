from dataclasses import dataclass
from enum import Enum


class IntentType(Enum):

    PROCESS="PROCESS"

    FILESYSTEM="FILESYSTEM"

    NETWORK="NETWORK"

    PACKAGE="PACKAGE"

    SYSTEM="SYSTEM"

    UNKNOWN="UNKNOWN"


@dataclass
class Intent:

    type: IntentType

    confidence: float

    raw_text: str