# Lesson 7: filling in the Managed Agent kit

The kit in `graduate/` turns the course into a **signal-watching agent** on Claude Managed Agents: on the schedule the founder sets, it checks the course's accounts for the course's buying signals, and writes a short report with a draft first message for each new signal. A separate grader checks each run against a rubric before it finishes.

## Copy and fill in

Copy `graduate/` to `<course folder>/agent/`, then:

| File | Fill in |
|---|---|
| `accounts.md` | The checked account table from lesson 2: name, domain, segment, why it fits |
| `brief.md` | Replace `{{COMPANY}}` and `{{ONE_LINER}}`. Fill in the ICP card, the personas, the signals from lesson 3 (what to watch, why, and freshness), and the message rules from lesson 5 |
| `agent.json` | Nothing: `launch.sh` fills `{{COMPANY}}` (in `name`, `description` and `system`) from the `# Brief:` heading and the model from `.env` |
| `outcome.md` | Nothing to change unless the course needs an extra rule |

Keep dates relative ("in the last 7 days as of this run"). The deployment replays the same kickoff every week, so a literal date would go stale.

## What the founder runs

```bash
cd agent
cp .env.example .env        # paste an Anthropic API key into .env
bash launch.sh              # creates the environment, agent and schedule, then runs once now
```

`launch.sh` is safe to re-run: it records IDs in `IDS.env` and skips what already exists. Write the commands as `bash launch.sh` and `python3 report.py` in the lesson: a downloaded folder loses the executable bit.

Set `MODEL` in `agent/.env.example` from the model lab, with a one-line comment saying why (for example, Sonnet if it matched Opus on your accounts at lower cost).

## What to say in the lesson

- Each run reads every account's news, careers page and site, so cost grows with the account list. Don't quote a number you haven't measured: tell the founder that each run's cost shows in the Console, and that `launch.sh` sets a hard per-run cap (`RUN_BUDGET_CENTS` in `.env`).
- The agent **only writes a report**. It doesn't email, post or change anything.
- To go further: set `OTTO_MCP_URL` and `OTTO_API_KEY` in `.env` and `launch.sh` connects Otto through a vault, with only Otto's free tools on, so each signal comes with a verified person to contact; add a memory store so it never reports the same signal twice, or change `MODEL` in `.env` before launching.

## The pipeline block

```json
{"type": "pipeline", "steps": [
  {"icon": "🗓️", "label": "On your schedule", "detail": "Scheduled deployment"},
  {"icon": "🤖", "label": "Agent", "detail": "Your ICP, signals and message rules"},
  {"icon": "🔎", "label": "Tools", "detail": "Web search and fetch (plus Otto if connected)"},
  {"icon": "🎯", "label": "Grader", "detail": "Checks sources, dates and drafts against the rubric"},
  {"icon": "📄", "label": "Report", "detail": "New signals, each with a draft message"}
]}
```
