from datetime import datetime

from pymongo import MongoClient
from textblob import TextBlob

try:
    client = MongoClient("mongodb://mongo:27017/chatbot")
    db = client.chatbot_db
    collection = db.conversations
    print("Connected to MongoDB successfully.")
except Exception as e:
    print("Error connecting to MongoDB: {e}")


def log_conversation(user_message, bot_response, message_type, sentiment, room):
    """
    Logs the conversation to MongoDB.
    """
    conversation = {
        "user_message": user_message,
        "bot_response": bot_response,
        "message_type": message_type,
        "sentiment": sentiment,
        "room": room,
        "timestamp": datetime.now()
    }
    collection.insert_one(conversation)


def analyze_sentiment(user_message):
    """
    Analyzes the sentiment of a user message.
    """
    blob = TextBlob(user_message)
    return {
        "polarity": blob.sentiment.polarity,  # Range: -1 (negative) to 1 (positive)
        "subjectivity": blob.sentiment.subjectivity  # Range: 0 (objective) to 1 (subjective)
    }
