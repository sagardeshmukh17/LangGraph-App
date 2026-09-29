# 🎓 Student Support Chatbot  
Built with **LangGraph + Ollama + SQLite**

## 🚀 Overview
This project is a simple student support chatbot that answers queries like fee details, batch timings, and course info.  
It uses:
- **LangGraph** for workflow orchestration
- **Ollama** for LLM responses
- **SQLite** for student database management
- **Python dotenv** for environment configuration

## 📂 Project Structure
06-LangGraph-App/
│── config/
│   └── settings.py
│── database/
│   └── db.py
│── .env
│── requirements.txt
│── app.py



## ⚙️ Setup
1. Create the project

2. Create virtual environment:
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Configure .env:
OLLAMA_MODEL=gemma:latest
OLLAMA_TEMPERATURE=0
DATABASE_NAME=students.db
EXTERNAL_API_URL=https://jsonplaceholder.typicode.com/todos/1

5. Initialize database:
python -m database.db

6. Run chatbot:
streamlit run app.py

LangChain → Tools are often called in a linear chain. Each step runs one after another, even if not needed.

LangGraph → At one time, only one tool/node responds, based on the graph’s state.
This avoids unnecessary sequential calls.
Example: If the user asks “How much fee is due?”, only the DB node runs → fetches fee → passes to LLM → final answer.
No wasted calls like “search → calculator → DB” unless required.
