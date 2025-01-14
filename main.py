from models.chatgpt_api import chatgpt_request
from models.claude_api import claude_request
from models.gemini_api import gemini_request
from utils.prompt_loader import load_prompt
from utils.file_manager import save_response
from settings import (
    CHATGPT_API_KEY, CLAUDE_API_KEY, GEMINI_API_KEY, CHATGPT_MODEL, 
    TEMPERATURE, NUM_RESPONSES, SYSTEM_PROMPT_PATH, 
    FIRST_USER_PROMPT_PATH, FINAL_USER_PROMPT_PATH, 
    OUTPUT_FILENAME, MODEL, EXAM, DATATYPE
)

prompt = load_prompt(FINAL_USER_PROMPT_PATH)
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

# Extract and format the assistant's responses
response_content = ""

for i, choice in enumerate(response.choices):
    response_content += f"Response {i + 1}:\n"
    response_content += choice.message.content.strip() + "\n"
    response_content += "-" * 60 + "\n\n"

save_response(MODEL, EXAM, DATATYPE, OUTPUT_FILENAME, response_content)

print(f"✅ {MODEL} response saved to outputs/{MODEL}/{OUTPUT_FILENAME}")
