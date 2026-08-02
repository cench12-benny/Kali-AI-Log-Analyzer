import os
import pandas as pd

print("========================================")
print("RUNNING KALI LOG ANALYZER ENGINE")
print("========================================")

# This forces Python to look inside the exact folder where this script lives
current_folder = os.path.dirname(os.path.abspath(__file__))
target_file = os.path.join(current_folder, "network_logs.csv")

try:
    # 1. Load the network dataset cleanly
    df = pd.read_csv(target_file)

    # 2. Display the data structure
    print("\n[+] Structured Network Log Matrix Data:")
    print(df.to_string(index=False))

    # 3. Cybersecurity Status Check
    print("\n[+] Scanning Interface Status...")
    for index, row in df.iterrows():
        interface = row['Interface Name']
        ip_addr = row['IP Address']
        status = row['Status']
        
        if str(status).strip().upper() == 'UP':
            print(f"   ALERT WARNING: Interface [{interface}] is active on IP {ip_addr}!")
        else:
            print(f"   STATUS SAFE: Interface [{interface}] is offline or hidden.")

except FileNotFoundError:
    print(f"\nERROR: Could not find 'network_logs.csv' in this folder.")
    print(f"Expected Location: {target_file}")
    print("\nFIX: Please make sure your 'network_logs.csv' file from Excel is sitting right next to this script on your left sidebar!")

print("========================================")
