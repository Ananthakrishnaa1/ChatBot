# ChatBot

An offline chatbot powered by LLAMA, LangChain, and Ollama.

## Overview

This project implements a chatbot with a clean web interface using Streamlit. It leverages the LLAMA language model through Ollama for generating responses and LangChain for managing the conversation flow.

## Features

- 🤖 Offline operation using local LLAMA model
- 🎯 Expert coding assistance 
- 📝 Code generation capabilities
- 🐞 Debugging support
- 💬 Interactive chat interface
- 🎨 Dark mode UI
- 🛡️ Content moderation
- 💾 In-memory response caching

## Requirements

```txt
streamlit
langchain
langchain-ollama 
pydantic-settings
python-dotenv

Here's a sample README file to guide you through installing Ollama and the Llama 3.1:8B model:

---

# README: Installing Ollama and Llama 3.1:8B

## Prerequisites
1. **Operating System**: Ensure you are using a supported OS:
   - macOS 12+ (Intel & Apple Silicon)
   - Windows 10/11 with WSL2
   - Linux (Ubuntu 20.04+, Debian 11+, Fedora 37+)
2. **Hardware Requirements**:
   - CPU: 64-bit processor
   - RAM: Minimum 8GB (16GB recommended)
   - Storage: At least 10GB free space
   - GPU: Optional but recommended for better performance
3. **Dependencies**:
   - Python 3.8 or higher (for additional scripting)
   - Docker (optional for containerized setup)

---

## Step 1: Install Ollama
### macOS
1. Open Terminal.
2. Run the following command:
   ```bash
   brew install ollama
   ```
   Alternatively, use:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

### Linux
1. Open Terminal.
2. Run the following command:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

### Windows (via WSL2)
1. Enable WSL2:
   ```bash
   wsl --install
   ```
2. Install Ubuntu on WSL2:
   ```bash
   wsl --install -d Ubuntu
   ```
3. Inside WSL2, run:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

---

## Step 2: Verify Installation
1. Open your terminal or command prompt.
2. Type:
   ```bash
   ollama --version
   ```
   You should see the installed version of Ollama.

---

## Step 3: Download and Install Llama 3.1:8B
1. Open your terminal or command prompt.
2. Run the following command to download the Llama 3.1:8B model:
   ```bash
   ollama run llama3.1:8b
   ```
3. Wait for the download and installation to complete. This may take some time depending on your internet speed.

---

## Step 4: Test the Installation
1. Run the following command to test the model:
   ```bash
   ollama run llama3.1:8b "Hello, world!"
   ```
2. If the model responds, the installation is successful.

---

## Additional Notes
- For advanced configurations, such as GPU setup or custom model directories, refer to the [Ollama Documentation](https://ollama.readthedocs.io/en/quickstart/).
- Ensure you have sufficient system resources to run the Llama 3.1:8B model effectively.

---

Let me know if you need further assistance!


Setup
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

Configure environment variables in .env:

OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=llama3.1:8b
TEMPERATURE=0.3


streamlit run src/main.py

Project Structure

ChatBot/
├── src/
│   ├── config/        # Configuration settings
│   ├── core/          # Core chat functionality 
│   ├── ui/            # User interface components
│   ├── utils/         # Utility functions
│   └── main.py        # Application entry point
├── requirements.txt    # Project dependencies
└── .env               # Environment variables

Usage
Start the chat interface in your browser
Type coding questions in the input field
Get AI-powered responses for coding assistance
Continue the conversation naturally
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

