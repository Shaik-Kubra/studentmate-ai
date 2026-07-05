from services.gemini_service import GeminiService

from agents.academic_agent import AcademicAgent
from agents.placement_agent import PlacementAgent
from agents.planner_agent import PlannerAgent
from agents.resource_agent import ResourceAgent


class CoordinatorAgent:

    def __init__(self):

        self.gemini = GeminiService()

        self.academic = AcademicAgent()
        self.placement = PlacementAgent()
        self.planner = PlannerAgent()
        self.resource = ResourceAgent()


    def choose_agent(self, message):

        msg = message.lower()


        # Fast keyword routing

        if any(word in msg for word in [
            "dsa",
            "coding",
            "interview",
            "resume",
            "placement",
            "job",
            "internship"
        ]):
            return "placement"


        if any(word in msg for word in [
            "timetable",
            "schedule",
            "plan",
            "goal",
            "routine",
            "productivity"
        ]):
            return "planner"


        if any(word in msg for word in [
            "course",
            "book",
            "notes",
            "resources",
            "roadmap",
            "tutorial"
        ]):
            return "resource"



        # Gemini fallback

        prompt = f"""

        Classify this student request.

        Request:
        {message}


        Categories:

        academic
        placement
        planner
        resource


        Reply with only category name.

        """


        result = self.gemini.generate_response(prompt)

        result = result.lower().strip()


        if "placement" in result:
            return "placement"

        if "planner" in result:
            return "planner"

        if "resource" in result:
            return "resource"


        return "academic"



    def respond(self, message):

        selected_agent = self.choose_agent(message)


        if selected_agent == "placement":

            answer = self.placement.respond(message)


        elif selected_agent == "planner":

            answer = self.planner.respond(message)


        elif selected_agent == "resource":

            answer = self.resource.respond(message)


        else:

            answer = self.academic.respond(message)



        return {
            "selected_agent": selected_agent,
            "answer": answer
        }