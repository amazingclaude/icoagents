import streamlit as st
from agent.client import ConnectedKerbAgent

def init_chat_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "agent" not in st.session_state:
        st.session_state.agent = ConnectedKerbAgent()

def render_chat():
    # Display history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input box
    user_input = st.chat_input("Ask a question...")

    if user_input:
        # Show user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.agent.ask(user_input)
                st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )