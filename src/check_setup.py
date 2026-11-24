"""Check the environment is ready. Makes no API calls.

    python src/check_setup.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def check_python():
    ok = sys.version_info >= (3, 11)
    return ok, f"Python {sys.version_info.major}.{sys.version_info.minor} (need 3.11+)"


def check_packages():
    try:
        import dotenv  # noqa: F401
        from google import genai  # noqa: F401
    except ImportError as exc:
        return False, f"{exc.name} missing - run: pip install -r requirements.txt"
    return True, "google-genai and python-dotenv installed"


def check_env_file():
    if (ROOT / ".env").exists():
        return True, ".env exists"
    return False, ".env missing - copy .env.example to .env and add your key"


def check_gitignore():
    """The important one: this is what keeps your key out of GitHub."""
    text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    if ".env" in text.split():
        return True, ".gitignore excludes .env"
    return False, ".gitignore does NOT exclude .env - fix before committing"


CHECKS = [
    ("python", check_python),
    ("packages", check_packages),
    (".env", check_env_file),
    (".gitignore", check_gitignore),
]


def main():
    failed = 0
    for name, check in CHECKS:
        ok, message = check()
        print(f"[{'PASS' if ok else 'FAIL'}] {name:<10} {message}")
        failed += not ok

    print()
    if failed:
        print(f"{failed} check(s) failed. Fix these before running first_call.py.")
        return 1
    print("Ready. Next: python src/first_call.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
