"""Break the first call three ways on purpose and read each traceback.

    python src/break_it.py

Uses 2 API calls (both of which fail on purpose). The missing-key case makes
no call at all - that is the point of it.

Three failures, three different layers:
    wrong key    -> the server rejected you          (their side)
    missing key  -> nothing was ever sent            (your config)
    no network   -> the request could not leave      (the wire)

Telling these apart on sight is most of debugging an AI pipeline.
"""

import os
import traceback

from dotenv import load_dotenv
from google import genai

PROMPT = "Say the single word: hello"
MODEL = "gemini-2.0-flash"


def wrong_key():
    """A well-formed key that no account owns. The request IS sent.

    The value below is deliberately fake. The trailing comment is an
    allowlist pragma - the secret scanner you write in Week 15 skips lines
    carrying it, which is how a scanner stays testable. Use it only for
    values you know are not real.
    """
    client = genai.Client(
        api_key="AIzaSyNotARealKey00000000000000000000000"  # pragma: allowlist secret
    )
    return client.models.generate_content(model=MODEL, contents=PROMPT).text


def missing_key():
    """No key at all. Fails before anything is sent."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY is not set.")
    return "(key was present - unset it in .env to see this one fail)"


def no_network():
    """Points at a host that does not exist, to imitate being offline."""
    client = genai.Client(
        api_key="placeholder",
        http_options={"base_url": "https://no-such-host.invalid"},
    )
    return client.models.generate_content(model=MODEL, contents=PROMPT).text


SCENARIOS = [
    ("1. WRONG KEY", wrong_key),
    ("2. MISSING KEY", missing_key),
    ("3. NO NETWORK", no_network),
]


def main():
    load_dotenv()
    for title, scenario in SCENARIOS:
        print("=" * 60)
        print(title)
        print("=" * 60)
        try:
            print("No error. Returned:", scenario())
        except Exception as exc:
            print(f"Exception type: {type(exc).__name__}")
            print(f"Message: {exc}\n")
            traceback.print_exc()
        print()

    print("Now fill in worksheets/traceback-notes.md.")


if __name__ == "__main__":
    main()
