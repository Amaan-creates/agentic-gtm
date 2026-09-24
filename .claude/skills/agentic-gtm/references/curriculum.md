# Curriculum: the eight lessons

Each lesson has the same shape:

1. **The idea** (`idea`): one or two sentences of the concept, in plain words. This is the only "lecture".
2. **A principle** (`principle` block): one GTM principle from `principles.md`, made specific to this company.
3. **For <Company>**: the concept applied to their market, **led by a chart or diagram** (`funnel`, `bars`, `timeline`, `matrix`, `stack`, `stats`), then the detail.
4. **A trap or a tip** (`callout`): something real from this run that a founder would get wrong.
5. **A quiz** (1 or 2 questions) or an **exercise**: a decision, not a definition.

Show before you tell: every lesson has at least one chart or diagram, and no lesson opens with a wall of text. Charts use real counts from this run, never illustrative numbers.

Write every lesson title as the question a founder actually asks ("Who buys this?"), not a textbook heading ("Ideal Customer Profiles"). Set `nav` to a 1 to 3 word version for the sidebar.

Use glossary terms (`{{ICP}}`, `{{persona}}`, `{{buying signal}}`, `{{roll-up}}`) the first time a term appears. Define every term you use in `glossary`.

---

## Lesson 1. Who buys this?

**Teach:** the user, the buyer and the signer are often different people. The {{ICP}} describes the *company* that buys. A {{persona}} describes a *person* inside it. A good ICP says who it is **not** for.

