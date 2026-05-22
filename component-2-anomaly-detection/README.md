# Anomaly Detection
Owner: Joshua Maldonado

## Description
This component analyzes financial transactions to detect suspicious or fraudulent activity.
It uses AI models to identify unusual transaction patterns.

## Tools
- n8n
- Groq

## Input
The transaction data that was processed by the ingestion workflow. This excludes all transactions marked as "error" by the ingestion workflow.

## Output
Anomaly score, risk level, anomaly reasoning, and confidence score.

## Standalone demo
