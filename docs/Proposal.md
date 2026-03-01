# Financial Fraud Detection System

## Team Members
| Name | Role/Component | GitHub Username | 
|------|---------------|-----------------| 
| Jack Sklover | Transaction Ingestion | @jacksklover | 
| Joshua Maldonado | Anomaly Detection | @joshuam0506 | 
| Tejbir Singh | Case Management | @Tejbir-S | 
| Jack Sklover | Dashboard | @jacksklover | 

## Problem Statement 
With Internet access and digital banking being at an all-time high as technology evolves, financial companies are receiving a constant influx of transactions, impeding their ability to properly detect and manage fraudulent activity. The potential of misdiagnosing a non-suspicious action such as a large withdrawal or purchase is an issue, which can wrongly block innocent account holders instead of detecting under-the-radar fraudulent acts. To combat these issues, a system that can reliably detect financial fraud and target those who commit fraud is exceedingly important to ensure suspicious behavior can actively be distinguished from non-fraudulent activity; this will not only make the process more accurate, but will also instill trust with users of financial services if fraud is accurately detected.

## Target Users 
The target users for this project will be fraud investigators, financial analysts, and security teams that work within banking and digital financial companies. Those who are responsible for identifying suspicious account activity and mananging fraud investigations will benefit from the system as it grants the ability to detect potentially fraudulent transactions, reduce false positives, and improve efficiency to both accurately and quickly detect financial fraud. Financial institutions also benefit from this system as it protects the assets and money of their customers, thereby instilling trust.

## Architecture 
![Architecture Diagram](architecture.png) 

## Component Breakdown 
### Component 1: Transaction Ingestion 
Owner: Jack Sklover 
- **Description:** n8n workflow that parses transaction feeds and normalizes them, then stores the records in an Airtable transaction base.
- **Tools:** n8n, Airtable
- **Input:** The input will be raw transaction data that includes fields such as timestamps, transaction amount and currency type, account holder name/ID, type of transaction, payment recipient, and short description if applicable. The raw data will be stored in a CSV file.
- **Output:** The output will result in normalized Airtable records that are organized into a table displaying transactions, with each field being mapped from the raw data into a normalized schema. The n8n workflow that is created will accurately ingest, parse, and transport the data into Airtable.
- **Standalone demo:** A sample CSV file will be uploaded into n8n which demonstrates how the data is ingested. Then, the workflow will display how the raw data is parsed into streamlined and normalized data, which will then be transported into Airtable. Before and after comparisons will be provided to show how the workflow takes raw data and transforms it into the Airtable dataset.
### Component 2: Anomaly Detection 
Owner: Joshua Maldonado
- **Description:** The component in this stage will identify unusual financial transactions by making comparisons with each new transaction against the account’s historical behavior, it will detect abnormalities inside of its own system based on things like the amount, transaction frequency, patterns, and timing, the system will assign a risk score and flags, so that way the anomalies detected are those that significantly vary from the user’s normal spending profile.
- **Input:** The input will be normalized transaction records recovered from Airtable, every transaction will include fields like: transaction_id, account_holder_id, timestamp, transaction_amount, transaction_type, merchant or recipient, name, category. This specific part of the component will also access historical transactions from the account to create a baseline of normal activity, showing average spending amount, transaction frequency, and regular purchases.
- **Output:** The output will be a detection of anomaly analysis results for each transaction, this result will include: anomaly_score (numerical value representing level of abnormality), anomaly_flag (Normal or Suspicious), risk_level (Low, Medium, High), anomaly_reason (brief explanation of what triggered the anomaly), these results can and will be stored in Airtable and can be used by other components or analysts to check anything that could possibly be suspicious transactions.
- **Standalone demo:** The demo will use example alerts stored in Airtable with different levels of seriousness, confidence, and descriptions, this system will read each alert and compare it to what is normally expected, the after that if the system detects something that could look unusual or more dangerous than normal, the system will give it a higher abnormality score and mark it as risky, now if it looks normal it will be marked as safe, after the analysis the results will be saved in Airtable, where users can clearly see which alerts are normal and which ones need attention. 
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
- **Input:** The dashboard component will receive the structured tables from the three previous components, including fraud alerts from the anomaly detection workflow, case management data, and transaction history. The data directly comes from the airtable case record database from the previous component, but indirectly stems from all of the prior parts of the project.
- **Output:** The data will be displayed visually in a dashboard encompassing all of the data, with features such as graphs and charts to show trends, risk scores, and where most fraudulent alerts occur in terms of transaction statistics; Streamlit will also compute metrics. UI elements will be included like dropdowns, buttons, et cetera to enhance the UI/UX of the dashboard. The Streamlit dashboard will act as a webpage.
- **Standalone demo:** To display how this component works, CSVs for the prior three components' datasets with fixed data can be loaded into the dashboard, where then the dashboard renders the data. The dashboard can then be ran, where the data can be displayed and interacted with to show its full functionality.

## Data Sources
- **Primary data:** Raw transaction records with fields including timestamp, monetary amount and currency, transaction type, account holder and ID, and a short description. The data will be sourced from CSV file uploads.
- **Sample data:** Similarly to Week 2's lab concerning fraud investigation data, simulated transaction records will be used.
- **Data format:** CSV files, JSON files, Airtable bases. Ultimately, all of the data will end up being displayed in a dashboard using Streamlit.

## AI Capabilities 
| Capability | Purpose | Model/API | 
|-----------|---------|-----------| 
| Transaction Classification | Provides classifications for each transaction; the options being normal, or fraud risk. | Hugging Face dslim/bert-large-NER |
| Anomaly Scoring/Pattern Analysis | Assigns risk scores for each transaction and detects similar patterns. | Groq LLaMA |
| Pattern Analysis and Explanation | Analyzes transaction frequency, amounts, and anomaly categories; readable explanations are LLM-generated. | Groq LLaMA |
| Estimating Confidence | Produces a confidence score for each classification. | Hugging Face/Groq API |

## Success Criteria
1. The ingestion workflow should normalize and store the data for each incoming transaction accurately, and within three minutes of completion.
2. Anomaly detection should correctly flag at least 80 percent of sample transactions that have known anomalies. Hugging Face and Groq API should return classifications as well as confidence scores for 100% of transactions submitted.
3. The Case Record Airtable database should correctly store all anomalies with correct fields.
4. The Streamlit dashboard should display all of the fraud case records and alert records; the data displayed should be accurate, including risk levels and timestamps.
5. To test the end-to-end process, a batch of at least 50 test transactions should be processed successfully through the entire pipeline. Anomalies should be correctly flagged, and data should be accurately represented and stored.

## Timeline 
| Week | Milestone | 
|------|-----------| 
| 3 (Now) | Project proposal + architecture diagram + GitHub repo | 
| 4-6 | Build individual components, test with sample data | 
| 7-9 | Add LLM/agent capabilities, refine AI processing | 
| 10-12 | Integration, error handling, dashboard/UI | 
| 13-14 | Polish, documentation, demo preparation | 
| 15 | Final presentation | 
