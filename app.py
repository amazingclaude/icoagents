from ui.layout import apply_page_config, render_header
from ui.chat import init_chat_state, render_chat, render_chat_sidebar


def main():
    apply_page_config()
    init_chat_state()
    render_chat_sidebar()
    render_header()
    render_chat()


if __name__ == "__main__":
    main()
