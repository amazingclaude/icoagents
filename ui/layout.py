import streamlit as st
from config.settings import APP_TITLE, APP_SUBTITLE

def apply_page_config():
    st.set_page_config(
        page_title=APP_TITLE,
        layout="wide",
    )

def render_header():
    st.markdown(
        f"""
        <div style="padding: 1.5rem 0;">
            <h1 style="margin-bottom: 0;">{APP_TITLE}</h1>
            <p style="color: #555; font-size: 1.1rem;">
                {APP_SUBTITLE}
            </p>
        </div>
        <hr/>
        """,
        unsafe_allow_html=True,
    )

def render_intro():
    st.info(
        """
        This assistant demonstrates how AI can support Connected Kerb teams by:
        - Answering operational and policy questions
        - Providing contextual guidance from knowledge sources
        - Acting as a secure interface to internal intelligence

        This is a demo environment.
        """
    )
