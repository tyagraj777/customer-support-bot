from fastapi import FastAPI, Request
from dialogflow_handler import detect_intent
from salesforce_api import log_case
from faq_lookup import get_faq_answer  # <-- NEW import

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_message = body.get("message")

    intent, confidence = detect_intent(user_message)

    if intent == "basic_query" and confidence > 0.7:
        # Use FAQ lookup
        answer = get_faq_answer(user_message)
        if answer:
            reply = answer
        else:
            reply = "I couldn’t find an exact answer, but I’ll escalate this for you."
            case_id = log_case(user_message, "customer123")  # <-- INPUT NEEDED: Replace with real customer ID
            reply += f" Case ID: {case_id}"
    else:
        # Escalation
        case_id = log_case(user_message, "customer123")  # <-- INPUT NEEDED
        reply = f"Your query has been escalated. Case ID: {case_id}"

    return {"reply": reply}
