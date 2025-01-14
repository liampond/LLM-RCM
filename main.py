import os
from models.chatgpt_api import chatgpt_request
from models.claude_api import claude_request
from models.gemini_api import gemini_request
from utils.prompt_loader import load_prompt
from utils.encoded_file_loader import load_encoded_file
from utils.file_manager import save_response
from config.settings import (
    CHATGPT_API_KEY, CLAUDE_API_KEY, GEMINI_API_KEY, CHATGPT_MODEL, 
    TEMPERATURE, NUM_RESPONSES, SYSTEM_PROMPT_PATH, 
    DATATYPE_PROMPT_PATH, MODEL, EXTENSION_MAP
)
from config.config_loader import load_runtime_config, build_encoded_filename, check_encoded_file_exists

# ✅ Dynamically load runtime configuration
config = load_runtime_config()

# Dynamically build MAIN_PROMPT_PATH based on the QUESTION
MAIN_PROMPT_PATH = f"prompts/{config['EXAM']}/{config['CONTEXT']}/{config['EXAM']}_{config['YEAR']}_{config['QUESTION']}_{config['CONTEXT']}Prompt.txt"

# Load system and final prompts
system_prompt = load_prompt(SYSTEM_PROMPT_PATH)
final_user_prompt = load_prompt(MAIN_PROMPT_PATH)

# Handle special questions
questions_without_encoded_files = ["Q3a", "Q3b", "Q3c", "Q3d", "Q3e", "Q5", "Q6", "Q9a", "Q9b"]

if config["QUESTION"] in questions_without_encoded_files:
    conversation = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": final_user_prompt}
    ]
else:
    if not check_encoded_file_exists(config):
        print(f"⚠️ Skipping {config['QUESTION']} due to missing encoded file.")
        exit()

    first_user_prompt = load_prompt(DATATYPE_PROMPT_PATH)
    encoded_filename = build_encoded_filename(config)
    encoded_file_content = load_encoded_file(config["EXAM"], config["DATATYPE"], encoded_filename)

    conversation = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": first_user_prompt},
        {"role": "user", "content": f"Here is the encoded music file in {config['DATATYPE']} format:\n\n{encoded_file_content}"},
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

# Save responses
response_content = "\n".join([choice.message.content.strip() for choice in response.choices])
output_filename = f"{config['EXAM']}_{config['YEAR']}_{config['QUESTION']}_{config['CONTEXT']}_{config['DATATYPE']}_Output.txt"
save_response(MODEL, config["EXAM"], config["DATATYPE"], output_filename, response_content)

print(f"✅ {MODEL} response saved to outputs/{MODEL}/{config['EXAM']}/{config['DATATYPE']}/{output_filename}")
