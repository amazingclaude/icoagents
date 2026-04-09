import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

import streamlit as st

from agent.client import ConnectedKerbAgent
from config.settings import CHAT_HISTORY_PATH, MAX_HISTORY_ITEMS, STARTER_QUESTIONS


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _history_path() -> Path:
    return Path(CHAT_HISTORY_PATH)


def _default_title() -> str:
    return f"New chat {datetime.now().strftime('%d %b %H:%M')}"


def _build_title(messages: list[dict[str, str]]) -> str:
    for message in messages:
        if message["role"] == "user" and message["content"].strip():
            return message["content"].strip()[:60]
    return _default_title()


def _load_conversations() -> list[dict]:
    history_path = _history_path()
    if not history_path.exists():
        return []

    try:
        payload = json.loads(history_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

    if not isinstance(payload, list):
        return []

    conversations = []
    for item in payload:
        if not isinstance(item, dict):
            continue

        raw_messages = item.get("messages", [])
        messages = [
            {
                "role": message.get("role", "assistant"),
                "content": message.get("content", ""),
            }
            for message in raw_messages
            if isinstance(message, dict)
        ]
        created_at = item.get("created_at") or _utc_now()
        updated_at = item.get("updated_at") or created_at

        conversations.append(
            {
                "id": item.get("id", str(uuid4())),
                "title": item.get("title") or _build_title(messages),
                "created_at": created_at,
                "updated_at": updated_at,
                "messages": messages,
            }
        )

    return sorted(
        conversations,
        key=lambda conversation: conversation["updated_at"],
        reverse=True,
    )[:MAX_HISTORY_ITEMS]


def _save_conversations() -> None:
    history_path = _history_path()
    history_path.parent.mkdir(parents=True, exist_ok=True)
    history_path.write_text(
        json.dumps(st.session_state.conversations, indent=2),
        encoding="utf-8",
    )


def _create_conversation() -> dict:
    timestamp = _utc_now()
    return {
        "id": str(uuid4()),
        "title": _default_title(),
        "created_at": timestamp,
        "updated_at": timestamp,
        "messages": [],
    }


def _get_current_conversation() -> dict:
    conversation_id = st.session_state.current_conversation_id
    for conversation in st.session_state.conversations:
        if conversation["id"] == conversation_id:
            return conversation

    conversation = _create_conversation()
    st.session_state.conversations.insert(0, conversation)
    st.session_state.current_conversation_id = conversation["id"]
    _save_conversations()
    return conversation


def _touch_conversation(conversation: dict) -> None:
    conversation["title"] = _build_title(conversation["messages"])
    conversation["updated_at"] = _utc_now()
    st.session_state.conversations.sort(
        key=lambda item: item["updated_at"],
        reverse=True,
    )
    st.session_state.current_conversation_id = conversation["id"]
    st.session_state.conversations = st.session_state.conversations[:MAX_HISTORY_ITEMS]
    _save_conversations()


def _start_new_chat() -> None:
    conversation = _create_conversation()
    st.session_state.conversations.insert(0, conversation)
    st.session_state.conversations = st.session_state.conversations[:MAX_HISTORY_ITEMS]
    st.session_state.current_conversation_id = conversation["id"]
    _save_conversations()


def init_chat_state():
    if "agent" not in st.session_state:
        st.session_state.agent = ConnectedKerbAgent()

    if "conversations" not in st.session_state:
        conversations = _load_conversations()
        if not conversations:
            conversations = [_create_conversation()]
        st.session_state.conversations = conversations

    if "current_conversation_id" not in st.session_state:
        st.session_state.current_conversation_id = st.session_state.conversations[0]["id"]

    if "pending_prompt" not in st.session_state:
        st.session_state.pending_prompt = None


def render_chat_sidebar():
    with st.sidebar:
        st.image("assets/ck_logo.png", width=180)
        st.markdown('<div class="ck-sidebar-title">Conversation history</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="ck-sidebar-text">Switch between saved chats, start a new thread, or pick up where you left off.</div>',
            unsafe_allow_html=True,
        )

        if st.button("New chat", use_container_width=True):
            _start_new_chat()
            st.rerun()

        st.markdown("##### Recent chats")
        for conversation in st.session_state.conversations[:MAX_HISTORY_ITEMS]:
            button_type = "primary" if conversation["id"] == st.session_state.current_conversation_id else "secondary"
            if st.button(
                conversation["title"],
                key=f"conversation-{conversation['id']}",
                use_container_width=True,
                type=button_type,
            ):
                st.session_state.current_conversation_id = conversation["id"]
                st.rerun()


def _queue_starter(prompt: str) -> None:
    st.session_state.pending_prompt = prompt


def _render_empty_state():
    st.markdown(
        """
        <div class="ck-panel">
            <h3>Ask a strategic or operational question</h3>
            <p>
                Try a starter prompt below, or type your own question about planning, delivery, policy, or stakeholder engagement.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    columns = st.columns(len(STARTER_QUESTIONS))
    for column, prompt in zip(columns, STARTER_QUESTIONS):
        with column:
            if st.button(prompt, key=f"starter-{prompt}", use_container_width=True):
                _queue_starter(prompt)
                st.rerun()


def _run_prompt(prompt: str, conversation: dict) -> None:
    conversation["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Preparing a Connected Kerb response..."):
            response = st.session_state.agent.ask(conversation["messages"])
            st.markdown(response)

    conversation["messages"].append({"role": "assistant", "content": response})
    _touch_conversation(conversation)


def render_chat():
    conversation = _get_current_conversation()

    if not conversation["messages"]:
        _render_empty_state()

    for message in conversation["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask about Connected Kerb delivery, planning, policy, or operations")
    prompt = st.session_state.pending_prompt or user_input
    st.session_state.pending_prompt = None

    if prompt:
        _run_prompt(prompt, conversation)
