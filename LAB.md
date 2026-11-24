# Week 1 Lab — Agents, Setup and the First Gemini Call

**Time: 2 hours · API calls used: 3**

| # | Activity | Time | Code? |
|---|----------|------|-------|
| 1 | Decision matrix worksheet | 20 min | no |
| 2 | Live demo — watch an agent fail | 15 min | no |
| 3 | Environment setup | 25 min | run only |
| 4 | First Gemini call | 15 min | yes |
| 5 | Break it three times | 20 min | run only |
| 6 | Commit and push to GitHub | 15 min | no |
| 7 | Journal Entry #1 | 10 min | no |

---

## 1. Decision matrix worksheet (20 min, no code)

Open `worksheets/decision-matrix.md` and fill it in for **your own Semester 1
system**. Break it into components, apply the five rules top to bottom, stop at
the first rule that fits.

Compare with the person next to you. Where you disagree, work out why — the
disagreement is the learning, not the table.

---

## 2. Live demo (15 min, no code)

Faculty runs an agent through a multi-step task, then makes it fail.

Write down three things:
- the moment the agent **chose** its next step rather than following a script
- which failure mode you saw: hallucinated tool call, scope drift, infinite
  loop, or silent failure
- what in the output would have let you catch it automatically

---

## 3. Environment setup (25 min)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # mac/linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env                 # mac/linux: cp .env.example .env
```

Paste your Gemini API key into `.env`, then:

```powershell
python src/check_setup.py
```

Do not continue until all four checks pass. The `.gitignore` check is the one
that keeps your key off GitHub.

---

## 4. First Gemini call (15 min, 1 API call)

Read `src/first_call.py` first. It is 25 lines and does four things: load
`.env`, read the key, send one request, print the reply. Everything you build
this semester is this with structure around it.

```powershell
python src/first_call.py
python src/first_call.py "Explain the ReAct loop in one sentence."
```

---

## 5. Break it three times (20 min, 2 API calls)

```powershell
python src/break_it.py
```

Fill in `worksheets/traceback-notes.md` as it runs. Copy the exception types
and messages **exactly**.

The three failures sit at three layers — the server rejected you, your config
was wrong, the request never left. Students who cannot tell these apart spend
Week 13 debugging the wrong thing.

---

## 6. Commit and push (15 min)

This repository carries the start of **Assessment 1** (due Week 3).

```powershell
git init
git add .
git status          # CHECK: .env must NOT be listed
git commit -m "Week 1: setup, first Gemini call, decision matrix"
git branch -M main
git remote add origin <your repo URL>
git push -u origin main
```

If `.env` appears in `git status`, stop and fix `.gitignore` before you commit.

---

## 7. Journal Entry #1 (10 min, no code)

Fill in `worksheets/journal-01.md`. Half a page.

---

## Before you leave

- [ ] Decision matrix filled in, with a rule number per component
- [ ] One agent failure mode named from the demo
- [ ] `python src/check_setup.py` — four PASS lines
- [ ] `python src/first_call.py` — a real reply
- [ ] Three tracebacks recorded word for word
- [ ] Pushed to GitHub, with no `.env` in it
- [ ] Journal Entry #1 written
