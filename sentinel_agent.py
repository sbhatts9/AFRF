import requests
import json
from datetime import datetime

# Mock Wazuh alert
alert = {
    "id": "WZH-2082-001",
    "severity": "high",
    "source_ip": "192.168.1.45",
    "event": "Multiple failed SSH login attempts detected - possible brute force attack",
    "timestamp": datetime.now().isoformat(),
    "target": "bank-server-01"
}

def sentinel_agent(alert):
    print("=" * 50)
    print("AFRF SENTINEL AGENT - ALERT RECEIVED")
    print("=" * 50)
    print(f"Event: {alert['event']}")
    print(f"Source IP: {alert['source_ip']}")
    print(f"Severity: {alert['severity']}")
    print(f"Timestamp: {alert['timestamp']}")
    print("\nConsulting LLM for triage decision...")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"""You are a digital forensics triage agent for a bank in Nepal.

A security alert has been detected:
- Event: {alert['event']}
- Source IP: {alert['source_ip']}
- Severity: {alert['severity']}
- Target: {alert['target']}

Decide:
1. Collection tier: L1 (logs and metadata only) or L2 (logs + RAM dump)
2. Your reasoning in 2 sentences
3. What evidence to collect

Respond in this exact format:
TIER: [L1 or L2]
REASON: [your reasoning]
COLLECT: [list evidence items]""",
            "stream": False
        }
    )

    result = response.json()
    llm_decision = result['response']

    print("\n🤖 LLM TRIAGE DECISION:")
    print("-" * 30)
    print(llm_decision)
    print("-" * 30)
    print(f"\n✅ Sentinel Agent complete at {datetime.now().isoformat()}")
    print("📦 Passing decision to Collector Agent...")

sentinel_agent(alert)