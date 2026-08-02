from application.intent.intent_engine import IntentEngine
from application.planner.planner import Planner
from application.validator.validator import Validator
from application.executor.executor import Executor


engine = IntentEngine()
planner = Planner()
validator = Validator()
executor = Executor()


text = "Show running processes"

print("\nUSER:")
print(text)


intent = engine.detect(text)

print("\nINTENT:")
print(intent)


plan = planner.create(intent)

print("\nPLAN:")

for task in plan.tasks:
    print(f"- {task.description}")


command = ["ps", "aux"]

print("\nCOMMAND:")
print(" ".join(command))


if validator.validate(command):

    print("\nSECURITY:")
    print("Command approved.")

    result = executor.run(command)

    print("\nOUTPUT:")
    print(result.stdout)

    print("\nEXIT CODE:")
    print(result.exit_code)

    print("\nEXECUTION TIME:")
    print(f"{result.duration_ms:.2f} ms")

else:

    print("\nSECURITY:")
    print("Command rejected.")