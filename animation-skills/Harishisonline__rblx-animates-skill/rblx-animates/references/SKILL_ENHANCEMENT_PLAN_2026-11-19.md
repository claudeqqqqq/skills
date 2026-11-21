# RBLX ANIMATES: total skill enhancement plan (2026-11-19, for the owner's approval)

**Purpose:** why our Shorts don't go viral, measured against the channels that are booming, and every change to the
rblx-animates skill and kit, in the order to implement. Nothing here is applied yet. Mark each item **YES / NO / CHANGE**,
and I implement the approved ones.

**Evidence levels used below:**
- **measured:** our numbers (yt-dlp metadata, audio analysis).
- **claim:** a creator, vendor or blog says it.
- **YT:** YouTube's own statements.

---

## 0. Summary: the 10 gaps, biggest first

| # | Gap | Us (measured) | Booming channels (measured) | Cost to fix |
|---|---|---|---|---|
| 1 | **Viewers swipe away. Every Short stalls at the first test batch** | 7 Shorts: 42-1,500 views, **flat at 1,400-1,500**. That is the size of YouTube's first test audience; it never widens | Gneef median 3.8M, Baseplate 4.9M, GreenBroRants 3.1M, Noobifiedd 4.0M; small breakouts 13k-275k median | the sum of 2-8 |
| 2 | **Narration flow** | 10.8-15.7 pauses of 0.3-0.6 s **per minute**; 23-47 % of sentence ends pause over 0.3 s; gap after a full stop 0.24-0.30 s | **1.9-3.1 per minute**; **4-7 %** of sentence ends pause; gap after a full stop **0.18-0.20 s**. Practically continuous speech | low |
| 3 | **Voice is flat (robotic)** | Adam samples have a pitch range of only **8-10 semitones** (D 9.5). Alex had 13.6-15.1 | narrators range **12-17 semitones**, median pitch **166-196 Hz** (young, bright) | medium |
| 4 | **Packaging (titles)** | median **94 characters**, **86 % with hashtags in the title**, long caps sentences, a typo ("In this town aughing charges you"). Channel name "Roblox animated" ≠ handle @rblxanimates | Gneef, GreenBro, Baseplate, Ashyyy, dripdyl: **3-4 words, 13-18 characters, 1 emoji (90-100 %), 0 % hashtags, 0 % "In this town"** | low |
| 5 | **Script density and specificity** | 330 words / 100 s; generic townspeople; few chain reactions | 550-710 words / 124-174 s; named neighbours (Mrs. Ruiz, Coach Briggs, Mr. Hale), exact numbers (300 donuts, 11:15), chain reactions, inline sound words ("Snap!", "Ding!", "Crack!"), short quoted lines in character | low (writing) |
| 6 | **Volume** | 7 Shorts in about 7 days | leaders 11-41 Shorts a week (RESEARCH_2026-11-17); breakouts land about 1 in 10-40 uploads | high (render time) |
| 7 | **Originality / channel identity** | stock voice (Alex, now Adam), copied caption style (miro), "In this town" phrasing, kit look not yet a recognisable cast | one recognisable narrator, cast, colour mood and title style per channel | medium |
| 8 | **Motion density** | 0.39 keyed actions/s; 18 % recipe cameras | miro claim: viral Shorts move more (the "strongest signal") | medium (approved 2026-11-19) |
| 9 | **We don't see our own funnel** | no "viewed vs swiped away" numbers; Windsor returns empty YouTube rows | YT: the "viewed vs swiped away", average-viewed and satisfaction signals drive the Shorts feed | low (screenshots) |
| 10 | **Runtime vs stage** | 80-120 s for every Short (owner decision) | giants 124-174 s; small-channel breakouts median about 59 s (RESEARCH_2026-11-17) | decision |

---

## 1. Data and method

