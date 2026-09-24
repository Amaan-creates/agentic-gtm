#!/usr/bin/env bash
# Launch the signal-watch agent on Claude Managed Agents, on the schedule you set.
#
#   bash launch.sh              create environment, agent and scheduled deployment, then run once now
#   bash launch.sh --redeploy   rebuild the agent and deployment after editing .env, brief.md, accounts.md or outcome.md
#   bash launch.sh --run        trigger one run now
#   bash launch.sh --pause      stop the schedule (nothing is deleted)
#   bash launch.sh --resume     start it again from the next scheduled time
#   bash launch.sh --status     show the schedule and the next runs
#   bash launch.sh --dry-run    print the agent and schedule it would create; no API calls, no key needed
#
# Safe to re-run: IDs are saved to IDS.env and existing objects are reused.
set -euo pipefail
cd "$(dirname "$0")"
if [ "${1:-}" = "--dry-run" ]; then
  set -a; source "$( [ -f .env ] && echo .env || echo .env.example )"; set +a
  COMPANY=$(sed -n 's/^# Brief: *//p' brief.md | head -1)
  python3 - "$COMPANY" "${MODEL:-claude-sonnet-5}" <<'PY'
import json, os, sys
a = json.load(open("agent.json"))
for k in ("name", "description", "system"):
    a[k] = a[k].replace("{{COMPANY}}", sys.argv[1] or "Your company")
a["model"] = sys.argv[2]
task = open("kickoff.md").read().replace("{{WINDOW_DAYS}}", os.environ.get("WINDOW_DAYS", "7"))
task += "\n\n" + open("brief.md").read() + "\n\n" + open("accounts.md").read()
dep = {"name": "Signal watch", "agent": "<created by launch.sh>", "environment_id": "<created by launch.sh>",
       "schedule": {"type": "cron", "expression": os.environ.get("SCHEDULE", "0 8 * * 1"), "timezone": os.environ.get("TIMEZONE", "UTC")},
       "budget": {"type": "limit", "max_list_cost": {"amount": os.environ.get("RUN_BUDGET_CENTS", "500"), "currency": "USD"}},
       "initial_events": [{"type": "user.define_outcome", "description": task[:400] + " …", "rubric": {"type": "text", "content": open("outcome.md").read()[:200] + " …"}, "max_iterations": 3}],
       "resources": [{"type": "memory_store", "memory_store_id": "<created by launch.sh>", "access": "read_write"}]}
print("AGENT\n" + json.dumps({k: (v[:300] + " …" if isinstance(v, str) and len(v) > 300 else v) for k, v in a.items()}, indent=2))
print("\nSCHEDULE\n" + json.dumps(dep, indent=2))
leftover = [f for f in ("brief.md", "accounts.md") if "{{" in open(f).read()]
print("\nplaceholders still to fill: " + (", ".join(leftover) if leftover else "none"))
PY
  exit 0
fi
[ -f .env ] || { echo "Copy .env.example to .env and add your API key first."; exit 1; }
set -a; source .env; [ -f IDS.env ] && source IDS.env; set +a
: "${ANTHROPIC_API_KEY:?Add ANTHROPIC_API_KEY to .env}"

BASE=https://api.anthropic.com/v1
AUTH=(-H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01")
[ -n "${ANTHROPIC_WORKSPACE_ID:-}" ] && AUTH+=(-H "anthropic-workspace-id: $ANTHROPIC_WORKSPACE_ID")
H=("${AUTH[@]}" -H "anthropic-beta: managed-agents-2026-04-01" -H "content-type: application/json")
# Memory store calls use their own beta header in place of the managed-agents one (never both).
MH=("${AUTH[@]}" -H "anthropic-beta: agent-memory-2026-07-22" -H "content-type: application/json")
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

api() {  # METHOD PATH [curl args…] → $TMP/resp.json, exits on error
  local m=$1 p=$2; shift 2
  local code; code=$(curl -sS -X "$m" "$BASE$p" "$@" -o "$TMP/resp.json" -w '%{http_code}')
  if [[ $code != 2* ]]; then echo "✗ $m $p → HTTP $code"; cat "$TMP/resp.json"; echo; exit 1; fi
}
id() { python3 -c "import json; print(json.JSONDecoder(strict=False).decode(open('$TMP/resp.json').read())['$1'])"; }
save() { echo "$1=$2" >> IDS.env; export "$1=$2"; }
CONSOLE="https://platform.claude.com/workspaces/${ANTHROPIC_WORKSPACE_ID:-default}"

if [ "${1:-}" = "--pause" ] || [ "${1:-}" = "--resume" ] || [ "${1:-}" = "--status" ]; then
  : "${DEPLOYMENT_ID:?Nothing deployed yet: run bash launch.sh first}"
  case "$1" in
    --pause)  api POST "/deployments/$DEPLOYMENT_ID/pause?beta=true" "${H[@]}" -d '{}'; echo "⏸  schedule paused" ;;
    --resume) api POST "/deployments/$DEPLOYMENT_ID/unpause?beta=true" "${H[@]}" -d '{}'; echo "▶️  schedule resumed" ;;
    --status) api GET "/deployments/$DEPLOYMENT_ID?beta=true" "${H[@]}" ;;
  esac
  python3 -c "import json; d=json.load(open('$TMP/resp.json')); s=d.get('schedule',{}); print('schedule:', s.get('expression'), s.get('timezone'), '| paused:', bool(d.get('paused_reason') or d.get('paused_at'))); print('next runs:', ', '.join(s.get('upcoming_runs_at',[])[:3]))"
  exit 0
