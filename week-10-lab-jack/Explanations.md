**Explanation on Error Handling**: The error I handled was to identify invalid transaction types. In my test records, I have some records with type "purchase", which falls outside of the valid types of transfer, withdraw, payment, and withdrawal. My workflow now mitigates this problem. The amount also has to be valid, for exmaple no commas, or negative values.

**Threshold Value Explanation:** We chose 0.8 as the threshold value because a confidence score of above 0.8 indicates the AI is highly confident, while under 0.8 leaves a lot of room for error -- in a situation such as financial fraud which is high-priority, it is important to investigate alerts even if there is a relatively high confidence score to prevent false positives or negatives.

**Dashboard View -- Errors:** One dashboard view is to filter all of the transactions which came up as errors; this view is for transaction processers to identify non-legit alerts and filter them out quickly.

**Dashboard View -- Pipeline Status**: This view is for fraud investigators to know how many alerts have been analyzed, how many cases have been created, how many are pending and how many are errors to stay on top of the data and identify trends in statuses.
