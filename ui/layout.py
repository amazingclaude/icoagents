import streamlit as st

from config.settings import (
    ACCENT_COLOR,
    APP_SUBTITLE,
    APP_TITLE,
    MUTED_TEXT_COLOR,
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    SURFACE_COLOR,
    TEXT_COLOR,
)


def apply_page_config():
    st.set_page_config(
        page_title=APP_TITLE,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        f"""
        <style>
            :root {{
                --ck-primary: {PRIMARY_COLOR};
                --ck-accent: {ACCENT_COLOR};
                --ck-surface: {SURFACE_COLOR};
                --ck-surface-alt: {SECONDARY_COLOR};
                --ck-text: {TEXT_COLOR};
                --ck-muted: {MUTED_TEXT_COLOR};
            }}

            .stApp {{
                background:
                    radial-gradient(circle at top right, rgba(166, 206, 57, 0.15), transparent 28%),
                    linear-gradient(180deg, #f8faf8 0%, var(--ck-surface) 100%);
            }}

            [data-testid="stSidebar"] {{
                background: linear-gradient(180deg, rgba(51, 69, 79, 0.98) 0%, rgba(22, 49, 58, 0.98) 100%);
                border-right: 1px solid rgba(255, 255, 255, 0.08);
            }}

            [data-testid="stSidebar"] * {{
                color: #f5f7f6;
            }}

            .ck-shell {{
                padding: 1rem 0 0.5rem 0;
            }}

            .ck-hero {{
                background: linear-gradient(135deg, rgba(51, 69, 79, 0.98) 0%, rgba(29, 55, 64, 0.96) 58%, rgba(166, 206, 57, 0.92) 100%);
                border-radius: 24px;
                padding: 2.2rem;
                color: white;
                box-shadow: 0 22px 50px rgba(30, 51, 59, 0.14);
                margin-bottom: 1.25rem;
            }}

            .ck-kicker {{
                font-size: 0.82rem;
                font-weight: 700;
                letter-spacing: 0.18em;
                text-transform: uppercase;
                opacity: 0.82;
                margin-bottom: 0.7rem;
            }}

            .ck-hero h1 {{
                margin: 0;
                font-size: 2.45rem;
                line-height: 1.05;
            }}

            .ck-hero p {{
                margin: 0.9rem 0 0 0;
                font-size: 1.02rem;
                max-width: 46rem;
                color: rgba(255, 255, 255, 0.88);
            }}

            .ck-panel {{
                background: rgba(255, 255, 255, 0.82);
                border: 1px solid rgba(51, 69, 79, 0.08);
                border-radius: 20px;
                padding: 1.1rem 1.2rem;
                box-shadow: 0 16px 38px rgba(51, 69, 79, 0.06);
                margin-bottom: 1rem;
            }}

            .ck-panel h3 {{
                margin: 0 0 0.35rem 0;
                color: var(--ck-primary);
                font-size: 1rem;
            }}

            .ck-panel p {{
                margin: 0;
                color: var(--ck-muted);
                font-size: 0.95rem;
            }}

            .ck-sidebar-title {{
                font-size: 1.1rem;
                font-weight: 700;
                margin: 0.6rem 0 0.2rem 0;
            }}

            .ck-sidebar-text {{
                font-size: 0.92rem;
                line-height: 1.45;
                color: rgba(245, 247, 246, 0.78);
                margin-bottom: 1rem;
            }}

            .stButton > button {{
                border-radius: 999px;
                border: 1px solid rgba(51, 69, 79, 0.12);
                background: white;
                color: var(--ck-primary);
                font-weight: 600;
            }}

            [data-testid="stSidebar"] .stButton > button {{
                width: 100%;
                justify-content: flex-start;
                border: 1px solid rgba(255, 255, 255, 0.12);
                background: rgba(255, 255, 255, 0.06);
                color: white;
                padding: 0.55rem 0.8rem;
            }}

            .stChatInputContainer {{
                background: rgba(255, 255, 255, 0.95);
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header():
    st.markdown(
        f"""
        <div class="ck-shell">
            <div class="ck-hero">
                <div class="ck-kicker">Connected Kerb Demo</div>
                <h1>{APP_TITLE}</h1>
                <p>{APP_SUBTITLE}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_intro():
    st.markdown(
        """
        <div class="ck-panel">
            <h3>How this demo helps</h3>
            <p>
                Explore how an AI assistant can support Connected Kerb teams with programme planning,
                stakeholder messaging, policy interpretation, and operational guidance in a secure demo setting.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
