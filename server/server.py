from flask import Flask, jsonify, request
import random
import process_data

app = Flask(__name__)

def process_choice(profile1, profile2):
    choices = process_data.get_choice(profile1, profile2)
    return {"choices": choices}


@app.route("/", methods=["POST"])
def process_json():
    content = request.json
    response = {}
    if "profile1" in content and "profile2" in content:
        response["profile1"] = content["profile1"]
        response["profile2"] = content["profile2"]
        response["sender"] = "P2"
        response["msg_attr"] = ["creative", "witty", "teasing", "funny"]
        response["history"] = [{"sender": "P1", "msg": "Hey there, you must be Taurus because you’re the only 10 out of 10 I see!"}]
        response["choices"] = process_choice(content["profile1"],content["profile2"])["choices"]
    else:
        response = {"error": "invalid request"}
    return jsonify(response)

if __name__ == "__main__":
    app.run()
