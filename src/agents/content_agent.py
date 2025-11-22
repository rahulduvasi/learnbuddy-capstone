# src/agents/content_agent.py
from tools.llm_client import LLMClient

class ContentAgent:
    def __init__(self, memory):
        self.memory = memory
        self.llm = LLMClient()

    def generate_lessons(self, plan):
        lessons = []
        for item in plan['lessons']:
            prompt = f"Create a short micro-lesson about {item['title']} for {item['difficulty']} learners."
            content = self.llm.generate_text(prompt)
            lessons.append({'title': item['title'], 'content': content})
        return lessons
