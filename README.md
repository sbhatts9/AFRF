# AFRF - Automated Forensic Readiness Framework

LLM-powered multi-agent system for automated digital evidence collection, preservation, and chain of custody documentation.

## Overview

AFRF is a forensic readiness framework designed for financial institutions, with a primary case study in Nepal's banking sector. When a security incident is detected, AFRF's AI agents automatically collect, hash, vault, and document digital evidence without human intervention, preserving forensic integrity from the moment of detection (t=0).

This addresses the **Human Latency Gap**: the window between incident detection and manual evidence collection where evidence can be lost, corrupted, or rendered legally inadmissible.

## Agent Pipeline

Wazuh Alert → Sentinel Agent → Collector Agent → Integrity Agent → Vault Agent → Auditor Agent


| Agent | Role |
|---|---|
| **Sentinel Agent** | Receives security alert, uses LLM to decide collection tier (L1 or L2) |
| **Collector Agent** | Collects evidence based on tier — logs only (L1) or logs + RAM dump (L2) |
| **Integrity Agent** | Generates SHA-256 hashes at t=0 before any human touches the evidence |
| **Vault Agent** | Stores evidence in WORM-protected vault with unique incident ID |
| **Auditor Agent** | Uses LLM to generate a formal chain of custody report for legal proceedings |

## Tech Stack

- **LLM**: LLaMA 3 via Ollama (local, no data leaves the machine)
- **Language**: Python 3
- **Storage**: Simulated WORM vault (production: AWS S3 Object Lock or equivalent)
- **SIEM Integration**: Designed for Wazuh (GNS3 simulation in progress)

## How to Run

**Prerequisites:**
```bash
pip install requests
ollama pull llama3
```

**Run the full pipeline:**
```bash
python main.py
```

**Output:**
- Timestamped evidence folder with collected files
- SHA-256 integrity manifest
- WORM-protected vault entry
- Chain of custody report (JSON)

## Regulatory Context

AFRF is designed to satisfy Nepal's financial sector requirements:
- **NRB Cyber Resilience Guidelines** — 2-hour RTO compliance
- **NCSC IT Decade Roadmap** — forensic readiness alignment
- **Cyber Security Bill 2082** — chain of custody and legal admissibility

## Status

- [x] Sentinel Agent — LLM-powered triage
- [x] Collector Agent — tiered evidence collection  
- [x] Integrity Agent — SHA-256 hashing at t=0
- [x] Vault Agent — WORM protected storage
- [x] Auditor Agent — LLM chain of custody report
- [ ] GNS3 network simulation
- [ ] Real SSH collection from bank server
- [ ] Wazuh webhook integration