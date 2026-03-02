import json

# Load FAQ dataset
with open("config/faq_dataset.json", "r") as f:
    faq_data = json.load(f)

def get_faq_answer(user_message: str) -> str:
    """
    Simple keyword-based FAQ lookup.
    """
    user_message = user_message.lower()
    for keyword, answer in faq_data.items():
        if keyword in user_message:
            return answer
    return None
