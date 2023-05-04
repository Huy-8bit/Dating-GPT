from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import random
import process_data
import json

app = Flask(__name__)
CORS(app)


def process_choice(profile1, profile2, sender, history):
    choices = process_data.get_choice(profile1, profile2, sender, history)

    return {"choices": choices}



@app.route('/', methods=['OPTIONS', 'POST'])
@cross_origin()
def handle_request():
    print("check")
    if not request.is_json:
        print(request)
        print("response ERROR Missing JSON data in request ")
        return jsonify({"error": "Missing JSON data in request"}), 400

    content = request.json
    response = {}

    if "profile1" in content and "profile2" in content:
        response["profile1"] = content["profile1"]
        response["profile2"] = content["profile2"]

        if "sender" in content:
            if content["sender"] == "P1":
                response["sender"] = "P2"
            elif content["sender"] == "P2":
                response["sender"] = "P1"
            response["msg_attr"] = content["msg_attr"]

        # Check if content includes chat history
        if "history" in content and isinstance(content["history"], list):
            response["history"] = content["history"]
        else:
            response["history"] = []

        response["choices"] = process_choice(
            content["profile1"], content["profile2"], response["sender"], response["history"]
        )["choices"]

    else:
        print("response ERROR")
        return jsonify({"error": "Invalid request: Missing required fields"}), 400

    print("response SUCCESS")
    return jsonify(response)


if __name__ == '__main__':
    app.run()
