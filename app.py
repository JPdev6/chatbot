from flask import Flask, request, jsonify, render_template, session
from database import log_conversation, collection, analyze_sentiment
from ml_chatbot import get_ml_response
from rule_based import get_rule_based_response
from transformer_chatbot import get_transformer_response, clean_message

# Initialize Flask
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for session handling


# Home route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Chatbot API!"


@app.route("/chat-ui", methods=["GET"])
def chat_ui():
    return render_template("index.html")


# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        if not request.is_json:
            return jsonify({"error": "Invalid content type. Use 'application/json'"}), 400

        data = request.get_json()
        if "message" not in data:
            return jsonify({"error": "Missing 'message' key in JSON payload"}), 400

        room = data.get("room", "default")  # Default room if not specified
        user_message = clean_message(data.get("message", ""))

        # Analyze sentiment
        sentiment = analyze_sentiment(user_message)

        # 1. Rule-Based
        response = get_rule_based_response(user_message)
        if response:
            log_conversation(user_message, response, "rule_based", sentiment, room)
            return jsonify({"reply": response})

        # 2. Machine Learning
        response = get_ml_response(user_message)
        if response:  # Check if ML model provides a confident response
            log_conversation(user_message, response, "ml", sentiment, room)
            return jsonify({"reply": response})

        # 3. Transformers
        response = get_transformer_response(user_message)
        log_conversation(user_message, response, "transformer", sentiment, room)
        return jsonify({"reply": response})

        # Default fallback in case no valid response is generated
        return jsonify({"reply": "I'm sorry, I couldn't generate a meaningful response."})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# History route
@app.route("/history", methods=["GET"])
def history():
    try:
        room = request.args.get("room", "default")
        print(f"Fetching history for room: {room}")  # Debugging log

        # Fetch session history
        session_history = session.get("history", {}).get(room, [])
        print(f"Session History: {session_history}")  # Debugging log

        # Fetch persistent history from MongoDB
        persistent_history = list(collection.find({"room": room}, {"_id": 0}))
        print(f"Persistent History: {persistent_history}")  # Debugging log

        return jsonify({
            "session_history": session_history,
            "persistent_history": persistent_history
        })
    except Exception as e:
        print(f"Error in /history: {str(e)}")  # Debugging log
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Analytics for frequent queries
@app.route("/analytics/frequent", methods=["GET"])
def get_frequent_queries():
    try:
        room = request.args.get("room", "default")
        pipeline = [
            {"$match": {"room": room}},
            {"$group": {"_id": "$user_message", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ]
        frequent_queries = list(collection.aggregate(pipeline))
        return jsonify({"frequent_queries": frequent_queries})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
