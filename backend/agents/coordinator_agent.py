class CoordinatorAgent:

    def __init__(self):
        self.name = "StudentMate Coordinator Agent"


    def route_query(self, user_message):

        message = user_message.lower()


        if (
            "placement" in message
            or "job" in message
            or "interview" in message
            or "resume" in message
            or "dsa" in message
        ):
            return "placement"


        elif (
            "study" in message
            or "schedule" in message
            or "timetable" in message
            or "plan" in message
        ):
            return "planner"


        elif (
            "notes" in message
            or "paper" in message
            or "resource" in message
            or "material" in message
        ):
            return "resource"


        else:
            return "academic"