class AcademicAgent:

    def __init__(self):
        self.name = "Academic Agent"


    def respond(self, query):

        return {
            "agent": self.name,
            "response": (
                "🎓 Academic Agent: I can help you understand subjects, "
                "clear doubts, and improve your learning."
            )
        }