
import os
import pandas as pd
import subprocess

print("========================================")
print("RUNNING KALI LOG ANALYZER WITH RULE ENGINE")
print("========================================")

# 1. Locate and load your dataset file path
current_folder = os.path.dirname(os.path.abspath(__file__))
target_file = os.path.join(current_folder, "network_logs.csv")

try:
    # 2. Ingest data using Pandas
    df = pd.read_csv(target_file)

    print("[+] Ingesting logs matrix...")
    print("[+] Running Network Rule Engine checks...\n")

    # Set up a tracking flag variable to see if any threat was found
    threat_detected = False

    # 3. THE ANALYTICAL RULE ENGINE LOOP
    for index, row in df.iterrows():
        interface = row['Interface Name']
        ip_addr = str(row['IP Address']).strip()
        status = str(row['Status']).strip().upper()
        
        # Check if the interface is online first
        if status == 'UP':
            # RULE 1: Check if the IP address is internal or external
            if ip_addr.startswith('10.') or ip_addr.startswith('192.168.') or ip_addr.startswith('127.'):
                print(f"   [INTERNAL] Interface [{interface}] is online safely on local IP {ip_addr}")
            else:
                print(f"   CRITICAL ALERT: External traffic detected on [{interface}]! Unrecognized IP: {ip_addr}")
                # Flip the tracking variable to True because a hacker IP was spotted!
                threat_detected = True
        else:
            print(f"   [OFFLINE] Interface [{interface}] is currently disabled.")

    # 4. THE AUTOMATED AI CHAIN TRIGGER
    if threat_detected:
        print("\n[!] CRITICAL SYSTEM ACTION TRIGGERED")
        print("[!] Threat detected by Rule Engine. Booting Kali AI Brain script automatically for triage...")
        
        # Locate the exact pathway to your brain file
        brain_script_path = os.path.join(current_folder, "kali_brain.py")
        
        # This forces Python to run your kali_brain.py script right now!
        subprocess.run(["py", brain_script_path])
    else:
        print("\n[+] System Scan complete. No external threats detected. AI triage skipped.")

except FileNotFoundError:
    print("ERROR: Missing network_logs.csv data file asset.")
except Exception as e:
    print(f"ANALYTICS FAILURE: {str(e)}")

print("\n========================================")
