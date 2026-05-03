## Checkpoint 2 Readiness Assessment

### Status: 🔴 AT RISK
**Reasoning:** While the "Bookends" (Ingestion and Dashboard) are functional, the lack of an **AI Core** and **Specialist** component means the mandatory "end-to-end flow" cannot be demonstrated. Currently, data enters the system but does not move through the analytical pipeline.

---

### What's Working
- **Ingestion (Component 1):** Python/n8n script successfully pushes raw transaction data to Airtable.
- **Integration/Dashboard (Component 4):** Streamlit dashboard is built, connected to Airtable, and rendering metrics.
- **Database Connectivity:** Real-time reading from Airtable to the Dashboard is confirmed.

---

### Critical Gaps (must fix before Checkpoint 2)
- **Automated Data Processing:** Records currently sit in Airtable with no analysis or status updates.
    - **Action Item:** Create a "Pass-Through" workflow in n8n that triggers on a new Airtable record and populates the `anomaly_score`.
    - **Owner:** AI Core Lead.
- **Handoff Logic:** There is no automated trigger to signal the Specialist component to act once the AI Core is finished.
    - **Action Item:** Configure n8n to "watch" for a specific status change (e.g., `status` = "Analyzed") to trigger the next node.
    - **Owner:** Specialist Lead.
- **End-to-End Automation:** The system requires manual intervention to bridge the middle components.
    - **Action Item:** Chain all 4 components into a single n8n execution flow.
    - **Owner:** Integration Lead.

---

### Schema Issues Found
- **Missing Handoff Triggers:** The `status` field lacks standardized values required for n8n filters.
    - **Change:** Standardize `status` field values to: `New`, `In_Progress`, `Flagged`, and `Resolved`.
- **Field Name Mismatches:** The Dashboard expects `anomaly_score` and `explanation`, but these columns are not yet consistently populated or named in the shared table.
    - **Change:** Add/Rename fields to exactly `anomaly_score` (Number) and `explanation` (Long Text) in the primary Airtable view.

---

### Recommended Fix Order
1. **Standardize Schema (15 mins):** Update Airtable columns to match the Dashboard's expected field names (`anomaly_score`, `explanation`) and add the `status` dropdown options.
2. **Setup "Mock" AI Node (45 mins):** Create an n8n node that triggers on "New" records and writes a random value to `anomaly_score`. This simulates the AI Core so you have a flow to show.
3. **Link Specialist Logic (30 mins):** Create a second n8n node that takes any record with a score > 0.7 and writes a generic string to the `explanation` field. 
4. **Final Dashboard Filter (15 mins):** Update the Streamlit `dataframe` and `metric` calls to filter specifically for records where `status` is "Flagged" or "Resolved."

---

### Test Data Gaps
- **Low-Risk Baseline:** Need a transaction that should naturally result in a low score to verify the "Green" risk level logic.
    - **Example:** `TXN-2001`, Amount: `12.50`, Description: `Subscription Payment`, Expected Score: `0.10`.
- **High-Value Edge Case:** A very large transaction that should trigger an "Amount" based anomaly.
    - **Example:** `TXN-2002`, Amount: `15000.00`, Description: `International Transfer`, Expected Score: `0.95`.
- **Incomplete Data:** A record missing a `description` to test the system's resilience to "Bad Data."
    - **Example:** `TXN-2003`, Amount: `50.00`, Description: `NULL`, Expected Score: `0.50`.
