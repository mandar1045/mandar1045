<h1 align="center">Hi there, I'm Mandar Joshi 👋</h1>

<p align="center">
  <b>Software Engineer specializing in Distributed Systems, Payment Infrastructure & Cloud-Native Platforms</b>
</p>

<p align="center">
  <a href="https://mandarjoshi-portfolio.vercel.app">
    <img src="https://img.shields.io/badge/Portfolio-mandarjoshi--portfolio.vercel.app-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" />
  </a>
  <a href="https://www.linkedin.com/in/mandar-joshi-0b951b28a/">
    <img src="https://img.shields.io/badge/LinkedIn-Mandar%20Joshi-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:mandarjoshi1045@gmail.com">
    <img src="https://img.shields.io/badge/Email-mandarjoshi1045%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://github.com/mandar1045">
    <img src="https://img.shields.io/badge/GitHub-mandar1045-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Go-gRPC%20%26%20Protobuf-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go gRPC badge" />
  <img src="https://img.shields.io/badge/Distributed%20Systems-Payment%20Infra-0f766e?style=for-the-badge" alt="Payment Infra badge" />
  <img src="https://img.shields.io/badge/Cloud%20Native-Kubernetes%20%26%20Kafka-2563eb?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes badge" />
  <img src="https://img.shields.io/badge/Open%20Source-CNCF%20%26%20Linux%20Foundation-f59e0b?style=for-the-badge" alt="Open Source badge" />
</p>

---

## ⚡ Executive Summary

I am a Software Engineer focused on building high-performance, fault-tolerant backend platforms, microservice architectures, and cloud-native systems. Currently pursuing **B.Tech in Information Technology** at **Vellore Institute of Technology (VIT Vellore)**.

