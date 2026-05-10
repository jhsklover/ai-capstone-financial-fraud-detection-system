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

## 2025-05-09 — Used Copilot to help me design the error handling and which errors to focus on
**Prompt:**
> How do I accurately handle relevant errors?
- **Context:** The pieces of data present for each alert, valid transaction types and amount formatting.
- **Result:** Copilot helped me to design error handling and pick what errors are the most relevant to mitigate.
- **Evaluation:** It helped me implement the error handling and successfully discard alerts which had invalid amounts or transaction types.
- **What I changed:** I was able to add an "If" node and have the condition being that the transaction type and amount type were valid.
- **What I learned:** How to use the "If" node in n8n.

- ## 2025-05-09 — Used Copilot to inquire about the confidence threshold to use
**Prompt:**
> For financial fraud detection systems, what confidence score should I use as the threshold?
- **Context:** The architecture of the system, such as the case management workflow and anomaly detection workflow.
- **Result:** Copilot assisted me in picking a confidence threshold I was comfortable with, which was 0.8. Using 0.7 would leave way more room for error, and in a system which has to be as accurate as possible, leaving more room for error is unacceptable, prompting us to use 0.8. 
- **Evaluation:** It accurately helped me to be more careful and choose a more optimal threshold.
- **What I changed:** Initially, we planned to use 0.70 as the threshold but changed it to 0.80.
- **What I learned:** Being careful is the best practice to prevent false positives and negatives.

- ## 2025-05-09 — Used Copilot to generate case records which would purposely result in "error"
**Prompt:**
> Can you add test records which will result in an error to my CSV?
- **Context:** What constitutes an error: invalid transaction type and amounts and what is accepted for those fields.
- **Result:** Copilot helped me generate five test records which purposely threw an error.
- **Evaluation:** It helped me to test the error detection functionality.
- **What I changed:** The test records to purposely include errors.
- **What I learned:** Implementing error handling and testing error handling are equally as important.

## 2025-05-09 — Used Copilot to help me create a Kanban view for the pipeline status dashboard view
**Prompt:**
> How do I make a dashboard view to show the differences in pipeline status?
- **Context:** The table I am using, the fields it has, and what statuses are available.
- **Result:** Copilot informed me about Kanban views in Airtable, which displays data in a streamlined format. This helped me show the different pipeline statuses and how many records were present for each of them.
- **Evaluation:** I was pleased with the information on the Kanban feature of Airtable.
- **What I changed:** Adding a Kanban view for statuses in Airtable.
- **What I learned:** About Kanban and the different functionalities in Airtable.

## 2025-05-09 — Used Copilot to help me figure out next steps for the project
**Prompt:**
> What should we do next as a team for this project?
- **Context:** What we've done already and covered in the previous labs, the presentation and video demo aspects.
- **Result:** Copilot gave me a plan for the next couple of weeks on what to get done.
- **Evaluation:** It helped me devise strategies to feel better about the status of the project.
- **What I changed:** Communication with the team to not only work on my parts, but help the other members of the team where needed.
- **What I learned:** How to maximize a short amount of time to get a large workload done and new strategies for teamwork.
