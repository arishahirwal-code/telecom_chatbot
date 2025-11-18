from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from chatbot_logic import get_response

app = Flask(__name__, static_folder="static", static_url_path="/static")
CORS(app)  # Allow frontend to talk to backend

@app.route("/chat", methods=["POST"])
def chat():
    """Receive a message and return chatbot reply as JSON."""
    data = request.get_json()
    user_text = data.get("message", "")
    if not user_text:
        return jsonify({"error": "empty message"}), 400
    reply = get_response(user_text)
    return jsonify({"reply": reply})

@app.route("/")
def index():
    """Serve the main HTML file."""
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(debug=True)

