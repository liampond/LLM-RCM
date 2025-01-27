import openai
from config.settings import DEEPSEEK_MODEL, TEMPERATURE, NUM_RESPONSES

def deepseek_request(conversation, api_key):
    client = openai.OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    
    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=conversation,
        temperature=TEMPERATURE,
        n=NUM_RESPONSES
    )

    output = response.choices[0].message.content
    
    return output