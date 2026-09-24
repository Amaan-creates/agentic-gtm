# course.json schema

`scripts/build_course.py` checks this shape and embeds it into `templates/course.html`, which renders it in the browser. All text is escaped before rendering, so plain text is always safe.

## Inline markup (any text field)

| Write | Renders as |
|---|---|
| `**bold**` | bold |
| `` `code` `` | inline code |
| `[label](https://…)` | link (http and https only) |
| `{{Term}}` | dotted underline with a hover definition from `glossary` (exact key match) |
| `[s3]` or `[s1, s4]` | numbered citation linking to `sources[]` |
| a blank line (`\n\n`) | new paragraph (in `text`, `callout`, `exercise`, `takeaway`) |

## Top level

```json
{
  "title": "How to sell Example Co",
  "lede": "One sentence on what the company does, and the one thing that makes selling it hard or interesting.",
  "company": { "name": "Example Co", "url": "https://example.com", "one_liner": "…" },
  "meta": [ { "label": "Built from", "value": "14 sources" }, { "label": "Reading time", "value": "20 min" } ],
  "glossary": { "ICP": "Ideal customer profile: the kind of company that buys, and why.", "persona": "…" },
  "sources": [ { "id": "s1", "title": "Example Co: customer stories", "url": "https://example.com/customers" } ],
  "lessons": [ { "…": "see below" } ],
  "credit": "optional footer line; defaults to a link to this repo"
}
```

## Lesson

```json
{
  "id": "who",
  "nav": "Who buys",
  "kicker": "Lesson 1",
  "title": "Who buys this?",
  "idea": "The person who uses the product is rarely the one who pays for it.",
  "blocks": [ { "type": "…" } ],
  "quiz": [
    { "q": "The team lead loves the demo. Who signs?", "options": ["The team lead", "The operations director", "IT"], "answer": 1, "why": "They own the headcount, so the saving lands in their budget." }
  ]
}
```

`id` must be unique. `answer` is the zero-based index of the right option. Any block can carry an optional `"heading"`. Lesson keys are only `id`, `nav`, `kicker`, `title`, `idea`, `blocks` and `quiz`: an exercise is a **block**, not a lesson field (the build warns about unknown keys). `company.one_liner` is only shown when `lede` is missing.

## Block types

**text**: `{"type": "text", "body": "Two or three sentences. Cite facts [s2]."}`

**cards**: `{"type": "cards", "items": [{"title": "Operations director", "body": "Owns the team's headcount.", "tag": "Signs", "tone": "accent"}]}`. `tone` is optional: `accent` or `amber`.

**fields**: `{"type": "fields", "items": [{"label": "Industries", "value": "Regional logistics firms, freight brokers"}]}`. Use this for the ICP card.

**table**: `{"type": "table", "columns": ["Company", "Why it fits"], "rows": [["[Example Co](https://example.com)", "…"]], "numeric": [2], "caption": "…"}`. `numeric` lists the column indexes shown in monospace.

**callout**: `{"type": "callout", "tone": "trap", "title": "Two companies, one name", "body": "…"}`. `tone` is `trap`, `tip` or `warning`.

**signals**:
```json
{"type": "signals", "items": [
  {"name": "Hiring intake staff", "watch": "Job posts for intake or referral coordinators", "why": "The queue is outgrowing the team.",
   "example": {"company": "Example Co", "fact": "Posted 3 roles for this job [s7]", "date": "2026-08-14"}}
]}
```
`example.date` is optional but expected: signals go stale. When no account has a live example, use `"example": {"none": true, "note": "Checked all 23 accounts."}` and it renders as "No live example this week".

**compare**: `{"type": "compare", "left": {"label": "The message everyone sends", "body": "…"}, "right": {"label": "Yours", "body": "…", "notes": "Opens on their hiring post. One question."}}`. `body` keeps line breaks.

**modellab**: paste the `runs` from `model-lab.json` after judging:
```json
{"type": "modellab", "task": "Sort 15 accounts into fit / no fit, with a reason.", "measured": true,
 "runs": [{"model": "claude-haiku-4-5", "label": "Haiku 4.5", "latency_s": 4.1, "input_tokens": 2100, "output_tokens": 640,
           "cost_usd": 0.0053, "output": "…", "verdict": "Fast, missed the two roll-ups", "score": "12/15"}],
 "takeaway": "…"}
```
Set `"measured": false` when the lab ran without an API key (costs shown as 0).

**pipeline**: `{"type": "pipeline", "steps": [{"icon": "🗓️", "label": "On your schedule", "detail": "Scheduled deployment"}]}`

**code**: `{"type": "code", "body": "cd agent\nbash launch.sh", "caption": "…"}`

**steps**: `{"type": "steps", "items": ["Open the domain.", "Check the location matches."]}`

**exercise**: `{"type": "exercise", "title": "Check one person", "body": "…"}`
