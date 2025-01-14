# Prompt settings
EXAM = "RCM6"             # Options: "RCM5" or "RCM6"
CONTEXT = "NoContext"     # Options: "Context" or "NoContext"
QUESTION = "Q3a"          # Options: "Q#"
YEAR = "August2024"       # Option: "August2024"

# API settings
DATATYPE = "MEI"          # Options: "ABC", "HumDrum", "MEI", "MusicXML"
MODEL = "ChatGPT"         # Options: "ChatGPT", "Claude", "Gemini"

# ChatGPT Configuration
CHATGPT_MODEL = "gpt-4o-2024-11-20"
TEMPERATURE = 0
NUM_RESPONSES = 5

# API Keys (loaded from .env)
import os
from dotenv import load_dotenv

load_dotenv()

CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PROMPT_FILENAME = f"{EXAM}_{YEAR}_{QUESTION}_{CONTEXT}Prompt.txt" # Ensure EXAM and CONTEXT match in the PROMPT_FILENAME

# Prompt paths
BASE_PROMPT_DIR = "prompts"
SYSTEM_PROMPT_PATH = f"{BASE_PROMPT_DIR}/AllPrompts/AllPromptsSystem.txt"
FIRST_USER_PROMPT_PATH = f"{BASE_PROMPT_DIR}/AllPrompts/AllPromptsUser_{DATATYPE}.txt"
FINAL_USER_PROMPT_PATH = f"{BASE_PROMPT_DIR}/{EXAM}/{CONTEXT}/{PROMPT_FILENAME}"

# File extension mapping
EXTENSION_MAP = {
    "MEI": ".mei",
    "MusicXML": ".musicxml",
    "HumDrum": ".krn",
    "ABC": ".abc"
}

# Encoded file path
FILE_EXTENSION = EXTENSION_MAP.get(DATATYPE, ".txt")
ENCODED_FILENAME = f"{EXAM}_{YEAR}_{QUESTION}{FILE_EXTENSION}"

# List of questions without encoded files
QUESTIONS_WITHOUT_ENCODED_FILES = ["Q3a", "Q3b", "Q3c", "Q3d", "Q3e", "Q9"]  # Add questions that don't have encoded files here

# Function to check if the encoded file exists
def check_encoded_file_exists(question):
    if question in QUESTIONS_WITHOUT_ENCODED_FILES:
        print(f"Skipping encoded file check for {question} as it is known to have no encoded file.")
        return False
    encoded_file_path = os.path.join(BASE_PROMPT_DIR, f"{EXAM}_{YEAR}_{question}_{CONTEXT}Encoded.txt")
    if not os.path.exists(encoded_file_path):
        raise FileNotFoundError(f"Encoded file not found for {question}")
    return True

# Output path
OUTPUT_DIR = f"outputs/{MODEL}/{EXAM}/{DATATYPE}/"
OUTPUT_FILENAME = f"{EXAM}_{YEAR}_{QUESTION}_{CONTEXT}_{DATATYPE}_Output.txt"

# Example usage
try:
    if check_encoded_file_exists(QUESTION):
        # Proceed with loading the encoded file
        pass
except FileNotFoundError as e:
    print(e)
