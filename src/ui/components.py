import streamlit as st
import os
from typing import List
import uuid
from .styles import CUSTOM_CSS

def initialize_ui():
    """Initialize the Streamlit UI configuration."""
    st.set_page_config(
        page_title="Offline Code Assistant",
        page_icon="🚀",
        layout="wide",
    )
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    # Create container for header
    header_container = st.container()
    with header_container:
        st.title("🚀 Offline Code Assistant")
        st.caption("⚙️ LLAMA, LangChain, Ollama, Python and more!")
    # Add separator
    st.markdown("---")

def setup_sidebar():
    """Setup the sidebar with PDF management controls."""
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    with st.sidebar:
        st.header("Document Management")
        
        # Initialize session state for upload tracking
        if "uploaded_files" not in st.session_state:
            st.session_state.uploaded_files = set()
        
        # File uploader
        uploaded_file = st.file_uploader("Upload PDF", type=['pdf'])
        
        if uploaded_file is not None and uploaded_file.name not in st.session_state.uploaded_files:
            # Generate unique filename
            unique_filename = f"{uuid.uuid4().hex[:8]}_{uploaded_file.name}"
            if save_uploaded_file(uploaded_file, unique_filename):
                st.session_state.uploaded_files.add(uploaded_file.name)
                st.success(f"Successfully uploaded: {uploaded_file.name}")
        
                # Display uploaded files
        st.subheader("Available Documents")
        upload_dir = os.path.join(os.getcwd(), "uploads")
        if os.path.exists(upload_dir):
            files = [f for f in os.listdir(upload_dir) if f.endswith('.pdf')]
            
            if files:
                selected_file = st.selectbox(
                    "Select a document:",
                    options=files,
                    format_func=lambda x: x.split('_', 1)[1]  # Show original filename
                )
                
                if selected_file:
                    if st.button("Delete Selected Document"):
                        filepath = os.path.join(upload_dir, selected_file)
                        if delete_uploaded_file(filepath):
                            st.success("File deleted successfully!")
                            st.rerun()
            else:
                st.info("No documents uploaded yet.")
        
        # ...rest of the sidebar code...

def save_uploaded_file(uploaded_file, filename: str) -> bool:
    """Save uploaded file to disk."""
    upload_dir = os.path.join(os.getcwd(), "uploads")
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    filepath = os.path.join(upload_dir, filename)
    # Check if file already exists
    if os.path.exists(filepath):
        return True
    
    try:
        with open(filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except Exception as e:
        st.error(f"Error saving file: {str(e)}")
        return False

def delete_uploaded_file(filepath: str) -> bool:
    """Delete uploaded file from disk."""
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            # Remove from session state
            original_filename = os.path.basename(filepath).split('_', 1)[1]
            if original_filename in st.session_state.uploaded_files:
                st.session_state.uploaded_files.remove(original_filename)
        return True
    except Exception as e:
        st.error(f"Error deleting file: {str(e)}")
        return False

def display_chat_history(message_log):
    """Display chat message history."""
    for message in message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])