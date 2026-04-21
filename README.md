# 🚀 Miner-X: Autonomous B2B Prospecting & Data Mining Engine

<p align="center">
    <a href="https://github.com/Luo-max-dev/miner-x/stargazers"><img src="https://img.shields.io/github/stars/Luo-max-dev/miner-x?style=flat-square" alt="Stars"></a>
    <a href="https://github.com/Luo-max-dev/miner-x/network/members"><img src="https://img.shields.io/github/forks/Luo-max-dev/miner-x?style=flat-square" alt="Forks"></a>
    <a href="https://github.com/Luo-max-dev/miner-x/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Luo-max-dev/miner-x?style=flat-square" alt="License"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10+-blue?style=flat-square" alt="Python"></a>
</p>

<p align="center">
    <a href="#-disclaimer">Disclaimer</a> •
    <a href="#-key-features">Key Features</a> •
    <a href="#-configuration">Configuration</a> •
    <a href="#-quick-start">Quick Start</a>
</p>

Miner-X is an industrial-grade B2B lead generation engine optimized for the Australian and global supply chain markets. It integrates OSINT, Multi-Agent Orchestration, and Official Business Registry Validation (ABN Lookup) to deliver high-precision prospecting.

---

### ⚠️ Disclaimer

01. **Use of this project is at the user's own discretion and risk. The author is not responsible for any loss, liability, or risk arising from the user's use of this project.**
02. The code and functionality provided by the author of this project are the results of development based on existing knowledge and technology. The author strives to ensure the correctness and safety of the code according to the current level of technology but does not guarantee that the code is completely free of errors or defects.
03. All third-party libraries, plugins, or services that this project relies on follow their original open-source or commercial licenses. Users must review and comply with the corresponding agreements themselves. The author assumes no responsibility for the stability, safety, and compliance of third-party components.
04. Users must strictly comply with the requirements of the **GNU General Public License v3.0** when using this project and indicate the use of GNU General Public License v3.0 code in appropriate places.
05. Users must conduct their own research on relevant laws and regulations when using the code and functionality of this project and ensure that their use is legal and compliant. Any legal liability and risks resulting from the violation of laws and regulations shall be borne by the user.
06. Users must not use this tool to engage in any infringement of intellectual property rights, including but not limited to unauthorized downloading and dissemination of copyrighted content. Developers do not participate in, support, or endorse any illegal content acquisition or distribution.
07. This project does not assume responsibility for the compliance of data collection, storage, transmission, and other processing activities involved by the user. Users should comply with relevant laws and regulations themselves to ensure that processing behaviors are legal and justified; legal liabilities caused by illegal operations shall be borne by the user.
08. Users shall not under any circumstances link the author, contributors, or other related parties of this project to the user's use behavior, or hold them responsible for any loss or damage arising from the user's use of this project.
09. **The authors of this project will not provide a paid version of the Miner-X project, nor will they provide any commercial services related to the Miner-X project.**
10. Any programs based on secondary development, modification, or compilation of this project are unrelated to the original author. The original author assumes no responsibility for the secondary development behavior or its results. Users should take full responsibility for various situations that may arise from secondary development.
11. This project does not grant users any patent license; if use of this project leads to patent disputes or infringement, the user assumes all risks and responsibilities. Without the written authorization of the author or right holder, this project shall not be used for any commercial publicity, promotion, or sub-licensing.
12. The author reserves the right to terminate service to any user who violates this statement at any time and may require them to destroy the obtained code and derivative works.
13. The author reserves the right to update this statement without notice. The user's continued use is deemed acceptance of the revised terms.
14. **Before using the code and functionality of this project, please carefully consider and accept the above disclaimer. If you have any questions or disagree with the above statement, please do not use the code and functionality of this project. If you use the code and functionality of this project, you are deemed to have fully understood and accepted the above disclaimer and voluntarily assume all risks and consequences of using this project.**

---

## 🌟 Key Features

- **🇦🇺 AU ABN Deep Integration**: Natively connects to the Australian Business Register (ABR) to verify company status and official registration names.
- **🛡️ Triple-Check Verification**:
    - **Physical**: SMTP handshake verification without sending emails to confirm mailbox existence.
    - **Social**: OSINT-based social mapping (LinkedIn, Twitter, IG) via Holehe.
    - **Identity**: AI matching of founder biographies to professional email patterns.
- **🤖 Role-Based Orchestration**: Powered by CrewAI with specialized agents for Research, Identity Locking, and Sales Strategy.
- **📉 Cost Optimized**: Full support for DeepSeek-V3 and LiteLLM, reducing lead costs to < $0.01 per high-quality lead.

---

## ⚙️ Configuration

The project uses a `.env` file for configuration:

| Parameter | Description | Required |
| :--- | :--- | :--- |
| `LLM_API_KEY` | Your LLM API Key | Yes |
| `MODEL_NAME` | Model Name (e.g., `deepseek-chat`) | Yes |
| `ABN_GUID` | Australian ABR Official GUID | Yes (AU Market) |

---

## 🚀 Quick Start

1. **One-Click Installation (Ubuntu/Debian)**:
   ```bash
   curl -sSL https://raw.githubusercontent.com/Luo-max-dev/miner-x/main/setup.sh | bash
   ```
2. **Run a Mining Task**:
   ```bash
   python core/engine.py --industry "Packaging" --city "Sydney"
   ```

---
