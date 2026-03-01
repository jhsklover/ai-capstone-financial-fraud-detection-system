# Financial Fraud Detection System

## Team Members
| Name | Role/Component | GitHub Username | 
|------|---------------|-----------------| 
| Jack Sklover | Transaction Ingestion | @jacksklover | 
| Joshua Maldonado | Anomaly Detection | @joshuam0506 | 
| Tejbir Singh | Case Management | @[username] | 
| Jack Sklover | Dashboard | @jacksklover | 

## Problem Statement 
With the access to the Internet and digital banking being at an all-time high, financial companies are receiving a constant influx of transactions, which impedes their ability to properly detect and manage fraudulent activity. The potential of misdiagnosing a non-suspicious action such as a large withdrawal or purchase is an issue, which sometimes wrongly blocks innocent account holders instead of detecting those who are committing fraudulent acts. To combat this, a system which can reliably detect financial fraud and target those who commit fraud is exceedlingly important so that suspicious behavior can actively be distinguished from non-fraudulent activity; this will not only help the accuracy, but will also instill trust with users of these financial services as the actual fraud will be targeted. 

## Target Users 
The main users that will benefit form this system are fraud investigators, financial analysts, and security teams working within banks and digital financial institutions, they will be responsible for many detection in the system like transaction activity, identifying suspicious behavior, and managing fraud investigations, using this system will be beneficial because it will be able to detect potentially fraudulent transactions, reduce false positives, and improve the efficiency in fraud detection. The financial intuitions will benefit because it will protect the assets and money of a lot of their own customers, making the bank more trustworthy by creating a safe system.

## Architecture 
![Architecture Diagram](docs/architecture.png) 

## Component Breakdown 
### Component 1: Transaction Ingestion 
Owner: Jack Sklover 
- **Description:** n8n workflow parsing transaction feeds, account activity, and data normalization
- **Tools:** n8n, Airtable
- **Input:** The input will be raw transaction data that includes fields such as: timestamps, transaction amount and currency type, account holder name/ID, type of transaction, payment recipient, and short description if applicable. The raw data will be stored in a CSV file.
- **Output:** The output will result in Airtable records that are organized into a table displaying transactions, with each field being mapped from the raw data into a normalized schema. The n8n workflow that is created will accurately ingest, parse, and transport the data into Airtable.
- **Standalone demo:** A sample CSV file will be uploaded into n8n which demonstrates how the data is ingested. Then, the workflow will display how the raw data is parsed into streamlined and normalized data, which will then be transported into Airtable. Before and after comparisons will be provided to show how the workflow takes raw data and transforms it into the Airtable dataset.
### Component 2: Anomaly Detection 
Owner: Joshua Maldonado
- **Description:** Pattern analysis on transaction amounts, frequency, and categories and LLM-powered explanation generation
- **Tools:** n8n, Groq, Hugging Face
- **Input:** [What data it receives]
- **Output:** [What data it produces]
- **Standalone demo:** [How this component can be demonstrated independently] 
### Component 3: Case Management
Owner: Tejbir Singh
- **Description:** n8n workflow creating investigation cases with risk scores and escalation rules based on thresholds
- **Tools:** n8n, Airtable
- **Input:** [What data it receives]
- **Output:** [What data it produces]
- **Standalone demo:** [How this component can be demonstrated independently] 
### Component 4: Dashboard 
Owner: Jack Sklover
- **Description:** Streamlit app showing fraud alerts, investigation queue, and trend analytics with drill-down
- **Tools:** Streamlit
- **Input:** The dashboard component will receive the structured tables from the three previous components, including fraud alerts from the anomaly detection workflow, case management data, and transaction history; this data will be sourced from Airtable, and APIs used during the prior parts of the project.
- **Output:** The data will be displayed visually in a dashboard encompassing all of the data, with features such as graphs and charts to show trends, risk scores, and where most fraudulent alerts occur in terms of transaction statistics; Streamlit will also compute metrics. UI elements will be included like dropdowns, buttons, et cetera to enhance the UI/UX of the dashboard. The Streamlit dashboard will act as a webpage.
- **Standalone demo:** To display how this component works, CSVs for the prior three components' datasets with fixed data can be loaded into the dashboard, where then the dashboard renders the data. The dashboard can then be ran, where the data can be displayed and interacted with to show its full functionality.

## Data Sources
- **Primary data:** Transaction records with fields such as timestamp, amount, type, account ID/holder name, description, sourced from CSV uploads and webhook feeds. Outputs from anomaly detection and case management records will also be primary data.
- **Sample data:** Randomized sample data for transactions, and mock anomaly alerts and case records; these can either be written from scratch or randomly generated.
- **Data format:** CSV, JSON, Airtable tables.

## AI Capabilities 
2026-02-23
| Capability | Purpose | Model/API | 
|-----------|---------|-----------| 
| [e.g., Text Classification] | [e.g., Classify alert severity] | [e.g., Hugging 
Face distilbert] | 
| [e.g., Summarization] | [e.g., Summarize incident reports] | [e.g., Groq LLaMA] 
| 
## Success Criteria
1. [Measurable criterion, e.g., "System correctly classifies 8 out of 10 test 
alerts"] 
2. [Measurable criterion, e.g., "Data pipeline processes all records within 2 
minutes"] 
3. [Measurable criterion, e.g., "Dashboard displays all enriched records with 
filtering"] 
4. [Measurable criterion, e.g., "All 4 components integrate and exchange data 
correctly"] 
5 / 17
week-03-lab-instructions.md
5. [Measurable criterion, e.g., "Each component has its own README with setup 
instructions"] 
## Timeline 
| Week | Milestone | 
|------|-----------| 
| 3 (Now) | Project proposal + architecture diagram + GitHub repo | 
| 4-6 | Build individual components, test with sample data | 
| 7-9 | Add LLM/agent capabilities, refine AI processing | 
| 10-12 | Integration, error handling, dashboard/UI | 
| 13-14 | Polish, documentation, demo preparation | 
| 15 | Final presentation | 
