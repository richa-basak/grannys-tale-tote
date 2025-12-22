import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

MODEL = "gpt-3.5-turbo"  # DO NOT CHANGE per assignment

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

if not client.api_key:
    raise RuntimeError("OPENAI_API_KEY not found. Check your .env file.")


def call_model(prompt: str, max_tokens: int = 1200, temperature: float = 0.7) -> str:
    """
    Unified OpenAI call using the new OpenAI >=1.0.0 client.
    """
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )

    return response.choices[0].message.content.strip()
