from domain.execution_plan import ExecutionPlan
from domain.task import Task
from domain.intent import Intent, IntentType


class Planner:

    def create(self, intent: Intent) -> ExecutionPlan:

        plan = ExecutionPlan()

        if intent.type == IntentType.PROCESS:

            plan.tasks.append(
                Task(
                    id="1",
                    description="List running processes"
                )
            )

        return plan