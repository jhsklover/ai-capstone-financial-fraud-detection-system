import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
_env_token = os.getenv("AIRTABLE_TOKEN", "")

# ── Config ───────────────────────────────────────────────────────────────────
INGESTION_BASE  = "appA3QrSBzsMn8Mdp"
INGESTION_TABLE = "tbltjvfUBbabGJZRN"
CASE_BASE       = "appA3QrSBzsMn8Mdp"
CASE_TABLE      = "tblyXehoOh0yXpkPD"

RISK_COLORS = {
    "LOW":      "#86efac",
    "MEDIUM":   "#fcd34d",
    "HIGH":     "#f87171",
    "CRITICAL": "#c084fc"
}

STATUS_COLORS = {
    "pending":      "#94a3b8",
    "analyzed":     "#3b82f6",
    "case_created": "#fcd34d",
    "error":        "#f87171"
}

st.set_page_config(
    page_title="Fraud Monitor",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Styling ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500&family=Geist:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Geist', sans-serif;
    background: #eef0f4;
    color: #1a1d23;
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding: 2.5rem 3rem 5rem;
    max-width: 1440px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #f8f9fb;
    border-right: 1px solid #d1d5db;
}
[data-testid="stSidebar"] .block-container {
    padding: 2rem 1.5rem;
}

/* Page title */
.page-title {
    font-family: 'Geist Mono', monospace;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #4b5563;
    margin-bottom: 0.25rem;
}
.page-subtitle {
    font-size: 1.75rem;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 2.5rem;
    letter-spacing: -0.03em;
}

/* Section labels */
.section-label {
    font-family: 'Geist Mono', monospace;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #6b7280;
    margin: 2.5rem 0 1rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid #d1d5db;
}

/* KPI row */
.kpi-row {
    display: flex;
    gap: 0;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    overflow: hidden;
    background: #ffffff;
    margin-bottom: 2rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.kpi-cell {
    flex: 1;
    padding: 1.2rem 1.5rem;
    border-right: 1px solid #e5e7eb;
    min-width: 0;
}
.kpi-cell:last-child { border-right: none; }
.kpi-label {
    font-family: 'Geist Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #6b7280;
    margin-bottom: 0.4rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.kpi-value {
    font-size: 1.65rem;
    font-weight: 600;
    color: #0f172a;
    letter-spacing: -0.03em;
    line-height: 1;
}
.kpi-value.accent { color: #1d4ed8; }
.kpi-value.warn   { color: #b45309; }
.kpi-value.danger { color: #b91c1c; }

/* Chart containers */
.chart-wrap {
    background: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    padding: 1.25rem 1.25rem 0.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}

/* Alert banner */
.alert-banner {
    background: #fff1f2;
    border: 1px solid #fca5a5;
    border-left: 3px solid #b91c1c;
    border-radius: 4px;
    padding: 0.75rem 1rem;
    font-size: 0.85rem;
    color: #7f1d1d;
    margin-bottom: 1.25rem;
}

/* Sidebar label */
.sidebar-section {
    font-family: 'Geist Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #6b7280;
    margin: 1.5rem 0 0.5rem;
}

/* Streamlit overrides */
div[data-testid="stMetric"] { display: none; }
.stSelectbox label {
    font-size: 0.75rem !important;
    color: #6b7280 !important;
    font-weight: 400 !important;
}
</style>
""", unsafe_allow_html=True)


# ── Airtable fetcher ─────────────────────────────────────────────────────────
def fetch_airtable(token: str, base_id: str, table_id: str) -> pd.DataFrame:
    headers = {"Authorization": f"Bearer {token}"}
    url     = f"https://api.airtable.com/v0/{base_id}/{table_id}"
    records, params = [], {}
    while True:
        resp = requests.get(url, headers=headers, params=params, timeout=15)
        if resp.status_code == 401:
            st.error("Invalid token.")
            return pd.DataFrame()
        if resp.status_code != 200:
            st.error(f"Error {resp.status_code}: {resp.text}")
            return pd.DataFrame()
        data = resp.json()
        for rec in data.get("records", []):
            row = {"record_id": rec["id"], "createdTime": rec.get("createdTime")}
            row.update(rec.get("fields", {}))
            records.append(row)
        offset = data.get("offset")
        if not offset:
            break
        params["offset"] = offset
    return pd.DataFrame(records)


def chart_layout(title=""):
    return dict(
        title=dict(text=title, font=dict(size=12, color="#6b7280", family="Geist Mono"), x=0, xanchor="left"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Geist", color="#374151", size=11),
        margin=dict(t=36, b=8, l=0, r=0),
        showlegend=False,
    )


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="page-title">Fraud Monitor</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div class="sidebar-section">Connection</div>', unsafe_allow_html=True)
    token = st.text_input(
        "Airtable Token",
        value=_env_token,
        type="password",
        placeholder="patXXXXXXXXXXXXXX",
        label_visibility="collapsed"
    )
    st.caption("Airtable → Account → Developer hub → Personal access tokens")
    st.markdown('<div class="sidebar-section">Actions</div>', unsafe_allow_html=True)
    refresh = st.button("Refresh", use_container_width=True)
    st.markdown("---")
    st.markdown('<div class="sidebar-section">Sources</div>', unsafe_allow_html=True)
    st.caption("Transactions table\nFraud Investigation Cases table")


# ── Main ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">Financial Crime</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Fraud Detection</div>', unsafe_allow_html=True)

if not token:
    st.info("Enter your Airtable token in the sidebar to load data.")
    st.stop()

with st.spinner("Loading..."):
    txn_df  = fetch_airtable(token, INGESTION_BASE, INGESTION_TABLE)
    case_df = fetch_airtable(token, CASE_BASE, CASE_TABLE)

if txn_df.empty and case_df.empty:
    st.warning("No data returned. Check your token and table IDs.")
    st.stop()

# Coerce types
if not txn_df.empty:
    for col, typ in [("amount", "numeric"), ("anomaly_score", "numeric"), ("timestamp", "datetime")]:
        if col in txn_df.columns:
            txn_df[col] = (pd.to_numeric(txn_df[col], errors="coerce")
                           if typ == "numeric" else
                           pd.to_datetime(txn_df[col], errors="coerce"))

if not case_df.empty and "confidence_score" in case_df.columns:
    case_df["confidence_score"] = pd.to_numeric(case_df["confidence_score"], errors="coerce")


# ── KPI row ──────────────────────────────────────────────────────────────────
total_txn     = len(txn_df)
flagged       = len(txn_df[txn_df["status"] == "case_created"]) if "status" in txn_df.columns else 0
high_critical = len(txn_df[txn_df["risk_level"].isin(["HIGH","CRITICAL"])]) if "risk_level" in txn_df.columns else 0
avg_score     = txn_df["anomaly_score"].mean() if "anomaly_score" in txn_df.columns else None
open_cases    = len(case_df[case_df["investigation_status"] == "NEW"]) if "investigation_status" in case_df.columns else 0

flag_pct = f"{flagged/total_txn*100:.1f}%" if total_txn else "—"

st.markdown(f"""
<div class="kpi-row">
  <div class="kpi-cell">
    <div class="kpi-label">Transactions</div>
    <div class="kpi-value">{total_txn:,}</div>
  </div>
  <div class="kpi-cell">
    <div class="kpi-label">Flagged</div>
    <div class="kpi-value accent">{flagged:,} <span style="font-size:0.85rem;color:#9ca3af;font-weight:300">{flag_pct}</span></div>
  </div>
  <div class="kpi-cell">
    <div class="kpi-label">High / Critical</div>
    <div class="kpi-value danger">{high_critical:,}</div>
  </div>
  <div class="kpi-cell">
    <div class="kpi-label">Avg Anomaly Score</div>
    <div class="kpi-value">{f"{avg_score:.3f}" if avg_score is not None else "—"}</div>
  </div>
  <div class="kpi-cell">
    <div class="kpi-label">Open Cases</div>
    <div class="kpi-value warn">{open_cases:,}</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Transactions ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Transactions</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    if "risk_level" in txn_df.columns:
        order = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        risk_counts = (txn_df["risk_level"]
                       .value_counts()
                       .reindex(order)
                       .dropna()
                       .reset_index())
        risk_counts.columns = ["risk_level", "count"]
        fig = go.Figure(go.Bar(
            x=risk_counts["risk_level"],
            y=risk_counts["count"],
            marker_color=[RISK_COLORS.get(r, "#94a3b8") for r in risk_counts["risk_level"]],
            text=risk_counts["count"],
            textposition="outside",
            textfont=dict(size=11, family="Geist Mono"),
        ))
        fig.update_layout(**chart_layout("RISK LEVEL"))
        fig.update_xaxes(showgrid=False, tickfont=dict(size=10))
        fig.update_yaxes(showgrid=True, gridcolor="#f3f4f6", zeroline=False)
        st.markdown('<div class="chart-wrap">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.caption("No risk_level data yet.")

with col2:
    if "status" in txn_df.columns:
        status_counts = txn_df["status"].value_counts().reset_index()
        status_counts.columns = ["status", "count"]
        fig = go.Figure(go.Bar(
            x=status_counts["status"],
            y=status_counts["count"],
            marker_color=[STATUS_COLORS.get(s, "#94a3b8") for s in status_counts["status"]],
            text=status_counts["count"],
            textposition="outside",
            textfont=dict(size=11, family="Geist Mono"),
        ))
        fig.update_layout(**chart_layout("STATUS"))
        fig.update_xaxes(showgrid=False, tickfont=dict(size=10))
        fig.update_yaxes(showgrid=True, gridcolor="#f3f4f6", zeroline=False)
        st.markdown('<div class="chart-wrap">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.caption("No status data yet.")

# Scatter
if "anomaly_score" in txn_df.columns and "amount" in txn_df.columns:
    scatter_df = txn_df.dropna(subset=["anomaly_score", "amount"])
    if not scatter_df.empty:
        hover_cols = [c for c in ["transaction_id", "transaction_type", "sender_id", "recipient_id"] if c in scatter_df.columns]
        fig = px.scatter(
            scatter_df,
            x="amount",
            y="anomaly_score",
            color="risk_level" if "risk_level" in scatter_df.columns else None,
            color_discrete_map=RISK_COLORS,
            hover_data=hover_cols or None,
            labels={"amount": "Amount ($)", "anomaly_score": "Anomaly Score"},
            opacity=0.7,
        )
        fig.update_traces(marker=dict(size=6))
        fig.update_layout(**chart_layout("AMOUNT vs ANOMALY SCORE"))
        fig.update_xaxes(showgrid=True, gridcolor="#f3f4f6", zeroline=False)
        fig.update_yaxes(showgrid=True, gridcolor="#f3f4f6", zeroline=False)
        st.markdown('<div class="chart-wrap">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ── Cases ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Case Management</div>', unsafe_allow_html=True)

if case_df.empty:
    st.caption("No case records found. Run the case management workflow first.")
else:
    # Escalated alert
    if "escalation_flag" in case_df.columns:
        escalated = case_df[case_df["escalation_flag"] == True]
        if not escalated.empty:
            st.markdown(
                f'<div class="alert-banner">{len(escalated)} escalated case{"s" if len(escalated) != 1 else ""} require immediate attention.</div>',
                unsafe_allow_html=True
            )

    c1, c2 = st.columns(2, gap="medium")

    with c1:
        if "investigation_status" in case_df.columns:
            inv_counts = case_df["investigation_status"].value_counts().reset_index()
            inv_counts.columns = ["status", "count"]
            fig = go.Figure(go.Bar(
                x=inv_counts["status"],
                y=inv_counts["count"],
                marker_color="#2563eb",
                text=inv_counts["count"],
                textposition="outside",
                textfont=dict(size=11, family="Geist Mono"),
            ))
            fig.update_layout(**chart_layout("INVESTIGATION STATUS"))
            fig.update_xaxes(showgrid=False, tickfont=dict(size=10))
            fig.update_yaxes(showgrid=True, gridcolor="#f3f4f6", zeroline=False)
            st.markdown('<div class="chart-wrap">', unsafe_allow_html=True)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        if "priority_tier" in case_df.columns:
            pri_counts = case_df["priority_tier"].value_counts().reset_index()
            pri_counts.columns = ["priority", "count"]
            fig = go.Figure(go.Bar(
                x=pri_counts["priority"],
                y=pri_counts["count"],
                marker_color=[RISK_COLORS.get(p, "#94a3b8") for p in pri_counts["priority"]],
                text=pri_counts["count"],
                textposition="outside",
                textfont=dict(size=11, family="Geist Mono"),
            ))
            fig.update_layout(**chart_layout("PRIORITY TIER"))
            fig.update_xaxes(showgrid=False, tickfont=dict(size=10))
            fig.update_yaxes(showgrid=True, gridcolor="#f3f4f6", zeroline=False)
            st.markdown('<div class="chart-wrap">', unsafe_allow_html=True)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # Escalated table
    if "escalation_flag" in case_df.columns and not escalated.empty:
        st.markdown('<div class="section-label" style="margin-top:1.5rem">Escalated Cases</div>', unsafe_allow_html=True)
        display_cols = [c for c in [
            "case_id", "transaction_id", "sender_id", "priority_tier",
            "risk_level", "investigation_status", "alert_description"
        ] if c in escalated.columns]
        st.dataframe(escalated[display_cols], use_container_width=True, hide_index=True)


# ── Transaction Explorer ──────────────────────────────────────────────────────
st.markdown('<div class="section-label">Transaction Explorer</div>', unsafe_allow_html=True)

fc1, fc2, fc3 = st.columns(3, gap="medium")
filtered_df = txn_df.copy()

with fc1:
    if "risk_level" in txn_df.columns:
        risk_opts = ["All"] + sorted(txn_df["risk_level"].dropna().unique().tolist())
        sel = st.selectbox("Risk level", risk_opts)
        if sel != "All":
            filtered_df = filtered_df[filtered_df["risk_level"] == sel]

with fc2:
    if "status" in txn_df.columns:
        status_opts = ["All"] + sorted(txn_df["status"].dropna().unique().tolist())
        sel = st.selectbox("Status", status_opts)
        if sel != "All":
            filtered_df = filtered_df[filtered_df["status"] == sel]

with fc3:
    if "transaction_type" in txn_df.columns:
        type_opts = ["All"] + sorted(txn_df["transaction_type"].dropna().unique().tolist())
        sel = st.selectbox("Type", type_opts)
        if sel != "All":
            filtered_df = filtered_df[filtered_df["transaction_type"] == sel]

display_cols = [c for c in [
    "transaction_id", "sender_id", "recipient_id", "amount",
    "transaction_type", "status", "risk_level", "anomaly_score", "anomaly_reason", "timestamp"
] if c in filtered_df.columns]

sort_col = "anomaly_score" if "anomaly_score" in filtered_df.columns else None
st.dataframe(
    filtered_df[display_cols].sort_values(sort_col, ascending=False) if sort_col else filtered_df[display_cols],
    use_container_width=True,
    hide_index=True,
)
st.caption(f"{len(filtered_df):,} of {len(txn_df):,} transactions")
