# Prompt Log — Jack Sklover
- **Project:** Financial Fraud Detection System
- **Team:** Jack Sklover, Joshua Maldonado & Tejbir Singh
- **My Component:** Transaction Ingestion & Dashboard
- **AI Tools Used:** GitHub Copilot; Airtable --

## How to Use This Log
**Add an entry for each significant AI interaction:**
- Discussed with Copilot the next steps on how to progress with the project, which will start with creating the transaction data.
- Asked Copilot to assist me in creating 20 sample test records to use for the transaction ingestion workflow.

## 2025-05-02 — Generated 20 pieces of sample data
**Prompt:**
> Generate transaction records since that's the starting point.
- **Context:** README.md, Audit to reference necessary fields
- **Result:** Copilot produced 20 test records with when the record was ingested, the transaction amount, recipient and sender IDs, and the transaction types.
- **Evaluation:** Yes, it was accurate and produced 20 records with the correct fields.
- **What I changed:** For me, these records were sufficient to begin the testing phase, so I did not alter them. In the future, I may change them or generate a larger dataset.
- **What I learned:** The project is in trouble as it currently is barely even off the ground. We have to work and get a lot done in the next couple of weeks if we want to survive the course.

## 2025-05-02 — Used Copilot to assess what pieces of data are relevant versus irrelevant
**Prompt:**
> For each transaction, what data should be included or omitted?
- **Context:** README.md which has the outline of what the transactions will look like, as well as the sample CSV created previously.
- **Result:** Copilot suggested that the fields I had planned were effective, but instructed me on how to format the monetary values. The way I had it set up, the money would not have commas, or a "$" at the front.
- **Evaluation:** Copilot's suggestions were helpful and ensured me I was on the right track.
- **What I changed:** I was able to format the data in an effective way, and change the format of money values.
- **What I learned:** What data is the most important for financial records.

## 2025-05-02 — Debugging JavaScript code in the Ingestion component
**Prompt:**
> How do I fix the code so that it correctly identifies fields within the raw data?
- **Context:** The CSV, the code prior to its suggestions.
- **Result:** Copilot identified that I had a syntax error which was preventing the data from being correctly ingested.
- **Evaluation:** It accurately helped me debug my code.
- **What I changed:** Altered the syntax issue (a missing semicolon) and reviewed the field names to determine that they were correct.
- **What I learned:** Instead of just coding, I have to take my time and understand the errors I'm making.

## 2025-05-02 — Re-ran the audit prompt
**Prompt:**
> The audit prompt, used in the previous lab after updated progress
- **Context:** Previous audit and current status of the project
- **Result:** Copilot identified that I was in a better position than beginning, but that there were still gaps within the project that needed to get fixed.
- **Evaluation:** It devised a gameplan to finish the project with the alotted time.
- **What I changed:** Organizational strategies. Instead of just saying "this will get done..." I decided to more actively communicate with my team.
- **What I learned:** To be a leader even when you aren't the "team leader".

## 2025-05-02 — Used Copilot to help me design the Dashboard, as I haven't used Streamlit before
**Prompt:**
> How do I create the Streamlit dashboard and add specs to it?
- **Context:** What data fields are included for each piece of data, and the anomaly detection component. The README.md file since it details the entire architecture.
- **Result:** Copilot helped me understand how Streamlit works and how you create a Python code which can then be ran in Terminal to load a webpage with the dashboard metrics. 
- **Evaluation:** It accurately instructed me on valuable metrics, such as number of anomalies, how to make graphs, and styling aspects.
- **What I changed:** I was able to create the Dashboard and understand the features of it.
- **What I learned:** How Streamlit operates.
