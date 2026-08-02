# Import your IntentEngine from application/intent/intent_engine.py
from application.intent.intent_engine import IntentEngine

# Import your Intent types/models from domain/intent.py
from domain.intent import Intent, IntentType  

engine = IntentEngine()
result = engine.detect("Show running processes")
print(result)