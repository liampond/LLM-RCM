from models.chatgpt_api import chatgpt_request
from models.claude_api import claude_request
from models.gemini_api import gemini_request
from utils.prompt_loader import load_prompt
from utils.encoded_file_loader import load_encoded_file
from utils.file_manager import save_response
from settings import (
    CHATGPT_API_KEY, CLAUDE_API_KEY, GEMINI_API_KEY, CHATGPT_MODEL, 
    TEMPERATURE, NUM_RESPONSES, SYSTEM_PROMPT_PATH, 
    FIRST_USER_PROMPT_PATH, FINAL_USER_PROMPT_PATH, 
    OUTPUT_FILENAME, MODEL, EXAM, DATATYPE, ENCODED_FILENAME
)

# Load prompts
system_prompt = load_prompt(SYSTEM_PROMPT_PATH)
first_user_prompt = load_prompt(FIRST_USER_PROMPT_PATH)
encoded_file_content = load_encoded_file(EXAM, DATATYPE, ENCODED_FILENAME)
final_user_prompt = load_prompt(FINAL_USER_PROMPT_PATH)

# Construct conversation
conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": first_user_prompt},
    {"role": "user", "content": f"Here is the encoded music file in {DATATYPE} format:\n\n{encoded_file_content}"},
    {"role": "user", "content": final_user_prompt}
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

# Format and save responses
response_content = ""

for i, choice in enumerate(response.choices):
    response_content += f"Response {i + 1}:\n"
    response_content += choice.message.content.strip() + "\n"
    response_content += "-" * 60 + "\n\n"

save_response(MODEL, EXAM, DATATYPE, OUTPUT_FILENAME, response_content)

print(f"✅ {MODEL} response saved to outputs/{MODEL}/{EXAM}/{DATATYPE}/{OUTPUT_FILENAME}")
