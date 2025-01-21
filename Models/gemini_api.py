import google.generativeai as genai
from config.settings import GEMINI_MODEL, TEMPERATURE, NUM_RESPONSES

def gemini_request(conversation, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(GEMINI_MODEL)
    
    response = model.generate_content(
    conversation,
    generation_config = genai.GenerationConfig(
        temperature=TEMPERATURE,
        candidate_count=NUM_RESPONSES
        )  
    )
    
    return response