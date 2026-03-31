# Connected Kerb – AI Assistant (Demo)

This repository contains a Streamlit-based demonstration UI for an AI Agent built using **Azure AI Foundry**.

The application showcases how an AI assistant can be securely integrated into enterprise environments to support operational, policy, or knowledge-based use cases, without embedding API keys or secrets in the application.

---

## Overview

The application provides:

- A web-based chat interface built with Streamlit
- Secure integration with an Azure AI Foundry agent
- Azure Entra ID (Azure AD) authentication using managed identities
- A deployment-ready architecture suitable for Azure hosting

This is a **demonstration application** and can be extended for production use.

---

## Architecture Summary

- **UI Layer**: Streamlit web application
- **AI Layer**: Azure AI Foundry Agent
- **Authentication**: Azure Entra ID (`DefaultAzureCredential`)
- **Secrets Management**: None stored in code or config
- **Configuration**: Environment variables

---

## Prerequisites

### Software

- Python **3.9 or later** (3.10 recommended)
- Azure CLI
- Git

### Azure Access

You must have access to:
- An Azure subscription
- An Azure AI Foundry project
- An AI Foundry agent (name + version)

Your Azure identity must have one of the following roles on the AI Foundry resource:
- Cognitive Services User  
- AI Developer  
- Contributor  

---

## Installation

### 1. Clone the repository

```bash
git clone <repo-url>
cd ck-ai-agent-demo
```
### 2. Create and activate a virtual environment
It is recommended to create the environment in an Anaconda environment


### 3. Install dependencies

```
pip install -r requirements.txt
```
Note: pip-system-certs is included to ensure SSL certificate trust in enterprise environments.


## Configuration
The application is configured entirely via environment variables.
### Required environment variables in the config file
```
AI_FOUNDRY_ENDPOINT=https://<your-foundry-endpoint>/api/projects/<project-name>
AI_FOUNDRY_AGENT_NAME=<agent-name>
AI_FOUNDRY_AGENT_VERSION=<agent-version>
```

## Authentication Model (Important)
This application uses Azure Entra ID authentication via:
```
DefaultAzureCredential()
```
What this means:

- ✅ No API keys are stored in code
- ✅ No secrets are committed to source control
- ✅ Access is controlled using Azure RBAC


## Running the Application
```
az login
az account set
streamlit run app.py
http://localhost:8501

```

## Project Structure

```
ck-ai-agent-demo/
│
├── app.py                     # Streamlit entry point
├── agent/
│   ├── __init__.py
│   ├── client.py               # AI Foundry / Agent wrapper
│
├── ui/
│   ├── __init__.py
│   ├── layout.py               # Page layout & styling
│   ├── chat.py                 # Chat UI logic
│
├── config/
│   ├── settings.py             # Agent name, endpoint, branding
│
├── assets/
│   ├── ck_logo.png             # Optional Connected Kerb logo
│
├── requirements.txt
└── README.md
```