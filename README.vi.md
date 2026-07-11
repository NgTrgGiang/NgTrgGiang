<a href="https://github.com/NgTrgGiang/NgTrgGiang/blob/main/README.md">English</a> &nbsp;·&nbsp; <b>Tiếng Việt</b>

<a href="https://readme-typing-svg.demolab.com">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=26&pause=1000&color=34D399&vCenter=true&width=520&height=52&lines=Nguy%E1%BB%85n+Tr%C6%B0%E1%BB%9Dng+Giang;K%E1%BB%B9+s%C6%B0+AI+%2F+LLM+%C2%B7+Chuy%C3%AAn+RAG;T%E1%BB%AB+prototype+%C4%91%E1%BA%BFn+s%E1%BA%A3n+ph%E1%BA%A9m" alt="Nguyen Truong Giang - Ky su AI/LLM, chuyen RAG" />
</a>

<p><b>Mình xây dựng AI RAG chạy được thật.</b><br/>
<sub>Kỹ sư AI/LLM (mid-level). Đưa hệ thống RAG từ prototype lên production. Đang tìm cơ hội, ở Việt Nam.</sub></p>

<p>
  <a href="https://github.com/NgTrgGiang"><img src="https://img.shields.io/badge/-0a0a0b?style=flat&logo=github&logoColor=34d399" alt="GitHub" height="26" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/ngtruonggiang/"><img src="https://img.shields.io/badge/-0a0a0b?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzM0ZDM5OSI%2BPHBhdGggZD0iTTIwLjQ0NyAyMC40NTJoLTMuNTU0di01LjU2OWMwLTEuMzI4LS4wMjctMy4wMzctMS44NTItMy4wMzctMS44NTMgMC0yLjEzNiAxLjQ0NS0yLjEzNiAyLjkzOXY1LjY2N0g5LjM1MVY5aDMuNDE0djEuNTYxaC4wNDZjLjQ3Ny0uOSAxLjYzNy0xLjg1IDMuMzctMS44NSAzLjYwMSAwIDQuMjY3IDIuMzcgNC4yNjcgNS40NTV2Ni4yODZ6TTUuMzM3IDcuNDMzYy0xLjE0NCAwLTIuMDYzLS45MjYtMi4wNjMtMi4wNjUgMC0xLjEzOC45Mi0yLjA2MyAyLjA2My0yLjA2MyAxLjE0IDAgMi4wNjQuOTI1IDIuMDY0IDIuMDYzIDAgMS4xMzktLjkyNSAyLjA2NS0yLjA2NCAyLjA2NXptMS43ODIgMTMuMDE5SDMuNTU1VjloMy41NjR2MTEuNDUyek0yMi4yMjUgMEgxLjc3MUMuNzkyIDAgMCAuNzc0IDAgMS43Mjl2MjAuNTQyQzAgMjMuMjI3Ljc5MiAyNCAxLjc3MSAyNGgyMC40NTFDMjMuMiAyNCAyNCAyMy4yMjcgMjQgMjIuMjcxVjEuNzI5QzI0IC43NzQgMjMuMiAwIDIyLjIyNSAweiIvPjwvc3ZnPg%3D%3D" alt="LinkedIn" height="26" /></a>
  &nbsp;
  <a href="https://www.facebook.com/giang.6064"><img src="https://img.shields.io/badge/-0a0a0b?style=flat&logo=facebook&logoColor=34d399" alt="Facebook" height="26" /></a>
  &nbsp;
  <a href="mailto:ntg0356868808@gmail.com"><img src="https://img.shields.io/badge/-0a0a0b?style=flat&logo=gmail&logoColor=34d399" alt="Email" height="26" /></a>
</p>

---

### Giới thiệu

Mình là **Kỹ sư AI/LLM** (mid-level), chuyên về **retrieval-augmented generation (RAG)**. Mình đưa hệ thống RAG từ prototype lên production: ingest dữ liệu, chunking, retrieval, đánh giá (eval) và API ổn định. Mình coi trọng eval và guardrails ngang với bản demo, ưu tiên hệ thống nhỏ gọn, được kiểm thử kỹ.

- RAG đầu-cuối: ingest, retrieval, đánh giá, API sẵn sàng chạy
- Tự động hóa với n8n và Python để bỏ việc thủ công lặp lại
- Eval và guardrails để câu trả lời bám nguồn, an toàn
- Tư duy production: deploy, giám sát, cải tiến

---

### Dự án nổi bật

