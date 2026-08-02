# Autonomous Kali AI Network Log Analyzer & Orchestration Pipeline (SOAR)

A hybrid project combining programmatic Data Analytics and automated Cybersecurity Operations to build an autonomous event triage system. This system acts as a digital first responder, mimicking the data pipeline and incident response responsibilities of a Tier-1 SOC Analyst.

## 🚀 System Architecture & Operational Blueprint
The application engine is divided into three decoupled layers that execute dynamically based on host data file modifications:

1. **Automated Event Detection (`watcher.py`)**: Utilizes low-overhead file system tracking hooks (`watchdog`) to constantly monitor specific network log data dumps for real-time change vectors without system resource draining.
2. **Algorithmic Rule Sorting Engine (`analyzer.py`)**: Ingests messy, unstructured matrix formats programmatically into a structured **Pandas DataFrame**. It executes string-matching condition logic loops to divide traffic and isolate malicious foreign IP nodes from standard internal segments.
3. **AI Incident Response Triage (`kali_brain.py`)**: Orchestrates context injections through high-velocity pipelines straight to specialized open-source LLM reasoning models via **Groq** APIs. It produces immediate technical remediation playbooks and saves structural artifacts locally to text logs.

## 🛠️ Technical Stack & Framework Foundations
- **Primary Language**: Python 3.14+
- **Data Engineering**: Pandas, NumPy, Data Frames
- **System Monitoring**: Watchdog Daemon Engine, Subprocess Script Pipelines
- **AI Intelligence Hook**: Groq Cloud Engine Client SDK (`llama-3.1-8b-instant`)
- **Version Control**: Git Architecture, GitHub Desktop Enterprise Repositories

## 📊 Sample Pipeline Telemetry Output
When a network data frame is modified via manual log entries, the rule engine isolates local layers and logs immediate structural responses:
- `[INTERNAL] Interface [eth0] is online safely on local IP 10.0.2.15`
- `CRITICAL ALERT: External traffic detected on [ext0]! Unrecognized IP: 185.220.101.5`

## 📁 Repository Map
- `/network_logs.csv`: Core dataset storing raw interface configuration details.
- `/analyzer.py`: Main Pandas analytics parsing component and alert generator.
- `/kali_brain.py`: AI model client pipeline interface framework connector script.
- `/watcher.py`: Local folder event listener monitor daemon script.
- `/security_report.txt`: Automated local storage text archive for AI analysis payloads.