**Channels compared** (shorts tab, latest 60 each, yt-dlp, 2026-11-19):
- Gneef (2.2M subs)
- GreenBroRants (1.47M)
- ItsBaseplate (1.07M)
- Ashyyy- (890k)
- GeloStories98 (776k)
- UnluckyGuyStories (568k)
- Noobifiedd (548k)
- dripdyl (511k)
- VoidCastRants (448k)
- itsRedBear (50k)
- FriendBobN1 (23k)
- and **ours** (@rblxanimates, channel name "Roblox animated", 27 subs, 7 Shorts)

**"Ears" (measured audio):**
- Pipeline: vocals separated from the music (demucs), then word timing (faster-whisper on the vocals), then pitch and loudness (Praat).
- Viral videos: Never Be Caught Awake (Gneef, 34M), The Knocker Copies Your Voice (Gneef, 31M), Shadow Tag (Baseplate, 19M), Sorry 10 Times (VoidCast, 16M).
- Ours: EP3, EP4, Laughs Charge You v1/v2, and the Adam samples A-F.
- **Limit:** YouTube's bot check blocked more downloads from the Mac after 4 viral audios (HTTP 403/429, "confirm you're not a bot").
  - A slow retry runs in the background, and the numbers get updated when it finishes.
  - Using your browser's YouTube cookies would lift the block. I didn't, because it uses your login; say if you want it.
- Code and raw data: Mac `~/RobloxStories_tmp/research/ears/` (`analyze_ears.py`, `out/*.json`, `ears_summary.json`).

**SEO and algorithm:** YouTube's statements as reported in 2026 guides. Sources are at the end.

---

## 2. The narration, measured (the core of "it sounds like AI slop")

| Metric | Viral (4 videos, 16-34M) | EP3 | EP4 | LCY v2 | Sample D (your pick) | F1 (pause map) |
|---|---|---|---|---|---|---|
| Words per second | **4.07-4.41** | 3.24 | 3.46 | 3.16 | 4.63 | 4.70 |
| Gap after a full stop (median) | **0.18-0.20 s** | 0.28 | 0.30 | 0.24 | 0.18 | 0.40 |
| Sentence ends with a pause over 0.3 s | **4-7 %** | 44 % | 47 % | 32 % | 0 % | 50 % |
| Pauses of 0.3-0.6 s per minute | **1.9-3.1** | 14.4 | 15.7 | 11.6 | 0 | 14.1 |
| Pauses over 0.6 s per minute | **0-0.4** | 0.6 | 0.6 | 1.7 | 0 | 0 |
| Median pitch | **166-196 Hz** | 135 | 136 | 143 | 141 | 162 |
| Pitch range (10th-90th percentile) | **12-17 semitones** | 14.3 | 13.6 | 15.1 | **9.5** | 9.3 |
| Sentence endings falling / rising | **54-74 % / 5-15 %** | 89 % / 2 % | 98 % / 0 % | 59 % / 11 % | 50 % / 0 % | 80 % / 0 % |

**What this means:**
1. **Viral narration is almost continuous.**
   - The next sentence starts about 0.2 s after a full stop, about the same as after a comma.
   - A real pause (0.3-0.6 s) happens only 2-3 times a minute, and nothing longer.
   - The one long pause in 158 s of Shadow Tag (0.46 s) comes just before the clock strikes.
   - **Our pause map (F) went the wrong way; I added pauses the viral narrators don't use. D's continuous flow was right.**
2. **D is right on flow and pace but flat on melody.**
   - Adam's pitch moves 8-10 semitones; the viral narrators move 12-17.
   - That missing up-and-down is the "robotic" sound. Speeding up 1.5-1.9x in post makes it worse.
3. **Their sentence endings vary.** About 70 % fall and about 10 % rise ("...and it jumps right back together."). Our EP3/EP4 fell 89-98 % of the time: a "reading out loud" pattern.
4. **Their voices are younger and brighter** (166-196 Hz). Adam is 119 Hz raw; D's alien effect lifts it to 141 Hz.
5. **Stress.** Our loudness-based measure was too crude to separate them (all near 0). Stress has to be judged by ear (yours) for now.

