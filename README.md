# LearnBuddy – AI-Powered Personalized Study Coach  
**Track:** Agents for Good  
**Version:** C (Advanced – Multi-Agent + Tools + Memory + Observability)  
**Language:** Python  

LearnBuddy is a multi-agent educational assistant designed to help underserved students access personalized learning. The system generates custom micro-lessons, quizzes, progress tracking, and actionable feedback using an LLM-powered agent framework.

---

## ⭐ 1. Problem Statement  
Millions of students lack access to personalized, affordable tutoring. Traditional learning materials do not adapt to the learner’s pace, weak areas, or preferred learning style.

---

## ⭐ 2. Solution – LearnBuddy AI  
LearnBuddy provides:  
- Multi-agent learning pipeline  
- Micro-lessons generation  
- Quiz creation and auto-grading  
- Long-term progress tracking  
- Feedback and learning recommendations  
- Mock search tool for curated resources  
- Logging, metrics, and observability  

---

## ⭐ 3. Architecture Overview  
```
Student → Intake Agent
            ↓
        Planner Agent
            ↓
   +---------------------+
   |    Parallel Agents  |
   |  Content Agent      |
   |  Quiz Agent         |
   |  Search Agent*      |
   +---------------------+
            ↓
      Feedback Agent
            ↓
       Memory Store
```

---

## ⭐ 4. Project Structure  
```
learnbuddy-capstone/
│
├── README.md
├── requirements.txt
├── data/
│   └── students.json
├── src/
│   ├── main.py
│   ├── agents/
│   │   ├── intake.py
│   │   ├── planner.py
│   │   ├── content_agent.py
│   │   ├── quiz_agent.py
│   │   └── feedback_agent.py
│   ├── tools/
│   │   ├── llm_client.py
│   │   ├── search_tool.py
│   │   └── code_exec.py
│   ├── memory/
│   │   └── memory_store.py
│   └── utils/
│       └── logger.py
└── logs/
```

---

## ⭐ 5. How to Run Locally  
### Step 1 — Create virtual environment  
```
python -m venv venv
venv\Scriptsctivate
```

### Step 2 — Install dependencies  
```
pip install -r requirements.txt
```

### Step 3 — Run  
```
python src/main.py
```

---

## ⭐ 6. LLM Configuration (Optional)  
Create `.env` file:

```
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
```

---

## ⭐ 7. Tools  
- **LLM Client** → `tools/llm_client.py`  
- **Search Tool (mock)** → `tools/search_tool.py`  
- **Code Execution Tool** → `tools/code_exec.py`  

---

## ⭐ 8. Memory System  
JSON-based long‑term memory stored at:
```
data/students.json
```

---

## ⭐ 9. Logging & Observability  
Logs stored in:
```
logs/run.log
```

---

## ⭐ 10. Future Improvements  
- Gemini / OpenAI integration  
- Real web search  
- FAISS vector memory  
- UI with Flask/Streamlit  
- Notebook visual analytics  

---

## ⭐ 11. License  
MIT License.

---

## ⭐ 12. Credits  
Built by **Rahul Duvasi**, guided by AI.
