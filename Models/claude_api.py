import anthropic
from config.settings import CLAUDE_MODEL, TEMPERATURE

def claude_request(conversation, api_key):
    client = anthropic.Anthropic(api_key=api_key)
    
    message = client.messages.create(
    model=CLAUDE_MODEL,
    max_tokens = 8192,
    temperature=TEMPERATURE,
    messages=conversation
)

    output = message.content
    
    return output