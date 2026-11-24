"""Tests that run without an API key."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import check_setup


def test_python_version_is_new_enough():
    ok, message = check_setup.check_python()
    assert ok, message


def test_gitignore_excludes_env():
    """If this fails, your API key is one `git add .` away from being public."""
    ok, message = check_setup.check_gitignore()
    assert ok, message


def test_env_example_has_no_real_key():
    text = (check_setup.ROOT / ".env.example").read_text(encoding="utf-8")
    assert "GEMINI_API_KEY" in text
    assert "AIza" not in text, ".env.example looks like it contains a real key"
