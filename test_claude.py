from anthropic import Anthropic
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()

# Create the Claude client
client = Anthropic()

# Send a message to Claude
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Say hello and tell me you're ready to help find great flight deals!"}
    ]
)

# Print Claude's reply
print(response.content[0].text)