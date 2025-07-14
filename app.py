from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/assess", methods=["POST"])
def assess():
    data = request.get_json()
    questions = ["q1", "q2", "q3", "q4", "q5", "q6"]
    score = sum(1 for q in questions if data.get(q) == "yes")
    result = "⚠️ You may be experiencing symptoms. Please consult a mental health professional." if score >= 3 else "✅ You are not currently showing strong signs of psychosis."
    return jsonify({"score": score, "result": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
