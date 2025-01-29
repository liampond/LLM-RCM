import google.generativeai as genai
from config.settings import GEMINI_MODEL, TEMPERATURE, NUM_RESPONSES, sys_prompt_path

with open(sys_prompt_path, "r", encoding="utf-8") as file:
    system_instruction = file.read()

def gemini_request(conversation, history, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=GEMINI_MODEL,
        system_instruction=system_instruction
        )
    chat = model.start_chat(
        history=history
    )
    
    response = chat.send_message(
    conversation,
    generation_config = genai.GenerationConfig(
        temperature=TEMPERATURE,
        candidate_count=NUM_RESPONSES
        )  
    )
    print(conversation)
    output = response.text
    
    return output