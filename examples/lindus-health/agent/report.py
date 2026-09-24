#!/usr/bin/env python3
"""Download the latest report from your signal-watch deployment.

  python3 report.py            latest run's report into reports/<date>/
  python3 report.py --list     the recent runs, with status and grader verdict
"""
import json, os, sys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://api.anthropic.com/v1"


def env():
    out = {}
    for name in (".env", "IDS.env"):
        path = os.path.join(HERE, name)
        if os.path.exists(path):
            for line in open(path):
                if "=" in line and not line.lstrip().startswith("#"):
                    k, v = line.strip().split("=", 1)
                    out[k] = v
    return out


E = env()
HDRS = {"x-api-key": E.get("ANTHROPIC_API_KEY", ""), "anthropic-version": "2023-06-01",
        "anthropic-beta": "managed-agents-2026-04-01"}
if E.get("ANTHROPIC_WORKSPACE_ID"):
    HDRS["anthropic-workspace-id"] = E["ANTHROPIC_WORKSPACE_ID"]


def get(path, raw=False):
    req = urllib.request.Request(BASE + path, headers=HDRS)
    try:
        data = urllib.request.urlopen(req, timeout=60).read()
    except urllib.error.HTTPError as e:
        sys.exit(f"✗ GET {path} → HTTP {e.code}: {e.read().decode()[:400]}")
    return data if raw else json.JSONDecoder(strict=False).decode(data.decode())


def main():
    dep = E.get("DEPLOYMENT_ID") or sys.exit("No DEPLOYMENT_ID in IDS.env: run bash launch.sh first.")
    runs = get(f"/deployment_runs?deployment_id={dep}&beta=true").get("data", [])
    if not runs:
        sys.exit("No runs yet.")
    if "--list" in sys.argv:
        for r in runs[:10]:
            sid = r.get("session_id") or "-"
            verdict = "-"
            if r.get("session_id"):
                evals = get(f"/sessions/{sid}").get("outcome_evaluations") or []
                verdict = evals[-1].get("result") if evals else "running"
            err = (r.get("error") or {}).get("type", "")
            print(f"{r.get('created_at', '')[:16]}  {sid}  {verdict}  {err}")
        return
    run = next((r for r in runs if r.get("session_id")), None) or sys.exit("No run has started a session yet.")
    sid = run["session_id"]
    sess = get(f"/sessions/{sid}")
    if sess.get("status") == "running":
        sys.exit(f"Latest run is still going: https://platform.claude.com/workspaces/{E.get('ANTHROPIC_WORKSPACE_ID') or 'default'}/sessions/{sid}")
    evals = sess.get("outcome_evaluations") or []
    out = os.path.join(HERE, "reports", (run.get("created_at") or "latest")[:10])
    os.makedirs(out, exist_ok=True)
    for f in get(f"/files?scope_id={sid}&limit=100").get("data", []):
        name = os.path.basename(f.get("filename") or f["id"])
        open(os.path.join(out, name), "wb").write(get(f"/files/{f['id']}/content", raw=True))
        print("📥", os.path.join(out, name))
    print("🎯 grader:", evals[-1].get("result") if evals else "n/a")


if __name__ == "__main__":
    main()
