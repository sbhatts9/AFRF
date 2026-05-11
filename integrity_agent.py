import hashlib
import os
import json
from datetime import datetime

def integrity_agent(evidence_folder, collected_files):
    print("=" * 50)
    print("AFRF INTEGRITY AGENT - EVIDENCE HASHING")
    print("=" * 50)
    print(f"Evidence folder: {evidence_folder}")
    print(f"Files to hash: {collected_files}")
    print("\nGenerating SHA-256 hashes...")

    hash_record = {
        "timestamp": datetime.now().isoformat(),
        "evidence_folder": evidence_folder,
        "hashes": {}
    }

    for filename in collected_files:
        filepath = os.path.join(evidence_folder, filename)

        # Generate SHA-256 hash
        sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)

        file_hash = sha256.hexdigest()
        hash_record["hashes"][filename] = file_hash

        print(f"✅ {filename}")
        print(f"   SHA-256: {file_hash}")

    # Save hash record to evidence folder
    hash_file = os.path.join(evidence_folder, "integrity_manifest.json")
    with open(hash_file, "w") as f:
        json.dump(hash_record, f, indent=4)

    print(f"\n📋 Integrity manifest saved: integrity_manifest.json")
    print(f"🔐 All {len(collected_files)} files hashed at t=0")
    print("\nIntegrity Agent complete. Passing to Vault Agent...")

    return hash_record
