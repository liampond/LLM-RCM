import anthropic
from config.settings import CLAUDE_MODEL, TEMPERATURE, NUM_RESPONSES

def claude_request(conversation, api_key):
    client = anthropic.Anthropic(api_key=api_key)
    
    message = client.messages.create(
    model=CLAUDE_MODEL,
    messages=conversation,
    temperature=TEMPERATURE
)

    output = message.content
    
    return output