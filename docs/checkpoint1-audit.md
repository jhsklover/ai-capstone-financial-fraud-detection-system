## Checkpoint 2 Readiness Assessment

### Status: AT RISK

### What's Working

- Team roles/responsibilities are clarified (Joshua: Anomaly Detection, Tejbir: Case Management, You: Ingestion + Dashboard)
- Project scope and handoff strategy (polling Airtable status fields) are verbally mapped

### Critical Gaps (must fix before Checkpoint 2)

- **No components built yet:** All n8n workflows and dashboard still at 0%
  - *Owner: Everyone (Joshua, Tejbir, You)*
- **No agreed field names or status values:** Schema not aligned across components
  - *Owner: Team (coordinate 15-min meeting to finalize)*
- **No test data/sample transactions:** `transactions.csv` missing or incomplete
  - *Owner: You (create at least 10 sample records)*
- **No Airtable connection verified:** API/config not tested yet
  - *Owner: You (verify as part of building Ingestion)*

### Schema Issues Found

- Field names, status values, and conventions are **NOT agreed or documented**
  - Specific fields in question:
    - `sender_id` vs `senderId`
    - `transaction_type` vs `type`
    - `analysis_status` vs `status` vs `analysisStatus`
    - `anomaly_score` vs `score`
  - Status value inconsistencies (`pending` vs `PENDING` vs `analyzed`)
- *Action:* Create and share a single schema document with the agreed names/values before coding

### Recommended Fix Order

1. Finalize schema (field names, status values) in a team meeting — **Owner: You (start group DM/call)**
2. Create `transactions.csv` with at least 10 records (normal, suspicious, edge/test cases) — **Owner: You**
3. Build & test Transaction Ingestion n8n workflow (CSV → Airtable) with 5 working records — **Owner: You**
4. Joshua starts Anomaly Detection n8n workflow scaffold (even untested) — **Owner: Joshua**
5. Tejbir starts Case Management n8n workflow scaffold (even untested) — **Owner: Tejbir**

### Test Data Gaps

- No sample transaction data currently exists
- **Add these sample records:**

| Record | sender_id | recipient_id | amount | transaction_type | description | analysis_status |
|--------|-----------|--------------|--------|------------------|-------------|-----------------|
| 1 | U1000 | U2000 | 125.00 | transfer | Monthly rent | pending |
| 2 | U1010 | U2020 | 5000.00 | wire | Equipment purchase | pending |
| 3 | U1020 | U2030 | 0 | refund | (empty) | pending |
| 4 | U1040 | U2050 | 20000.00 | loan | High-risk business loan, offshore | pending |
| 5 | U1050 | U999999 | 15000.00 | transfer | Suspicious | pending |
| 6 | U1060 | U2070 | 50.00 | payment | Coffee | pending |
| 7 | U1070 | U2080 | 3000.00 | wire | Invoice #12345 | pending |
| 8 | INVALID | U2090 | abc | transfer | Bad data test | pending |
| 9 | U1080 | (empty) | 500.00 | transfer | Missing recipient | pending |
| 10 | U1090 | U2100 | 100000.00 | wire | Extremely high value transfer | pending |
