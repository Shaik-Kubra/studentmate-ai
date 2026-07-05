class PlannerAgent:

    def __init__(self):
        self.name = "Study Planner Agent"


    def respond(self, query):

        return {
            "agent": self.name,
            "response": (
                "📅 Planner Agent: I can create study schedules, "
                "daily goals, and productivity plans."
            )
        }