
# Project Overview – LearnBuddy AI Study Coach

**NOTE:** This README follows the official Kaggle submission structure.  
It reflects a complete multi-agent system design for educational assistance.

LearnBuddy is a multi-agent AI-powered study coach designed to help students learn challenging topics through personalized study plans, micro-lessons, quizzes, feedback, and long‑term progress tracking.  
The system is built using a modular multi-agent architecture.

---

# Problem Statement

Many students struggle with self‑learning because they lack:

- Personalized learning paths  
- Beginner‑friendly explanations  
- Instant evaluation  
- Feedback loops  
- Progress tracking  
- Motivation & structure  

Without teachers or guidance, students get overwhelmed, confused, and often quit early.

LearnBuddy solves this by acting as a **virtual AI tutor**, delivering a fully guided & adaptive learning experience.

---

# Solution Statement

LearnBuddy uses a **multi‑agent pipeline** to automate the entire teaching cycle:

1. **Intake Agent** – understands the student  
2. **Planner Agent** – creates personalized learning plan  
3. **Content Agent** – generates micro‑lessons  
4. **Quiz Agent** – creates & grades quizzes  
5. **Feedback Agent** – provides improvement suggestions  
6. **Memory Store** – saves progress for long‑term learning  

Together, these create a structured, personalized, and efficient learning experience.

---

# Architecture

LearnBuddy is implemented as a modular multi‑agent ecosystem.

## 1. Intake Agent – Student Profiler
Collects:
- Student ID  
- Topic  
- Level  
- Learning style  
- Context for planning  

## 2. Planner Agent – Curriculum Designer
Generates a structured 3‑phase plan:
- Easy → Medium → Easy  
- Based on student level  
- Beginner‑friendly  
- Clear learning flow  

## 3. Content Agent – Lesson Generator
- Writes micro‑lessons  
- Simple explanations  
- Clean and easy to understand  
- Based on planner outputs  

## 4. Quiz Agent – Evaluator
- Generates MCQs  
- Based on the lessons  
- Simulates answers  
- Calculates score  

## 5. Feedback Agent – Mentor
- Reviews performance  
- Generates personalized feedback  
- Encourages improvements  

## 6. Memory Store – Long‑Term History
Stores:
- Lessons  
- Scores  
- Feedback  
- Student history  
- Performance trends  

Stored in `students.json` for future personalization.

---

# Workflow

**1. Intake → 2. Plan → 3. Lessons → 4. Quiz → 5. Feedback → 6. Memory**

A complete tutor cycle, similar to a human teaching workflow.

---

# Essential Tools & Utilities

### 🔧 LLM Client (Mock)
Simulates content generation.

### 🔧 Search Tool
Extensible for future information retrieval.

### 🔧 Code Execution Tool
Placeholder for future advanced tasks.

### 💾 Memory Store
Handles persistent learning data.

### 🧠 Logger
Tracks all agent actions.

---

# Conclusion

LearnBuddy demonstrates how multi‑agent systems can replicate a real tutor’s workflow using:

- Specialization of tasks  
- Agent coordination  
- Feedback loops  
- Memory mechanisms  

It is modular, extendable, and aligned with **Agents for Good**, helping beginners learn effectively with structured, personalized guidance.

---

# Value Statement

LearnBuddy helps students by:

- Reducing confusion  
- Structuring learning  
- Giving clear explanations  
- Providing feedback  
- Tracking progress  

If extended, it could include:

- Real LLM lesson generation  
- Diagrams & visual learning  
- Adaptive difficulty  
- Web/mobile app  
- Voice‑based tutoring  

---

# Installation

### Create environment:
```
python -m venv venv
venv\Scripts\activate
```

### Install dependencies:
```
pip install -r requirements.txt
```

### Run:
```
python src/main.py
```

---

# Project Structure
```
src/
  agents/
    intake.py
    planner.py
    content_agent.py
    quiz_agent.py
    feedback_agent.py
  memory/
    memory_store.py
  tools/
    llm_client.py
    search_tool.py
    code_exec.py
  utils/
    logger.py

data/
  students.json
logs/
README.md
requirements.txt
```

---

# Credits

Developed by **Rahul Duvasi**  
For **Kaggle Agents Intensive Capstone 2025**

