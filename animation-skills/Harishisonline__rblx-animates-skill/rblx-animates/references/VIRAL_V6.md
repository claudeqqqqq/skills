# VIRAL v6: script, narration, packaging and the self-learning loop (kit v6.0, 2026-11-19)

Approved by the owner on 2026-11-19 ("implement everything that the viral videos do"). Source:
`research/SKILL_ENHANCEMENT_PLAN_2026-11-19.md`. This file is the single source of truth for HOW an In-this-town Short
is written, voiced and packaged. Numbers live in `FORMATS.json` (`in_this_world.script_v3`, `.narration_v3`,
`.package_v6`); the tools read them from there.

**Evidence:**

- Viral narration (EARS, demucs + faster-whisper + Praat): Never Be Caught Awake (Gneef J0OQXSo1chk, 34M), The Knocker
  (Gneef RVszt4A-ucc, 31M), Shadow Tag (Baseplate AYdbna6xYrU, 19M), Sorry 10 Times (VoidCast TAYxdugYgzg, 16M).
- Viral scripts: those 4 transcripts + dripdyl outliers No Leaving The Water (j3igYdggxBg, 7.8M) and Monster Under The
  Bed (25smqwt9wVc, 6.0M), auto-captions from `growth_scan.py`.
- Packaging: the last 60 Shorts of 11 booming channels (yt-dlp).
- Ours: EP3, EP4, Laughs Charge You v1/v2, voice samples A-F.

**Levels:**

- **observed:** 3+ independent channels.
- **measured:** our own measurement.
- **claim:** a creator or vendor says it; becomes an experiment, not a rule.

**Honesty rule:** a gate that passes does not mean a video will go viral. It means the video no longer fails the
numbers the viral videos share.

---

## 1. Scripts v3 (gate: `tools/script_lint_v3.py script.txt` = 0 FAIL before the owner sees the script)

What the viral transcripts share, measured (viral vs ours):

| | Viral (6 outliers) | Ours (EP3, EP4, LCY) |
|---|---|---|
| Length | 549-708 words | 328-330 words |
| Trigger ("Then one night" / "Last Friday at sunset") | 6/6 | 0/3 |
| Mechanics opener ("You see," / "The rule is simple.") | 5/6 | 0/3 |
| Narrator intro ("Me? I'm ..." / "My name is ...") | 4/6 | 1/3 |
| and/so/but/then/because per 100 words | 3.9-6.7 | 2.4-5.0 |
| Fragments of 1-3 words | 9-41 % (dripdyl 9-11 %) | 30-49 % |
| A clock (minutes away, at midnight, 11:59) | 6/6 have one or more | 1/3 |

**Write it like this:**

