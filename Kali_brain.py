import os
import pandas as pd
from groq import Groq

print("========================================")
print("INITIALIZING KALI AI SECURITY AGENT")
print("========================================")

# 1. Provide your free Groq API key here
GROQ_API_KEY = "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"

# 2. Locate and load your dataset file path
current_folder = os.path.dirname(os.path.abspath(__file__))
target_file = os.path.join(current_folder, "network_logs.csv")

try:
    # 3. Read the data with Pandas
    df = pd.read_csv(target_file)
    data_string = df.to_string(index=False)
    
    # 4. Initialize the free AI connector client
    client = Groq(api_key=GROQ_API_KEY)
    
    print("[+] Packaging network log metrics...")
    print("[+] Querying Kali AI analytics model...")
    
    # 5. Tell the AI exactly how to behave and think
    system_rules = (
        "You are Kali AI, a senior SOC Analyst. Analyze the incoming user network logs matrix. "
        "Explain what interfaces are active, point out any security anomalies, and suggest "
        "the exact technical terminal commands an engineer should run next."
    )
    
    # 6. Send the matrix packet over to the updated active AI model
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Updated active free-tier model id
        messages=[
            {"role": "system", "content": system_rules},
            {"role": "user", "content": f"Review this network log capture data:\n\n{data_string}"}
        ]
    )
    
    # 7. Print the professional security report
    print("\n================ KALI AI REPORT ================")
    print(response.choices[0].message.content)
=
    print("================================================")

except FileNotFoundError:
    print("ERROR: Missing network_logs.csv data file asset.")
except Exception as e:
    print(f"CONNECTION FAILURE: {str(e)}")
