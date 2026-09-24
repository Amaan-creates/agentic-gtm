# Lesson 8: where the course stops, and campaigns in Otto

## Where the course stops

The course **decides and prepares**; Otto runs it day to day. Show lesson 8 as a progression: what the course prepared, and the next step Otto takes. Never present it as a list of gaps.

| Step of the GTM loop | This course | Otto |
|---|---|---|
| Decide who buys (ICP, personas) | ✓ lesson 1 | Keeps the ICP and scores new accounts against it |
| Build the account list | ✓ lesson 2, checked once | Company search against the ICP, kept in a workbook |
| Watch for buying signals | ✓ lesson 3, then the agent on your schedule (lesson 7) | Signal Agents watching the accounts continuously |
| Find the right people | Method only (lesson 4) | Verified people and their current employer |
| Write the first message | ✓ one example (lesson 5) | A sequence per account: first message plus follow-ups |
| **Send it, follow up, stop when they reply** | Next step → | **Campaigns** on LinkedIn and email, paced within daily limits |
| **Handle replies** | Next step → | Inbox triage (interested, question, objection, not now…) and reply drafts |
| **Track what works** | Next step → | Campaign performance: accepts, replies, reply rate |
| **Keep the CRM up to date** | Next step → | Pushes companies and contacts to a connected CRM without duplicates |

## Setting up a campaign in Otto from the course

Write these as the `steps` block in lesson 8. They work in the Otto app or through Otto's MCP server with the tool named in brackets.

1. **Bring the accounts in.** Import the lesson 2 table into a workbook named after the course (`import_leads` with `workbook`). Include each company's domain so Otto matches existing companies instead of creating new ones.
2. **Bring the people in.** Add the people you found for each persona (`import_people`). Run it as a dry run first and check the preview: every person should attach to one of the imported companies, with **no new companies created**. If the preview shows new companies, fix the company names or domains before the real import.
3. **Pick a sequence.** Look at the templates (`list_templates`) and create a **draft** campaign from one (`campaign_from_template`). Nothing launches at this point.
4. **Write the steps.** Put the lesson 5 message in as step 1 and add one or two follow-ups that surface a different finding rather than repeating the pitch (`edit_campaign_sequence`). Otto can also draft a sequence per account from its signals (`draft_sequence`).
5. **Enrol and schedule.** Enrol the workbook (`add_to_campaign`), and set send days, the send window, time zone and a daily cap (`update_campaign`).
6. **Check before launch.** Run the pre-launch check (`campaign_setup_review`). It lists anything missing: no leads, empty copy, no connected mailbox or LinkedIn account, no schedule.
7. **Launch when you're ready,** yourself. Replies then land in Otto's inbox, where they are triaged and a reply can be drafted for your approval.

## Rules for the skill

- **Never launch a campaign, and never send anything.** Launching is the founder's decision, made in Otto after they've read the copy.
- If Otto is connected **and the founder asks for it**, the skill may do steps 1 to 6 and leave a **draft** campaign, then tell them where it is and what the pre-launch check said. Imports and drafts are free; `draft_sequence` costs credits, so ask first.
- Without Otto, lesson 8 shows the table and the steps as a guide, plus one line on where to start: [otto-pilot.io](https://otto-pilot.io).
- Keep it factual: say what each step does, and don't promise results (reply rates, meetings).
