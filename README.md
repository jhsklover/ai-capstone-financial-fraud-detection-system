# Financial Fraud Detection System

## Problem Statement
With the access to the Internet and digital banking being at an all-time high, financial companies are receiving a constant influx of transactions, which impedes their ability to properly detect and manage fraudulent activity. The potential of misdiagnosing a non-suspicious action such as a large withdrawal or purchase is an issue, which sometimes wrongly blocks innocent account holders instead of detecting those who are committing fraudulent acts. To combat this, a system which can reliably detect financial fraud and target those who commit fraud is exceedlingly important so that suspicious behavior can actively be distinguished from non-fraudulent activity; this will not only help the accuracy, but will also instill trust with users of these financial services as the actual fraud will be targeted.

## Architecture
![Architecture Diagram](docs/architecture.png) 

## Components
- **Transaction Ingestion:** The transactions will be ingested using a n8n workflow that parses transaction feeds and normalizes the data. The data is then sent to Airtable, where a base will accurately represent all of the information.
- **Anomaly Detection:** A pattern analysis will be performed on transaction amounts, frequency, and categories. An n8n workflow will be created to take the data from the transaction ingestion step and process it through Groq/Hugging Face to retrieve analysis on the data, and an LLM-powered explanation.
- **Case Management:** The detected anomalies will then be turned into investigation cases with risk scores and escalation rules via a n8n workflow. The cases will be displayed and organized in Airtable.
- **Dashboard:** Using the created cases, a Streamlit applicaton will be created to display trend analytics, fraud alerts, and the investigation queue. Data will be accurately represented, which can be interacted with by fraud analysts. 

## How to Run
1. Set up required credentials to use Hugging Face, Airtable, and Groq in n8n.
2. Prepare the data by uploading a CSV file with transactions.
3. Run the ingestion workflow to normalize and store transactions.
4. Run anomaly detection and classification to assign risk scores, classifications, and confidence levels.
5. Generate the alerts by flagging potentially fraudulent transactions using AI predictions and fraud detection rules.
6. Manage the cases by storing flagged transactions along with their details into the case management system.
7. Launch the Streamlit dashboard.
8. Perform end-to-end testing using a sample batch.
