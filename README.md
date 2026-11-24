# Week 1 — Agents: What They Are and When to Use Them

**CIT AI-Native Engineering Program · Year 1 · Semester 2 · Module M1**

Reference material for the Week 1 lab. Semester 1 introduced agents
conceptually; this week applies the framework with code, and sets up the
toolchain the rest of the semester depends on.

**Lab time: 2 hours. API calls: 3.** See [LAB.md](LAB.md) for the timed plan.

## Contents

| Path | What it is |
|---|---|
| `src/check_setup.py` | Four environment checks. No API calls. |
| `src/first_call.py` | The smallest Gemini script that works. 1 call. |
| `src/break_it.py` | Three deliberate failures and their tracebacks. 2 calls. |
| `worksheets/decision-matrix.md` | The matrix, filled in by hand |
| `worksheets/traceback-notes.md` | Where you record the three failures |
| `worksheets/journal-01.md` | AI Decision Journal Entry #1 |
| `tests/` | 3 tests. No API key needed. |

Most of this lab is done **on paper**. Only three of the seven activities touch
code, and two of those are just running a script.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # mac/linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env                 # mac/linux: cp .env.example .env
# paste your Gemini API key into .env
python src/check_setup.py
```

Get a free key at [aistudio.google.com](https://aistudio.google.com/apikey).

## Running

```powershell
python src/check_setup.py     # no API calls
python -m pytest tests        # no API calls
python src/first_call.py      # 1 API call
python src/break_it.py        # 2 API calls, both fail on purpose
```

> **Not verified in this repo:** `first_call.py` and `break_it.py` need a live
> key and have not been run here. `check_setup.py` and the tests run offline
> and are verified.

## Free-tier budget

You are on the Gemini free tier. It is generous per day but limited per
minute, so if you get a `RESOURCE_EXHAUSTED` error, wait sixty seconds rather
than re-running in a loop. This whole lab costs 3 calls.

## The decision matrix

Check the rules top to bottom. Stop at the first one that fits.

| # | If the component…                       | Then use                            |
|---|-----------------------------------------|-------------------------------------|
| 1 | is high-stakes or irreversible          | human-in-the-loop, **not** an agent |
| 2 | needs external data or tools            | agent with tool use                 |
| 3 | has steps that depend on earlier output | agent with a planning loop          |
| 4 | is a multi-step **fixed** sequence      | chained LLM calls                   |
| 5 | is a single well-defined task           | one direct LLM call                 |

## Secrets

No key appears in any file here. Every script reads `GEMINI_API_KEY` from the
environment, loaded from `.env` by `python-dotenv`. `.env` is in `.gitignore`.
If you ever paste a key into a `.py` file "just to test", assume it is public
from that moment and get it reissued.

---

## Set B (non-IT background)

You are not expected to write this code from scratch. You are expected to say
what it does. Here it is in plain English.

**`src/check_setup.py`** — four small checks, each answering one question:
- `check_python()` — is Python new enough (3.11 or later)?
- `check_packages()` — are the two libraries installed?
- `check_env_file()` — does a `.env` file exist?
- `check_gitignore()` — does `.gitignore` list `.env`? This is the one that
  keeps your key private.
- `main()` — runs all four, prints PASS or FAIL for each.

**`src/first_call.py`**
- `ask(prompt)` — reads the key, creates the client, sends one prompt, returns
  the reply as text.
- `main()` — loads `.env`, picks the prompt (yours if you typed one), prints
  the answer.

**`src/break_it.py`**
- `wrong_key()`, `missing_key()`, `no_network()` — three functions, each built
  to fail one specific way.
- `main()` — runs all three inside a `try`, so instead of crashing it prints
  the error type, the message and the traceback for each.

### What Set B may simplify

- Fill in the decision matrix worksheet **by hand only** — no need to argue
  with the code.
- If you cannot safely turn your network off, the `no_network()` scenario
  already fakes it for you. Just read what it prints.
- Journal Entry #1 may be written entirely in plain language. It is graded on
  whether your reasoning follows the rules, not on vocabulary.

### What Set B may **not** simplify

The `.env` / `.gitignore` discipline. No key in any file, ever. This rule has
no Set B exception, because the consequence of breaking it is the same for
everyone.
