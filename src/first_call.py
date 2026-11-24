"""The smallest Gemini script that works.

    python src/first_call.py
    python src/first_call.py "your own question"

Uses 1 API call.
"""

import os
import sys

from dotenv import load_dotenv
from google import genai

MODEL = "gemini-2.0-flash"


def ask(prompt):
    """Send one prompt to Gemini and return the reply as text."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY is not set. Copy .env.example to .env.")

    client = genai.Client(api_key=key)
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text


def main():
    load_dotenv()
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Explain a planning loop in two sentences."
    print(f"PROMPT: {prompt}\n")
    print(ask(prompt))


if __name__ == "__main__":
    main()