fi

if [ "${1:-}" = "--run" ]; then
  : "${DEPLOYMENT_ID:?Nothing deployed yet: run bash launch.sh first}"
  api POST "/deployments/$DEPLOYMENT_ID/run?beta=true" "${H[@]}" -d '{}'
  echo "▶️  run started. Watch it: $CONSOLE/sessions   Then: python3 report.py"
  exit 0
fi

# 1. Environment: a cloud sandbox with open networking so the agent can read company sites.
if [ -z "${ENV_ID:-}" ]; then
  api POST /environments "${H[@]}" -d '{"name":"gtm-signal-watch-env","config":{"type":"cloud","networking":{"type":"unrestricted"}}}'
  save ENV_ID "$(id id)"
fi
echo "✅ environment $ENV_ID"

# 1b. Optional Otto connector: a vault holds the key; Anthropic adds it to Otto's requests, the agent never sees it.
OTTO=""
if [ -n "${OTTO_MCP_URL:-}" ] && [ -n "${OTTO_API_KEY:-}" ]; then
  OTTO=1
  if [ -z "${VAULT_ID:-}" ]; then
    api POST /vaults "${H[@]}" -d '{"display_name":"agentic-gtm signal watch"}'
    save VAULT_ID "$(id id)"
  fi
  if [ -z "${OTTO_CRED_ID:-}" ]; then
    python3 -c "import json,os; print(json.dumps({'display_name':'Otto','auth':{'type':'static_bearer','mcp_server_url':os.environ['OTTO_MCP_URL'],'token':os.environ['OTTO_API_KEY']}}))" > "$TMP/cred.json"
    api POST "/vaults/$VAULT_ID/credentials" "${H[@]}" -d @"$TMP/cred.json"
    rm -f "$TMP/cred.json"
    save OTTO_CRED_ID "$(id id)"
  fi
  echo "✅ Otto connected through vault $VAULT_ID"
fi

# 1c. Memory: what earlier runs already reported, so each report only has new signals.
if [ -z "${MEMSTORE_ID:-}" ]; then
  api POST /memory_stores "${MH[@]}" -d '{"name":"signal-watch-memory","description":"Signals this agent has already reported: one line per signal with company, signal, date and source URL."}'
  save MEMSTORE_ID "$(id id)"
  api POST "/memory_stores/$MEMSTORE_ID/memories" "${MH[@]}" -d '{"path":"/reported.md","content":"# Signals already reported\n\nOne line per signal: date reported | company | signal | date of the event | source URL\n"}'
fi
echo "✅ memory $MEMSTORE_ID"

# 2. Agent: the model, instructions and tools. --redeploy rebuilds it, so a new MODEL or Otto key takes effect.
if [ "${1:-}" = "--redeploy" ] && [ -n "${AGENT_ID:-}" ]; then
  sed -i.bak '/^AGENT_ID=/d' IDS.env && rm -f IDS.env.bak; unset AGENT_ID
fi
if [ -z "${AGENT_ID:-}" ]; then
  COMPANY=$(sed -n 's/^# Brief: *//p' brief.md | head -1)
  python3 - "$COMPANY" "${MODEL:-claude-sonnet-5}" "$OTTO" > "$TMP/agent.json" <<'PY'
