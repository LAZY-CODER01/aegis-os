from domain.intent import Intent, IntentType


class IntentEngine:

    def detect(self, text: str) -> Intent:

        normalized = text.lower()

        if "process" in normalized:

            return Intent(
                type=IntentType.PROCESS,
                confidence=0.95,
                raw_text=text
            )

        if "file" in normalized:

            return Intent(
                type=IntentType.FILESYSTEM,
                confidence=0.93,
                raw_text=text
            )

        if "network" in normalized:

            return Intent(
                type=IntentType.NETWORK,
                confidence=0.91,
                raw_text=text
            )

        return Intent(
            type=IntentType.UNKNOWN,
            confidence=0.0,
            raw_text=text
        )