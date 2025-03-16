# Offline Code Assistant

An offline chatbot powered by Ollama, LLAMA, LangChain, Python.

## Overview

This project implements a chatbot with a clean web interface using Streamlit. It leverages the LLAMA language model through Ollama for generating responses and LangChain for managing the conversation flow.

## Features

- 🤖 Offline operation using local LLAMA model
- 🎯 Expert coding assistance 
- 📝 Code generation capabilities
- 🐞 Debugging support
- 💬 Interactive chat interface
- 🛡️ Content moderation
- 💾 In-memory response caching

## Requirements

```txt
streamlit
langchain
langchain-ollama 
pydantic-settings
python-dotenv


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

# ChatBot

## Setup

### Create and Activate a Virtual Environment
```bash
# For Linux/Mac
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
Create a `.env` file in the root directory and add the following:
```
OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=llama3.1:8b
TEMPERATURE=0.3
```

### Run the Application
To start the application, run:
```bash
streamlit run src/main.py
```

---

## Project Structure
```plaintext
ChatBot/
├── src/
│   ├── config/        # Configuration settings
│   ├── core/          # Core chat functionality 
│   ├── ui/            # User interface components
│   ├── utils/         # Utility functions
│   └── main.py        # Application entry point
├── requirements.txt    # Project dependencies
└── .env               # Environment variables
```

---

## Usage

1. Start the chat interface in your browser.
2. Type your coding questions in the input field.
3. Get AI-powered responses for coding assistance.
4. Continue the conversation naturally.

---


---

Feel free to adapt this format further to suit your project's needs. Let me know if you'd like any additional sections or details!

