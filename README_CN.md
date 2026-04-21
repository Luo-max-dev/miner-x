# 🚀 Miner-X: 自动化 B2B 获客与数据挖掘引擎 (V3.0)

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://opensource.org/licenses/AGPL-3.0)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-brightgreen.svg)](https://www.python.org/)
[![AI: CrewAI](https://img.shields.io/badge/AI-CrewAI-red.svg)](https://www.crewai.com/)

**Miner-X** 是一款基于 AI Agent 的工业级 B2B 获客工具，专为澳洲及全球供应链市场设计。通过集成 **ABN 官方核验**、**OSINT 社交指纹**与**多模型 LLM 适配**，实现从原始公司名到“100% 验证线索”的自动化转化。

---

## 🌟 核心功能

- **🔍 深度挖掘**: 基于 CrewAI 的多 Agent 协同，自动识别 Founder/CEO 身份。
- **🇦🇺 澳洲特化**: 原生支持 ABR 官方 API 校验，确保 ABN 状态活跃。
- **🛡️ 三重校验**: SMTP 物理层握手 + 社交注册反查 + AI 逻辑匹配。
- **🤖 模型自由**: 完美适配 DeepSeek, Claude, GPT, Ollama (Local)。
- **🚀 极简部署**: 支持 Docker 一键拉起所有依赖环境。

---

## ⚙️ 配置说明 (Settings)

项目使用 `.env` 文件进行配置，核心参数如下：

| 参数 | 说明 | 必需 |
| :--- | :--- | :--- |
| `LLM_API_KEY` | 你的模型 API 密钥 (DeepSeek/OpenAI 等) | 是 |
| `MODEL_NAME` | 指定模型名称 (如 `deepseek-chat`) | 是 |
| `ABN_GUID` | 澳洲 ABR 官方 GUID (需自行申请) | 是 (澳洲市场) |
| `PROXY_URL` | 住宅代理地址 (用于大规模采集) | 否 |

---

## 📖 快速上手

1. **安装环境**:
   ```bash
   chmod +x setup.sh && ./setup.sh
   ```
2. **启动爬虫**:
   ```bash
   docker-compose up -d
   ```
3. **运行程序**:
   ```bash
   python core/engine.py --industry "Packaging"
   ```

---

## 📢 项目声明 (Statement)

1. 本项目开源于 GitHub，仅供 **个人学习、研究和 B2B 市场调研** 使用。
2. 使用者在利用本工具进行数据抓取时，必须遵守目标网站的 `robots.txt` 协议及当地法律（如澳洲 Privacy Act 1988、GDPR 等）。
3. 使用者需自行承担因使用本工具而产生的任何法律后果、版权纠纷或平台封禁。
4. 本项目不提供任何形式的商业保证，也不对由于使用本工具造成的任何数据丢失或财产损失负责。

---

## 🛡️ 免责声明 (Disclaimer)

- **合法使用**: 严禁将本工具用于 any 形式的非法垃圾邮件群发 (Spamming)、网络攻击或非法获取他人隐私。
- **知识产权**: 抓取到的所有数据版权归原作者/公司所有，请勿用于商业牟利。
- **合规申请**: 本项目内置的 ABN 校验功能需要用户自行前往澳洲政府官网申请 GUID，开发者不提供任何凭证。
- **版权联系**: 如果本工具对相关平台造成了困扰或侵犯了您的权利，请通过 Issue 联系，我们将立即进行技术调整。

---

## ⭐️ Star Trend
如果你喜欢这个项目，请点一个 Star！

*Developed by ❤️ for the Open Source Community.*
