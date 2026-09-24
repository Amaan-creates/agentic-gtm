# Your signal-watch agent

This folder turns your GTM course into an agent that runs every week on [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview): it checks your target accounts for buying signals on the schedule you set, and writes a report with a draft first message for each new one. It never contacts anyone.

## Launch

```bash
cp .env.example .env     # add your Anthropic API key
bash launch.sh              # creates everything, puts it on your schedule, runs it once now
python3 report.py        # when the run finishes: downloads the report
```

## What each file is

| File | Managed Agents piece | What it does |
|---|---|---|
| `agent.json` | **Agent** | The model, the instructions and the tools (web search, web fetch, bash) |
| `brief.md` + `accounts.md` + `kickoff.md` | The **task** each run starts with | Your ICP, signals, message rules and account list |
| `outcome.md` | **Outcome** rubric | A separate grader checks every run against it and sends the agent back to fix what fails (up to 3 rounds) |
| `launch.sh` | **Environment** + **Deployment** (+ **Vault** with Otto) | The sandbox the agent works in, your schedule, and (optionally) Otto's key held safely |
| `report.py` | Files API | Downloads the report from the latest run |

## Your schedule

Set `SCHEDULE` and `TIMEZONE` in `.env` (examples are in the file), then:

```bash
bash launch.sh --status     # the schedule and the next three runs
bash launch.sh --run        # run it now
bash launch.sh --pause      # pause the schedule
bash launch.sh --resume     # start it again
```

## Change things

- **Accounts, signals or rules:** edit `accounts.md` / `brief.md`, then `bash launch.sh --redeploy`.
- **Model:** set `MODEL` in `.env` before the first launch (for example `claude-sonnet-5` to spend less).
- **Schedule:** `SCHEDULE` and `TIMEZONE` in `.env`, then `bash launch.sh --redeploy`.
- **Run it now:** `bash launch.sh --run`.

## Go further

- **Otto** for verified people at each account with a signal: set `OTTO_MCP_URL` and `OTTO_API_KEY` in `.env` before `bash launch.sh`. It stores the key in a **vault** (the agent never sees it), adds Otto's MCP server to the agent with only Otto's free tools switched on, and attaches the vault to the deployment. Already launched? Delete `AGENT_ID` and `DEPLOYMENT_ID` from `IDS.env` and run `bash launch.sh` again.
- **Memory is built in:** each run reads what earlier runs reported (a memory store, `MEMSTORE_ID` in `IDS.env`) and only brings you new signals.
- **Delivery:** have the report posted to Slack or email through a connector, behind an approval step.

Docs: https://platform.claude.com/docs/en/managed-agents/overview
