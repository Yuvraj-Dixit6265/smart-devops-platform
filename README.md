🚀 Smart DevOps Platform

A production-style DevOps & FinOps platform that automates CI/CD, deploys applications to Kubernetes, monitors application health using AI-based log analysis, and detects cloud cost anomalies with actionable recommendations.

📌 Problem Statement

Modern engineering teams face multiple challenges:

Slow and unreliable deployments

Silent application failures after deployment

DevOps teams wasting hours manually reading logs

Sudden cloud cost spikes with no clear explanation

This project solves all of the above in one unified platform.

🧠 What This Platform Does
✅ End-to-End CI/CD

Automated CI using GitHub Actions

Containerized application using Docker

Kubernetes deployment manifests included

CD pipeline designed with manual gating for safety (industry best practice)

🤖 AI-Powered Application Monitoring

Structured logging inside the application

AI-style log analysis to:

Detect crashes

Identify failure patterns

Explain issues in human-readable form

Exposed as an API endpoint:

GET /analyze/logs

💰 Cloud Cost Optimization (FinOps)

Simulates Azure-style cloud billing data

Tracks daily cloud costs

Detects abnormal cost spikes

Explains why the cost increased

Provides optimization recommendations

Exposed as an API endpoint:

GET /analyze/costs

🏗️ Architecture Overview
Code Push
   ↓
CI Pipeline (GitHub Actions)
   ↓
Docker Build
   ↓
Kubernetes Deployment (Manual CD)
   ↓
Application Runtime
   ├── Logs → AI Log Analyzer
   └── Cost Data → Cost Anomaly Engine

🧩 Project Structure
smart-devops-platform/
│
├── app/                    # FastAPI application
├── ai_assistant/           # AI-based log analyzer
├── cost_engine/            # Cloud cost optimization & anomaly detection
├── ci/                     # CI helper scripts
├── docker/                 # Dockerfile
├── k8s/                    # Kubernetes manifests
├── terraform/              # Infrastructure-as-Code (cloud-ready)
├── .github/workflows/      # CI/CD pipelines
└── README.md

🔍 Key API Endpoints
Health Check
GET /
GET /health

Trigger Log Analysis
GET /analyze/logs

Trigger Cloud Cost Analysis
GET /analyze/costs

☁️ Cloud & Azure Readiness

Designed to be cloud-agnostic

Kubernetes manifests are compatible with Azure AKS

Cost engine follows Azure Cost Management export format

Logic can be connected to real Azure APIs using:

Service Principals

Azure Cost Management API

Azure Monitor

For this portfolio project, cloud cost data is simulated intentionally to validate logic without incurring real cloud charges.
This mirrors real FinOps development workflows.

🚦 CI/CD Design Decision

CI runs automatically on every push

CD is gated and manual (workflow_dispatch)

This prevents unsafe deployments when a live Kubernetes cluster is not attached — a real-world DevOps best practice.

🧪 How to Run Locally
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
uvicorn app.main:app --reload

🎯 Why This Project Matters

This project demonstrates real-world skills in:

DevOps Automation

Kubernetes Deployment

CI/CD Design

Observability & Monitoring

AI-assisted Operations (AIOps)

Cloud Cost Optimization (FinOps)

Production-safe engineering decisions

👨‍💻 Author

Yuvraj Dixit
DevOps | Cloud | Automation | AI Ops

📣 Final Note

This is one unified platform, not multiple small demos.
It reflects how modern DevOps teams design, deploy, monitor, and optimize systems in production.