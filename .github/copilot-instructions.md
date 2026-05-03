# Capstone Project Context
## Project
- **Name:** Financial Fraud Detection System
- **Team:** Jack Sklover (Transaction Ingestion & Dashboard), Joshua Maldonado (Anomaly Detection), Tejbir Singh (Case Management)
- **What it does:** Raw sample transaction records in CSV format enter the transaction ingestion workflow in n8n, which are the normalized and sent into an Airtable transaction database. The records stored in Airtable then go into the anomaly detection workflow in n8n, which are then assessed via Hugging Face API and Groq, which gives each transaction anomaly scores. These are then passed into the case management n8n workflow, which will create fraud investigation case records and send them to Airtable. The alerts and case records are sent into a Streamlit dashboard, where fraud analysts can then review the data and alerts.
- **Project type:** Financial fraud detection system. Detects fraudulent transactions and suspicious actions.
## Architecture
- **Ingestion:** n8n will receive sample transactions which are stored in a CSV and then parse them to transmit them into an Airtable transaction database.
- **AI Core:** Via the anomaly detection n8n workflow, the transaction records will be analyzed using Hugging Face sentiment analysis and Groq API will provide its in-depth analysis on the trends found in the transactions and why they seem fraudulent or non-fraudulent.
- **Specialist:** n8n workflow creates alert records based on the records with high anomaly scores.
- **Integration:** Each component builds off the previous. So the anomaly detection workflow uses the Airtable base created by the transaction ingestion portion. The case management workflow uses the anomaly scores to create an Airtable base with the records, which then are used by the Dashboard.
## Tech Stack
- n8n Cloud (workflow automation)
- Groq API (LLM inference — llama-3.3-70b-versatile)
- Hugging Face Inference API (sentiment analysis, NER, zero-shot classification)
- Airtable (shared database — [2] tables)
- GitHub (repo, documentation, portfolio)
- Streamlit (dashboard)
## Airtable Schema
[Paste your actual table and field names here. This is the most valuable context you 
can give.]
### Transaction Records 
| Field | Type | Written By | Status Values |
|-------|------|-----------|---------------|
| transaction_id | Single-line text | Transaction Ingestion | ... |
| timestamp | Date | Transaction Ingestion | ... |
| sender_id | Single-line text | Transaction Ingestion | ... |
| amount | Number | Transaction Ingestion | ... |
| transaction_type | Single line text | Transaction Ingestion | ... |
| description | Long text | Transaction Ingestion | ... |
| status | Single select | Transaction Ingestion | pending, analyzed, case_created |
### Fraud Investigation Case Records
| Field | Type | Written By | Status Values |
|-------|------|-----------|---------------|
| sender_id | Single line text | Case Management | ... |
| recipient_id | Single line text | Case Management | ... |
| alert_description | Long text | Case Management | ... |
| confidence_score | Number | Case Management | ... |
| risk_level | Single-select | Case Management | low, medium, high, critical |
| investigation_status | Single-select | Case Management | new, in_progress, resolved, dismissed |
## Conventions
- Field names: snake_case
- Status values: lowercase
- Date fields end in _at- Boolean fields use is_ prefix

## Current State
- **What's working:** Transaction Ingestion workflow and Streamlit Dashboard
- **What's in progress:** Case Management and Anomaly Detection being developed currently
- **Known issues:** Full pipeline cannot be tested due to the incompleteness of the Case Management and Anomaly Detection workflows
- **Next milestone:** Checkpoint 3 (Week 10) - All components completed and we can test more records 
## Repository Structure
.
└── ai-capstone-financial-fraud-detection-system/

    ├── component-1-transaction-ingestion/
    │   ├── transaction-ingestion.json
    │   └── README.md
    ├── component-2-anomaly-detection/
    │   ├── anomaly-detection.json
    │   └── README.md
    ├── component-3-case-management/
    │   ├── case-management.json
    │   └── README.md
    ├── component-4-dashboard/
    │   └── README.md
    ├── data/
    │   ├── transactions.csv
    │   ├── alert_records.csv
    │   └── README.md
    ├── docs/
    │   ├── Proposal.md
    │   └── architecture.png
    ├── screenshots/
    ├── .gitignore
    └── README.md
