from flask import Flask, jsonify, request
from flask_cors import CORS

from agents.coordinator_agent import CoordinatorAgent


app = Flask(__name__)

CORS(app)


# Initialize Coordinator Agent
coordinator = CoordinatorAgent()



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


    result = coordinator.respond(
        user_message
    )


    return jsonify(
        result
    )



if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )