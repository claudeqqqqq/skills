# GROWTH LOOP: measure -> compare -> learn -> update the skill -> ship (RBLX ANIMATES, v1 2026-11-17)

Instructions for Claude. Read this after HANDOFF.md and LESSONS.md whenever the user says "check my reach", "how is the
channel doing", "what are others doing better", "run the growth loop", "weekly review", or "/rblx-animates growth".
The goal is not views for their own sake. **The goal is a monetized channel that earns money.** Every step ends in a
decision that moves one of the monetization numbers below.

---

## 0. The target (re-verify every cycle; these rules changed in Aug 2026 and change again 1 Feb 2027)

Before each weekly review, search YouTube Help / the YouTube blog and Instagram Help for the current rules and update this
table with the date checked. Never quote thresholds from memory.

| Platform | Milestone | Requirement (checked 2026-11-17) | What it unlocks |
|---|---|---|---|
| YouTube | YPP tier 1 | 500 subs + 3 public uploads in 90 days + 3M qualified Shorts views in 90 days (or 3,000 long-form watch hours / 12 months) | memberships, Super Thanks, Shopping |
| YouTube | YPP tier 2 (now) | 1,000 subs + 10M qualified Shorts views in 90 days (or 4,000 watch hours) | Shorts ad revenue share |
| YouTube | YPP tier 2 (new applicants from 1 Feb 2027) | 1,000 subs + 20M qualified Shorts views in 90 days (or 8,000 watch hours) | same |
| Instagram (India) | Gifts on Reels | 500 followers, professional account, owner 18+ | fan gifts |
| Instagram | Creator Marketplace | 1,000 followers | brand deals |
| Instagram | Subscriptions | 10,000 followers | monthly fan payments |

Facts that change how we work:
- **Watch hours and Shorts views never combine.** We are a Shorts channel, so the Shorts-views lane is ours.
- **Only the last 90 days count**, and only *qualified* views (public Shorts, engaged views). The public counter on the
  video is not the qualified number; read qualified views only from YouTube Studio > Earn.
- **Daily pace needed:** 3M / 90 d = ~33k qualified views per day; 10M = ~111k/day; 20M = ~222k/day.
- **YPP review takes about a month.** Say this honestly: from today's baseline (one Short at 28-1,426 views), reaching 10M
  before 1 Feb 2027 needs a breakout, not a plan. Plan for tier 1 + Instagram Gifts first; treat tier 2 as the 2027 target.
