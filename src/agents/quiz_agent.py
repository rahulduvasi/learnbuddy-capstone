# src/agents/quiz_agent.py
import random

class QuizAgent:
    def __init__(self, memory):
        self.memory = memory

    def generate_quiz(self, lessons, num_q=3):
        questions = []
        for i, lesson in enumerate(lessons[:num_q]):
            q = {
                'id': f'q{i+1}',
                'question': f"What is a key idea from: {lesson['title']}?",
                'options': ['Option A', 'Option B', 'Option C', 'Option D'],
                'answer': 'Option A'  # placeholder; content agent could supply correct answer
            }
            questions.append(q)
        return questions

    def simulate_answers(self, questions):
        # Random simulated answers for demo
        return {q['id']: random.choice(q['options']) for q in questions}

    def grade(self, questions, answers):
        total = len(questions)
        correct = 0
        for q in questions:
            if answers.get(q['id']) == q['answer']:
                correct += 1
        score = int((correct / total) * 100) if total else 0
        return score
