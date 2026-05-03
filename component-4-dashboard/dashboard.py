import streamlit
import pandas
import plotly.express

streamlit.set_page_config(page_title="Financial Fraud Analysis Dashboard", layout="wide")

streamlit.title("Fraud Detection and Risk Analysis")
streamlit.markdown("---")

# Data

raw_data = [
    {"transaction_id": "TXN-0001", "anomaly_score": 0.88, "risk_level": "High", "explanation": "Duplicate transaction detected"}
]

df = pandas.DataFrame(raw_data)

high_risk_alerts = len(df[df['risk_level'] == 'High'])
average_anomaly = df['anomaly_score'].mean()

m1, m2, m3 = streamlit.columns(3)
m1.metric("Total Transactions Analyzed", len(df))
m2.metric("High Risk Alerts", high_risk_alerts, delta="Critical", delta_color="inverse")
m3.metric("Avg Anomaly Score", f"{average_anomaly:.2f}")

streamlit.markdown("---")

# 4. Two-Column Layout for Visuals
col1, col2 = streamlit.columns([2, 1])

with col1:
    streamlit.subheader("Anomaly Score Distribution")
    # Creating a simple bar chart for scores
    fig = plotly.express.bar(df, x="transaction_id", y="anomaly_score", 
                 color="risk_level", 
                 color_discrete_map={"High": "#EF553B", "Medium": "#FECB52", "Low": "#00CC96"},
                 title="Risk Level by Transaction")
    streamlit.plotly_chart(fig, use_container_width=True)

with col2:
    streamlit.subheader("Quick Insights")
    # Filter for only High Risk to show as warnings
    high_df = df[df['risk_level'] == "High"]
    for _, row in high_df.iterrows():
        streamlit.error(f"**{row['transaction_id']}**\n\n{row['explanation']}")

# 5. Full Data Table
streamlit.subheader("Raw Analysis Data")
streamlit.dataframe(df, use_container_width=True)