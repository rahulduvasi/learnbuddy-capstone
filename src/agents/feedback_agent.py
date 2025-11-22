# src/agents/feedback_agent.py
class FeedbackAgent:
    def __init__(self, memory):
        self.memory = memory

    def summarize_feedback(self, score, questions, answers):
        if score >= 80:
            return 'Great job! Move to the next topic.'
        elif score >= 50:
            return 'Good effort — review the middle lesson and retry.'
        else:
            return 'Review basics and try simpler exercises.'
