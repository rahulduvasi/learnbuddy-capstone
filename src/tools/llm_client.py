# src/tools/llm_client.py
# Placeholder LLM client - replace with real provider (Gemini/OpenAI) calls.
import os
from dotenv import load_dotenv
load_dotenv()

class LLMClient:
    def __init__(self):
        # load env variables or keys (DO NOT commit keys)
        self.provider = os.getenv('LLM_PROVIDER', 'mock')

    def generate_text(self, prompt, max_tokens=256):
        # Mock implementation for testing offline
        return f"[LLM MOCK] Generated content for prompt: {prompt}"
