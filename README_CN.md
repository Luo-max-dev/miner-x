# 🚀 Miner-X: 自动化 B2B 获客与数据挖掘引擎

<p align="center">
    <a href="https://github.com/Luo-max-dev/miner-x/stargazers"><img src="https://img.shields.io/github/stars/Luo-max-dev/miner-x?style=flat-square" alt="Stars"></a>
    <a href="https://github.com/Luo-max-dev/miner-x/network/members"><img src="https://img.shields.io/github/forks/Luo-max-dev/miner-x?style=flat-square" alt="Forks"></a>
    <a href="https://github.com/Luo-max-dev/miner-x/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Luo-max-dev/miner-x?style=flat-square" alt="License"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10+-blue?style=flat-square" alt="Python"></a>
</p>

<p align="center">
    <a href="#-免责声明">免责声明</a> •
    <a href="#-核心功能">核心功能</a> •
    <a href="#-配置说明">配置说明</a> •
    <a href="#-快速上手">快速开始</a>
</p>

Miner-X 是一款工业级 B2B 获客引擎，专为澳洲及全球供应链市场优化。集成 OSINT、多 Agent 协作及官方商业登记核验（ABN Lookup），实现极高准确率的线索挖掘。

---

### ⚠️ 免责声明

01. **使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项目所产生的任何损失、责任、或风险概不负责。**
02. 本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者按现有技术水平努力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。
03. 本项目依赖的所有第三方库、插件或服务各自遵循其原始开源或商业许可，使用者需自行查阅并遵守相应协议，作者不对第三方组件的稳定性、安全性及合规性承担任何责任。
04. 使用者在使用本项目时必须严格遵守 **GNU General Public License v3.0** 的要求，并在适当的地方注明使用了 GNU General Public License v3.0 的代码。
05. 使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。
06. 使用者不得使用本工具从事任何侵犯知识产权的行为，包括但不限于未经授权下载、传播受版权保护的内容，开发者不参与、不支持、不认可任何非法内容的获取或分发。
07. 本项目不对使用者涉及的数据收集、存储、传输等处理活动的合规性承担责任。使用者应自行遵守相关法律法规，确保处理行为合法正当；因违规操作导致的法律责任由使用者自行承担。
08. 使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。
09. **本项目的作者不会提供 Miner-X 项目的付费版本，也不会提供与 Miner-X 项目相关的任何商业服务。**
10. 基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的各种情况负全部责任。
11. 本项目不授予使用者任何专利许可；若使用本项目导致专利纠纷或侵权，使用者自行承担全部风险和责任。未经作者或权利人书面授权，不得使用本项目进行任何商业宣传、推广或再授权。
12. 作者保留随时终止向任何违反本声明的使用者提供服务的权利，并可能要求其销毁已获取的代码及衍生作品。
13. 作者保留在不另行通知的情况下更新本声明的权利，使用者持续使用即视为接受修订后的条款。
14. **在使用本项目的代码 and 功能之前，请您认真考虑并接受以上免责声明。如果您对上述声明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险和后果。**

---

## 🌟 核心功能

- **🇦🇺 AU ABN 深度集成**: 原生连接澳洲商业登记局 (ABR)，核验公司状态与官方名称。
- **🛡️ 三重校验系统**:
    - **物理层**: SMTP 握手验证，无需发送邮件即可确认邮箱存在。
    - **社交层**: 基于 OSINT 的社交映射（LinkedIn, Twitter, IG），使用 Holehe 进行反查。
    - **身份层**: AI 匹配创始人背景与专业邮箱模式。
- **🤖 Agent 协同编排**: 基于 CrewAI，通过研究、身份锁定及销售策略 Agent 协同工作。
- **📉 成本极致优化**: 全面支持 DeepSeek-V3 与 LiteLLM，将高质量线索成本降至 < $0.01。

---

## ⚙️ 配置说明

项目使用 `.env` 文件进行配置：

| 参数 | 说明 | 必需 |
| :--- | :--- | :--- |
| `LLM_API_KEY` | 模型 API 密钥 | 是 |
| `MODEL_NAME` | 模型名称 (如 `deepseek-chat`) | 是 |
| `ABN_GUID` | 澳洲 ABR 官方 GUID | 是 (澳洲市场) |

---

## 🚀 快速上手

1. **一键安装 (Ubuntu/Debian)**:
   ```bash
   curl -sSL https://raw.githubusercontent.com/Luo-max-dev/miner-x/main/setup.sh | bash
   ```
2. **运行挖掘任务**:
   ```bash
   python core/engine.py --industry "Packaging" --city "Sydney"
   ```

---
