class ResourceAgent:

    def __init__(self):
        self.name = "Resource Agent"


    def respond(self, query):

        return {
            "agent": self.name,
            "response": (
                "📚 Resource Agent: I can recommend notes, "
                "courses, books, and learning resources."
            )
        }