# 🐝 Ask the Hive

An AI-powered multi-agent expert panel that answers complex, multi-domain questions across Legal, Finance, Tech, Marketing, and Creative perspectives.

Built with:
- Gradio 4.x
- OpenAI GPT-4-turbo
- Python 3.10+

---

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ask-the-hive.git
cd ask-the-hive

2. pip install -r requirements.txt

Create a .env file and paste your OpenAI key inside:
3. OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Start the app:
python app.py

http://127.0.0.1:7860/

Project Structure:
File | Purpose
app.py | Main Gradio app UI
agents.py | Agent logic for Legal, Finance, Tech, Marketing, Creative
synthesizer.py | Synthesizer bot that consolidates all agent answers
requirements.txt | Dependency list
.gitignore | Ignores .env and local files
README.md | Project documentation

✨ Features
🔹 Multi-agent architecture — 5 domain experts generate independent takes

🔹 Executive synthesis — Combines all views into 1 strategic summary

🔹 Follow-up mode — Ask deeper questions to individual agents

🔹 Simple Gradio UI — Fast, interactive panel layout

🔹 Deployable to Hugging Face Spaces

📄 Requirements
Python 3.10+

Gradio

OpenAI

Python-dotenv
