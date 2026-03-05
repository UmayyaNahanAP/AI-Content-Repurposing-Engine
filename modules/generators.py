import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load env variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set in .env")

# Initialize client
client = Groq(api_key=api_key)

# Load templates
with open("prompts/templates.json") as f:
    TEMPLATES = json.load(f)

def generate_platform_content(plan):
    outputs = {}
    for platform, info in plan.items():
        # Build a chat-style prompt
        prompt_text = TEMPLATES.get(platform, "").replace("{content}", "\n".join(info["content"]))
        
        # Prepare messages for Groq chat completion
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text}
        ]

        # Call Groq chat completions
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # example model name — pick one you have access to
            messages=messages,
            max_completion_tokens=500,
            temperature=0.7
        )

        # Extract text from the response
        text = ""
        if hasattr(response, "choices") and len(response.choices) > 0:
            text = response.choices[0].message.content

        outputs[platform] = text

    return outputs