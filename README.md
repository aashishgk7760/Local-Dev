# 🧠 AI Dev Agent

A terminal-based AI coding assistant powered by OpenAI, designed to help developers scaffold and iteratively build full-stack projects using natural language prompts.

---

## ✨ Features

- 📁 **Generate Project Structure:** Create frontend and backend folders and files based on prompt.
- 🧠 **Context-Aware Coding:** Understands your project and adds features via follow-up prompts (e.g., "Add a login page").
- 💾 **Writes Code to Files:** Supports full code generation and saves it in the correct structure.
- 🛠️ **Executes Commands:** Can run commands like `npm install`, `pip install`, and `npm run build` in the project directory.
- 🔁 **Prompt History Memory:** Maintains context for follow-up interactions.

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/your-username/ai-dev-agent.git
cd ai-dev-agent

### 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate


### 3. Install dependencies
pip install openai python-dotenv

### 4.Set your OpenAI API key

Create a .env file in the root directory:

echo "OPENAI_API_KEY=your-api-key-here" > .env

🧪 How to Use
python AI-dev.py


You: Create a React frontend and Flask backend
🤖 Agent: (responds with folder structure, installation commands)

You: Add a login page to the frontend
🤖 Agent: (adds necessary files and code)