| Dự án | Làm gì | Stack |
|---|---|---|
| **[RAG Nội quy công ty](https://github.com/NgTrgGiang/demo-rag-noi-quy-cong-ty)** | Trợ lý RAG trả lời câu hỏi về nội quy công ty bằng tiếng Việt, có trích nguồn. | `RAG` `ChromaDB` `OpenAI` `Streamlit` |
| **[GraphRAG vs Flat RAG](https://github.com/NgTrgGiang/2A202600624-NguyenTruongGiang-Day19)** | Trích xuất bộ ba bằng LLM dựng knowledge graph Neo4j, truy vấn 2-hop so với baseline ChromaDB, chấm trên bộ 20 câu hỏi. | `GraphRAG` `Neo4j` `ChromaDB` `LLM` |
| **[TrustFed](https://github.com/NgTrgGiang/trustfed-federated-llm)** | Fine-tune LoRA kiểu federated cho LLM, bảo mật từ thiết kế: dữ liệu non-IID và differential privacy mức người dùng. | `LoRA` `Federated` `PyTorch` `DP` |
| **[dev-starter](https://github.com/NgTrgGiang/dev-starter)** | Khung xương full-stack AI: FastAPI + Postgres/pgvector + React/Vite/TS + Docker. | `FastAPI` `pgvector` `React` `Docker` |

---

### Công nghệ

**Core / RAG**
&nbsp;
[![Python](https://img.shields.io/badge/Python-0a0a0b?style=flat&logo=python&logoColor=34d399)](https://www.python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0a0a0b?style=flat&logo=langchain&logoColor=34d399)](https://www.langchain.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-0a0a0b?style=flat&logo=openai&logoColor=34d399)](https://openai.com)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-0a0a0b?style=flat&logo=huggingface&logoColor=34d399)](https://huggingface.co)
[![PyTorch](https://img.shields.io/badge/PyTorch-0a0a0b?style=flat&logo=pytorch&logoColor=34d399)](https://pytorch.org)

**Data / Infra**
&nbsp;
[![FastAPI](https://img.shields.io/badge/FastAPI-0a0a0b?style=flat&logo=fastapi&logoColor=34d399)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0a0a0b?style=flat&logo=postgresql&logoColor=34d399)](https://www.postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-0a0a0b?style=flat&logo=docker&logoColor=34d399)](https://www.docker.com)
[![Render](https://img.shields.io/badge/Render-0a0a0b?style=flat&logo=render&logoColor=34d399)](https://render.com)

**Automation**
&nbsp;
[![n8n](https://img.shields.io/badge/n8n-0a0a0b?style=flat&logo=n8n&logoColor=34d399)](https://n8n.io)
[![JavaScript](https://img.shields.io/badge/JavaScript-0a0a0b?style=flat&logo=javascript&logoColor=34d399)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

### Hoạt động gần đây

<!-- RECENT:START -->
- **[claude-code-token-saver](https://github.com/NgTrgGiang/claude-code-token-saver)** &nbsp; One-shot installer for token-saving Claude Code rails (CLAUDE.md, hooks, subagents, slash commands, dev-docs). &nbsp; `updated 2026-07-10`
- **[claude-code-read](https://github.com/NgTrgGiang/claude-code-read)** &nbsp; JavaScript project &nbsp; `updated 2026-07-09`
- **[ngtruonggiang-portfolio](https://github.com/NgTrgGiang/ngtruonggiang-portfolio)** &nbsp; TypeScript project &nbsp; `updated 2026-07-09`
- **[test](https://github.com/NgTrgGiang/test)** &nbsp; HTML project &nbsp; `updated 2026-07-09`
- **[demo-rag-noi-quy-cong-ty](https://github.com/NgTrgGiang/demo-rag-noi-quy-cong-ty)** &nbsp; [DEMO] Hệ thống RAG cho nội quy công ty &nbsp; `updated 2026-07-09`
<!-- RECENT:END -->

---

### Hoạt động GitHub

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NgTrgGiang/NgTrgGiang/output/github-snake-dark.svg?v=1" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/NgTrgGiang/NgTrgGiang/output/github-snake.svg?v=1" />
  <img alt="Con ran an bieu do dong gop GitHub" src="https://raw.githubusercontent.com/NgTrgGiang/NgTrgGiang/output/github-snake.svg?v=1" />
</picture>

</div>

---

<div align="center">

### Liên hệ

Mình đang tìm cơ hội về AI/LLM Engineering và RAG.

<a href="mailto:ntg0356868808@gmail.com">ntg0356868808@gmail.com</a>

</div>
