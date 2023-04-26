from flask import Flask, jsonify, request

app = Flask(__name__)

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
        response["choices"] = [
            "Thanks for noticing! I think you're a Gemini because you have quite the wit!",
            "Ah, so you must be a Gemini because you can spot a Taurus from a mile away!",
            "I'm flattered! You must be a Gemini, the sign of intelligence and charm!"
        ]
    else:
        response = {"error": "invalid request"}
    print(response)
    return jsonify(response)

if __name__ == "__main__":
    app.run()
