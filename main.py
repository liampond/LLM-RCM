from models.chatgpt_api import chatgpt_request
from models.claude_api import claude_request
from models.gemini_api import gemini_request
from utils.prompt_loader import load_prompt
from utils.encoded_file_loader import load_encoded_file
from utils.file_manager import save_response
from settings import (
    CHATGPT_API_KEY, CLAUDE_API_KEY, GEMINI_API_KEY, CHATGPT_MODEL, 
    TEMPERATURE, NUM_RESPONSES, SYSTEM_PROMPT_PATH, 
    DATATYPE_PROMPT_PATH, MAIN_PROMPT_PATH, 
    OUTPUT_FILENAME, MODEL, EXAM, DATATYPE, ENCODED_FILENAME,
    QUESTIONS_WITHOUT_ENCODED_FILES, check_encoded_file_exists,
    QUESTION, 
)

# Load prompts
system_prompt = load_prompt(SYSTEM_PROMPT_PATH)
first_user_prompt = load_prompt(DATATYPE_PROMPT_PATH)
final_user_prompt = load_prompt(MAIN_PROMPT_PATH)

# Check if the encoded file should be skipped
if check_encoded_file_exists(QUESTION):
    encoded_file_content = load_encoded_file(EXAM, DATATYPE, ENCODED_FILENAME)
    conversation = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": first_user_prompt},
        {"role": "user", "content": f"Here is the encoded music file in {DATATYPE} format:\n\n{encoded_file_content}"},
        {"role": "user", "content": final_user_prompt}
    ]
else:
    print(f"⚠️ Skipping {QUESTION} due to no encoded file.")
    conversation = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": first_user_prompt},
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
    response_content += f"\n{'=' * 100}\n"  # Clean divider before each response
    response_content += f"📝 Response {i + 1}\n"
    response_content += f"{'=' * 100}\n\n"
    response_content += choice.message.content.strip() + "\n"

save_response(MODEL, EXAM, DATATYPE, OUTPUT_FILENAME, response_content)

print(f"✅ {MODEL} response saved to outputs/{MODEL}/{EXAM}/{DATATYPE}/{OUTPUT_FILENAME}")
