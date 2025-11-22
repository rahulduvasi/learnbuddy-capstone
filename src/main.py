# src/main.py
"""Orchestrator for LearnBuddy - demonstrates a simple run of the multi-agent flow."""
from agents.intake import IntakeAgent
from agents.planner import PlannerAgent
from agents.content_agent import ContentAgent
from agents.quiz_agent import QuizAgent
from agents.feedback_agent import FeedbackAgent
from memory.memory_store import MemoryStore
from utils.logger import get_logger

def demo_run():
    logger = get_logger('learnbuddy')
    memory = MemoryStore('data/students.json')

    intake = IntakeAgent(memory)
    planner = PlannerAgent(memory)
    content = ContentAgent(memory)
    quiz = QuizAgent(memory)
    feedback = FeedbackAgent(memory)

    # Collect student profile (interactive in real demo; here we simulate)
    student = intake.collect_profile_simulated()
    logger.info(f"Collected profile: {student}")

    # Create plan
    plan = planner.create_plan(student)
    logger.info(f"Plan created: {plan}")

    # Generate lessons
    lessons = content.generate_lessons(plan)
    logger.info(f"Generated {len(lessons)} lessons.")

    # Generate quiz
    questions = quiz.generate_quiz(lessons)
    logger.info(f"Generated {len(questions)} questions.")

    # Simulate answers
    answers = quiz.simulate_answers(questions)
    score = quiz.grade(questions, answers)
    logger.info(f"Student {student['name']} scored {score}% on the quiz.")

    # Update feedback & memory
    feedback_text = feedback.summarize_feedback(score, questions, answers)
    memory.update_progress(student['id'], score, feedback_text)
    logger.info("Run complete. Check data/ and logs/ for outputs.")

if __name__ == '__main__':
    demo_run()
