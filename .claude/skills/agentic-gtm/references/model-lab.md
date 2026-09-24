# Model lab

The point: show the founder, on their own data, which Claude model to use for which GTM job, with **measured** cost, time and quality instead of opinions.

## The task

Use a task that has a right answer you already know, so quality can be scored rather than judged by taste. The default:

> **Sort 15 accounts into "fit" or "no fit" for <Company>'s ICP, with a one-line reason.**

Build the input from your check log: 10 accounts that passed (from lesson 2) and 5 you dropped (from the check log in `research.md`). Pick failures a model can judge from the line itself: owned by a group, already a customer, a competitor, wrong size, builds it in house. Skip name collisions and closed businesses unless the line says so plainly ("we meant the procurement company; this domain is a pay-later company") and the prompt has a matching rule. Your check results are the answer key. Shuffle the order.

**Each account line must contain the fact your check found** ("owned by <Group> since 2023 [source]", "sells the same product", "closed in 2025"). The model can only get it right from what's on the page; without the fact, the task can't be scored fairly.

All lab files go in `<course folder>/lab/`: the prompt in `lab/prompt.md` (the ICP card plus the instruction, asking for a markdown table Company | Fit? | Reason), the 15 accounts (name, domain, one line of description with the fact) in `lab/accounts.md`, and the answer key in `lab/answer-key.md` (# | Company | Answer | Why) so anyone can check the scoring.

## Running it

**With an API key** (`ANTHROPIC_API_KEY` set, or an `ant auth login` profile). Run from the course folder, with `<skill>` being this skill's folder. Price it first (free), tell the user the estimate, and run only on their OK:

```bash
pip install anthropic          # use a virtualenv if your Python's SDK is old or broken
python3 <skill>/scripts/model_lab.py --prompt lab/prompt.md --input lab/accounts.md --estimate
python3 <skill>/scripts/model_lab.py --prompt lab/prompt.md --input lab/accounts.md --out model-lab.json
```

Defaults: `claude-haiku-4-5`, `claude-sonnet-5`, `claude-opus-5-5`. Add others with `--models`.

**Without a key** (inside Claude Code): run the same prompt through three subagents with the model set to haiku, sonnet and opus. Time each one. Write `model-lab.json` yourself in the same shape with the token and cost fields set to 0, and set `"measured": false` on the block.

## Judging

For each model:
- `score`: correct fit / no-fit calls out of 15 against your answer key, e.g. `"13/15"`.
- `verdict`: under 15 words on *how* it did (it renders as a heading). Put detail in the `takeaway`.
- `output`: the model's answer exactly as returned. It is measured data, so the writing rules (em dashes and so on) don't apply to it.

Then write the `takeaway`: two or three sentences based on what you measured, not on reputation. If Haiku scored as well as Opus on this task, say so. That is a real finding: sorting at volume can run on the cheap model.

## The "which model for which job" table

Add a `table` block after the lab. Base the rows on this lab plus the rest of the course run, and keep them honest:

| Job | Model | Why |
|---|---|---|
| Sorting hundreds of accounts, pulling fields from pages | Usually Haiku | High volume, clear instructions, a right answer. Measure it: see the lab |
| Researching a company, drafting messages at volume | Usually Sonnet | Needs judgement and good writing, runs often |
| Deciding the ICP, a message to a key account, grading an agent's work | Usually Opus | The costly mistakes happen here. Few calls, so cost barely matters |

Mention **effort** in one line: every current model also takes an effort setting (low to max). A lower effort on a bigger model is sometimes the better trade than a smaller model.

Prices change. `model-lab.json` records `prices_used`, `prices_checked`, `run_date` and `total_cost_usd`: quote those and link to https://claude.com/pricing.

When judging, also read the **reasons**, not just the fit call: a cheap model can get the label right while inventing facts in the reason. That is worth a line in the verdict.
