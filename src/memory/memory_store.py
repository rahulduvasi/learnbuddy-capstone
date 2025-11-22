# src/memory/memory_store.py
import json, os
from pathlib import Path

class MemoryStore:
    def __init__(self, path='data/students.json'):
        self.path = path
        Path(os.path.dirname(path) or '.').mkdir(parents=True, exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump({'students': [], 'progress': []}, f)

    def _read(self):
        with open(self.path, 'r') as f:
            return json.load(f)

    def _write(self, obj):
        with open(self.path, 'w') as f:
            json.dump(obj, f, indent=2)

    def save_student(self, student):
        obj = self._read()
        obj['students'].append(student)
        self._write(obj)

    def update_progress(self, student_id, score, feedback):
        obj = self._read()
        obj['progress'].append({
            'student_id': student_id,
            'score': score,
            'feedback': feedback
        })
        self._write(obj)
