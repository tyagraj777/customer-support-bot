## Smart-Customer-Support-Bot-with-Escalation
Smart Customer Support Bot with Escalation   A cloud-native chatbot built with FastAPI, Dialogflow CX, and Salesforce API integration. The bot handles basic customer queries using an FAQ knowledge base and escalates complex issues to human agents, automatically logging structured case details in Salesforce.

##  Smart Customer Support Bot with Escalation

##  Project Concept
This project implements a **cloud-native chatbot** that:
- Handles **basic customer queries** (FAQs, case status, troubleshooting).
- Escalates **complex queries** to human agents.
- Logs structured information (customer ID, issue summary, urgency) into a **Salesforce Case record** before escalation.
- Demonstrates integration of **ML/NLP, cloud deployment, and enterprise CRM systems**.

---

##  Architecture Overview
```mermaid
flowchart TD
    A[User] --> B[Chatbot UI]
    B --> C[Backend (FastAPI)]
    C --> D[Intent Detection (Vertex AI or Dialogflow CX)]
    C --> E[FAQ Lookup (JSON/Firestore)]
    C --> F[Escalation Workflow]
    F --> G[Salesforce API - Case Logging]
    C --> H[Cloud Run Deployment]
    H --> I[CI/CD via GitHub Actions]
---

## Repository Structure
customer-support-bot/
├── frontend/
│   ├── index.html          # Chat UI
│   └── chatbot.js          # Sends queries to backend (Cloud Run URL needed)
├── backend/
│   ├── main.py             # FastAPI app entrypoint
│   ├── dialogflow_handler.py # Dialogflow CX or Vertex AI intent detection
│   ├── faq_lookup.py       # FAQ keyword-based lookup
│   ├── salesforce_api.py   # Salesforce case logging integration
│   └── escalation_rules.yaml # Rules for escalation
├── docker/
│   ├── Dockerfile          # Container setup
│   └── entrypoint.sh       # Startup script
├── ci-cd/
│   └── deploy.yml          # GitHub Actions workflow for Cloud Run deployment
├── config/
│   ├── faq_dataset.json    # FAQ knowledge base
│   └── intents.json        # Dialogflow CX intents
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore
---

## Setup Instructions
1. Prerequisites
a. GCP account with Cloud Run, Vertex AI or Dialogflow CX, Artifact Registry enabled.
a. Salesforce Developer Org (sandbox) for API integration
c. GitHub repository for CI/CD.
---

## 2. Clone Repo
bash
git clone https://github.com/yourusername/customer-support-bot.git
cd customer-support-bot
---

## 3. Install Dependencies
```bash
pip install -r requirements.txt
4. Configure Environment
a. Dialogflow/Vertex AI: Add project ID and endpoint details in dialogflow_handler.py or vertex_ai_handler.py.
b. Salesforce: Insert Connected App credentials in salesforce_api.py
c. Frontend: Update Cloud Run URL in frontend/chatbot.js
---

5. Containerization
bash
docker build -t support-bot .
docker tag support-bot gcr.io/PROJECT_ID/support-bot
docker push gcr.io/PROJECT_ID/support-bot
6. Deploy to Cloud Run
bash
gcloud run deploy support-bot \
  --image gcr.io/PROJECT_ID/support-bot \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
7. CI/CD Setup
Add GCP service account key as GitHub secret GCP_CREDENTIALS.

GitHub Actions workflow (ci-cd/deploy.yml) automates build & deploy.

🧪 Testing
Open frontend/index.html in browser.

Ask a basic query:

“How do I reset my password?” → Bot answers from FAQ dataset.

Ask a complex query:

“I need a refund for my order.” → Bot escalates, logs case in Salesforce, returns Case ID.

Verify case creation in Salesforce sandbox.
