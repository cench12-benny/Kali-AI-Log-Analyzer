import os
import pandas as pd
from groq import Groq

print("========================================")
print("ACTIVATING PROACTIVE AI THREAT MONITOR")
print("========================================")

# 1. Provide your free Groq API key here
GROQ_API_KEY = "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"

current_folder = os.path.dirname(os.path.abspath(__file__))
target_file = os.path.join(current_folder, "network_logs.csv")

try:
    # 2. Ingest background telemetry data
    df = pd.read_csv(target_file)
    threats_found = []

    print("[+] Scanning background network matrix for hidden vulnerabilities...")
    
    # 3. ADVANCED ALGORITHMIC ANOMALY SORTING (Catches hidden vectors)
    for index, row in df.iterrows():
        interface = row['Interface Name']
        ip_addr = str(row['IP Address']).strip()
        status = str(row['Status']).strip().upper()
        
        # Rule check: Detect active, unauthorized external network channels
        if status == 'UP':
            if not (ip_addr.startswith('10.') or ip_addr.startswith('192.168.') or ip_addr.startswith('127.')):
                # If an external IP is live on an internal system interface, it's a critical anomaly!
                threats_found.append(f"Interface: {interface} | Unauthorized External IP: {ip_addr}")

    # 4. PROACTIVE RESPONSE ALARM CORES
    if threats_found:
        print("\n!!! CRITICAL SECURITY ANOMALY DETECTED !!!")
        print("[!] Human analysts would likely miss this hidden configuration drift.")
        print("[!] Activating autonomous AI remediation protocol...")
        
        # Package threat data string
        threat_payload = "\n".join(threats_found)
        
        # Query AI to build an immediate emergency containment script
        client = Groq(api_key=GROQ_API_KEY)
        system_rules = (
            "You are Kali AI, an autonomous defense system. A critical hidden network anomaly "
            "has been discovered. Write a short, severe alert summary detailing the immediate danger "
            "and specify the exact protective firewall rule command to run to cut off this attacker."
        )
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_rules},
                {"role": "user", "content": f"CRITICAL INCIDENT DETECTED VIA LOG PARSING:\n\n{threat_payload}"}
            ]
        )
        
        ai_alert_payload = response.choices.message.content
        
        print("\n================ SYSTEM PUSH NOTIFICATION ALERT ================")
        print(ai_alert_payload)
        print("==================================================================")
        
        # Update our active log file so the browser dashboard flashes the update live!
        report_file_path = os.path.join(current_folder, "live_security_report.txt")
        with open(report_file_path, "w", encoding="utf-8") as f:
            f.write(f"⚠️ SECURITY BREACH DETECTION VECTOR ALERT:\n\n{ai_alert_payload}")
            
        # EXTRA AGENTIC STEP: This is where we plug in an email sender function!
        print("\n[+] SUCCESS: Push notification payload compiled.")
        
    else:
        print("[+] Scan complete. All background parameters match normal baseline patterns.")
        # Clear old alerts if the system is safe again
        report_file_path = os.path.join(current_folder, "live_security_report.txt")
        with open(report_file_path, "w", encoding="utf-8") as f:
            f.write("System Status Nominal. No active network anomalies detected.")

except Exception as e:
    print(f"MONITOR SYSTEM CRASH DETECTED: {str(e)}")

print("\n========================================")
