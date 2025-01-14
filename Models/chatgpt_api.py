import openai
from settings import CHATGPT_MODEL, TEMPERATURE, NUM_RESPONSES

def chatgpt_request(conversation, api_key):
    client = openai.OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        model=CHATGPT_MODEL,
        messages=conversation,
        temperature=TEMPERATURE,
        n=NUM_RESPONSES
    )
    
    return response