---

## 3. The script, measured (transcripts of the 4 viral videos)

| | Viral | Ours |
|---|---|---|
| Length | 549-708 words, 124-174 s | 323-330 words, 95-103 s |
| Opening | the rule in 1 sentence, then "You see," + mechanics in the next 2-3 sentences, often with a sound word ("Snap! Good as new... Ding!") | the rule plus fragments ("At your jokes." "Like a phone.") |
| World examples | 4-8 concrete ones with **names and numbers**: "the driver used one, and 300 donuts flew back into the window"; "Pizza delivered after 11:59 gets left on the roof" | 3-4 generic ("our mayor", "the weatherman") |
| Narrator intro | "Me? I'm 12, and I'm down to one." / "My name is Max, and I'm the best fake sleeper alive." + 3 proof details | "And me? I'm Nico. I'm not funny." |
| The person at stake | a sibling or best friend, with **one signature detail that pays off later** (Pearl's bridge, Dex can't sleep) | Grandma (OK), but no planted detail |
| Plot trigger | "Then, one night, a giant storm came." / "Last Friday, at sunset, ..." | "Then came the storm." (OK) |
| Escalation | a **chain reaction** told fast ("She tagged the mailman. The mailman got Coach Briggs. Coach Briggs got a kid on a skateboard...") + a **clock** ("The fire trucks were 20 minutes away") | linear list of doors |
| Solution | **the narrator uses the rule's loophole** ("If I cut the last rope, the bridge would be mine to fix.") | laughing (OK) |
| Dialogue | short quoted lines inside the narration ("Pearl, no!"; the Knocker: "Hey, sweetie! It's Grandma!") | quotes read in the narrator's voice |
| Sentence style | full conversational sentences joined by "and / so / but", 6-12 words, fragments only for SFX or punch | many 2-4-word fragments |

---

## 4. Packaging and YouTube SEO (measured + YT + claims)

YouTube says the Shorts feed reads **viewed vs. swiped away**, average view duration and % viewed, plus likes and survey
satisfaction (YT, via YouTube Help and creator-liaison statements). Click-through rate is not the Shorts signal. In 2026 YouTube
added a push toward **original content** (reported). Titles still matter for search, for the channel page and for how
viewers judge the channel. Hashtags have only a minor categorisation role (claims; YouTube ignores all of them above 60 per video).

