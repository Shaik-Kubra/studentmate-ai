class PlacementAgent:

    def __init__(self):
        self.name = "Placement Agent"


    def respond(self, query):

        return {
            "agent": self.name,
            "response": (
                "💼 Placement Agent: I can help you prepare DSA, "
                "resume, interviews, and career roadmap."
            )
        }