1. **Sentence 1 = the rule:** "In this town / In this world, [something everyone has or does] [does something]." 9-14 words.
2. **"You see,"** + the mechanics in 2-3 sentences, often with a sound word ("Snap! Good as new." "Ding!").
3. **The world:** 4-6 concrete examples with a name or a number, told as little chain reactions ("The driver used one, and
   300 donuts flew back through the window."). The town's laws ("Sleepovers are banned.").
4. **"The rule is simple."** + the rule again in one line (optional, 3 of 6 do it).
5. **"Me? I'm [age], and [my number/flaw]."** or "My name is X, and I'm the best [skill] alive." + 2-3 proof details.
6. **My person** (sibling or best friend) with one signature detail that pays off later (Dex can't sleep; Pearl's bridge).
7. **"Then one night, ..." / "Last Friday, at sunset, ..."** The trigger.
8. **Fast chain reaction + a clock** ("The fire trucks were 20 minutes away.").
9. **The narrator uses a loophole of the rule** (sleepwalkers are asleep; cut the last rope so the bridge is mine to fix).
10. **The planted detail pays off.**
11. **A 3-12-word wry last line** (callback, twist), then a hard cut. No CTA in this format.

**Sentences:** told to a friend. Full sentences of 6-12 words, joined with and / so / but / because. Fragments are only for
lists ("Slow breathing. One arm off the bed."), sound words and the punch line. 1-6 short quoted lines, spoken in
character voices (section 2).

**Banned** (linter FAIL): "little did I know", "in a world where", "everything changed", "it was then that", morals spelled
out, any like/share/comment CTA in In-this-town.

**Hard idea criteria (unchanged, owner 2026-11-19):**

- the rule is about something everyone has or does
- a friend or family member is at stake
- a visible counter or clock
- a twist that pays off the rule

Then the 20/25 VIRAL_PLAYBOOK score.

**Tiers** (`FORMATS.json` `in_this_world.tiers`):

| Tier | Words | Runtime at 4.35 w/s | Role |
|---|---|---|---|
| **full** | 450-720 | 100-165 s | the main format, like the giants |
| **lite** | 250-340 | 60-78 s | volume and the runtime experiment (section 5) |

---

## 2a. House narration "v3" (owner 2026-11-20, supersedes the generation part of section 2)

`tools/ep_audio/narrate_house.py` (see VOICE_SPEC v6.1) is the only way voices are made.
- **Model:** eleven_v3 Creative, one request per paragraph, tags as written.
- **Editing per sentence:** silences capped at 0.12 s, a 4.75 w/s speech pace, 0.06 s joins.
- **FX:** applied last (Adam + D for In-this-town; Alex for Blox City).
- **Approved by ear on the full Yawn Curfew take:** "This is what I want".
- **Measured:** 4.21 w/s, pitch range 12.7 st, 0.18 s after a full stop, 2.8 pauses of 0.3-0.6 s per minute.

## 2. Narration v3 (gate: `tools/ears_check.py audio/voice.wav --script script.txt` = 0 FAIL, then the owner's ear)

Viral numbers (all 4 pass the gate; our old takes fail 4-5 checks, sample D fails only melody):

| Metric | Viral | Gate |
|---|---|---|
| Pace | 4.07-4.41 w/s | 4.05-4.65 |
| Gap after a full stop | 0.18-0.20 s | 0.13-0.24 s |
| Sentence ends with a >0.3 s pause | 4-7 % | at most 10 % |
| Pauses of 0.3-0.6 s | 1.9-3.1 a minute | at most 3.5 a minute |
| Pauses over 0.6 s | 0-0.4 a minute | at most 0.6 a minute |
| Pitch range (p10-p90) | 12.1-16.8 semitones | at least 12 st |
| Median pitch | 166-196 Hz | 155-210 Hz (WARN) |
| Rising sentence ends | 5-15 % | at least 5 % (WARN) |
| First word | - | at most 0.06 s |
| Script words spoken | - | at least 97 % |

**Recipe** (`tools/ep_audio/narrate_v3.py` replaces `tts.py`; then `words.py`, `post.py` with `{"mode": "flow"}`, then `ears_check.py`):

- **Voice everywhere (owner 2026-11-19):** ElevenLabs premade "Adam - Dominant, Firm" `pNInz6obpgDQGcFmaJgB` + the "D"
  alien FX: `asetrate=44100*1.1892,aresample=44100,atempo=0.8409,vibrato=f=5.5:d=0.08`. Alex is retired for new
  episodes; never change the narrator without a clip and a yes.
- **Generate per story section** (blank-line sections in `tts_script.txt`), and take speed from the model, not from post.
  `post.py` tempo is capped at 1.35: F1/F2 at 1.6-1.9x measured 9.3 st, and the owner heard "robotic".
- **3 routes for the melody (the owner picks by ear on one 20-second hook; ~1,500 credits for all 3):**
  - `v2`: multilingual_v2, stability 0.30, style 0.45, speed 1.2, previous/next text.
  - `v3`: eleven_v3, Creative (stability 0.0), style 0.35, with [excited] [whispers] [deadpan] tags per section.
  - `sts`: the owner reads `tts_script.txt` energetically into a phone (`audio/performance.wav`) and Speech-to-Speech turns it
    into Adam, keeping the owner's timing and melody. This is also the most original voice for YouTube's originality
    push. Never a performance taken from another creator's video.
- **Flow edit** (`post.py` mode `flow`):
  - every silence over 0.20 s becomes 0.18 s
  - meme SFX play under the voice (no inserted pauses)
  - at most 3 deliberate beats of 0.3-0.5 s in `beats.json`: the trigger, the clock, the twist.
  - This supersedes the 2026-11-19 pause map (NARRATION_DELIVERY): the pause map added the pauses the viral narrators
    don't use.
- **Character voices on quoted lines** (owner-approved 2026-11-19):
  - Write `{grandma} "Nico, sweetie!"` in `tts_script.txt`.
  - Map the names in `audio/voices.json`. Voice ids come only from the ElevenLabs voice list, shown to the owner.
  - 1-6 lines per Short, mixed at the narrator's level. No alien FX on them.
- Measure every take. A take under target is regenerated, not shipped.

---

## 3. Packaging and YouTube SEO (gate: `tools/package_check.py <ep>` = 0 FAIL; `<ep>/package.json`)

What YouTube says the Shorts feed uses:

- viewed vs swiped away
- average view duration and % viewed
- likes and satisfaction surveys

In 2026 YouTube also pushes original content. Click-through rate is not the Shorts feed signal. Titles still matter for
search, the channel page and Suggested. More than 60 hashtags makes YouTube ignore all of them.

The booming channels (last 60 Shorts each, measured 2026-11-19):

| | Booming channels | Ours (before v6) |
|---|---|---|
| Title length | 3-4 words, 13-18 characters | 94 characters |
| Emoji in the title | 98-100 % have one | 71 % |
| Hashtags in the title | 0 % | 86 % |
| "In this town" in the title | 0 % | 29 % |
| Hashtags in the description | - | up to 39 |

- **Title:** 2-4 words + 1 emoji, naming the rule's object ("Laugh Battery 🔋"). Title Case, no caps sentence, no "PART",
  "ROBLOX STORY" or hashtags, spell-checked.
- **Description:** line 1 is a teaser: the rule as a question ("Would you laugh to stay alive?"). Then 3-5 hashtags:
  #roblox #robloxstory #robloxanimation #shorts + 1 topic.
- **Pinned comment:** one open question about the loophole or twist. Reply to every comment in the first hour.
- **Instagram caption:** a hook line + 3-5 hashtags.
- **Channel identity:**
  - display name "RBLX ANIMATES" on YouTube and Instagram (the YouTube name still reads "Roblox animated")
  - a channel banner and description that say what the channel is ("Roblox stories where one rule changes everything")
  - playlists per format: In This Town and Blox City; Blox City stays on this channel as its own playlist
  - pin the best Short to the channel page.
- **First frame:** the rule visibly happening, plus the first word at 0.0 s (SKILL section 3, first 3 seconds).
- **Made for kids:** the owner answers truthfully on every upload.
- **Cadence:** a fixed daily posting slot. Same file to YouTube Shorts and Instagram Reels, no watermark.

---

## 4. The funnel targets (what "viewed, not swiped away" means in numbers)

YouTube Studio > a Short > Analytics shows "Viewed vs swiped away". Windsor does not expose it, so screenshots are needed
48 h and 7 d after each post.

| Metric | Target (claims in 2026 guides; mark as claim) |
|---|---|
| Viewed (stayed to watch) | 70-75 % or more |
| Average % viewed | 70 % or more |

Our history: 7 Shorts that all stalled at 1,400-1,600 views. That is the size of the first test audience, which
suggests a low "viewed" share; it is not measured yet.

**Likes and comments come from the story, not from asking:**

- a debatable loophole, an easter egg or a mystery in the last 10 s
- the pinned question
- replies in the first hour

---

## 5. Experiments queued (one variable at a time, 3 posts per arm, judged at 7 days; `docs/EXPERIMENTS.md`)

1. Narration route v2 / v3 / sts (the owner's ear first, then viewed % on 3 posts each).
2. Runtime: full 100-150 s vs lite 60-78 s (primary: viewed %; guardrail: % viewed).
3. Title: object + emoji vs a 4-6-word premise with emoji.
4. Beats: 0 vs 3 deliberate beats.

---

## 6. Monetization: the honest pace (re-verify on YouTube Help each weekly run)

YPP tier 1 needs 500 subscribers, 3 public uploads in 90 days, and 3M qualified Shorts views in 90 days. Tier 2 (ad revenue)
needs 1,000 subscribers and 10M (20M for applicants from 1 Feb 2027). Thresholds were checked 2026-11-17.

On 2026-11-19 we have 27 subscribers and about 9k views in total. Tier 1 in 2 weeks would need about 214k qualified
views a day, roughly one 3M-view breakout, and YouTube's review then takes about a month.

So the plan does not promise a date. It maximises the chance of a breakout: more uploads that each pass every gate, a
weekly loop that removes the biggest measured gap, and 2 follow-ups within 48 h of any Short that beats 5x our median.

---

## 7. The self-learning loop (weekly; `docs/GROWTH_LOOP.md` section 9)

Every Monday 10:17 IST a scheduled run on the Mac:

1. `tools/growth_scan.py --discover` (+ `--ears` when YouTube allows):
   - re-measures our channel and the roster
   - finds this week's outliers and new channels
   - profiles their titles and scripts
   - writes `research/growth/<date>/GAPS.md`
   - appends `CHANNEL_LOG.md`
2. Runs the gates on our latest episode: `script_lint_v3`, `ears_check`, `package_check`, `ep_viral_check`.
3. Writes `research/growth/<date>/REPORT.md`. It follows GROWTH_LOOP section 7: money progress, scorecard, best and
   worst Short, top 3 gaps, experiment results, changes for approval, next week's plan.
4. **Self-updates (no approval needed, logged):**
   - re-measured thresholds in `FORMATS.json` when 3+ new outliers move a viral range
   - new rows in `COMPETITORS.md` / `roster.json`
   - new lessons
   - new experiments.
   Each self-update gets a LESSONS line and a CHANGELOG line with the evidence.
5. **Needs the owner's yes:**
   - any change to `SKILL.md`, delivered as a skill-update card
   - the narrator, music, runtime, endings, captions style, posting, deleting.
   The run leaves these as proposals in REPORT.md.
6. **Never:** post, delete, buy engagement, invent a number, copy a script, title or character.
