# src/agents/planner.py
class PlannerAgent:
    def __init__(self, memory):
        self.memory = memory

    def create_plan(self, student):
        # Very simple plan: 3 micro-lessons
        topic = student.get('topic', 'general')
        plan = {
            'student_id': student['id'],
            'topic': topic,
            'lessons': [
                {'title': f'Intro to {topic}', 'difficulty': 'easy'},
                {'title': f'{topic} Practice', 'difficulty': 'medium'},
                {'title': f'{topic} Tips & Tricks', 'difficulty': 'easy'}
            ]
        }
        return plan
