import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from groq import Groq

print("========================================")
print("LAUNCHING LIVE KALI CYBER-ENGINE DETECTOR")
print("========================================")

# 1. PASTE YOUR FREE GROQ API KEY IN THE QUOTES BELOW
GROQ_API_KEY = "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"

# Hardcoded open ports data collected from your network environment
ports = ["22 (SSH)", "80 (HTTP)", "443 (HTTPS)", "631 (IPP)", "3306 (MySQL)"]
risk_scores = [4.5, 7.5, 2.0, 5.0, 6.8]

# --- TRACK 1: DATA VISUALIZATION GENERATOR ---
print("[+] Generating attack surface telemetry visualization chart...")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 5))
colors = sns.color_palette("OrRd", len(risk_scores))

ax = sns.barplot(x=ports, y=risk_scores, palette=colors, hue=ports, legend=False)
plt.title("Kali Linux System Attack Surface Matrix", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Discovered Network Ports & Operational Services", fontsize=12, labelpad=10)
plt.ylabel("Vulnerability Risk Exposure Index (0 - 10)", fontsize=12, labelpad=10)
plt.ylim(0, 10)

# Add numeric tags to the graph bars
for p in ax.patches:
    ax.annotate(f"{p.get_height()}", (p.get_x() + p.get_width() / 2., p.get_height() + 0.3),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontweight='bold')

current_folder = os.path.dirname(os.path.abspath(__file__))
chart_output_path = os.path.join(current_folder, "attack_surface_chart.png")
plt.tight_layout()
plt.savefig(chart_output_path, dpi=300)
plt.close()
print("[+] SUCCESS: Security chart image saved locally to: attack_surface_chart.png")

# --- TRACK 2: AGENTIC AI TRIAGE LOOP ---
print("\n[+] Initializing live threat assessment connection...")
try:
    client = Groq(api_key=GROQ_API_KEY)
    
    log_summary = "Discovered Open Ports:\n"
    for p, r in zip(ports, risk_scores):
        log_summary += f"- Port {p} with an assigned Vulnerability Risk Index score of {r}/10\n"

    system_rules = (
        "You are Kali AI, a senior incident responder. Review the user open port matrix data. "
        "Point out the riskiest open network vector, explain the danger briefly in universal language, "
        "and suggest the exact mitigation terminal command to protect the machine."
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_rules},
            {"role": "user", "content": log_summary}
        ]
    )

    ai_report = response.choices[0].message.content
    print("\n================ KALI AI RISK EVALUATION ================")
    print(ai_report)
    print("=========================================================")

    # Permanently archive the results
    report_file_path = os.path.join(current_folder, "live_security_report.txt")
    with open(report_file_path, "w", encoding="utf-8") as f:
        f.write(ai_report)
    print(f"\n[+] SUCCESS: Full analysis summary log compiled at: live_security_report.txt")

except Exception as e:
    print(f"CONNECTION FAILURE: {str(e)}")

print("\n========================================")
