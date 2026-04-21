# Miner V3.0: Autonomous B2B Prospecting Engine
## Technical Architecture Blueprint

### 1. Overview
Miner V3.0 transforms from a sequential script into a **Multi-Agent Orchestration Framework**. It decouples "Searching", "Verification", "Enrichment", and "Outreach" into autonomous roles.

### 2. Core Modules (The 4-Layer Stack)

#### Layer A: Data Acquisition (The Scraper)
*   **Target:** Clean, markdown-ready web content.
*   **Tooling:** 
    *   **Exa AI:** For intent-based semantic search.
    *   **Firecrawl / Jina Reader:** Converts complex HTML into structured Markdown for LLM efficiency.
    *   **Custom Scrapers:** For ABN (Australian Business Register) and specialized packaging directories.

#### Layer B: Verification Suite (The Gatekeeper)
*   **SMTP Handshake:** Direct verification with mail servers (using `pyMailVerify` or custom scripts).
*   **OSINT (Holehe/Sherlock):** Confirming social presence.
*   **Pattern Validation:** Cross-referencing identified names with domain formats.

#### Layer C: Multi-Agent Orchestration (The Brain)
*   **Framework:** **CrewAI** (Role-based) or **LangGraph** (State-based).
*   **Agents:**
    1.  **Researcher Agent:** Finds company details and news dynamic.
    2.  **Identity Agent:** Scans LinkedIn/Team pages for the "Power Person" (CEO/Founder).
    3.  **Validator Agent:** Runs the Triple-Check protocol.
    4.  **Strategist Agent:** Analyzes the target's background and writes the "Ice-breaker".

#### Layer D: Delivery & Integration (The Pipeline)
*   **LLM Adapter:** **LiteLLM** to support DeepSeek, Claude, and GPT interchangeably.
*   **Storage:** Scalable SQLite/PostgreSQL with Vector Indexing (for semantic de-duplication).
*   **Scheduler:** GitHub Actions or Dockerized Cron.

### 3. Key Differentiators
*   **Semantic De-duplication:** Prevents reaching out to the same entity via different brand names.
*   **Dynamic Ice-breakers:** Moves beyond "I saw your website" to "I saw your 10-year transition from FoodTech to Sustainable Packaging."
*   **Open-Source First:** Every component can be self-hosted or swapped for a local model (Ollama).
