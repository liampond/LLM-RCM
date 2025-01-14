# Prompt settings
EXAM = "RCM6"             # Options: "RCM5" or "RCM6"
CONTEXT = "NoContext"     # Options: "Context" or "NoContext"
QUESTION = "Q1a"          # Options: "Q#"
YEAR = "August2024"       # Option: "August2024"

# API settings
DATATYPE = "MEI"          # Options: "ABC", "HumDrum", "MEI", "MusicXML"
MODEL = "ChatGPT"         # Options: "ChatGPT", "Claude", "Gemini"

# General model configuration
TEMPERATURE = 0
NUM_RESPONSES = 5

# API Keys (loaded from .env)
import os
from dotenv import load_dotenv

load_dotenv()

CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

FILENAME = f"{EXAM}_{YEAR}_{QUESTION}_{CONTEXT}Prompt.txt" # Ensure EXAM and CONTEXT match in the FILENAME

# Prompt paths
BASE_PROMPT_DIR = "prompts"
SYSTEM_PROMPT_PATH = f"{BASE_PROMPT_DIR}/AllPrompts/AllPromptsSystem.txt"
FIRST_USER_PROMPT_PATH = f"{BASE_PROMPT_DIR}/AllPrompts/AllPromptsUser_{DATATYPE}.txt"
FINAL_USER_PROMPT_PATH = f"{BASE_PROMPT_DIR}/{EXAM}/{CONTEXT}/{FILENAME}"

# Output path
OUTPUT_DIR = f"outputs/{MODEL}/{EXAM}/{DATATYPE}/"
OUTPUT_FILENAME = f"{EXAM}_{YEAR}_{QUESTION}_{CONTEXT}_{DATATYPE}_Output.txt"
