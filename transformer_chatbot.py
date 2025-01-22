from transformers import AutoModelForCausalLM, AutoTokenizer
import re

model_name = "microsoft/DialoGPT-small"  # Correct model name

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name) #Converts user input into numerical tokens.
transformer_model = AutoModelForCausalLM.from_pretrained(model_name)

#Response with transformer_response
def get_transformer_response(user_message):
    """
    Generates a response using the Hugging Face DialoGPT model.
    """
    context = "You are a helpful assistant. User says: "  # Context guidance
    input_text = context + user_message
    input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")

    output = transformer_model.generate(
        input_ids,
        max_length=50,
        num_return_sequences=1,
        no_repeat_ngram_size=3,
        temperature=0.7,
        top_p=0.9,
    )
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Remove user_message from the beginning of the response if echoed
    if response.lower().startswith(user_message.lower()):
        response = response[len(user_message):].strip()

    return response or "I'm sorry, I couldn't generate a meaningful response."

def clean_message(message):
    """
    Clean the user message by removing unnecessary whitespace, special characters, etc.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", message).strip()