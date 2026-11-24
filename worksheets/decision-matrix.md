# Worksheet 1 — The Agent Decision Matrix

**Do this by hand. No code.** (20 minutes)

## The matrix

Check the rules **top to bottom** and stop at the first one that fits.

| # | If the component…                      | Then use                            |
|---|----------------------------------------|-------------------------------------|
| 1 | is high-stakes or irreversible         | human-in-the-loop, **not** an agent |
| 2 | needs external data or tools           | agent with tool use                 |
| 3 | has steps that depend on earlier output| agent with a planning loop          |
| 4 | is a multi-step **fixed** sequence     | chained LLM calls                   |
| 5 | is a single well-defined task          | one direct LLM call                 |

Rule 1 is first on purpose. A component that issues refunds does not become
safe just because it also needs a tool.

## Your Semester 1 system

Break your system into components. A component is one thing it does, in one
sentence. Most systems have 3–6.

| # | Component (one sentence) | Rule that fired | Verdict |
|---|--------------------------|-----------------|---------|
| 1 |                          |                 |         |
| 2 |                          |                 |         |
| 3 |                          |                 |         |
| 4 |                          |                 |         |
| 5 |                          |                 |         |

## Worked example (a study-notes assistant)

| # | Component | Rule | Verdict |
|---|-----------|------|---------|
| 1 | Answer a question about notes the student pasted in | 5 | direct LLM call |
| 2 | Build a revision plan: extract topics, rank, lay out a week | 4 | chained calls |
| 3 | Find which lecture a claim came from | 2 | agent with tool use |
| 4 | Email the plan to the student's tutor | 1 | human-in-the-loop |

Note that component 2 has three steps but is **not** an agent: the steps never
change, so I can write the sequence myself. That is the distinction most
people get wrong.

## The question to answer in your journal

For every row you marked "agent": **what is the worst thing it could do if its
planning loop went wrong, and would you find out?**
