# Autonomous Kali AI Network Log Analyzer & Orchestration Pipeline (SOAR)

A hybrid project combining programmatic Data Analytics, automated Data Visualization, and Cybersecurity Operations to build an autonomous threat triage engine. This system acts as a digital first responder, mimicking the data pipeline and incident response responsibilities of a Tier-1 SOC Analyst.

## 🚀 System Architecture & Operational Blueprint
The application engine is divided into three decoupled tracks that execute dynamically based on system telemetry:

1. **Automated Event Detection (`watcher.py`)**: Utilizes low-overhead file system tracking hooks (`watchdog`) to constantly monitor specific network log data dumps for real-time change vectors without system resource draining.
2. **Algorithmic Rule Sorting Engine (`analyzer.py`)**: Ingests messy, unstructured matrix formats programmatically into a structured **Pandas DataFrame**. It executes string-matching condition logic loops to divide traffic and isolate malicious foreign IP nodes from standard internal segments.
3. **Attack Surface Telemetry Visualizer (`live_cyber_engine.py`)**: A unified data engineering pipeline that maps network ports to vulnerability density vectors. It automatically generates high-fidelity analytical bar charts using **Matplotlib** and **Seaborn**, scales threat scores, and updates the local security matrix database.
4. **AI Incident Response Triage (`kali_brain.py`)**: Orchestrates context injections through high-velocity pipelines straight to specialized open-source LLM reasoning models via **Groq** APIs. It produces immediate technical remediation playbooks and saves structural artifacts locally to text logs.

## 🛠️ Technical Stack & Framework Foundations
- **Primary Language**: Python 3.14+
- **Data Engineering & Analytics**: Pandas, NumPy, Data Frames
- **Data Visualization**: Matplotlib Framework, Seaborn Dashboard Engines
- **System Monitoring**: Watchdog Daemon Engine, Subprocess Script Pipelines
- **AI Intelligence Hook**: Groq Cloud Engine Client SDK (`llama-3.1-8b-instant`)
- **Version Control**: Git Architecture, GitHub Desktop Enterprise Repositories

## 📁 Repository Map
- `/network_logs.csv`: Core dataset storing raw interface configuration details.
- `/analyzer.py`: Main Pandas analytics parsing component and alert generator.
- `/live_cyber_engine.py`: Integrated data visualization dashboard and script execution pipeline.
- `/attack_surface_chart.png`: Automatically generated data visualization bar chart tracking system risk weight.
- `/live_security_report.txt`: Automated local storage text archive for AI analysis payloads.
