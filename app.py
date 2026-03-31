import streamlit as st
from ui.layout import apply_page_config, render_header, render_intro
from ui.chat import init_chat_state, render_chat

def main():
    apply_page_config()
    render_header()
    render_intro()

    init_chat_state()
    render_chat()

if __name__ == "__main__":
    main()