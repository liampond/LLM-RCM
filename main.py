from dotenv import load_dotenv
import openai
import os
from settings import MODEL_NAME, TEMPERATURE, NUM_RESPONSES

# ==============================
# 🔧 CONFIGURABLE VARIABLES
# ==============================
DATATYPE = "MEI"         # Options: "ABC", "HumDrum", "MEI", "MusicXML"
EXAM = "RCM6"            # Options: "RCM5", "RCM6"
CONTEXT = "NoContext"    # Options: "Context", "NoContext"
FILENAME = "RCM6_August2024_Q1a_NoContextPrompt.txt"  # The specific prompt file to load

# ==============================
# 🔑 API INITIALIZATION
# ==============================
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# ==============================
# 📂 FILE PATHS
# ==============================
BASE_DIR = "/Users/liampond/LLM-RCM/Prompts"

# System prompt
SYSTEM_PROMPT_PATH = os.path.join(BASE_DIR, "AllPrompts", "AllPromptsSystem.txt")

# First user prompt based on datatype
FIRST_USER_PROMPT_PATH = os.path.join(BASE_DIR, "AllPrompts", f"AllPromptsUser_{DATATYPE}.txt")

# Final user prompt from EXAM and CONTEXT folders
FINAL_USER_PROMPT_PATH = os.path.join(BASE_DIR, EXAM, CONTEXT, FILENAME)

# Output filepath
OUTPUT_PATH = "/Users/liampond/LLM-RCM/Outputs/ChatGPT/RCM6_August2024_Q1a_Output_MEI.txt"

# ==============================
# 📥 LOAD PROMPTS
# ==============================
def load_prompt(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"⚠️ File not found: {file_path}")
        return ""

# Load prompts
system_prompt = load_prompt(SYSTEM_PROMPT_PATH)
first_user_prompt = load_prompt(FIRST_USER_PROMPT_PATH)
final_user_prompt = load_prompt(FINAL_USER_PROMPT_PATH)

# ==============================
# 💬 SET UP CONVERSATION
# ==============================
conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": first_user_prompt},
    {"role": "user", "content": final_user_prompt}
]

# ==============================
# 🚀 MAKE API REQUEST
# ==============================
response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=conversation,
    temperature=TEMPERATURE,
    n=NUM_RESPONSES
)

# ==============================
# 💾 SAVE THE RESPONSE
# ==============================
with open(OUTPUT_PATH, "w") as file:
    file.write(f"{EXAM} - {CONTEXT} - Custom Prompt Analysis\n")
    file.write("=" * 60 + "\n\n")

    for i, choice in enumerate(response.choices):
        file.write(f"Response {i + 1}:\n")
        file.write(choice.message.content.strip() + "\n")
        file.write("-" * 60 + "\n\n")

    # Token usage stats
    file.write("Token Usage Summary:\n")
    file.write(f"Prompt tokens used: {response.usage.prompt_tokens}\n")
    file.write(f"Completion tokens used: {response.usage.completion_tokens}\n")
    file.write(f"Total tokens used: {response.usage.total_tokens}\n")

print(f"\n✅ Responses have been saved to {OUTPUT_PATH}")
