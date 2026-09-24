# Task: sort accounts for Greptile

Greptile sells an AI code reviewer: agents that review every pull request on GitHub or GitLab with context from the whole codebase. Pro is $30 per seat per month; Enterprise adds self-hosting, SSO and security reviews.

## The ICP (who we sell to)

- **Company:** a software company that writes its own product code, roughly 150 to 2,000 engineers, on GitHub or GitLab.
- **Where:** US first (San Francisco and New York hubs), then English-speaking markets.
- **The pain:** AI coding agents have multiplied pull requests and human review is now the bottleneck ("code review is going to be a bottleneck").
- **Best fit:** regulated or high-stakes codebases (fintech, health data, infrastructure), large monorepos, a developer-productivity or AI-tooling team that owns review tooling.

## Not a fit (any one of these rules it out)

1. Already a Greptile customer.
2. Sells its own AI code review product (a competitor).
3. A named public customer of a direct competitor (CodeRabbit, Graphite, Cursor Bugbot).
4. Acquired by, or now a subsidiary of, a larger group: the buying decision moves to the parent.
5. Has built its own AI pull-request reviewer and says publicly that it already auto-approves PRs.

## Instruction

For each account in the input, decide **Fit** or **No fit** using only the facts given in its line and the rules above. Do not use outside knowledge about these companies.

Return a markdown table with exactly these columns: `Company | Fit? | Reason`. One row per account, in the order given. Keep each reason to one line and name the rule number when you say No fit.