- 💼 **Full Stack Developer @ Xnotch iTech (Renew Care Plus)** — Engineering security-hardened B2B healthcare data infrastructure, encrypted storage at rest, RBAC, and real-time cohort analytics.
- 🛠️ **Creator of [Resync](https://resync.biz)** — A 9-microservice Go/gRPC UPI Autopay recovery platform with smart dunning, Kafka event streaming, and multi-gateway payment orchestration.
- 🌟 **Active Open Source Contributor** — Merged contributions across **Kubernetes** (CNCF), **FOSSology** (Linux Foundation, 8 PRs merged), **Supabase**, **Cal.com**, and **PostHog**.

---

## 🏗️ Featured Engineering Projects

### 💳 [Resync: UPI Autopay Recovery Platform](https://resync.biz)
> **Live at [resync.biz](https://resync.biz) | Repository: [`mandar1045/Resync`](https://github.com/mandar1045/Resync)**

Resync is the automated recovery layer for India's UPI Autopay ecosystem, executing smart retries on failed merchant payment mandates.
- **Microservices Architecture:** 9 Go microservices (`auth-svc`, `sub-svc`, `payment-svc`, `dunning-svc`, `invoice-svc`, `webhook-svc`, `checkout-svc`, `billing-cron`, `api-gateway`) communicating via gRPC/Protobuf.
- **Smart Dunning Classifier:** Categorizes 30+ raw NPCI/gateway failure codes into 8 internal types and routes through 4 context-aware retry strategies (Salary-day payday inference, Exponential backoff, Next-day, Hard Fail).
- **Event-Driven & Idempotency Engine:** Apache Kafka (Redpanda) event streaming combined with Redis `SETNX` distributed locks (30s TTL) ensuring zero double-charges.
- **Multi-SDK & Dashboard:** Published Node.js (`@mandar1045/resync` on npm) & Python (`resync-sdk` on PyPI) SDKs + Next.js merchant analytics dashboard.
- **Infrastructure & Observability:** Terraform IaC targeting AWS ECS Fargate & Oracle Cloud ARM with distroless Docker containers (~20MB), Prometheus, Grafana, and structured `slog` logging.

---

### 🤖 [Continum: AI/ML Workflow Automation Platform](https://continum.online)
> **Live at [continum.online](https://continum.online) | Repository: [`mandar1045/Continum`](https://github.com/mandar1045/Continum)**

Enterprise AI/ML automation platform for intelligent email classification and workflow routing.
- **NLP Triage Engine:** ML-powered email classifier supporting 15+ custom labels, reducing manual triage time by **60%** for enterprise clients.
- **High Uptime Infrastructure:** Microservice backend maintaining 99.5% uptime and sub-200ms API response times across production traffic.

---

### 👁️ [Real-Time Crowd Management & Stampede Prediction](https://github.com/mandar1045/Crowd-Management-System-software)
> **Repository: [`mandar1045/Crowd-Management-System-software`](https://github.com/mandar1045/Crowd-Management-System-software)**

Computer vision system for real-time crowd density monitoring and stampede risk prediction.
- **Multi-Stream Vision Pipeline:** Processes 4 simultaneous CCTV feeds using YOLO object detection for crowd density estimation at 24 FPS with 91% accuracy.
- **Sub-1.5s Alert Latency:** Predictive risk algorithm analyzing density gradients and flow velocity to trigger automated alert dispatching under 1.5 seconds.

---

### 🔐 [Vaulta: Web3 Browser & Desktop Wallet](https://github.com/mandar1045/Vaulta)
> **Repository: [`mandar1045/Vaulta`](https://github.com/mandar1045/Vaulta)**

Desktop browser and wallet application built with React, Tauri, Electron, and `viem`, featuring chain-aware browsing and native security controls.

---

## 🌐 Open Source Contributions

I regularly contribute to foundational cloud-native and open-source infrastructure projects:

| Project | Organization | Scope & Contributions |
| :--- | :--- | :--- |
| **[FOSSology](https://github.com/fossology/fossology)** | Linux Foundation | **8 Merged PRs** improving core license scanning, import reliability, and null-safety fixes. |
| **[Kubernetes](https://github.com/kubernetes/kubernetes)** | CNCF | Upstream contributor to container orchestration core and tooling. |
| **[Supabase](https://github.com/supabase/supabase)** | Supabase Inc. | Merged PRs enhancing developer tooling, table editor reliability, and documentation. |
| **[Cal.com](https://github.com/calcom/cal.com)** | Cal.com Inc. | Merged PRs addressing scheduling availability logic and product polish. |
| **[PostHog](https://github.com/PostHog/posthog)** | PostHog Inc. | Contributed resilience and developer experience improvements to the analytics pipeline. |

---

## 🛠️ Technical Stack & Tooling

### **Languages & Core**
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-003B57?style=for-the-badge&logo=postgresql&logoColor=white)

### **Backend & Distributed Systems**
![gRPC](https://img.shields.io/badge/gRPC-244c5a?style=for-the-badge&logo=grpc&logoColor=white)
![Protobuf](https://img.shields.io/badge/Protobuf-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Express.js](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)

### **Databases & Caching**
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

### **DevOps, Cloud & Observability**
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

---

## 📊 Contribution Signals

<p align="center">
  <img height="170" src="https://github-readme-stats-eight-theta.vercel.app/api?username=mandar1045&show_icons=true&hide_border=true&theme=transparent&rank_icon=github" alt="Mandar's GitHub stats" />
  <img height="170" src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=mandar1045&layout=compact&hide_border=true&theme=transparent" alt="Top languages" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=mandar1045&hide_border=true&theme=transparent" alt="GitHub streak" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=mandar1045&bg_color=ffffff&color=0f766e&line=2563eb&point=f59e0b&area=true&hide_border=true" alt="Contribution graph" />
</p>

---

## 📫 Connect & Contact

- **Portfolio:** [mandarjoshi-portfolio.vercel.app](https://mandarjoshi-portfolio.vercel.app)
- **LinkedIn:** [Mandar Joshi](https://www.linkedin.com/in/mandar-joshi-0b951b28a/)
- **Email:** [mandarjoshi1045@gmail.com](mailto:mandarjoshi1045@gmail.com)
- **GitHub:** [@mandar1045](https://github.com/mandar1045)
- **Location:** Vellore, India (Open to Relocation)
