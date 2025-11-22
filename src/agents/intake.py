# src/agents/intake.py
import uuid
import json
import os

class IntakeAgent:
    def __init__(self, memory):
        self.memory = memory

    def collect_profile_simulated(self):
        # Simulated profile for demo purposes
        student = {
            'id': str(uuid.uuid4()),
            'name': 'Demo Student',
            'level': 'beginner',
            'topic': 'fractions',
            'learning_style': 'visual'
        }
        # Persist initial profile
        self.memory.save_student(student)
        return student

    def collect_profile_interactive(self):
        # Replace this with interactive input prompts in notebook or UI
        name = input('Student name: ')
        topic = input('Topic to learn: ')
        level = input('Level (beginner/intermediate/advanced): ')
        student = {
            'id': str(uuid.uuid4()),
            'name': name,
            'level': level,
            'topic': topic,
            'learning_style': 'visual'
        }
        self.memory.save_student(student)
        return student
