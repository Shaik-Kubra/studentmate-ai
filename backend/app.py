from flask import Flask, jsonify, request
from flask_cors import CORS


from agents.coordinator_agent import CoordinatorAgent
from agents.academic_agent import AcademicAgent
from agents.placement_agent import PlacementAgent
from agents.planner_agent import PlannerAgent
from agents.resource_agent import ResourceAgent


app = Flask(__name__)

CORS(app)


# Initialize Agents
coordinator = CoordinatorAgent()

academic_agent = AcademicAgent()
placement_agent = PlacementAgent()
planner_agent = PlannerAgent()
resource_agent = ResourceAgent()



@app.route("/", methods=["GET"])
def home():

    return jsonify(
        {
            "message": "StudentMate AI Backend Running 🚀",
            "agents": "active"
        }
    )



@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    user_message = data.get(
        "message",
        ""
    )


    selected_agent = coordinator.route_query(
        user_message
    )


    if selected_agent == "placement":

        response = placement_agent.respond(
            user_message
        )


    elif selected_agent == "planner":

        response = planner_agent.respond(
            user_message
        )


    elif selected_agent == "resource":

        response = resource_agent.respond(
            user_message
        )


    else:

        response = academic_agent.respond(
            user_message
        )


    return jsonify(
        {
            "selected_agent": selected_agent,
            "answer": response
        }
    )



if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )