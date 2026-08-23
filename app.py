import os
import pandas as pd
import streamlit as st

# 1. Webpage Title Header
st.set_page_config(page_title="Kali AI Defense Portal", layout="wide")
st.title("🛡️ KALI AI ACTIVE DEFENSE DASHBOARD")
st.markdown("### Real-Time Network Telemetry, Vulnerability Auditing & AI Remediation Loops")
st.text("System Status: Active Monitoring Online")

# 2. Divide the browser screen into two columns side-by-side
col1, col2 = st.columns(2)

current_folder = os.path.dirname(os.path.abspath(__file__))

with col1:
    st.subheader("📋 Ingested System Log Matrix Data")
    # Show your Excel network data table inside the browser screen
    target_file = os.path.join(current_folder, "network_logs.csv")
    if os.path.exists(target_file):
        df = pd.read_csv(target_file)
        st.dataframe(df, use_container_width=True)
    
    st.subheader("📊 Current Attack Surface Density Matrix")
    # Show your security chart inside the browser screen
    chart_path = os.path.join(current_folder, "attack_surface_chart.png")
    if os.path.exists(chart_path):
        st.image(chart_path)

with col2:
    st.subheader("🤖 Live AI Incident Triage Engine Response")
    # Show the security report text your AI wrote inside a warning box
    report_path = os.path.join(current_folder, "live_security_report.txt")
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            report_content = f.read()
        st.info(report_content)
    else:
        st.warning("No triage reports found. Please run your processing scripts first.")

