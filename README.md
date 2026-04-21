# Miner-X: Autonomous B2B Prospecting Engine (V3.0)

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://opensource.org/licenses/AGPL-3.0)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-brightgreen.svg)](https://www.python.org/)
[![AI: CrewAI](https://img.shields.io/badge/AI-CrewAI-red.svg)](https://www.crewai.com/)

**Miner-X** is an industrial-grade B2B lead generation engine specifically optimized for the Australian market. It integrates **OSINT**, **Multi-Agent Orchestration**, and **Official Business Registry Validation (ABN Lookup)**.

> **Our Mission:** Skip `info@` general emails, lock on Founder/CEO identities, and verify high-conversion contact data with a 95%+ confidence score.

---

## 🌟 Key Features

- **🇦🇺 AU ABN Deep Integration:** Natively connects to the Australian Business Register (ABR) to verify company status and official registration names.
- **🛡️ Triple-Check Verification:**
    - **Physical:** SMTP handshake without sending emails.
    - **Social:** OSINT-based social mapping (LinkedIn, Twitter, IG) via Holehe.
    - **Identity:** AI matching of founder biographies to professional email patterns.
- **🤖 Role-Based Orchestration:** Powered by **CrewAI** with specialized agents for Research, Identity Locking, and Sales Strategy.
- **📉 Cost Optimized:** Full support for **DeepSeek-V3** and **LiteLLM**, reducing lead costs to < $0.01 per high-quality lead.

---

## 🛠️ Tech Stack

- **Orchestration:** CrewAI / Asyncio
- **LLM Adapter:** LiteLLM (Supporting DeepSeek, Claude, GPT, Ollama)
- **Scraper:** Crawl4AI / Firecrawl
- **Verification:** Holehe / GHunt / SMTP Handshake
- **Industry Specs:** ABN Lookup API

---

## 🚀 Quick Start

### 1. One-Click Installation (Ubuntu/Debian)
```bash
curl -sSL https://raw.githubusercontent.com/your-username/miner-x/main/setup.sh | bash
```

### 2. Configuration
Copy `.env.example` to `.env` and fill in your keys. **DO NOT commit `.env` to version control.**
```bash
# Core AI Config
LLM_API_KEY=sk-xxxx
MODEL_NAME=deepseek-chat

# Australian Market Config
ABN_GUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx # Get yours at abr.business.gov.au
```

### 3. Run Your First Mine
```bash
python core/engine.py --industry "Packaging" --city "Sydney"
```

---

## 📊 Confidence Matrix
Miner-X provides a **Confidence Score (0-100)** for every lead:
- **85-100:** Triple-verified. Ready for immediate outreach.
- **60-85:** Validated email with partial social presence.
- **< 60:** Requires manual review.

---

## ⚖️ Disclaimer
This tool is for legitimate B2B market research only. Users are responsible for complying with local privacy laws (e.g., Australian Privacy Act 1988) and platform Terms of Service.

---

## ⭐️ Support the Project
If you find this useful, give it a star! 

*Developed with ❤️ for the Supply Chain & Packaging Industry.*
