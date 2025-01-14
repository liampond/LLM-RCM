from models.chatgpt_api import chatgpt_request
from models.claude_api import claude_request
from models.gemini_api import gemini_request
from utils.prompt_loader import load_prompt
from utils.file_manager import save_response
from settings import CHATGPT_API_KEY, CLAUDE_API_KEY, GEMINI_API_KEY

# Configurable model selection
MODEL = "ChatGPT"  # Options: "ChatGPT", "Claude", "Gemini"
PROMPT_PATH = "prompts/RCM6/NoContext/prompt_01.txt"
OUTPUT_FILENAME = "response_output.txt"

# Load the selected prompt
prompt = load_prompt(PROMPT_PATH)
conversation = [
    {"role": "system", "content": "You are a music theorist."},
    {"role": "user", "content": prompt}
]

# Handle model-specific requests
if MODEL == "ChatGPT":
    response = chatgpt_request(conversation, CHATGPT_API_KEY)
elif MODEL == "Claude":
    response = claude_request(conversation, CLAUDE_API_KEY)
elif MODEL == "Gemini":
    response = gemini_request(conversation, GEMINI_API_KEY)
else:
    raise ValueError("Invalid model selected!")

# Save the response
save_response(MODEL, OUTPUT_FILENAME, str(response))

print(f"✅ {MODEL} response saved to outputs/{MODEL}/{OUTPUT_FILENAME}")
