RULE_BASED_RESPONSES = {
    "hello": "Hi there!",
    "how are you": "I'm doing great, how can I help you?",
    "bye": "Goodbye! Have a wonderful day!",
    "what's your name": "I'm your friendly chatbot."
}
#Response with Rule_Based_response
def get_rule_based_response(user_message):
    """
    Check if the user message matches a predefined rule.
    Returns the response if a match is found, otherwise None.
    """
    return RULE_BASED_RESPONSES.get(user_message.lower(), None)