# Research notes: Greptile (greptile.com)

Run date: 2026-09-24. Public-data path (Otto not connected). Every fact below has its URL. Source ids match `sources[]` in course.json.

## 1. The company

| Fact | Source |
|---|---|
| "The AI Code Reviewer": agents that review and test pull requests with full context of the codebase. Graph index of the repo, a swarm of agents per PR, learns from team PR comments. | [s1] https://www.greptile.com |
| "Over 22,000+ teams use Greptile." Logo strip: NVIDIA, Vanta, Scale, PostHog, Substack, WorkOS, Brex, Klaviyo, Retool, Mintlify, Zapier, Joby, Compass, Bilt, Crossmint, Material Security. | [s1] |
| Enterprise: self-hosted / air-gapped, SOC 2, SSO, audit logs; "Built for enterprises across defense, healthcare, and financial services." Works with GitHub and GitLab. | [s1] |
| Pricing: Starter free (1 active developer, 50 credits). Pro $30/seat/month with 50 credits per seat, extra credits $1. Enterprise custom: self-host, SSO/SAML, GitHub Enterprise, security reviews, custom DPA. 1 credit = standard review, 3 = TREX review. Free for qualified OSS; 50% off for pre-Series A startups under $2M revenue. | [s2] https://www.greptile.com/pricing |
| Legal entity Tabnam, Inc. (footer). | [s1] |
| $25M Series A led by Benchmark (Sept 2025), launched v3; named customers Brex, Substack, PostHog, Bilt, YC. | [s11] https://www.greptile.com/blog/series-a |
| Hiring (careers page): Enterprise Account Executive, Mid-market Account Executive, Customer Engineer, RevOps, Founding PMM, Forward Deployed Engineer. Reads as a push into mid-market and enterprise sales. | [s10] https://www.greptile.com/careers |

Pricing hint: per-seat pricing sells to the engineering leader who owns the seat count (VP Eng / DevEx), with a free tier that lets individual engineers try it first.

## 2. Named customers and why they bought (case studies read in full)

| Customer | Size / numbers | Person quoted | Why they bought (their words) | Source |
|---|---|---|---|---|
| Brex | 400+ engineers, ~8,200 issues caught per month, 8-year-old monorepo | CTO | "Other tools struggled with our eight-year old monorepo... Their feedback was generic"; building in-house "would have taken far longer" | [s4] https://www.greptile.com/customers/brex |
| Mixpanel | ~9,300 reviews/month; 95% of merged PRs have coding-agent attribution; in-house agent TAL opens 10% | EM, Platform Engineering | Biggest problem was latency; ran a "shootout" including an in-house build that was "verbose and expensive"; called the idea "a potential slop cannon" | [s5] https://www.greptile.com/customers/mixpanel |
| Coinbase | ~25,000+ PRs reviewed, ~150 engineers | Head of Coinbase Wallet | Built its own agents (Forge), bought the reviewer; runs it next to its own security agents | [s6] https://www.greptile.com/customers/coinbase |
| Scale | ~650 engineers, 100K+ bugs caught | VP Engineering | "code review is going to be a bottleneck"; turned it off for two days, engineers asked for it back | [s7] https://www.greptile.com/customers/scale |
| Datadog | ~3,800 reviews/month | VP Engineering | After an all-hands on AI output, "The first complaint from everyone was: yes, but what about review?"; ran it against other tools, "Greptile won" | [s8] https://www.greptile.com/customers/datadog |
| NVIDIA | Time to merge down from 24+ hrs to 6 hrs; 395K+ PRs | Sr. Engineering Manager; Architect | "Most code review tools just look at the diff"; "I was drowning in code reviews" | [s9] https://www.greptile.com/customers/nvidia |
| Also on /customers | Vouch, Gumloop, Podium (Podium compared Factory.ai) | | | [s3] https://www.greptile.com/customers |

Pattern: the quoted person is a VP Engineering, CTO or platform/DevEx manager at a company with roughly 150 to 650+ engineers, and the trigger is agent-written code overwhelming human review. Several (Mixpanel, Coinbase, Brex) considered building it themselves first.

## 3. Competitors

| Competitor | Note | Source |
|---|---|---|
| CodeRabbit | Named main rival; raised $60M Series B Sept 2025 | [s12] https://siliconangle.com/2025/09/23/greptile-bags-25m-funding-take-coderabbit-graphite-ai-code-validation/ ; Greptile's own comparison page [s13] https://www.greptile.com/greptile-vs-coderabbit |
| Graphite (Diamond) | Acquired by Cursor, announced 2025-12-19; stays an independent product. Customers named: Shopify, Snowflake, Figma, Perplexity. Homepage case studies: Ramp, Asana. | [s14] https://fortune.com/2025/12/19/cursor-ai-coding-startup-graphite-competition-heats-up/ ; [s15] https://graphite.com |
| Cursor Bugbot | Cursor's own reviewer (Greptile has a "vs Bugbot" page) | [s1] footer |
| Anthropic Code Review for Claude Code | Launched March 2026; "Code review has become a bottleneck" | [s16] https://claude.com/blog/code-review |
| Sentry Seer AI Code Review | $40 per active contributor per month | [s17] https://sentry.io/cookbook/ai-code-review-seer/ |

