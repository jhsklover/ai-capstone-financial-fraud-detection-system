# Prompt Log — Tejbir Singh
**Project:** $niper (Financial Fraud Detecion System)

**Team:** Jack Sklover, Joshua Maldonado, & Tejbir Singh

**My Component:** Case Management

**AI Tools Used:** GitHub Copilot, Airtable, n&n

---
## How to Use This Log
Add an entry for each significant AI interaction:
- Copilot Chat conversations where you asked it to generate, explain, or debug
something
- Moments where Copilot was wrong and you had to fix it (these are the most valuable
entries)
- Cases where you refined a prompt to get a better result
Don't log: every autocomplete of a bracket or variable name.
---
## [2026-05-04] — Case Management Component README Generation
**Prompt:**
> Using the project context from copilot-instructions.md, write a complete README for my Case Management component. Include:
  What it does (2-3 sentences)
  How it connects to other components (inputs and outputs)
  Setup instructions (what accounts/keys are needed, what to configure in n8n/Flowise)
  How to test it (specific steps)
  Known limitations
- **Context:** The only file that was open was the generated instructions by copilot for the project. I was working on lab 7, part 2.4 to get a 
full description of how I can fully understand what it is my component does.
- **Result:** Overview — Clear explanation of what Case Management does as the decision/escalation layer
  Component Architecture — Data flow diagram + input/output contracts with exact field mappings
  Setup Instructions — Step-by-step:
  How to get Groq API key and Airtable token
  How to create the Case Records table in Airtable
  Complete n8n workflow with all 11 nodes (polling, Groq integration, priority computation, escalation logic, audit trail, Airtable write)
  4 Test Scenarios — From synthetic data to edge cases to end-to-end testing
  Known Limitations — Groq rate limits, polling delays, hallucination risks, schema assumptions
  Troubleshooting Guide — Common issues and specific fixes
  Future Enhancements — Ideas for webhooks, Slack integration, ML feedback loops
- **Evaluation:** Yes, it worked with no errors.
- **What I changed:** I have found no need to change anything yet, things may need to be adjusted as I go through the project further.
- **What I learned:** Nothing.
---
## 2025-05-07 — Attempt to Fix Flowise Response Issues
**Prompt:**
> I got an error 400: Bad request - please check your parameters Invalid Chatflow ID Could it have been from the flowise link I used, it was this: https://cloud.flowiseai.com/api/v1/prediction/f9943792-7272-4e4a-801c-46d69ea9a534 \
- **Context:** During my original attempt at constructing the n&n pipeline, connectivity seemed to be okay, however, the Groq AI in Flowise struggled to recognize the prompt. Though information would pass, it would give the basic assitant answer as if no information had been presented.
- **Result:** ChatGPT suggested many potential problem causes (missing nodes, laggy servers, invalid JSON, etc), but no solutions ended up working. 
- **Evaluation:** No, it wasn' accurate as we could never truly identify what was causing the issue.
- **What I changed:** I decided to delete the use of Flowise entirely and integrate strictly through n&n itself.
- **What I learned:** Invisible issues can easily shutdown my entire problem. No mattter what I did, I could never understand what the problem was. However, I was able to form a new workaround rather quickly.
