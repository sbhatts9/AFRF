from sentinel_agent import sentinel_agent
from collector_agent import collector_agent
from datetime import datetime

print("=" * 50)
print("AFRF - AUTOMATED FORENSIC READINESS FRAMEWORK")
print(f"Pipeline started at: {datetime.now().isoformat()}")
print("=" * 50)

# Mock Wazuh alert
alert = {
    "id": "WZH-2082-001",
    "severity": "high",
    "source_ip": "192.168.1.45",
    "event": "Multiple failed SSH login attempts detected - possible brute force attack",
    "timestamp": datetime.now().isoformat(),
    "target": "bank-server-01"
}

# Step 1 — Sentinel Agent decides tier
tier = sentinel_agent(alert)

# Step 2 — Collector Agent grabs evidence
evidence_folder, collected_files = collector_agent(alert, tier)

# Step 3 — Integrity Agent hashes everything
from integrity_agent import integrity_agent
hash_record = integrity_agent(evidence_folder, collected_files)

# Step 4 — Vault Agent stores evidence securely
from vault_agent import vault_agent
vault_receipt = vault_agent(evidence_folder, hash_record)

print("\n" + "=" * 50)
print("PIPELINE COMPLETE")
print(f"Evidence stored in: {evidence_folder}")
print(f"Files collected: {collected_files}")
print(f"Integrity hashes generated: {len(hash_record['hashes'])}")
print(f"Vault receipt created: {vault_receipt['vault_path']}")  
print("=" * 50)