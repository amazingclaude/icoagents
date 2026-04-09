from pathlib import Path

# ===== Connected Kerb branding =====

APP_TITLE = "Connected Kerb AI Assistant"
APP_SUBTITLE = "Professional demo for EV infrastructure planning, operations, and policy support"

PRIMARY_COLOR = "#33454F"
ACCENT_COLOR = "#A6CE39"
SECONDARY_COLOR = "#EEF3EF"
SURFACE_COLOR = "#F6F8F7"
TEXT_COLOR = "#16313A"
MUTED_TEXT_COLOR = "#6A7A80"

STARTER_QUESTIONS = [
    "What are the key considerations when scoping a new kerbside charging rollout?",
    "Summarise the main risks and mitigations for a borough deployment programme.",
    "How should we explain Connected Kerb's value proposition to a local authority stakeholder?",
]

CHAT_HISTORY_PATH = Path(".streamlit") / "connected_kerb_history.json"
MAX_HISTORY_ITEMS = 10

# ===== AI Foundry Agent =====

AI_FOUNDRY_ENDPOINT = "https://ckagents.services.ai.azure.com/api/projects/ckagents"

AGENT_NAME = "CK-Planning-Agent"
AGENT_VERSION = "10"


