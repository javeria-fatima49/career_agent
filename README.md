# 🎓 Career Mentor Agent (Multi-Agent System)

This project is an interactive **Career Guidance AI Assistant** that helps students explore career paths, required skills, and real-world job roles.

---

## 🧠 What It Does

This agent system simulates a mentor that:

- 📌 Recommends career paths based on user input
- 🧠 Provides a roadmap of skills using Tool functions
- 💼 Suggests real-world job roles related to the career
- 🔄 Passes control between agents using handoff logic

---

## 🧱 Architecture Overview

```txt
User Input → CareerAgent → SkillAgent → JobAgent → Reply shown in Chainlit UI
🧠 Agents Included
Agent	Role
🤖 CareerAgent	Detects user interest and suggests a career using Gemini
🧠 SkillAgent	Generates a skill-building roadmap for the selected field
💼 JobAgent	Lists real-world job titles and sample positions related to the career

🧰 Tools Used
get_career_roadmap(field) → Returns skills for given field

get_job_roles(field) → Returns job examples for that field

🔗 Technologies
✅ Gemini 1.5 Flash by Google (via google.generativeai)

✅ Chainlit for Chat UI

✅ Python 3.10+

---

🗂️ Folder Structure
multi-agents/
├── main.py         # Chainlit app with all agent logic
├── career_agent.py
├── skill_agent.py
├── job_agent.py
├── tools/
│   ├── get_career_roadmap.py
│   └── get_job_roles.py
🚀 How to Run
Install required libraries manually:

pip install chainlit google-generativeai 
Set your Gemini API key in .env file:

GEMINI_API_KEY=AIzaSyDk...YourKeyHere
Run the Chainlit app:

chainlit run main.py
Interact in chat UI:
---
Write: I want to become a web developer

Agent will guide you step by step ✅

📋 Example Flow
👩 User: I want to become a data scientist

CareerAgent suggests: Data Scientist

SkillAgent lists required tools (Python, Pandas, ML, etc.)

JobAgent lists job titles like Junior Data Scientist, ML Engineer, etc.
---
💡 Features
💬 Gemini-generated smart replies

🔄 Agent-to-agent handoff logic

✅ Dynamic skill and job tool integration

💻 Clean Chainlit interface for live demo

🙋 Created By
Javeria Fatima
(GIAIC Student | Passionate about AI & Career Empowerment)
