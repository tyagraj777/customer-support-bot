import requests

# <-- INPUT NEEDED: Add Salesforce Connected App credentials
SALESFORCE_INSTANCE = "https://yourinstance.salesforce.com"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # <-- INPUT NEEDED

def log_case(issue_summary, customer_id):
    payload = {
        "Subject": "Escalated Support Case",
        "Description": issue_summary,
        "Origin": "Chatbot",
        "Status": "New",
        "ContactId": customer_id  # <-- INPUT NEEDED: Replace with real Salesforce Contact ID
    }
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.post(f"{SALESFORCE_INSTANCE}/services/data/vXX.X/sobjects/Case", json=payload, headers=headers)
    if response.status_code == 201:
        return response.json().get("id")
    else:
        return "Error logging case"
