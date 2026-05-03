# Checkpoint 2 Results

**Date:** 2026/05/02

**Team:** Jack Sklover, Joshua Maldonado & Tejbir Singh

**Test record:** A test record depicting a financial transaction. This included that the transaction was a transfer, the IDs of the sender, receiver, and transaction, the timestamp, and the amount.

## End-to-End Status: PARTIAL
## Component-by-Component Results
### Ingestion
- **Status:** Working
- **What happened:** The test record successfully made it into Airtable, with all of the columns being correctly matched.
- **Screenshot:** `screenshots/successful-ingestion-test.png`
### AI Core
- **Status:** Not Working
- **What happened:** It has not been started.
- **Screenshot:** N/A. The component does not exist.
### Specialist
- **Status:** Not Working
- **What happened:** It has not been started.
- **Screenshot:** N/A. The component does not exist.
### Integration Dashboard
- **Status:** Working
- **What happened:** The dashboard correctly displayed the test record, alongside insights such as the total transactions (1), how many high risk alerts there were, the average anomaly score, and raw data analysis.
- **Screenshot:** `screenshots/successful-dashboard-test.png`
## Gaps Found
- The AI Core and Specialist parts, anomaly detection (Joshua) and case management (Tejbir) are incomplete and therefore the entire workflow cannot be tested in tandem. These would need to be completed to run a fully complete test.
## Fix Plan
1. Joshua - Create the Anomaly Detection workflow and test it to ensure that it correctly works.
2. Tejbir - Create the Case Management workflow and test it to ensure that it correctly works.
3. Jack - Update the Dashboard component to reflect more of the data provided by Joshua and Tejbir's components.