**Must contain:**
- A `fields` block: the ICP card. Industries, company size, regions, the pain (in their customers' words where possible), disqualifiers, why now.
- A `cards` block: 2 to 4 personas. Each card says the role, what they own, and the one reason they'd care. Tag the one who signs.
- A `text` or `callout` showing **the decision**: which segments you considered and why you picked this one. Cite the evidence (case studies, pricing page, job posts).
- A `bars` chart of the evidence: named customers or case studies per segment, so the founder sees where proof clusters. Principle: beachhead market, anti-ICP, jobs to be done or positioning.

**Good quiz:** "A clinic's front-desk coordinator loves the product. Who most likely signs the contract?" with the persona cards as options.

## Lesson 2. Where are they?

**Teach:** a target account list is only useful if every row is the right company. Most list errors come from a few predictable traps.

**Must contain:**
- A `table`: 12 to 40 accounts (aim for about 20). Columns: Company (linked to its site), Location, Segment, Why it fits, Why now (if any), Check. (The agent kit's `accounts.md` uses the same columns.) Keep the "why" to one line.
- A `callout` with `tone: "trap"` for **each** trap you actually caught in this run (see `checks.md`): the name collision, the hidden parent company, the closed business, the existing customer. Name the real case.
- A `steps` block: the checks, in order, so the founder can run them on their own list.
- A `funnel`: candidates found → checks passed → kept, with the real counts.
- A `bars` chart of **why** accounts were dropped (owned by a group, competitor already in, existing customer, too small, could not settle…), with counts.
- Optional `matrix`: fit (x) against timing (y) for the kept accounts, with quadrant labels such as "Call now" (top right), "Watch" (bottom right). Place accounts only on evidence: timing is high when there is a dated signal.
Principle: tier your accounts, or a list is only as good as its checks.

**Good quiz:** "Two companies on your list share a name, one per coast. Which check tells you which one to keep?"

## Lesson 3. When are they ready?

**Teach:** the same account is a bad target in March and a great one in June. A {{buying signal}} is an event you can see from outside that makes the pain urgent.

**Must contain:**
- A `signals` block: 3 to 5 signals. For each: the name, what to watch (the exact thing on the page), why it means "ready", and **one live example** on an account from lesson 2, dated and sourced.
- A `timeline` of the dated signals you found, newest first (date, account, what happened).
- A `callout` on timing: signals go stale. Most are worth acting on for 30 to 90 days.
Principle: trigger events, or signals decay.

**Good quiz:** "Which of these is a buying signal for <Company> and which is just news?" with three real events.

## Lesson 4. Who exactly?

**Teach:** reach the person who owns the problem, then the person who signs. People change jobs constantly, so check that someone still works there before you write to them.

**Must contain:**
- A `table`: role to reach, where they sit, what they care about, how to find them. Use roles, not names.
- A `steps` block: how to verify a person (current employer on their own profile matches the account's domain, not just the name; a recent post or job change; a company page that lists them).
Principle: champion vs economic buyer, or multi-thread every account.
- If Otto was connected and used: say so in a `tip` callout and show counts ("Otto found 35 people at 24 of the 40 accounts, each checked against their current employer"). Still no names unless the user asked.

**Good exercise:** "Pick one account. Find the person in the persona you tagged as the signer, and check they still work there."

## Lesson 5. What do you say?

**Teach:** the first message is about them, not you. It proves you looked, makes one point, and asks one easy question. See `messages.md`.

**Must contain:**
- A `compare` block: the generic message on the left (the kind every founder gets ten of a day), yours on the right, written for a **real account from lesson 2** using a **real signal from lesson 3**. Put what changed in `notes`.
- A short `steps` or `cards` block with the rules you applied.
Principle: problem before product, or one ask per message.

**Good quiz:** "Which opening line gets a reply?" with one generic, one about you, one about them.

## Lesson 6. Model lab

**Teach:** different Claude models suit different GTM jobs. Bulk sorting and extraction don't need the biggest model. Judgement calls (the ICP decision, a message to a key account, grading work) do. Measure it instead of guessing.

**Must contain:**
- A `modellab` block from `model-lab.json`: the task, each model's cost, time, output, verdict and score, and a takeaway.
- A `table`: which model you would use for each job in this course (research, sorting accounts, drafting messages, grading), and why. Base it on what the lab measured.

See `model-lab.md` for the task and how to judge it. Principle: match the tool to the job.

## Lesson 7. Make it an agent

**Teach:** everything in this course can run every week without you. An agent is a model with instructions, tools and a way to check its own work. Claude Managed Agents hosts it, runs it on a schedule, and grades each run against a rubric you write.

**Must contain:**
- A `pipeline` block: Schedule (the one they set) → Agent (their ICP and signals as instructions) → Tools (web search, optionally Otto) → Grader (the rubric) → Output (new signals on their accounts, with a draft message each).
- A `code` block: the two commands to launch it from `agent/` (see `agent.md`).
- Principle: systems beat heroics.
- A `callout` (tip) on cost and control: where each run's cost shows (the Console), the hard per-run cap in `.env`, and that nothing is sent anywhere without them. Quote a cost only if you measured one.

**Good quiz:** "The agent's first run flags a company that was acquired last month. What do you change so it doesn't happen again: the instructions, the rubric, or the schedule?" Intended answer: the rubric. Add a check that every reported account is still independent, so the grader sends the run back when it isn't. Instructions help too, but only the rubric makes it a checked rule.

## Lesson 8. What happens next?

**Teach:** a plan turns into pipeline over the following weeks: sending, following up, handling replies and learning from results. Show where each piece sits in the 0→1 stack and who does it.

**Must contain** (details and wording in `campaigns.md`):
- A `stack` block: the 0→1 GTM stack (see `campaigns.md`), each layer coloured by who does it: this course, Otto, or the founder.
- A `table`: the GTM loop, one row per step, with columns Step | This course | Otto, as a progression ("Next step →"), never a list of gaps.
- Principle: founder-led sales first, or do things that don't scale.
- A `steps` block: setting up a campaign in Otto from this course, from importing the accounts to the pre-launch check.
- A `callout` (tip): nothing sends until the founder launches it. If the skill created a draft campaign in Otto (only when Otto is connected and the founder asked), say where it is and what the pre-launch check said.

**Good quiz:** "The pre-launch check says 'no mailbox that can see replies'. What happens if you launch anyway?" (Otto refuses to launch until the blocker is fixed.)

---

## Writing the hero

- `title`: "How to sell <Company>"
- `lede`: one sentence on what the company does and the one thing that makes selling it hard or interesting.
- `meta`: 3 or 4 headline numbers, rendered as a stats strip: `{"label": "accounts checked", "value": "107"}`, `{"label": "kept", "value": "23"}`, `{"label": "live signals", "value": "6"}`, `{"label": "sources", "value": "43"}`. Keep `value` short: a number or a short word.
