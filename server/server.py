# from flask import Flask, jsonify, request
# import random
# import process_data
# import json

# app = Flask(__name__)


# def process_choice(profile1, profile2, sender,history):
#     choices = process_data.get_choice(profile1, profile2, sender,history)
#     return {"choices": choices}



# @app.route("/", methods=["POST"])
# def process_json():
#     content = request.json
#     response = {}
    
#     if "profile1" in content and "profile2" in content:
#         response["profile1"] = content["profile1"]
#         response["profile2"] = content["profile2"]
#         if "sender" in content:
#             if content["sender"] == "P1":
#                 response["sender"] = "P2"
#             elif content["sender"] == "P2":
#                 response["sender"] = "P1"
#             response["msg_attr"] = content["msg_attr"]
        
                
#         # Check if content includes chat history
#         if "history" in content and isinstance(content["history"], list):
#             response["history"] = content["history"]
#         else:
#             response["history"] = []
            
#         response["choices"] = process_choice(content["profile1"],content["profile2"], response["sender"],response["history"])["choices"]
  
#     else:
#         response = {"error": "invalid request"}

#     return jsonify(response)

# if __name__ == "__main__":
#     app.run()


from flask import Flask, jsonify, request
import random
import process_data
import json

app = Flask(__name__)


def process_choice(profile1, profile2, sender, history):
    choices = process_data.get_choice(profile1, profile2, sender, history)
    return {"choices": choices}


@app.route("/getchoice", methods=["POST"])
def process_json():
    if not request.is_json:
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
        return jsonify({"error": "Invalid request: Missing required fields"}), 400

    return jsonify(response)


if __name__ == "__main__":
    app.run()
