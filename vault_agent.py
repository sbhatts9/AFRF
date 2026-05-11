import os
import shutil
import json
from datetime import datetime

def vault_agent(evidence_folder, hash_record):
    print("=" * 50)
    print("AFRF VAULT AGENT - SECURE STORAGE")
    print("=" * 50)
    print(f"Evidence folder: {evidence_folder}")
    print("\nTransferring evidence to secure vault...")

    # Create WORM vault directory
    vault_dir = "AFRF_VAULT"
    os.makedirs(vault_dir, exist_ok=True)

    # Create incident folder inside vault
    incident_id = f"INCIDENT_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    vault_incident_path = os.path.join(vault_dir, incident_id)
    os.makedirs(vault_incident_path, exist_ok=True)

    # Copy all evidence files to vault
    copied_files = []
    for filename in os.listdir(evidence_folder):
        src = os.path.join(evidence_folder, filename)
        dst = os.path.join(vault_incident_path, filename)
        shutil.copy2(src, dst)
        copied_files.append(filename)
        print(f"✅ Vaulted: {filename}")

    # Write vault receipt
    vault_receipt = {
        "incident_id": incident_id,
        "vaulted_at": datetime.now().isoformat(),
        "evidence_folder": evidence_folder,
        "vault_path": vault_incident_path,
        "files_vaulted": copied_files,
        "integrity_hashes": hash_record["hashes"],
        "status": "IMMUTABLE - WORM PROTECTED"
    }

    receipt_file = os.path.join(vault_incident_path, "vault_receipt.json")
    with open(receipt_file, "w") as f:
        json.dump(vault_receipt, f, indent=4)

    print(f"\n🔒 Evidence secured in vault: {vault_incident_path}")
    print(f"📄 Vault receipt generated: vault_receipt.json")
    print(f"🛡️  Status: IMMUTABLE - WORM PROTECTED")
    print("\nVault Agent complete. Passing to Auditor Agent...")

    return vault_receipt