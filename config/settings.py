# ChatGPT Configuration
CHATGPT_MODEL = "gpt-4o-2024-11-20"
TEMPERATURE = 0
NUM_RESPONSES = 1

# API Keys (loaded from .env)
import os
from dotenv import load_dotenv

load_dotenv()

CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# File extension mapping
EXTENSION_MAP = {
    "MEI": ".mei",
    "MusicXML": ".musicxml",
    "HumDrum": ".krn",
    "ABC": ".abc"
}

# List of questions without encoded files
QUESTIONS_WITHOUT_ENCODED_FILES = ["Q3a", "Q3b", "Q3c", "Q3d", "Q3e", "Q5", "Q9"]
