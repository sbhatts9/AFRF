import os
import json
from datetime import datetime

def collector_agent(alert, tier):
    print("=" * 50)
    print("AFRF COLLECTOR AGENT - EVIDENCE COLLECTION")
    print("=" * 50)
    print(f"Collection tier: {tier}")
    print(f"Target: {alert['target']}")
    print("\nStarting evidence collection...")

    # Create evidence folder with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    evidence_folder = f"evidence_{timestamp}"
    os.makedirs(evidence_folder, exist_ok=True)

    # L1 collection — logs and metadata
    collected = []

    print("\n📋 Collecting system logs...")
    log_file = os.path.join(evidence_folder, "system_logs.txt")
    with open(log_file, "w") as f:
        f.write(f"=== SYSTEM LOGS ===\n")
        f.write(f"Collected at: {datetime.now().isoformat()}\n")
        f.write(f"Target server: {alert['target']}\n")
        f.write(f"Source IP: {alert['source_ip']}\n")
        f.write(f"Event: {alert['event']}\n")
    collected.append("system_logs.txt")
    print("✅ System logs collected")

    print("\n📋 Collecting network metadata...")
    net_file = os.path.join(evidence_folder, "network_metadata.txt")
    with open(net_file, "w") as f:
        f.write(f"=== NETWORK METADATA ===\n")
        f.write(f"Collected at: {datetime.now().isoformat()}\n")
        f.write(f"Source IP: {alert['source_ip']}\n")
        f.write(f"Alert ID: {alert['id']}\n")
        f.write(f"Severity: {alert['severity']}\n")
    collected.append("network_metadata.txt")
    print("✅ Network metadata collected")

    # L2 collection — everything above plus RAM dump
    if tier == "L2":
        print("\n🔴 L2 tier — collecting volatile evidence...")

        print("💾 Capturing RAM dump...")
        ram_file = os.path.join(evidence_folder, "ram_dump.txt")
        with open(ram_file, "w") as f:
            f.write(f"=== RAM DUMP (SIMULATED) ===\n")
            f.write(f"Captured at: {datetime.now().isoformat()}\n")
            f.write(f"Target: {alert['target']}\n")
            f.write("Simulated memory snapshot — real capture via winpmem/LiME in production\n")
        collected.append("ram_dump.txt")
        print("✅ RAM dump captured")

        print("⚡ Capturing running processes...")
        proc_file = os.path.join(evidence_folder, "running_processes.txt")
        with open(proc_file, "w") as f:
            f.write(f"=== RUNNING PROCESSES (SIMULATED) ===\n")
            f.write(f"Captured at: {datetime.now().isoformat()}\n")
            f.write("sshd, bash, python3, wazuh-agent, nginx\n")
        collected.append("running_processes.txt")
        print("✅ Running processes captured")

    print(f"\n📁 Evidence folder created: {evidence_folder}")
    print(f"📦 Files collected: {collected}")
    print("\nCollector Agent complete. Passing to Integrity Agent...")

    return evidence_folder, collected