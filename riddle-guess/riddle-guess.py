from flask import Flask, request, jsonify
import redis
import os
import json

app = Flask(__name__)

r = redis.StrictRedis(host="redis-service", port=6379, decode_responses=True, db=1)

ans_type = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f"} 

@app.route("/get_riddle", methods=["GET"])
async def get_riddle():
    try:
        riddle = json.loads(r.get("riddle"))
        formatted_response = f"{riddle['statement']}\n"

        for k, v in riddle["choices"].items():
            formatted_response += f"{k}) {v}\n"

        return formatted_response, 200
    except:
        return "Error: Could not return a riddle!\n", 500

@app.route("/send_answer/<string:given_answer>")
async def send_answer(given_answer):
    try:
        riddle_answer = r.get("answer")

        if given_answer == riddle_answer:
            return "You guessed it!\n"
        return "Bad luck! Try again.\n"
    except:
        return "Error: Could not send the answer!\n", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
