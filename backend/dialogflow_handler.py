# Handles Dialogflow CX integration
# <-- INPUT NEEDED: Add your GCP project ID and Dialogflow agent details

def detect_intent(text):
    # Placeholder logic
    if "status" in text.lower():
        return "basic_query", 0.9
    else:
        return "complex_query", 0.8
