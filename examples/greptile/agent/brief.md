# Brief: Greptile

<!-- Filled in by the agentic-gtm skill from the course. Edit freely, then re-run ./launch.sh --redeploy -->

## What Greptile sells
An AI code reviewer: agents that review every pull request on GitHub or GitLab with context from the whole codebase, learn a team's standards from its PR comments, and can run the PR branch in a sandbox (TREX). Pro is $30 per seat per month; Enterprise adds self-hosting, SSO and security reviews.

## Ideal customer profile
- Industries: software companies that write their own product code. Sharpest: regulated or high-stakes codebases (fintech, health and life-science data, infrastructure), marketplaces with large monorepos.
- Company size: roughly 150 to 2,000 engineers, on GitHub or GitLab.
- Regions: US first (San Francisco, New York), then English-speaking markets.
- The pain, in customers' words: "code review is going to be a bottleneck", "drowning in code reviews", other tools' feedback "was generic", adding a reviewer agent felt like "a potential slop cannon".
- Not a fit: already a Greptile customer; sells its own AI code review (competitor); a named public customer of CodeRabbit, Graphite or Cursor Bugbot, or a competitor's bot already comments on its PRs; acquired by a larger group (the parent decides); built its own reviewer and already auto-approves PRs with it.

## Personas
- **VP Engineering or CTO** (signs): owns engineering headcount and velocity; cares because review time is now the limit on what agents can ship.
- **Head of Developer Productivity / DevEx / AI Dev Tools manager** (champion, runs the evaluation): owns review tooling and often the vendor contract; cares because leadership asked them to make agent-written code safe to merge.
- **Staff and principal engineers** (use it, and can kill it): the humans doing the reviews; care because they are the bottleneck and hate noisy bots.
- **Security or AppSec lead** (can block): cares about self-hosting, SOC 2 and what code leaves the building.

## Signals to watch
| Signal | What to look for | Why it means ready | Freshness |
|---|---|---|---|
| Hiring for AI dev tooling | Job posts for Developer Productivity, Developer Experience, AI Dev Tools or AI Enablement that mention code review, coding agents or vendor contracts | Someone is being hired to own the review problem, often with a budget | 30 days (or while the post is live) |
| Building review in-house | Job posts or engineering blog posts about building AI agents for code review | A build-vs-buy decision is open right now; Mixpanel and Coinbase both tried building first | 60 days |
| Funding or acquisitions | A new round, or the company acquiring other companies | More engineers and more codebases to merge; review load jumps | 90 days |
| New engineering leader | A new CTO, VP Engineering or Head of Platform announced | New leaders review tools in their first 90 days | 90 days |

Before reporting any signal, also check the account's public repos for a competitor's review bot (CodeRabbit, Graphite, Cursor) commenting on recent PRs. If one is active, report it as a warning, not a signal.

## Message rules
- Open on the signal, not on us.
- One sentence on why it matters to them.
- One easy question, ideally either/or.
- Under 90 words. No em dashes, exclamation marks, "hope you're well", or meeting asks.
- Optional last line: one plain fact about Greptile or a named customer, never a claim about results.
