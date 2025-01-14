import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model settings
CHATGPT_MODEL = "gpt-4o-2024-11-20"
TEMPERATURE = 0
NUM_RESPONSES = 5