import json, os, sys
a = json.load(open("agent.json"))
company, model, otto = sys.argv[1] or "Your company", sys.argv[2], sys.argv[3]
for k in ("name", "description", "system"):
    a[k] = a[k].replace("{{COMPANY}}", company)
a["model"] = model
if otto:
    # Otto's free tools only: the agent runs unattended, so nothing here can spend credits.
    free = ["workspace_status", "signals_feed", "linkedin_find_people", "linkedin_find_companies",
            "list_leads", "get_lead", "list_contacts"]
    a["mcp_servers"] = [{"type": "url", "name": "otto", "url": os.environ["OTTO_MCP_URL"]}]
    a["tools"].append({"type": "mcp_toolset", "mcp_server_name": "otto",
                       "default_config": {"enabled": False},
                       "configs": [{"name": t, "enabled": True, "permission_policy": {"type": "always_allow"}} for t in free]})
    a["system"] += ("\n\nOtto is connected. For each account with a signal, use linkedin_find_people with a companies filter "
                    "and the persona's roles to name the person to contact, and keep only people whose current employer is that account. "
                    "Say in the report which contacts Otto found. Never run a bare name search.")
else:
    a["system"] += ("\n\nOtto is not connected, so name roles, not people. Open signals.md with one line: how many accounts "
                    "are worth contacting this run, then \"Connect Otto and each one comes with the person to contact, "
                    "checked against their current employer.\"")
print(json.dumps(a))
PY
  api POST /agents "${H[@]}" -d @"$TMP/agent.json"
  save AGENT_ID "$(id id)"
fi
echo "✅ agent $AGENT_ID  $CONSOLE/agents/$AGENT_ID"

# 3. Deployment: your schedule. Its kickoff is the task + brief + accounts, graded by outcome.md.
if [ "${1:-}" = "--redeploy" ] && [ -n "${DEPLOYMENT_ID:-}" ]; then
  api POST "/deployments/$DEPLOYMENT_ID/archive?beta=true" "${H[@]}" -d '{}'
  sed -i.bak '/^DEPLOYMENT_ID=/d' IDS.env && rm -f IDS.env.bak; unset DEPLOYMENT_ID
  echo "↺ old deployment archived"
fi
if [ -z "${DEPLOYMENT_ID:-}" ]; then
  python3 - > "$TMP/deployment.json" <<PY
import json, os
task = open("kickoff.md").read().replace("{{WINDOW_DAYS}}", os.environ.get("WINDOW_DAYS", "7")) + "\n\n" + open("brief.md").read() + "\n\n" + open("accounts.md").read()
print(json.dumps({
  "name": "Signal watch",
  "agent": os.environ["AGENT_ID"],
  "environment_id": os.environ["ENV_ID"],
  "initial_events": [{"type": "user.define_outcome", "description": task,
                      "rubric": {"type": "text", "content": open("outcome.md").read()}, "max_iterations": 3}],
  "schedule": {"type": "cron", "expression": os.environ.get("SCHEDULE", "0 8 * * 1"),
               "timezone": os.environ.get("TIMEZONE", "UTC")},
  "budget": {"type": "limit", "max_list_cost": {"amount": os.environ.get("RUN_BUDGET_CENTS", "500"), "currency": "USD"}},
  **({"vault_ids": [os.environ["VAULT_ID"]]} if os.environ.get("VAULT_ID") else {}),
  "resources": [{"type": "memory_store", "memory_store_id": os.environ["MEMSTORE_ID"], "access": "read_write",
                 "instructions": "reported.md lists every signal already sent to the founder. Read it first and never report a signal that is already there. After writing the report, append one line per new signal."}],
}))
PY
  api POST "/deployments?beta=true" "${H[@]}" -d @"$TMP/deployment.json"
  save DEPLOYMENT_ID "$(id id)"
  python3 -c "import json; d=json.load(open('$TMP/resp.json')); print('🗓️  next runs:', ', '.join(d.get('schedule',{}).get('upcoming_runs_at',[])[:3]))"
  api POST "/deployments/$DEPLOYMENT_ID/run?beta=true" "${H[@]}" -d '{}'
  echo "▶️  first run started now"
fi
echo "✅ deployment $DEPLOYMENT_ID  $CONSOLE/deployments/$DEPLOYMENT_ID"
echo
echo "When a run finishes (usually several minutes): python3 report.py"
