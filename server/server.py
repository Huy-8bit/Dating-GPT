from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def process_json():
    content = request.json
    if "question" in content:
        question = content["question"]
        # response processing here
        response = {"answer": "hi there"}
    else:
        response = {"error": "invalid request"}
    return jsonify(response)


if __name__ == "__main__":
    app.run()
