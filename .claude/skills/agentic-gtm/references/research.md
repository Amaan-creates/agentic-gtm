# Research: what to collect and where it hides

Spend most of the research on **evidence of who already buys**. It decides the ICP, and it's the part founders get wrong.

## Checklist

| Collect | Where it usually is |
|---|---|
| What they sell, in one sentence | Home page hero, the meta description, the first paragraph of the About page |
| Who it's for | Solutions or industries pages, "built for" lines, the case-study index |
| Named customers | `/customers`, `/case-studies`, logo strips, testimonials, press releases, partner pages |
| Why customers bought | The **problem** paragraph of each case study; quotes from customers |
| Pricing or deal model | `/pricing`, or for deal-based businesses the licence or partnership terms they publish: per seat, per usage, per location? That hints at the buyer (per-seat sells to a team lead, per-location to operations) |
| Competitors | Comparison pages ("X vs Y"), "alternatives to" searches, review sites |
| Where they are going next | Job posts (a new sales hire for a segment is a strong hint), changelog, recent funding announcement, blog |
| Stage | Funding announcements, team size on the company page, accelerator directory |

## Method

0. **Check the company's current status first.** Search the company name with "acquired", "sells", "pivot", "renamed" and read the newest news before anything else. If it has pivoted, sold a business line or renamed, the course follows the **current** business: older case studies become proof that it can deliver, not evidence of who buys now.
1. Fetch the home page, then follow its own links to customers, pricing, careers and about. The site tells you what it thinks matters.
2. Read two or three case studies in full. Note the customer's **type**, **size**, **role of the person quoted**, and the **number** they cite.
3. Search for the company name plus "customers", "case study", "raises", "hiring". Watch for other companies with the same name: add the domain to the search.
4. Search for "<category> alternatives" to find competitors.
5. Write it all to `research.md` as you go, each fact with its URL. Number the sources `s1, s2, …` in any stable order, and keep the ids the same in `research.md` and `course.json`.

## When the company buys rather than sells

Some companies grow by acquiring or licensing (assets, supply, inventory, talent). Then "who buys" becomes **"who we need to win over"**: the owner of the thing they want. Build the ICP, accounts and signals around that party, and say so plainly in lesson 1.

## When a careers page looks empty

It is probably rendered by JavaScript. Look for the job board's public JSON feed (the page source usually names the job board) instead of concluding there are no jobs.

## When the site is thin

Early startups often have one page. Then:
- The founders' own posts and talks usually say who they built it for.
- Job posts describe the customer ("you'll work with operations teams at…").
- An accelerator profile often has a one-line customer description.
- If there is still no evidence of buyers, say so in lesson 1 and base the ICP on the problem the product solves. Mark it as a hypothesis.