- **Inauthentic content policy (YouTube, clarified Jul 2026):** template-based, near-identical, mass-produced videos are
  not monetized, AI or not. Our kit makes every video look alike by design (same cast, sets, narrator, end card). Volume is
  allowed; sameness is the risk. Every video needs its own story, its own visual hook, varied sets and cast, and real human
  creative decisions (the user's approvals are part of that). A YPP reviewer looks at the channel as a whole.
- **Made for kids:** Roblox-style school stories may be judged as made for kids. That label turns off comments (our ending
  asks for comments) and personalized ads. The user must answer YouTube's audience question truthfully; Claude explains the
  trade-off and never suggests mislabelling.
- **Instagram bonuses are invite-only**; never plan income around them.

---

## 1. Cadence

| When | What | Output |
|---|---|---|
| 48 h after each post | Post check (step 2 only, one video) | one row in CHANNEL_LOG |
| Every Monday | Full loop, steps 2-6 | weekly white card + updated files |
| First Monday of the month | Full loop + fresh competitor search (new channels, not only the known roster) | new RESEARCH_<date>_*.md |
| Any breakout (a video > 5x our median) | Teardown of our own winner: why it worked, make 2 follow-ups fast | lesson + next scripts |

---

## 2. MEASURE our reach (never invent a number)

Sources, in this order:
1. **Windsor.ai connector** (used for the 2026-11-17 baseline). `tool_search "windsor"`, then `get_connectors` to find the
   Instagram and YouTube accounts, `get_fields` to discover real field names (do not guess them), then `get_data` for the
   last 30 days per post and per day.
2. **Screenshots or exports the user gives** from YouTube Studio (Earn tab, Shorts "viewed vs swiped away", audience
   retention) and Instagram Insights (reach, avg watch time, skip rate, shares, saves, follows).
3. **Public metadata** of our own Shorts with `yt-dlp --skip-download -J <url>` (views, likes, comments, duration).
   Run it on the Mac in Claude Code; from claude.ai it may be blocked.

Per video, record (missing = `n/a (reason)`, every number tagged with its source):

`date | platform | ID | title | format | runtime s | views 48h | views 7d | reach | avg watch s | % watched | 3-s skip or swiped-away % | likes | comments | shares/sends | saves | follows gained`

Channel totals each week: followers/subs, uploads in last 90 days, **qualified Shorts views in last 90 days (Studio only)**,
progress to each milestone in section 0 as "X / target (n %)".

**Diagnose with the funnel.** Find the ONE weakest stage, compared with our own median and with the benchmarks in step 3:

| Stage | Metric | Our baseline 2026-11-17 | Healthy target to aim for |
|---|---|---|---|
| Stop | 3-s skip (IG) / swiped away (YT) | 18-33 % skip | lower every week; YT viewed >= 70 % |
| Hold | avg % watched | ~40 % (34-46 s of 95-110 s) | 70 %+ |
| Share | shares per 1k views | ~0 (EP3: 20 shares) | rising; sends are IG's strongest reach signal |
| Talk | comments per 1k views | 0-1 comments total | rising |
| Convert | follows/subs per 1k views | n/a | measure it from now on |
| Volume | uploads per week | 3-7 | see step 3 (leaders post 11-41/week) |

Write the result to `knowledge/CHANNEL_LOG.md` (append-only; create it on the first run with the baseline above).

---

## 3. COMPARE with creators already doing better

Roster (`knowledge/COMPETITORS.md`, append-only):
- **Ceiling:** @dripdyl, @butterbloxe (the user's named benchmarks) and the storyline giants in the 2026-11-17 research.
- **Learnable peers (most useful):** small or new Roblox-story channels whose recent Shorts get >= 10x their subscriber
  count. Add 3-5 new ones every month: YouTube search sorted by upload date and by views ("roblox story", "in this town",
  "roblox animation story", the premise families below), plus the Shorts shelf.
- Drop a channel from the roster after 2 months with no hits.

Method (proven 2026-11-17; LESSONS 2026-11-14 for browser rules): `yt-dlp` metadata + English auto-captions, no media
downloaded; in a browser use `/watch?v=ID`, never `/shorts/` (it auto-advances); Gemini only for qualitative notes on
YouTube links, never for numbers or music names; Instagram reels only through files or notes the user provides.

Per channel record: subs, uploads/week, median views of last 20 Shorts, hit rate (% > 100k, % > 1M), and for the top 5
Shorts: ID, date, views, runtime, title, first sentence, time of the crisis, ending line, comment prompt, series/part number.
Compute **outlier score = video views / channel median**; study the outliers, not the averages.

Then build one side-by-side table: us vs median peer vs ceiling, on every funnel stage plus runtime, words per second,
title pattern, ending type, cadence. Finish with a **gap list: top 3 gaps ranked by (size of gap x how cheap it is for us
to close)**. Public data only; mark estimates as estimates; never copy a script, title or character - take the mechanism.

---

## 4. LEARN: turn findings into rules and tests

Every finding becomes one line:
`rule | evidence (video IDs + counts) | level | how we test it | decision rule set before posting`

Levels: **proven** (our own test won) > **observed** (seen in >= 3 independent channels) > **hypothesis** (1-2 channels or
a hunch). Only proven and observed rules may go into the skill as defaults; hypotheses become experiments.

Experiments (`knowledge/EXPERIMENTS.md`): one variable at a time, everything else identical; 3 posts per arm minimum;
judge at 7 days against our own median; a variant wins only with a ~20 %+ consistent gain on the primary metric and no loss
on the guardrail (e.g. primary = % watched, guardrail = shares/1k). A tie is a valid result. One viral post is noise.

Open questions already waiting for tests (from RESEARCH_2026-11-17): runtime 60-75 s vs 90-120 s; comment question before
the reveal vs at the end; titles "2-5 words + emoji" vs "In This Town..."; pace ~240 wpm vs ~200 wpm; personal stake +
clock in the first 6 s; one-word callback ending.

---

## 5. UPDATE the rblx-animates skill (with change control)

Some rules are the user's decisions (HANDOFF "Decisions made, do not reopen"): runtime 90-120 s, the like/share/follow
ending, the Alex voice, music choices, approvals in white cards. **Claude never changes these on data alone.**

For every proposed change, show a white approval card:
`what changes | why (evidence + level) | how we test it | how we roll back`. Wait for the user's yes.

After a yes:
1. Edit the single source of truth, not every file: numbers in `FORMATS.json`; endings in `ENDING_RULE.md`; format rules in
   `INTOWN_FORMAT.md` / `BLOX_CITY.md`; premises in `EPISODE_CATALOGUE.md`; research in a dated `RESEARCH_*.md`.
2. Change `SKILL.md` itself only when a stage of the process changes (a new gate, a new step, a new tool).
3. Append to `LESSONS.md`: `date | problem | root cause | rule | check`.
4. Bump the kit version + CHANGELOG, and update `HANDOFF.md` (decisions + open items).
5. Where: on the Mac in Claude Code the skill and kit files can be edited directly. In this claude.ai Project the files are
   read-only copies, so write the updated files to outputs and tell the user exactly which files to re-upload.

---

## 6. SHIP content that applies what we learned

1. **Weekly batch plan:** propose 5-7 premises scored 1-5 on: winning premise family (night survival rule, playground game
   gone huge, reversed world, limited-count rule, bond + deadline, secret/monster parent, petty injustice + outsmart),
   personal stake + clock in sentence 1, a visual hook in frame 1, uniqueness vs our last 10 videos, production cost.
   Each week, at least one is a follow-up to our best performer and at least one runs a live experiment from step 4.
2. Each video goes through the normal rblx-animates gates (script + title, music, voice, look, never post without a yes).
3. **Volume vs quality:** breakouts land ~1 in 10-40 uploads in this niche, so cadence matters. Propose (for the user's OK)
   a lighter tier: shorter runtime, fewer shots, reusable but redressed sets - while keeping every story, hook and look
   distinct (section 0, inauthentic content).
4. **Package for each platform:** 3 title options (pattern from step 4), first-frame check (would it stop a scroll on mute?),
   description with 3-5 relevant keywords/hashtags, the same video to YouTube Shorts and Instagram Reels without another
   app's watermark, YouTube audience setting answered truthfully.
5. When the user says it is posted: log it in `<ep>/POSTED.md` and CHANNEL_LOG, and schedule the 48 h check.

---

## 7. The weekly report (one white card, then stop)

1. **Money progress:** each milestone from section 0 as X / target and %, plus the 90-day pace (on track / behind by N/day).
2. **Scorecard:** this week vs last week vs our median, by funnel stage; the weakest stage named.
3. **Best and worst video** and the one-sentence reason for each (evidence, not opinion).
4. **What leaders did differently** (top 3 gaps from step 3).
5. **Experiment results** (win / lose / tie, with numbers).
6. **Changes needing approval** (each in the card format from step 5).
7. **Next week's plan:** the premises, the experiment, the posting days.

---

## 8. Never

- Invent, round up or "estimate as fact" any view count, retention, threshold, track name or BPM. Missing = say so.
- Buy views, followers or comments; sub4sub; engagement pods; fake comments; misleading titles or first frames.
- Re-upload or closely copy another creator's video, script, character or title.
- Use ripped music or meme audio (muted/claimed reels); music follows MUSIC_PLAYBOOK.md.
- Change a user decision, the narrator, or post anything without the user's explicit yes.
- Promise that any video will go viral or that monetization will happen by a date.

