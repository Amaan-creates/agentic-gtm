#!/usr/bin/env python3
"""Run the same GTM task on several Claude models and measure what each one costs.

  python3 model_lab.py --prompt prompt.md [--input accounts.md] [--models a,b,c] [--out model-lab.json]
  python3 model_lab.py --prompt prompt.md [--input accounts.md] --estimate   # price it first, spends nothing

Needs `pip install anthropic` and an API key (ANTHROPIC_API_KEY, or an `ant auth login` profile).
Each model runs once with its default settings, so the numbers are what you'd pay in practice:
output tokens include any thinking the model did. Writes one JSON file the course's
`modellab` block reads (fill in `verdict` and `score` after you judge the outputs).
"""
import argparse, json, sys, time

# USD per million tokens (input, output), list prices from https://claude.com/pricing as of PRICES_CHECKED.
# Re-check before quoting; the course quotes whatever this table says.
PRICES_CHECKED = "2026-09-24"
PRICES = {
    "claude-haiku-4-5": (1.00, 5.00),
    "claude-sonnet-5": (2.00, 10.00),
    "claude-opus-5": (5.00, 25.00),
    "claude-opus-5-5": (4.00, 20.00),
    "claude-fable-5-1": (10.00, 50.00),
}
LABELS = {
    "claude-haiku-4-5": "Haiku 4.5",
    "claude-sonnet-5": "Sonnet 5",
    "claude-opus-5": "Opus 5",
    "claude-opus-5-5": "Opus 5.5",
    "claude-fable-5-1": "Fable 5.1",
}
DEFAULT_MODELS = "claude-haiku-4-5,claude-sonnet-5,claude-opus-5-5"
EST_OUTPUT_TOKENS = 1500  # typical for the fit / no-fit table; only used by --estimate


def run_one(client, anthropic, model, prompt, max_tokens):
    start = time.monotonic()
    try:
        # Fallbacks are left off on purpose: a lab that silently swaps models can't compare them.
        resp = client.messages.create(
            model=model, max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
    except anthropic.NotFoundError:
        return {"model": model, "label": LABELS.get(model, model), "error": "model not available to this key"}
    except anthropic.RateLimitError:
        return {"model": model, "label": LABELS.get(model, model), "error": "rate limited, try again in a minute"}
    except anthropic.APIStatusError as e:
        return {"model": model, "label": LABELS.get(model, model), "error": f"API error {e.status_code}: {e.message}"}
    except anthropic.APIConnectionError as e:
        cause = e.__cause__ or e
        return {"model": model, "label": LABELS.get(model, model), "error": f"connection failed: {type(cause).__name__}: {cause}"}
    except Exception as e:  # an SDK or environment problem: show it rather than hide it
        return {"model": model, "label": LABELS.get(model, model), "error": f"{type(e).__name__}: {e}"}
    latency = time.monotonic() - start

    if resp.stop_reason == "refusal":
        text = "(the model declined this task)"
    else:
        text = "\n".join(b.text for b in resp.content if b.type == "text").strip()
    pin, pout = PRICES.get(model, (0.0, 0.0))
    u = resp.usage
    cost = (u.input_tokens * pin + u.output_tokens * pout) / 1_000_000
    return {
        "model": model, "label": LABELS.get(model, model),
        "latency_s": round(latency, 2),
        "input_tokens": u.input_tokens, "output_tokens": u.output_tokens,
        "cost_usd": round(cost, 6),
        "stop_reason": resp.stop_reason,
        "output": text,
        "verdict": None, "score": None,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prompt", required=True, help="file with the task prompt")
    ap.add_argument("--input", help="optional file appended to the prompt (e.g. the account list)")
    ap.add_argument("--models", default=DEFAULT_MODELS, help=f"comma-separated model ids (default {DEFAULT_MODELS})")
    ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--out", default="model-lab.json")
    ap.add_argument("--estimate", action="store_true",
                    help=f"count input tokens (free) and price the run assuming ~{EST_OUTPUT_TOKENS} output tokens per model; runs nothing")
    args = ap.parse_args()

    try:
        import anthropic
    except ImportError:
        sys.exit("pip install anthropic   (then re-run)")

    prompt = open(args.prompt).read()
    if args.input:
        prompt += "\n\n<input>\n" + open(args.input).read() + "\n</input>"

    if (time.time() - time.mktime(time.strptime(PRICES_CHECKED, "%Y-%m-%d"))) > 30 * 86400:
        print(f"note: the price table was last checked {PRICES_CHECKED}; confirm https://claude.com/pricing before quoting costs", file=sys.stderr)
    client = anthropic.Anthropic()
    models = [m.strip() for m in args.models.split(",") if m.strip()]
    if args.estimate:
        total = 0.0
        for model in models:
            pin, pout = PRICES.get(model, (0.0, 0.0))
            tokens = client.messages.count_tokens(model=model, messages=[{"role": "user", "content": prompt}]).input_tokens
            cost = (tokens * pin + EST_OUTPUT_TOKENS * pout) / 1_000_000
            total += cost
            print(f"{LABELS.get(model, model):10} ~{tokens} in / ~{EST_OUTPUT_TOKENS} out  ≈ ${cost:.4f}")
        print(f"estimated total ≈ ${total:.4f} (models that think a lot can use more output)")
        return
    runs = []
    for model in models:
        print(f"→ {LABELS.get(model, model)} …", end=" ", flush=True)
        r = run_one(client, anthropic, model, prompt, args.max_tokens)
        runs.append(r)
        print(r.get("error") or f"{r['latency_s']}s · {r['input_tokens']} in / {r['output_tokens']} out · ${r['cost_usd']:.4f}")

    total = round(sum(r.get("cost_usd", 0) for r in runs), 6)
    json.dump({"task": None, "measured": True, "runs": runs, "takeaway": None,
               "total_cost_usd": total, "run_date": time.strftime("%Y-%m-%d"), "prices_checked": PRICES_CHECKED,
               "prices_used": {m: PRICES.get(m) for m in models}}, open(args.out, "w"), indent=2)
    print(f"total ${total:.4f}")
    print(f"wrote {args.out}. Judge the outputs, then fill in verdict/score/task/takeaway.")


if __name__ == "__main__":
    main()
