from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression #Learns patterns between user messages and bot responses.
from chatbot_data import ML_TRAINING_DATA

#Prepare training data
vectorizer = CountVectorizer() #Converts text data (user messages) into numerical format.Used to train the Logistic Regression model.
X = vectorizer.fit_transform(ML_TRAINING_DATA.keys())
y = list(ML_TRAINING_DATA.values())

#Train the ML model
ml_model = LogisticRegression()
ml_model.fit(X, y)

#Response with ml
def get_ml_response(user_message):#
    """
    Predicts the response for the given user message using the trained ML model.
    Takes a user message.
    Transforms it into numerical format using the vectorizer.
    Predicts a response if confidence exceeds 0.8.
    """
    X_test = vectorizer.transform([user_message])
    confidence = max(ml_model.predict_proba(X_test)[0])

    # Log the confidence for debugging
    print(f"ML Confidence for '{user_message}': {confidence}")

    if confidence > 0.6:  # Lower threshold for testing
        return ml_model.predict(X_test)[0]
    return None
