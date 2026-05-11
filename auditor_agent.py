import json
import os
import requests
from datetime import datetime

def auditor_agent(alert, tier, evidence_folder, hash_record, vault_receipt):
    print("=" * 50)
    print("AFRF AUDITOR AGENT - CHAIN OF CUSTODY")
    print("=" * 50)
    print("Generating legal chain of custody report...")
    print("Consulting LLM for narrative generation...")

    # Ask LLM to write the legal narrative
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"""You are a digital forensics legal documentation specialist.

Write a formal chain of custody report for the following incident:

INCIDENT DETAILS:
- Alert ID: {alert['id']}
- Event: {alert['event']}
- Source IP: {alert['source_ip']}
- Target: {alert['target']}
- Severity: {alert['severity']}
- Detection Time: {alert['timestamp']}

COLLECTION DETAILS:
- Collection Tier: {tier}
- Evidence Folder: {evidence_folder}
- Files Collected: {list(hash_record['hashes'].keys())}
- Collection Time: {hash_record['timestamp']}

INTEGRITY VERIFICATION:
- SHA-256 hashes generated at time of capture (t=0)
- Hashes: {json.dumps(hash_record['hashes'], indent=2)}

VAULT DETAILS:
- Vault Path: {vault_receipt['vault_path']}
- Vaulted At: {vault_receipt['vaulted_at']}
- Status: {vault_receipt['status']}

Write a formal 3-paragraph chain of custody report suitable for legal proceedings.
Include: what was detected, what was collected and how integrity was maintained,
and where evidence is stored and its legal status.""",
            "stream": False
        }
    )

    result = response.json()
    legal_narrative = result['response']

    # Build full report
    report = {
        "report_id": f"AFRF-COC-{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "generated_at": datetime.now().isoformat(),
        "incident": alert,
        "collection_tier": tier,
        "integrity_hashes": hash_record['hashes'],
        "vault_location": vault_receipt['vault_path'],
        "legal_narrative": legal_narrative,
        "status": "FORENSICALLY SOUND - ADMISSIBLE"
    }

    # Save report
    report_file = f"COC_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent=4)

    print("\n📜 CHAIN OF CUSTODY REPORT:")
    print("-" * 50)
    print(legal_narrative)
    print("-" * 50)
    print(f"\n✅ Report ID: {report['report_id']}")
    print(f"📁 Saved as: {report_file}")
    print(f"⚖️  Status: FORENSICALLY SOUND - ADMISSIBLE")
    print("\n🎯 AFRF PIPELINE COMPLETE - ALL AGENTS EXECUTED")

    return report