## 4. ICP decision

Segments considered:
1. **Small startups and YC teams.** Evidence: free tier, 50% startup discount, YC page. Decided: self-serve handles them; not where a founder's selling time goes.
2. **Mid-market and enterprise software orgs, ~150 to 2,000 engineers, heavy coding-agent use.** Evidence: every long case study (Brex, Mixpanel, Coinbase, Scale, Datadog, NVIDIA) and the Enterprise + Mid-market AE hires. **Picked.**
3. **Air-gapped / defense / healthcare.** Evidence: self-host and the "defense, healthcare, and financial services" line. Real, but no named case study in that segment, so treated as an expansion bet, not the core.

Sharpest sub-slice: regulated fintech and high-stakes infrastructure (Brex, Coinbase, Mixpanel's "irreversible data corruption").

## 5. Account list and checks (log)

Checks run on every account (checks.md), plus one check added for this market: **look at the account's public GitHub PRs for a competitor's review bot** (a public search of PR comments by `coderabbitai[bot]`, `graphite-app[bot]`, `greptile-apps[bot]` in 2026).

| Account | Domain check | Independent | Not customer / competitor | Competitor bot on public PRs | Result |
|---|---|---|---|---|---|
| Gusto | hiring page live | private | ✓ | none; Cursor's agent active on PRs in Gusto/embedded-react-sdk (Jul 2026) [s40] | keep (note Cursor) |
| Instacart | ✓ homepage | public | ✓ | none | keep |
| Samsara | ✓ | public | ✓ | none | keep |
| Plaid | ✓ | private | ✓ | none | keep |
| Chime | ✓ | public | ✓ | none | keep |
| Mercury | ✓ mercury.com (not Mercury Insurance, mercuryinsurance.com) | private, not selling (CEO) [s26] | ✓ | none | keep |
| Harvey | ✓ | private | ✓ | none | keep |
| Temporal | ✓ | private | ✓ | none | keep |
| Benchling | ✓ | private | ✓ | none | keep |
| Notion | ✓ | private | ✓ | one Graphite comment on one external PR (Feb 2026), ignored | keep |
| Checkr | ✓ | private | ✓ | none | keep |
| Webflow | ✓ | private (acquirer of Vidoso) | ✓ | none | keep |
| Affirm | ✓ | public | ✓ | none | keep |
| Zip | ziphq.com 301-redirects to zip.com; zip.co is Zip Co, a pay-later company | private | ✓ | no public repos found | keep, with collision note |
| **Supabase** | ✓ | private | ✓ | **CodeRabbit commented on 2,067 PRs since 2026-08-01** [s20] https://github.com/search?q=commenter%3Acoderabbitai%5Bbot%5D+org%3Asupabase+created%3A%3E2026-08-01&type=pullrequests | **dropped: competitor already in their PRs** |
| **Asana** | ✓ | public | **Graphite homepage case study** [s15] | none | **dropped: competitor's customer** (despite great signal: Dev Productivity roles posted 2026-09-17 [s39]) |
| **Ramp** | — | — | **Graphite homepage case study** [s15] | — | **dropped** |
| **Robinhood, Figma** | — | — | named Graphite customers [s14] | — | **dropped** (both hiring DevEx) |
| **Confluent** | ✓ | **IBM subsidiary since 2026-03-17** [s18] | | | **dropped: roll-up** |
| **Brex** | ✓ | **Capital One since 2026-04-07** [s19] | **existing Greptile customer** [s4] | | **dropped** |
| **Sentry** | ✓ | | **sells its own AI code review** [s17] | | **dropped: competitor** |
| **Intercom** | ✓ | | built its own PR review agent; 93% of PRs agent-driven, 19% auto-approved (2026-04-21) [s21] | | **dropped: built in-house** |
| **Grafana Labs** | ✓ | private | ✓ | CodeRabbit: 26 comments in 2026 | **dropped: could not settle** |
| **Faire** | ✓ | private | ✓ | Graphite bot on 2 PRs in one repo (Mar 2026) | **dropped: could not settle** |
| **Duolingo** | ✓ | public | ✓ | none | **dropped: no fit evidence**; its "AI Platform" EM post (2026-09-03) is product AI, not dev tooling [s37] |
| Existing customers a founder might list by habit | Datadog, Coinbase, Scale, NVIDIA, Mixpanel | | [s3] | | excluded |

## 6. Signals found (dated)

| Signal | Account | Fact | Date | Source |
|---|---|---|---|---|
| Hiring for AI dev tooling | Gusto | "Manager - Developer Productivity, AI Tools": owns "agentic coding environments... automated AI code review" and "vendor contracts" | posted 2026-08-24, still live 2026-09-22 | [s22] https://job-boards.greenhouse.io/gusto/jobs/8120017 |
| Hiring for AI dev tooling | Instacart | Staff SWE, Developer Experience: "from AI-powered code review to build infrastructure"; "1000+ engineers" | 2026-09-14 | [s23] https://instacart.careers/job/?gh_jid=8202247 |
| Building review in-house | Samsara | Staff SWE, DevEx: "Design and build AI agents that take real work off engineers' plates: coding, code review, test generation..." | 2026-08-05 | [s24] https://www.samsara.com/company/careers/roles/8109358 |
| Hiring for AI dev tooling | Plaid | Staff SWE, AI & Intelligent Tooling: engineers "will delegate lower-leverage work to AI agents" | 2026-08-12 | [s25] https://jobs.ashbyhq.com/plaid/41448609-24d6-44ea-a5ba-c87cf3dc3f0d |
| Hiring | Chime | Senior SWE, AI Enablement | 2026-09-15 | [s27] https://boards.greenhouse.io/chime/jobs/8788272002 |
| Funding + acquisitions | Harvey | $550M at $15.5B | 2026-09-09 | [s29] https://techcrunch.com/2026/09/09/harvey-hits-15-5b-valuation-months-after-reaching-11b/ ; Guardrails AI, fourth acquisition of 2026 [s30] https://www.abajournal.com/news/article/harvey-raises-550-million-in-latest-round-of-funding |
| Funding | Temporal | $550M Series E at $12.55B; team doubled to 570 | 2026-09-14 | [s31] https://theaiinsider.tech/2026/09/14/temporal-closes-550m-funding-round-at-a-12-55b-valuation-as-demand-surges-for-reliable-ai-infrastructure/ |
| Funding (stale) | Mercury | $200M Series D | 2026-05-20 (127 days: past the 90-day window) | [s26] https://www.cnbc.com/2026/05/20/fintech-mercury-valuation-fundraise-bank-charter.html |
| New engineering leader | none found | Searched for new CTO / VP Eng news on the list; the only hit (Instacart CTO) is from 2024 | | |

## 7. Other accounts' sources

- Mercury DevEx job (2026-07-15) [s28] https://job-boards.greenhouse.io/mercury/jobs/6116808004
- Benchling DevEx job (2026-08-25) [s32] https://jobs.ashbyhq.com/benchling/63d7d126-efaf-4a48-b328-f8d85b640ebf
- Notion DevEx job (2026-06-24) [s33] https://jobs.ashbyhq.com/notion/49bdf081-6e20-4323-8c73-6d6b19544ff5
- Checkr: ~800 employees, $800M+ gross revenue 2025 [s34] https://www.forbes.com/sites/iainmartin/2026/01/13/ai-fraud-has-exploded-this-background-check-startup-is-cashing-in/
- Webflow acquires Vidoso (2026-03-12) [s35] https://techcrunch.com/2026/03/12/webflow-buys-ai-content-generation-platform-vidoso-to-bolster-its-marketing-suite/
- Affirm jobs page (109 of 194 open roles are engineering, 2026-09-24) [s36] https://job-boards.greenhouse.io/affirm
- Zip Developer Platform job ("AI-assisted codemods", 2026-09-01) [s38] https://jobs.ashbyhq.com/zip/f003bb4d-8453-44bd-8ae0-2c1ad244a26e
- Zip Co (different company) [s42] https://zip.co
- Asana Senior Staff SWE, Developer Productivity (2026-09-17), "500+ developers" [s39] https://www.asana.com/jobs/apply/8212172
- Cursor's agent on a Gusto public PR (2026-07-29) [s40] https://github.com/Gusto/embedded-react-sdk/pull/2492
- Duolingo Senior EM, AI Platform (2026-09-03) [s37] https://careers.duolingo.com/jobs/8756745002

## 8. Model lab

Run 2026-09-24 with `scripts/model_lab.py` (API key present, pre-approved up to $1). Estimate $0.0635, actual $0.0583. Results in `model-lab.json`, prompt and inputs in `lab/`. Prices from the script's table; check https://claude.com/pricing [s41].

## 8b. Trap sources

- [s18] IBM completes Confluent acquisition, 2026-03-17: https://newsroom.ibm.com/2026-03-17-ibm-completes-acquisition-of-confluent,-making-real-time-data-the-engine-of-enterprise-ai-and-agents
- [s19] Capital One completes Brex acquisition, 2026-04-07: https://www.capitalone.com/about/newsroom/capital-one-completes-acquisition-of-brex/
- [s20] Public PR comments by CodeRabbit in the supabase org since 2026-08-01 (2,067 PRs): https://github.com/search?q=commenter%3Acoderabbitai%5Bbot%5D+org%3Asupabase+created%3A%3E2026-08-01&type=pullrequests
- [s21] Intercom, "AI is approving our pull requests", 2026-04-21: https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe/

## 9. What I could not do

- Named people: not collected (course rule). The method is taught instead.
- No live "new engineering leader" example on this list.
- Could not confirm whether any account uses Cursor Bugbot specifically (Cursor's bot account posts both agent work and reviews).
