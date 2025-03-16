import streamlit as st
from .styles import CUSTOM_CSS

def initialize_ui():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    st.title("🚀 Offline Code Assistant")
    st.caption("⚙️LLAMA, LangChain, Ollama, and more!")

def display_chat_history(message_log):
    for message in message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])