| Item | Now | Proposal |
|---|---|---|
| Title | 94 characters, caps, hashtags, "ROBLOX STORY PART 2", typos | **2-4 words + 1 emoji, the rule's object** ("Sorry Limit 🙏", "Laugh Battery 🔋"). No hashtags and no "In this town" in the title (the giants: 0 %). Checked for spelling before upload |
| Description | hashtags only | 1 teaser line (the rule as a question) + 3-5 hashtags (#roblox #robloxanimation #robloxstory #shorts + 1 topic) |
| Channel name | "Roblox animated" (generic, not the handle) | "RBLX ANIMATES" everywhere (YouTube, Instagram, watermark-free end frame) |
| Channel page | 7 mixed Shorts (Blox City storylines + In-this-town + a trailer) | one format per channel identity (decision below); a pinned best Short; playlists per format; the 2 weekly ~20-min compilations feed long-form watch hours |
| Upload time and cadence | irregular | a fixed daily slot; target 1-2 Shorts a day (see 7) |
| First frame | varies | the rule visibly happening + the first word at 0.0 s (already in the skill; becomes a hard check) |
| Made for kids | not decided | answer truthfully each upload (comments off if "made for kids") |
| Comments | none | the story ends on its last line (approved); comments come from a debatable twist; reply to every comment in the first hour |

---

## 5. Narration v3 recipe: built from the measurements, not from guides

1. **Voice:** Adam + the D alien effect (your pick) for In-this-town; you said "everywhere", so Blox City too, **pending your yes**.
2. **Flow targets** (checked automatically on every take, from the viral numbers):
   - 4.3-4.6 words/s
   - gap after a full stop 0.15-0.22 s
   - at most 3 pauses of 0.3-0.6 s per minute, **only** at "Then one night", the clock and the twist
   - nothing over 0.6 s
   - first word at 0.0 s
   - **no meme pauses**; sound effects play under the voice.
3. **Melody target:** pitch range 12 semitones or more, median 165-195 Hz after the effect, at least 8 % rising sentence ends. Every take is measured with the same ears pipeline, and a take under target is redone, not shipped.
4. **How to get Adam's melody wider.** We test 3 routes on the same 20-second hook and you pick by ear:
   - (a) eleven_v3 "Creative" (stability 0.0) per story section with emotion tags, little speed-up (at most 1.3x)
   - (b) multilingual_v2 with stability 0.25 / style 0.5 per section
   - (c) **Speech-to-Speech into Adam from an energetic read.** You read the script into your phone; ElevenLabs converts it to Adam's voice and keeps your timing and melody. This also makes the voice "only yours" (miro). Never a performance taken from someone else's video.
   - Cost: about 1,500 characters / credits for the 3.
5. **Post-processing rule:** speed-up at most 1.35x. Above that the voice turns robotic: F1 at 1.6x and F2 at 1.9x had a pitch range of only 9.3-9.4 semitones and sounded robotic to you. If the raw take is slower, regenerate faster instead of squeezing it.
6. **Quoted lines in character voices** (approved): 2-4 short lines per Short, each with one ElevenLabs voice per character type (kid, grandma, monster), mixed at the narrator's level.
7. **QA gate (new tool `tools/ears_check.py`):** words/s, pauses per minute, gap after a full stop, pitch range, median pitch, rising share, every word spoken (whisper). Prints PASS/FAIL against section 5.2-5.3.

## 6. Script v3 rules (replaces the earlier plan, built from the 4 transcripts)
1. **Length:** 450-650 words at 4.4 words/s, which is 100-150 s. This needs your decision, because it reopens the 80-120 s rule (see 9).
2. **Order:**
   1. the rule (1 sentence)
   2. "You see," + mechanics with a sound word
   3. 4-6 named, numbered world examples ("Mrs. Lane argued with it for an hour. Now her door is held together with duct tape.")
   4. "Me? I'm [age], and [my number/flaw]." + 2-3 proof details
   5. my person + one signature detail that pays off later
   6. "Then one night / Last Friday at sunset,"
   7. a fast chain reaction
   8. a clock ("20 minutes away")
   9. the narrator uses a loophole of the rule
   10. the payoff of the planted detail
   11. a 1-line wry ending.
3. **Sentences:** full conversational sentences of 6-12 words joined with and / so / but. Fragments only for sound words ("Snap!") and the punch line.
4. **Specificity:** at least 4 named townspeople, at least 6 exact numbers or times, 2-4 short quoted lines.
5. **Banned:** fragments as filler ("Like a phone."), moral statements, "little did I know", "everything changed".
6. **Style lock:** `references/STYLE_EXAMPLES.md` gets 3 scripts you approve, written to these rules (I draft them; you pick). Every new script is compared with them before it reaches you.

## 7. Volume: the second lever
- Breakouts land about 1 in 10-40 uploads. We post about 1 a day at 2-7 h of render each.
- Proposals:
  - (a) a **lite tier**: 60-75 s, 25-35 shots, 2 reusable but redressed sets, Eevee or low-sample Cycles. Target 1 render per hour of machine time.
  - (b) a batch-render queue overnight (the Mac renders while you sleep; keep it awake with `caffeinate`).
  - (c) 2 compilations a week (already decided).
- Each Short still gets its own premise, sets and cast (YouTube's inauthentic-content rule).

## 8. Measurement: stop guessing
- After 48 h and 7 d, a YouTube Studio screenshot of each Short: **"Viewed vs swiped away"**, average % viewed, and the retention graph. Windsor can't give these for our channel.
- Targets (claims, consistent across 2026 guides):
  - **viewed at least 70-75 %** (ours unknown; the flat 1.4-1.5k views suggest it is low)
  - average % viewed at least 70 %.
- **One experiment at a time:**
  - narration v3 vs the current one
  - title style
  - runtime 70 s vs 130 s.
- 3 posts per arm, judged at 7 days (GROWTH_LOOP rules).

## 9. Decisions only you can make
1. Adam + D effect for **Blox City too**? (You said "everywhere".)
2. Runtime: keep 80-120 s, or move In-this-town to **100-150 s** like the giants, with a 60-75 s lite tier for volume?
3. Narration route test (5.4): a/b/c, including **reading the script yourself** for Speech-to-Speech?
4. Use your browser cookies so yt-dlp can finish the bot-blocked downloads (more viral voices measured)?
5. Channel identity: one In-this-town world (one town, a recurring cast, one colour mood, our own caption style). Should Blox City move to a second channel or a playlist?

## 10. Implementation order (after your YES)

| Step | Change | Files |
|---|---|---|
| 1 | Narration v3 targets + ears QA gate + no meme pauses + max 1.35x speed-up + character voices | SKILL.md section 5, references/VOICE_SPEC.md, tools/ears_check.py (new), tools/ep_audio/post.py (no-pause mode), tools/ep_audio/tts.py (per-section + v3/v2/STS routes) |
| 2 | Script v3 rules + STYLE_EXAMPLES.md (3 approved scripts) | SKILL.md section 3, references/INTOWN_FORMAT.md, STYLE_EXAMPLES.md (new) |
| 3 | Packaging rules (titles, description, name, cadence) + a pre-upload checklist that checks spelling and length | SKILL.md section 10, references/VIRAL_PLAYBOOK.md section 5, tools/package_check.py (new) |
| 4 | Motion gate, own captions, audible bed (approved 2026-11-19) | already in the skill card; kit ep_viral_check thresholds |
| 5 | Lite tier + overnight queue | SKILL.md section 7/9, tools/ep_final.sh (caffeinate + queue), templates/lite_shots.py |
| 6 | Measurement: CHANNEL_LOG + swipe-away screenshots + EXPERIMENTS.md | references/GROWTH_LOOP.md, CHANNEL_LOG.md, EXPERIMENTS.md |
| 7 | Lessons + HANDOFF + kit version 6.0 + CHANGELOG | docs/LESSONS.md, HANDOFF.md, CHANGELOG.md |

---

**Sources (YouTube algorithm / SEO, 2026):**
- [OutlierKit: the Shorts algorithm in YouTube's words](https://outlierkit.com/resources/youtube-shorts-algorithm/)
- [vidIQ: How the YouTube Shorts algorithm works in 2026](https://vidiq.com/blog/post/youtube-shorts-algorithm/)
- [TrueFuture Media: data-backed guide](https://www.truefuturemedia.com/articles/youtube-shorts-algorithm-data-backed-guide)
- [fliki: Shorts algorithm and the 2026 originality push](https://fliki.ai/blog/youtube-shorts-algorithm)
- [Shopify: ranking signals by surface](https://www.shopify.com.au/blog/youtube-algorithm)
- [unil.ink: YouTube SEO 2026 (tags minimal role)](https://unil.ink/blog/youtube-seo-guide-2026)
- [hashtagtools: Shorts hashtags title vs description](https://hashtagtools.io/blog/youtube-shorts-hashtags-title-vs-description-2026)

Earlier research in the Project:
- RESEARCH_2026-11-17_viral_roblox_shorts.md
- RESEARCH_2026-11-19_miro_viral_roblox_shorts.md
- RESEARCH_2026-11-19_voice_and_growth.md
- NARRATION_DELIVERY_2026-11-19.md

The pause-map recommendation in that last file is **superseded** by section 5 here.
