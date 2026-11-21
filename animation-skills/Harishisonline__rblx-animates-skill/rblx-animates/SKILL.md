---
name: "rblx-animates"
description: "Make RBLX ANIMATES Roblox-style story Shorts end to end: research, script, voice, Blender animation, mix, finish, packaging and the growth loop."
---

# RBLX ANIMATES: Roblox story video studio

This skill reproduces the production line behind the Instagram channel @rblxanimates: original, blocky Roblox-style 3D story
reels, 9:16 (In-this-town Shorts: full tier 100-165 s, lite tier 60-78 s; Blox City storylines 90-120 s; plus ~20-minute compilations of uploaded videos), narrated by one voice (Adam + the "D" alien FX, kit v6.0), with meme sound effects, burned-in captions, a like/share/follow end card on Blox City episodes only, and a growth loop that measures the channel, compares it side by side
with Shorts that are winning right now (benchmark: @DripDyl) and updates this skill from what works. The quality bar is the two finished episodes in `examples/`:
EP2 "The Poor Boy Who Bought the School" and EP3 "I Told ONE Secret. By Lunch, Everyone Knew."

The work is long (about 5 hours, 2.5 of them unattended rendering) and the person cares about each stage, so the line has
**approval gates**. Treat them as part of the craft, not bureaucracy: every gate exists because skipping it once cost hours.

| # | Stage | Gate (stop and wait for the person) |
|---|---|---|
| 0 | Setup check | - |
| 1 | Viral research (when asked, when topics run dry, or when the growth loop finds a weak stage) | - |
| 2 | Topic + script | **Script + title approved** (white card) |
| 3 | Music question | **Music answer** (their track or the default) |
| 4 | Voice take | - (owner 2026-11-20: the house narration "v3" (`narrate_house.py`) is the approved sound, no more samples; the full take is made directly, must pass ears_check, and the owner hears it with the look-dev/final) |
| 5 | Meme SFX + mix | - (they hear it with the voice gate or the final) |
| 6 | Shots + low-res QA | - |
| 7 | Look-dev stills | **Look OK** |
| 8 | Final render + finish | - |
| 9 | Delivery + wrap-up | **Never post** without an explicit yes for that exact file |

If the person says "just make it, we'll review after", gates 4 and 7 may be skipped for that episode; write that down in
the episode's `story.json` (`"gates": "waived by the user <date>: '<their words>'"`).

---

## 0. Setup check (once per machine, 2 minutes)

The kit is the `kit/` folder of this repository, installed to `~/RobloxStories` by `scripts/install.sh`. Episode work lives in
`~/RobloxStories_tmp/<slug>` with a symlink `~/RobloxStories/videos/<slug>` pointing at it (Blender tools find episodes
through `videos/`). Check, in this order, and fix before writing anything:

1. `~/RobloxStories/rbx/shotlib.py` exists (else run `scripts/install.sh` from this repo).
2. Blender 5.3+: `/Applications/Blender.app/Contents/MacOS/Blender --version` (macOS) or `$BLENDER`.
3. `ffmpeg -version`, and `~/RobloxStories/.venv/bin/python -c "import numpy, PIL"`.
4. ElevenLabs: `~/RobloxStories/.env` has `ELEVENLABS_API_KEY=` (paid tier; library voices fail on free keys).
   `cd ~/RobloxStories/tools/ep_audio && python3 el.py` prints tier and credits left. **Never print or paste the key.**
5. Optional ears: a browser with Gemini (gemini.google.com) for listening reports (see section 5).

Running from a cloud agent linked to the person's computer: run Blender and long jobs **on the computer, detached**
(`subprocess.Popen(..., start_new_session=True)` or `nohup` there). Sandboxed shells usually kill background jobs when the
call ends; a 2-hour render must not depend on your shell staying open. Poll logs instead of waiting inside one call.

---

## 1. The formats - never mix them

Read the reference for the format you are making before writing a single line.

**Blox City** (`references/BLOX_CITY.md`): storyline episodes, each one custom. A first-person kid narrator, a clear wrong
(bullying, betrayal, a secret sold), an escalation, a reversal and a warm callback ending. Blox City branding is allowed
("Blox City High", "Blox Tea"). Ideas: `references/EPISODE_CATALOGUE.md` (Day 01-30 with punchy titles; 01 and 02 are made).

**In this town / In this world** (`references/INTOWN_FORMAT.md`, `FORMATS.json`): premise in the first sentence
("In this town, every lie shows on your wrist"), short dense sentences, time-marked escalation, twist ending. Its own bed and
rules. Never put Blox City names or branding into it.

**Current priority (owner, 2026-11-17): new viral "In this town / In this world" videos built to the section 2 and
section 3 rules. Do not remake or re-render old episodes.**

**Kit v6.0 (owner 2026-11-19: "implement everything the viral videos do"): `~/RobloxStories/docs/VIRAL_V6.md` is the
single source for script v3, narration v3, packaging/SEO, funnel targets and the self-learning loop. Where an older rule
in this skill disagrees with VIRAL_V6, VIRAL_V6 wins.** Three new gates must be 0 FAIL before the owner sees each
stage: `tools/script_lint_v3.py` (script), `tools/ears_check.py` (voice), `tools/package_check.py` (title/description).
Each gate passes the viral references and fails our old episodes (`tools/v6_selftest.sh` proves it weekly).

**Big Game (dripdyl style)** (section 2 rules, `RESEARCH_2026-11-17_dripdyl_gemini.md`): the owner's benchmark format. Cold open "I [tiny action] and [huge
overreaction]" ("I stepped off a couch and 50 firefighters blasted me with fire hoses."), then "Welcome to the world's
biggest game of [playground game]", "The rules were simple." (3 strikes, last one standing wins $1,000,000), a roster of
absurd rivals (one hasn't moved since 2019, a grandma, a 5x champion), traps and eliminations each with a deadpan tag
("He went down." / "Worth it."), the narrator wins by **noticing a small detail**, a host fake-out, and a 3-8-word home
callback gag ("I've been up here for 3 days."). dripdyl runs 130-165 s at 3.7-4.2 words/s; ours are 80-120 s Shorts. Original games and gags only.

All formats share the narrator, the ending rule (`references/ENDING_RULE.md`), the look and the kit.

---

## 2. Viral research (when asked "what's trending", when the growth loop finds a weak stage, or before a new batch)

Goal: learn the mechanism of videos that are winning **right now**, as rules you can apply. Copy the mechanism, never the
script, title or characters. The proven method (2026-11-17, 16 videos, `RESEARCH_2026-11-17_dripdyl_gemini.md`):

1. **Find candidates.** The person's links first. Then the benchmark roster (`references/COMPETITORS.md`): @DripDyl
   (benchmark the owner wants to match), @butterbloxe, @GreenBroRants, @Gneef, @RyoRants, @Xenost-j3i, @itsRedBear, @PurpleHat. Then
   YouTube search by upload date and by views ("roblox story", "in this world", "in this town", "roblox animation story")
   and the Shorts shelf. Prefer **outliers**: a Short with views >= 10x the channel's subscribers, or >= 5x its median.
   Ask Gemini (same task chat, step 3) for 10 more from the last 30 days with exact `/watch?v=` links; it finds them, you
   measure them. On 2026-11-17 all 10 of its links were real but only 1 was a winner (8.5M); the rest had 6k-370k views,
   so filter by measured views and outlier score before learning from anything.
   **Benchmark rule (owner 2026-11-19):** rules and numbers come ONLY from outliers (views >= 10x subscribers or >= 5x the
   channel median). A single video from a small channel (BvvcR_LJRuQ, 85 subs) once pulled our pace the wrong way. Tutorial,
   course and vendor videos (miro, Crealix, nicheless) are **claims**: record them, test them, never make them rules alone.
2. **Measure with yt-dlp (numbers only come from here):** `yt-dlp --skip-download -J https://www.youtube.com/watch?v=ID`
   for views, likes, comments, duration, upload date, channel subscribers; `--write-auto-subs --sub-langs "en.*" --sub-format
   json3` for the words. From the captions compute words per second, the first sentence, when the crisis starts, the ending
   line. Use `/watch?v=ID` links, never `/shorts/` (it auto-advances). No media is downloaded.
3. **Watch with Gemini, Task mode, one chat.** Signed-in pro account at `https://gemini.google.com/u/1/app` (the person's
   default for research; check the avatar says the pro account and the picker says **Hydrogen**). Click **Task** (not Chat:
   Chat mode often answers "I can't watch YouTube" and refuses several videos at once). Keep the whole research run in **one
   task chat**; follow-ups go into that chat, never new chats. Write "Watch each of these Shorts one by one with the YouTube
   tool" and give all links as `/watch?v=` URLs. Ask per video for: what is on screen in the first 3 s and the first sentence;
   structure with timestamps; narrator voice (gender, age, accent, pitch, energy, pauses, punchline delivery, side-character
   voices); shot length, camera, why the motion looks clean; faces and overlays; caption style/position; music moods and SFX;
   the ending; why it went viral. End the same task with a voice-direction brief and an animation checklist. Read the answer
   with JS (`[...document.querySelectorAll('model-response')].at(-1).innerText`), wait 30-60 s per video.
4. **Trust levels.** Gemini is good at describing visuals, structure and delivery. It is wrong on numbers (it said 165 words
   where the transcript had 276, and 175-190 wpm where dripdyl measures 220-250) and cannot name music. Numbers: yt-dlp.
   Music: Content-ID card, on-screen credit or the person's Shazam. Mark everything else "Gemini, unverified".
5. **Record** per video in a dated `RESEARCH_<date>_*.md` (Project + repo `references/`): ID, channel, subs, views, likes,
   comments, runtime, date, outlier score, words/s, first sentence, beat map with times, ending, voice notes, animation notes,
   lesson. Then turn findings into rules (section 11 step 3) - a finding is not a rule until it is observed in 3+ channels.

### What the winners do (observed in 16 Shorts + 10 measured finds, 2026-11-17; re-check monthly)

- **Sentence 1 is the whole premise**, and frame 1 **shows it working** (the boy visibly shrinks; numbers float over heads;
  50 firefighters blast him). No title card, no greeting.
- **Rule + cost/condition in sentence 2** ("...but if they get the ick, it's gone"; "the only way to grow back is a truth
  that's hard to say"), then **3-4 absurd world examples with numbers and authority figures** (mayor the size of a pencil,
  grandma 500 pull-ups), then **"And me?"**: the narrator's handicap or the opposite of everyone.
- **"Until one night..." / "On Friday..."** brings a family or crush stake (sister in a fire, mom's last word).
- **The weakness is the only solution / the villain trips his own rule** (the 4-inch kid is the only one light enough; the
  narrator yells "RON! YOUR MOM IS HERE!"; the liar mayor is forced to answer yes/no live).
- **Numbered escalation** ("Night 1... Night 5", "Strike one... Strike three", an on-screen clock) gives the rhythm.
- **The rule solves the crisis in reverse** (lie on purpose to shrink into the vent; the useless toast power floats the bus).
- **Visible counters/progress bars** (BRAD'S CRUSHES: 212 -> 0, word counts, 0 -> 8,000,000,000) act as a clock.
- **Pace 3.8-4.9 words per second** (dripdyl 3.7-4.2, In-this-world hits 4.1-4.9). Near-zero dead air.
- **Cuts every 0.5-2.5 s**, camera never still, 2D face swaps on the beat, anime overlays (sweat drops, "!", hearts, comic
  starbursts), 1-3-word yellow/white captions with a heavy black stroke.
- **Music changes mood with the story** (playful -> tense -> warm/triumphant) and drops to silence for a wait; SFX on
  nearly every cut.
- **Endings:** a callback gag (dripdyl: "I've been up here for 3 days"), an emotional truth line, a rule-reversal twist, or a
  cliffhanger question that sets up Part 2. Most have no like/share CTA; one used an open comment prompt.
- **Runtimes split in two:** In-this-world rule stories 37-57 s, and storyline/game stories 135-180 s. Titles: 2-6 words +
  emoji, or the full premise.

---

## 3. Topic and script (gate: script + title)

If the person did not name a topic, propose 3 one-line premises tied to the research or the catalogue and let them pick.
Then write the script. The model for structure and density is `examples/EP3_friend_secret/SCRIPT_AND_PLAN.md`
(and EP2's). What makes these work:

- **Script v3 (kit v6.0, VIRAL_V6 section 1; gate `python3 tools/script_lint_v3.py <ep>/script.txt [--tier lite]` = 0
  FAIL):** measured on 6 viral transcripts (16-34M views) vs ours. The real gaps are length (viral 549-708 words, ours
  ~330), a "Then one night / Last Friday at sunset" trigger (6/6 viral, 0/3 ours), "You see," / "The rule is simple."
  mechanics (5/6), "Me? I'm 12, and ..." / "My name is X, and ..." (4/6), a clock (6/6), flowing told-to-a-friend
  sentences joined with and/so/but (3.9-6.7 per 100 words) and fewer 1-3-word fragments (dripdyl 9-11 %, ours 30-49 %).
  Order: rule -> "You see," mechanics + a sound word -> 4-6 named/numbered world examples as little chain reactions ->
  "Me?" + proof -> my person with a planted detail -> trigger -> fast chain reaction + clock -> the narrator uses the
  rule's loophole -> the planted detail pays off -> 3-12-word wry last line, hard cut.
- **Length by format and tier (owner 2026-11-19, kit v6.0; numbers in `FORMATS.json` in_this_world.tiers):**
  In-this-town **full** 100-165 s (450-720 words, like the giants) and **lite** 60-78 s (250-340 words, for volume and
  experiment E2); Blox City 90-120 s (300-370 words). (Superseded: 80-120 s, 2026-11-18.) **Long videos**
  are ~20-minute compilations of videos already on the channel (2 a week, no new animation, built from finished
  `out/final.mp4` files; YouTube long-form watch hours count toward YPP separately from Shorts views). Kit v5.1 delivers
  ~3.8-4.2 words/s for In-this-town (TEMPO 1.12, 0.24 s meme pauses). Write `story.json` with
  `"format"` (`in_this_town` / `blox_city`), `"tier"` (`short`; `long` = compilation) and `"hook_word"` (the twist word that must land
  by 2.5 s); the kit reads them. Count words with a script, don't guess; if over the tier, cut pauses first, then a line.
- **Hook = the whole promise in one breath:** "I told my best friend one secret. By lunch, the whole school knew. And he
  got paid for it." The viewer decides in two seconds.
- **One line = one beat**, each beat a picture the camera can show. Concrete, visual details (a duck night-light, a shoe
  with a hole a pencil fits through) carry the story and become the props and callbacks.
- **Character voices on quoted lines (owner 2026-11-19, replaces "narrator reads everything"):** 1-6 short quoted
  lines per Short, written `{grandma} "Nico, sweetie!"` in `tts_script.txt`, voices mapped in `audio/voices.json` (ids
  only from the ElevenLabs voice list, shown to the owner).
- **Meme SFX marks** `[RECORD SCRATCH]`, `[BRUH]`, `[FAHHH]`... sit after a full stop, in a word gap, never on a word.
  Plan 15-20 per episode, but at most 8 get a pause (0.24 s); the others play in word gaps with `"no_pause": true` in
  `meme_cues.json`. They are never spoken.
- **Reversal + callback:** the wronged kid wins by character, not revenge, and the last story line returns to the opening
  object ("The hole still fits a pencil." / "half my class ordered duck night-lights").
- **What to make: `references/VIRAL_PLAYBOOK.md`.** Premises from the 7 families scored 1-5 on mute test, 3x
  escalation, buildable with the kit, reverse-rule climax and shareability; propose only premises at >= 20/25 (show the
  score on the white card), with a personal stake + clock early and a visible counter when the rule has a number. Write
  with its beat template (template B stretched to 80-120 s; template A 45-60 s and the 35-45 s "lite" format are not
  used for now - owner 2026-11-18), its first-sentence formulas and its ending formulas. Check COMPETITORS.md so a
  premise is not a recent hit (copy mechanisms, never premises, titles or characters).
- **Hard idea criteria (owner 2026-11-19), all four or the premise is dropped:** the rule is about something everyone has
  or does (your first word, your laugh, your last meal - never "I'm a sock"); a friend or family member is at stake; a
  visible counter or clock; a twist that pays off the rule. Then the 20/25 score.
- **In-this-town = the 12 beats (owner 2026-11-19, Crealix formula, matches our template):** 1 the rule in one line ->
  2 how it works, with visible details -> 3 a small case and a huge one -> 4 the legend (one crazy thing that once
  happened) -> 5 how the whole town lives with it -> 6 "And me?" (the narrator's flaw or role) -> 7 my person (friend or
  sibling, a detail that comes back) -> 8 the problem with real stakes -> 9 three tries that fail, each bigger -> 10 the
  last card (what the hero never wanted to do) -> 11 the big moment -> 12 the twist / a question to the viewer. One beat
  per line, every line a new picture, the rule always pays off. At 4.3-4.6 words/s: ~260-275 words per 60 s.
- **Style lock (owner 2026-11-19):** `references/STYLE_EXAMPLES.md` holds 3-5 scripts the owner approved. Every new script
  is written against them (rhythm, sentence length, jokes, endings), then checked for AI-slop phrases ("little did I
  know", "in a world where", "everything changed", "it was then that", stacked adjectives, morals spelled out). A
  generic AI script is never shown to the owner.
- **First 3 seconds decide "stayed to watch" (check before approval, every format):** frame 0 is motion or the weirdest
  picture of the video (open on the climax image or the rule happening), never a static phone screen, a text wall or a
  character standing; sentence 1 is a world rule or an absurd consequence ("I did X and Y happened"), never backstory -
  the twist word lands by 2.5 s; a sharp SFX inside 0.5 s; voice starts at full energy with no silence; only one thing to
  read (1-2-word captions, no UI paragraph); 2-3 cuts or one big camera move before 3 s; the stakes read on mute.
  Our EP3/EP4 openings failed this (backstory sentence, twist word at ~4 s, static phone UI for 2 s; Gemini comparison
  2026-11-17). Write the 0-3 s plan (frame, words, SFX, cuts) on the white card next to the title.
- **Viral rules (In this world / Big Game):** apply "What the winners do" in section 2: premise in sentence 1 shown in
  frame 1, rule + cost in sentence 2, 3-4 absurd world examples, "And me?", "Until one night", the rule used in reverse,
  an on-screen counter where the premise has a number, deadpan one-line tags after absurd beats. Build the story around
  one visual rule or twist; earnest moral arcs alone read as predictable (Gemini scored our premise 5.5 vs 9.5).
- **Pace and dead air:** measured 2026-11-17: EP3 3.3 and EP4 3.45 words/s overall with 17-18 meme pauses (~8 s of
  silence); dripdyl 3.7-4.2, In-this-world hits 4.1-4.9 with almost no dead air. Keep at most 6-8 meme pauses, cut every
  other silence over 0.15 s except a deliberate 0.25 s beat before a punchline. The owner wants faster takes like the
  viral channels (2026-11-18): kit v5.1 uses TEMPO 1.12 for In-this-town; still play the sample. Measure, never assume.
- **Title (kit v6.0, gate `tools/package_check.py`):** 2-4 words + exactly 1 emoji naming the rule's object ("Laugh
  Battery 🔋"), at most 32 characters, Title Case, spell-checked; never hashtags, "In this town", "PART 2" or "ROBLOX
  STORY" in the title. Measured 2026-11-19: booming channels 13-18 characters, 98-100 % one emoji, 0 % hashtags; ours
  94 characters, 86 % hashtags, one typo ("aughing").
- **Ending depends on the format (owner 2026-11-18, `references/ENDING_RULE.md` v2):**
  - **In this town / In this world: no like/share/follow line and no "Comment X or Y".** End on the last story line - a
    3-8-word callback gag, a truth line, a rule-reversal twist or a cliffhanger (VIRAL_PLAYBOOK ending formulas) - and cut.
    Comments come from the story (mystery, loophole, easter egg). The kit draws no end card without the like line.
  - **Blox City storylines keep it:** "Like, share and follow for more." then a one-word, two-option question: "Would you
    give Max a second chance? Comment TRUST or BLOCK." (one-tap answers get comments; themed phrases got zero).
- **TTS spelling:** the voice model mangles "Blox". Write "Blocks City" / "Blocks Tea" in `tts_script.txt` only; captions and
  the script keep "Blox".

Deliver a script document with: 2-3 punchy title options, cast, word count and runtime estimate, the script, the meme SFX
cue sheet (after which words, which sound, where it comes from), music options, and a beat map (time, beat, shots, kit notes).
Present title, script and music question for approval in a clean white card. **Stop until they approve.**

---

## 4. Music (ask before producing)

Ask: **"Do you have background music for this one?"**
- **Yes:** take their file (or track name). Use it as the bed for the whole video unless they give switch points.
- **No:** use the default bed. The channel's default is "Numbers" by TEMPOREX (the sound of viral "In this town" videos),
  but this repository cannot ship it. If the person has their own licensed copy at `~/RobloxStories/assets/music/default_bed.wav`,
  use it. Otherwise `tools/ep_audio/bed.py` composes an original bed with `tools/score.py` (numpy only, no samples), so
  the video never ships silent.

Make **one** final video with the bed mixed in (`out/final.mp4`). Write `MUSIC_LICENSE.txt` in the episode folder: what
the bed is and who holds the rights. Business accounts can get commercial songs muted; CC BY-NC music is never allowed;
Kevin MacLeod tracks were rejected by the channel owner (not the sound viral creators use).

---

## 5. Voice

**House narration "v3" = THE voice for every video (kit v6.1, owner 2026-11-20 on the full Yawn Curfew take: "This is
what I want ... this exact voice each and every time for all of my videos"; reference takes
`~/RobloxStories_tmp/yawn_curfew/voice_test/YawnCurfew_hook_v3_withbed.mp3` and `YawnCurfew_FULL_v3_withbed.mp3`). The
owner calls it "v3"; never rename it or change the method without a new yes.**
- **Who speaks:** In-this-town = Adam `pNInz6obpgDQGcFmaJgB` + the D alien FX; **Blox City storylines = Alex**
  `yl2ZDV1MzN4HbQJbMihG`, the same method, no FX. Character voices for quoted lines as below (no narrator FX on them).
- **Generate:** `EP=<ep> python3 tools/ep_audio/narrate_house.py [--voice adam_d|alex]` (preset from `story.json`
  format). One eleven_v3 request per `tts_script.txt` paragraph (stability 0.0 Creative, similarity 0.75, style 0.35,
  speaker boost), performed exactly as written - the tool adds no tags. Then per sentence from the alignment: trim, cap
  inner silences at 0.12 s (ffmpeg silenceremove -42 dB), stretch to a 4.75 w/s speech pace (factor 0.80-1.35; short
  lines the same pace as long ones; sentences starting with a sound word keep their length); 0.06 s joins; no extra beats
  (audio/beats.json only if the owner asks, max 3); THEN the narrator FX on the whole take + HPF/EQ/comp + loudnorm -14
  LUFS. Writes `audio/voice.wav`, `voice.mp3`, `words.json` (faster-whisper on the final take, matched to `script.txt`
  tokens) and `narrate_report.json`. Cached per paragraph: re-runs are free and rebuild the identical take (proven: the
  rebuild of the approved Yawn Curfew take differs by 0.0). Then `tools/ears_check.py audio/voice.wav --script
  script.txt`. Do NOT use `narrate_v4.py` (superseded: it added [speaking quickly] to the yawn lines).
- **Write `tts_script.txt` like `~/RobloxStories_tmp/yawn_curfew/tts_script.txt`:** one paragraph = 1-3 sentences =
  one request: `[emotion] [speaking quickly] text`, EXCEPT paragraphs with a written sound word, `[yawns]`, `[laughs]`
  or `[whispers]`, which get NO `[speaking quickly]`; emotion tags in an arc that RISES from the trigger to the climax
  ([mischievously] [curious] [playful] [matter-of-fact] [serious] -> [ominous] [tense] [urgent] [whispers] [excited]
  [determined] -> [proud] / [deadpan] for the ending); CAPS on the payoff word; numbers and times as words; otherwise
  the same words as `script.txt`. A 100-120 s Short costs about 3,000 characters.
- Never change a voice because of measurements; the owner decides by ear. Never clone a voice from someone else's video.

**Narration v3-route tools of kit v6.0 (`narrate_v3.py` + post.py flow; superseded for generation by narrate_house.py on 2026-11-20; the measurements and rules below still apply):**
- **Voice everywhere: ElevenLabs premade "Adam - Dominant, Firm"** `pNInz6obpgDQGcFmaJgB` **+ the "D" alien FX**
  (`asetrate=44100*1.1892,aresample=44100,atempo=0.8409,vibrato=f=5.5:d=0.08`; owner: "D is perfect, use it everywhere").
  (2026-11-20: Blox City storylines use Alex with narration v4.)
- **Generate:** `EP=<ep> python3 tools/ep_audio/narrate_v3.py --route v2|v3|sts` (replaces tts.py): one request per story
  section (blank-line sections in `tts_script.txt`), speed from the model, narrator FX applied, `{name}` lines in character
  voices; writes `audio/raw.wav`, `alignment*.json`, `narrate_report.json` and `post_cfg.json {"mode": "flow"}` with a
  tempo capped at 1.35. Then `words.py` -> `post.py` -> **`python3 tools/ears_check.py audio/voice.wav --script
  script.txt` = 0 FAIL** -> the owner's ear.
- **Viral numbers the gate holds (EARS: demucs + faster-whisper + Praat on 4 Shorts of 16-34M views; all 4 pass):**
  4.05-4.65 words/s; ~0.18 s after a full stop (0.13-0.24); at most 10 % of sentence ends pause over 0.3 s; at most 3.5
  pauses of 0.3-0.6 s a minute and 0.6 over 0.6 s; pitch range at least 12 semitones (Adam alone 8-10 = the "robotic"
  sound); first word at most 0.06 s. Our EP4 failed 4 checks, sample D only the melody one.
- **Flow edit (`post.py` mode "flow"):** every silence over 0.20 s becomes 0.18 s, meme SFX play under the voice (no
  inserted pauses), at most 3 deliberate beats in `beats.json` (trigger, clock, twist). Never speed a take past 1.35x
  (F1/F2 at 1.6-1.9x measured 9.3 st and the owner heard "robotic"): regenerate faster instead. This supersedes the
  2026-11-19 pause map and everything below about In-this-town pace.
- **Melody routes (experiment E1, the owner picks by ear on one 20-s hook):** `v2` (multilingual_v2, stability 0.30,
  style 0.45, speed 1.2, previous/next text), `v3` (eleven_v3 Creative + emotion tags per section), `sts` (the owner
  reads the script energetically into a phone -> Speech-to-Speech into Adam keeps the owner's timing and melody; the
  most original voice). Never a performance taken from another creator's video.

*History (old episodes only):* In-this-town used Adam multilingual_v2 stability 0.45 / style 0.10 / speed 1.2 + atempo;
Blox City used Alex `yl2ZDV1MzN4HbQJbMihG`, `eleven_v3`, stability 0.0, similarity 0.75, style 0.25 (kit preset `alex_ep1`).
Never change a voice because of measurements; only after playing a clip to the person and getting a yes. Never clone a
voice from someone else's video.

**Delivery direction (dripdyl-style, from the Gemini study; tags for eleven_v3, test at the voice gate):** a sharp friend
telling an unbelievable story - expressive in the setup, flat and matter-of-fact on absurd lines. Lift key nouns and numbers
("FIFTY firefighters"); setups rise, payoffs drop flat; a short breath (comma) before a number or twist; a full stop and a
beat before a deadpan punchline, then move on fast; deadpan = lower and flatter, "like a boring weather report", no
laugh. Rules and stakes slightly slower, action fast. For emotional storylines (butterbloxe), same clarity, ~15% warmer.
Gemini's verdict on our EP3/EP4 (2026-11-17): Alex reads dramatic and calm lines "at the same flat energy", and quoted
lines sound like the narrator. So tag every line with its emotion in `tts_script.txt` (`[excited]`, `[deadpan]`,
`[whispers]`, `[shouting]`, `[sad]`) and make the first line the most energetic of the video. Do not change the voice or
its settings for this; no side-character voices (owner 2026-11-18).
**In-this-town narration v2 (owner 2026-11-19, replaces the EP4 recipe below for this format):** the owner called every
3.2-3.4 words/s take "slow, an old man narrating" / "AI slop". Winners measure 4.1-4.9 words/s (miro's 58-Short study ~260
wpm; Volze 4.6; Crealix's own Adam stories 2.9-3.2 = the slow sound). Rules: **pace 4.3-4.6 words/s overall** (the exact
value = the owner's pick from the 2026-11-19 samples in `~/RobloxStories_tmp/voice_adam/`: B 4.3, C 4.6, D 4.6 + "alien"
FX); every pause over 0.12 s cut to 0.12 s; at most 4 meme pauses of at most 0.25 s; under 2 s of silence in the whole
Short; first word <= 0.05 s. Optional "alien" FX (Crealix claim, test): +3 semitones with tempo kept + `vibrato=f=5.5:d=0.08`.
Check every take by transcription (faster-whisper: every script word spoken, nothing added) and play it to the owner.
Generator: `~/RobloxStories_tmp/voice_adam/make_samples.py` (one request, variants made in post, no extra credits).
**Blox City narration = the EP4 recipe (owner 2026-11-18, after rejecting the per-line v5 takes as "slow-paced AI slop"
 and approving the "Laughs Charge You" video made with it):** ONE eleven_v3 request for the whole script, prefixed
`[fast, urgent, breathless]`, plain `tts_script.txt` lines (no per-line tags), Alex at stability 0.0 / similarity 0.75 /
style 0.25; post = silences over 0.22 s cut to 0.14 s, 0.45 s meme pauses, 0.10 s lead-in, tempo 1.08
(`audio/post_cfg.json` {"pause": 0.45, "gap": 0.14, "detect": 0.22, "lead": 0.10, "tempo": 1.08, "mode": "tight"};
`RBX_TTS_MODE=single RBX_TTS_DEFAULT_TAG="[fast, urgent, breathless]" python3 tts.py`). ~3.3-3.5 words/s, ~1,900 credits per
100 s. Worked example: `~/RobloxStories_tmp/laugh_battery_ep4voice`. The per-line method below stays available for tests only.
Narration (kit v5, `references/DRIPDYL_STYLE_GUIDE.md` section 8): `tts.py` now sends **one request per line** of
`tts_script.txt` with that line's tags (cached, so re-running only pays for changed lines; `RBX_TTS_MODE=single` = old
way); `post.py` starts the voice on frame 0, shrinks gaps to 0.08 s and makes meme pauses 0.24 s (warns above 8; mark
extra cues `"no_pause": true`). Targets: 3.8-4.2 words/s, first word <= 0.05 s. `TEMPO` is 1.12 for In-this-town (owner
2026-11-18: faster takes keep viewers curious to the end) and 1.08 for Blox City, from `story.json` "format";
`audio/post_cfg.json` {"tempo": x} overrides. The person still hears the sample before production.

```bash
E=~/RobloxStories_tmp/<slug>; mkdir -p $E/audio $E/sfx $E/out $E/frames $E/frames_lo
ln -s $E ~/RobloxStories/videos/<slug>
# script.txt (captions, "Blox") + tts_script.txt ("Blocks") + audio/meme_cues.json ([{"line","after_word","sfx"[,"nth"]}])
cd ~/RobloxStories/tools/ep_audio && export RBX_HOME=~/RobloxStories EP=$E
python3 tts.py && python3 words.py && python3 post.py      # raw.mp3 -> words.json, pauses.json, voice.wav (-14 LUFS)
```
`words.py` must print `mismatch []`. `post.py` prints duration, first word and words/s; the runtime must fit the tier
(`story.json`) or fix the script. Send the voice take
(as mp3) to the person and wait. About 1,800 characters of credits per episode.

---

## 6. Meme SFX and mix

All sounds are **our own**: the kit pack (`kit/sfx`, synthesized/generated), ElevenLabs sound generations and short Alex
takes ("[deadpan] Bruh."). Never use ripped meme clips: they get reels muted or claimed.

1. `audio/sfx_jobs.json`: `{"quack": {"sfx": "One single squeaky rubber duck toy quack", "dur": 0.8},
   "bruh": {"tts": "[deadpan] Bruh."}, "ohhh": {"copy": "<earlier episode>/sfx/ohhh.mp3"}}` then `python3 sfxgen.py`
   (existing files are skipped, so it never double-spends).
2. `audio/mix_cfg.json`: which file(s) play for each cue label, per-label gain, extras, and the bed (`examples/EP3_friend_secret/audio/mix_cfg.json`).
   `python3 bed.py` picks or composes the bed (section 4), then `python3 mix.py` then `python3 qa_audio.py` (must print PASS).
3. Levels by measurement: -14 LUFS, true peak <= -1.5 dB, meme hits inside word gaps, tails over speech <= -10 dB under the
   voice, bed clearly under the voice with an 8 dB dip under each hit. The mixer peak-normalises every sound, so dense sounds
   (a phone buzz) come out louder than sparse ones: lower their gain and fade their tails.
4. You cannot hear. Say which you used: measurements, or a Gemini listening report (the person uploads the mp3 at
   gemini.google.com; ask about voice clarity over the bed and whether any effect is too loud). The person's ear decides.

---

## 7. Animation (shots, low-res QA)

Read `references/CLEAN_ANIMATION.md` (the shot grammar and the EP2 post-mortem) and copy patterns from
`kit/templates/EP2_poor_boy_school_shots.py` and `examples/EP3_friend_secret/shots*.py`. Write `<ep>/shots.py`:

```python
from shotkit import *                     # Video, @S(id, word_a, word_b, desc) keyed to words.json indices
from rbx.shotlib import *                 # frame_on, hold, kneel_down, belly_laugh, crowd_laugh, game_screen, appear, car_door, seat_and_type, ...
from rbx import props3 as P3, cast, motion as mo, acting, qa, look
V = Video(__file__); install_snaps()
```
Helpers go **above** the `@S` decorator line, or the decorator swallows them. `V.shot(i, t0, t1, desc)(fn)` takes a zero-arg fn.

The grammar that makes it look clean (each rule fixed a mistake the channel owner caught in a posted video):
- **Cut each beat into simple shots** like the reference reels: MCU to the lens, OTS/POV, a straight-on readable insert, the
  aftermath. Hide big transitions in the cut (a car exit is three cuts: door opens, feet land, stands - never a float).
- **Frame by measurement:** `frame_on(chars, t0, t1, shot="mcu"|"med"|"cowboy"|"full")` for every character shot. A cut-off
  main character is a failure; a background kid's head at the edge can be fine.
- **Contact by construction:** `hold(ch, prop, ...)` puts the fists on the prop and the prop under the fists every frame;
  `P3` props carry grips (+X is the holder's left). Sit before the shot, never during it. Hands touch sleeves and props they
  interact with (`qa.touch`).
- **Acting:** `belly_laugh`/`crowd_laugh(target=...)` keep heads on the target (laughing kids "dancing" or looking away
  was a real complaint); `kneel_down` instead of a pose snap; heads down means head down, not turned away.
- **Readable props and screens:** phone/app/game screens are real UI images straight-on and big, never a number on a slab.
- **Camera and motion follow `references/DRIPDYL_STYLE_GUIDE.md`** (per-beat camera recipes with real `cams.py`
  calls, framing, focus, blur, motion density, pre-render pass/fail checklist; Gemini-written, checked against the code).
  EP4 root causes: 31 of 34 cameras were `frame_on` straight-on (pitch 4, 35 mm, 6 % push, f/2.8 focused between
  characters), 25 of 69 shots idle-only and 1 `strike()` in 96 s, shutter 0.5 on every shot including frame 0.
  **Kit v5 (2026-11-17) makes the fixes the defaults:** `frame_on` alternates +/-22 deg yaw, pitch -4, 45 mm, 15 % push
  from frame 1, f/2.8 solo / 5.6 two-shot, focus on `chars[0]`'s head; motion blur is off unless a shot calls
  `look.motion_blur(0.35-0.5)` (whips, crash zooms, throws, runs); `mo.strike(ch, t, pose, **mo.SNAP)` for comedy hits.
  You still choose: pass only the active character(s) to `frame_on`; use the beat recipes (crash_zoom, whip_pan, dutch,
  impact_shake, run_follow, hero_low, ots) for at least a third of the shots and always for the hook; key a strike, turn
  or gesture every 0.5-0.7 s; idle-only shots at most 15 % and never two in a row.
- **Smooth like the winners (apply and judge on the contact sheet):** no linear keys - ease in-out for moves, overshoot
  ease-out for pops and reactions, ease-in for falls; 2-3 frames of anticipation before jumps, throws, kneels and pick-ups;
  snap into an impact or shock pose in 3-6 frames and hold 8-12 frames with tiny drift; 5-10 deg torso/shoulder counter-
  rotation and head tilt on every pose (Gemini: our upper bodies stay "squared off"); 3/4 low or high angles for reactions
  instead of flat eye-level mediums; the camera always alive (5-8 % eased push-in on every static shot, whip pans or
  match-cut zooms between places); face swaps stepped, 1-2 frames **before** the sound, shock/anger/laugh mouths 20-30 %
  bigger, each big face swap with a head tilt or shoulder pop; motion blur only on fast flights, projectiles and whips,
  never on holds or frame 0; cuts every 0.5-2.5 s (ours already average ~1.4 s: 69 shots in 96 s). Overlays that carry
  the premise: floating counters, comic starbursts ("STRIKE THREE!"), phone pop-ups, sweat drops, "!" and hearts. Keep
  in-world UI in the top 60 % so captions never collide with it. 60 fps is a test (render cost doubles), not a default.
  Indoor and night scenes: test +10-15 % exposure at look-dev so characters pop on a phone (Gemini); the person decides.
- **Prop contact:** Gemini saw props hovering in front of flat hands (EP4 books, keyboard, paycheck; EP3 handshake, phone,
  money bag). Use `hold()` for every held prop and treat any NOTOUCH/PROPFLOAT flag as a blocker, then check those exact
  beats on the 2 fps contact sheet.
- **SFX on the picture:** a whoosh or pop on every cut and face swap and a hit on every impact, mixed under the voice;
  the bed should rise, drop out or change with the story's turns (Gemini: our bed "stays at one flat energy").
- **Look:** `look.STYLE="clean"`, `cast.CLEAN=True` (crisp, matte, neutral, not blue), night like reference
  `references/REF_IG_Dfe8B5Hs3G6.md`, day like `references/REF_IG_Dfs43n3oWqx.md`. Never judge the look from low-res frames.

**Characters:** the kit's blocky cast lives in `kit/rbx/cast.py`, `chars.py`, `acting.py` and the face atlases in
`kit/assets/faces` (Harry, Tyler, Luna, mom, dad, grandma, grandpa, mayor, kids...). Recolor and restyle per episode (see
`leo()`, `maxx()`, `chase()` in the EP3 shots). `kit/docs/CAST.md` lists them.

**Learned from the blocky-shorts build (2026-11-18; the owner rated its output good; our Blender animation stays):**
the same story was made with the Remotion blocky-shorts skill (`~/RobloxStories_tmp/blocky_laugh`, notes in
`BLOCKY_SHORTS_PIPELINE.md`). What made it work, applied to every Blender episode:
- **A shot table before any code:** one row per shot (id, anchor word, set, beat, lens), every shot 0.75-2.2 s, mean
  ~1.35 s (74 shots in 100 s); a cut on the word that changes the picture. Write it as a planner file that prints
  warnings and a SHOTS.md, then keep `shots.py` keyed to the same words.
- **The rule on screen in every frame:** a prop over every head that shows the rule (battery: `rbx/battery.py`
  `battery_hud`; counters, timers) plus a straight insert of it at EVERY number change, with a ding/charge or
  power-down sound on it.
- **A per-character timeline as data:** for each character, segments of (start word, end word, set, place, action,
  emotion, held prop); a shot only picks the set and the lens. At a cut, look the actor up in the shot's own set
  (3-frame tolerance), so nobody pops for a frame.
- **Lens numbers before any render:** LENS_IN (lens inside a body), BLOCKED (a body between lens and face), FACING (the
  face turned to the lens, dot > 0.3), FRAME (face inside a 6 % margin), NEAR (a body within 0.75 m of a fixed lens unless
  it is a planned over-the-shoulder). All clean, then render.
- **Critic the whole film, shot by shot, at least 3 rounds:** a labelled sheet of the middle frame of every shot (the
  low-res pass below gives it), fix, repeat, before look-dev and the final.
- **Vertical framing:** the 9:16 frame is ~30 deg wide: two people 2.3 m apart need the lens ~4 m back; seat a pair
  <= 1.9 m apart and cheat both faces toward the lens; head-down (powered-off, sad) poses get a low lens; in face
  close-ups the head prop sits lower and smaller so it is not cut at the top.
- **Sets:** every interior has four walls (any lens may turn around); doors open away from the lens; no translucent
  light cones in front of faces (a small warm point light under a face instead).
- **Captions: our own signature (owner 2026-11-19).** The white Poppins pop is miro's signature, so it is not ours any
  more. The channel's caption style (colour, font, animation) is the owner's pick from 3 options and is written to
  `references/LOOK.md`; keep 1-2 words, inside the safe zone (centre ~65-68 % height, 12 % side margins), at most 2
  lines, synced to the voice. Mute test: muted and with the name hidden, would someone still know it's ours?
- **Sound (owner 2026-11-19):** the music bed must be clearly audible: ~7 dB under the voice in speech (kit `qa_audio.py`
  "bed in preview" 6-8 dB; the blocky mix's 15+ dB was inaudible and the owner noticed), plus a pop, swoosh or boom on
  every payoff. Previously: the In-this-town bed side-chain ducked under the voice and dropped out for the one awkward-silence beat;
  ~30 kit SFX on story beats (ding on every charge, power-down on every switch-off, thunder on lightning, a rimshot on
  the last gag); -14 LUFS, true peak -1.5 dB.

**Low-res pass + QA:** `Blender -b --factory-startup -P ~/RobloxStories/tools/ep_lo.py -- <slug> all` (detached), then read
`render_lo.log`. Flags: FLOAT, CLIP, HALF, CUTOFF, TINY, NOTOUCH, PROPFLOAT, EYELINE, AWAY, BLOCKED. Fix every one or write
down why it is acceptable (e.g. AWAY on a POV phone shot where the holder's head is hidden on purpose). Then make a 2 fps
contact sheet and **look at it** - flags cannot see "uncanny". EP3 went from 280 flags to 31 accepted ones.
Then run the viral gate: `python3 ~/RobloxStories/tools/ep_viral_check.py <ep>` (static, no render: idle-only shots,
actions per second, recipe cameras, hook move, frame-0 blur, first word, words/s, silences, meme pauses, hook word time from
`story.json` "hook_word", tagged TTS lines, outro). 0 FAIL before look-dev; EP4 fails 8 of its checks.
**Motion density gate (owner 2026-11-19; miro: "the strongest signal" - in 9 of 10 channels the viral Shorts move more
than the same creator's weak ones):** >= 1 keyed action (strike, gesture, turn, react) per 0.7 s, >= 35 % of shots on a
recipe camera (crash_zoom, push_in, dutch, hero_low, dolly_zoom, run_follow, whip...), a push or move on EVERY shot, no
shot static for more than 2 s, and night scenes keyed bright enough to read on a phone. These viral-check lines must PASS
before look-dev (the voice lines follow section 5).

**Going faster with a team (optional):** for 60+ shots, split the work: a Manager/QA agent owns `shots.py` (shared helpers)
and the kit, Blender A owns `shots_a.py`, Blender B owns `shots_b.py` (`shots.py` execs both). They coordinate through an
append-only `BOARD.md` and inbox files. Copy the protocol from `examples/EP3_friend_secret/BRIEF.md`, `BOARD.md` and
`references/TEAM_AGENTS.md`. Give every agent the brief, the ownership rules and the "no final render" limit.

---

## 8. Look-dev (gate: look OK)

Render 6 full-quality 1080x1920 stills of the key looks (night interior, crowd, a readable prop close-up, a dark scene, the
emotional beat, a day exterior), put them side by side (`examples/EP3_friend_secret/lookdev/lookdev_strip.jpg`), compare with
the reference notes, and send them. Say what you measured (brightness, blue cast) and what only their eye can judge. Stop.

---

## 9. Final render and finish

```bash
cd ~/RobloxStories && zsh tools/ep_final.sh <slug> 32          # one Blender run per shot, lock + disk guard, ~1.4 min per second of video
python3 tools/ep_eta.py videos/<slug>                          # ETA from screen time
zsh tools/ep_finish.sh ~/RobloxStories_tmp/<slug>              # captions + end card + audio -> out/final.mp4
```
Test the overlay before the full finish: `tools/ep_captions.py <ep> test t:0 t:30 t:<Like time>`. The end card (Blox City only) is automatic when the script has the like ... follow line; In-this-town videos have none:
heart on "Like", share on "share", a cursor clicks + FOLLOW on "follow", a comment bubble on "Comment" and the two answer
buttons, all centred, with captions moved down to y 0.68.

Before delivering, make a 1 fps contact sheet of the final and look at every tile: readable screens, nobody floating or cut
off, captions not covering important text. Report anything you saw. Give progress updates with ticks and an honest ETA
while rendering (people ask "is it stuck?": answer with frame counts and the last frame time).

---

## 10. Delivery and wrap-up

- Package it (kit v6.0, VIRAL_V6 section 3): write `<ep>/package.json` {title, description, ig_caption,
  pinned_comment, made_for_kids, first_frame, playlist} and run `python3 tools/package_check.py <ep>` = 0 FAIL. Title
  2-4 words + 1 emoji (<= 32 characters, no hashtags / "In this town" / "PART"); description line 1 = the rule as a
  question, then 3-5 hashtags (#roblox #robloxstory #robloxanimation #shorts + 1 topic); a pinned open question about the
  loophole or twist, and replies to every comment in the first hour; Instagram caption = a hook line + 3-5 hashtags;
  playlist "In This Town" or "Blox City"; one fixed daily posting slot; made-for-kids answered truthfully by the owner.
  Channel identity (owner to do once): display name "RBLX ANIMATES" on YouTube (it still reads "Roblox animated"),
  banner + description that say what the channel is, the best Short pinned.
- After posting: ask for the YouTube Studio "Viewed vs swiped away" and retention screenshots at 48 h and 7 d (target
  >= 70-75 % viewed, a claim from 2026 guides); log them in CHANNEL_LOG.md.
- Deliver `out/final.mp4` (and the voice/mix files if asked). **Never post** to Instagram or YouTube without an explicit yes
  for that exact file. Record what was posted in `<ep>/POSTED.md` when they say they posted.
- Cloud backup: before saying a file is in Google Drive, check the Drive app is running and the file is **in the cloud**
  (search it with a Drive connector); a copy in the local Drive folder is not a backup until it uploads.
- Free disk space only after the backup is confirmed and with the person's OK: `frames/` and `frames_lo/` are ~7 GB per
  episode. Never delete their files without asking; deletes are permanent.
- After every fix, append a dated lesson to `~/RobloxStories/docs/LESSONS.md`
  (`date | problem | root cause | rule | check`). Every agent reads LESSONS first. This is how the kit keeps getting better.

---

## 11. Growth loop: measure -> find what wins -> learn -> update this skill -> ship

Run it when the person asks how the channel is doing, to check reach, what others do better, to grow or monetize, "run the
growth loop", every Monday, and 48 h after each post. Full instructions: `references/GROWTH_LOOP.md` (Project instructions).
The goal is a monetized channel, so every step ends in a decision that moves a monetization number.

**Self-learning loop (kit v6.0, owner 2026-11-19; `~/RobloxStories/docs/GROWTH_LOOP.md` section 9):** a scheduled task
"RBLX weekly self-learning loop" runs every Monday 10:17 IST on the Mac:
- `tools/growth_scan.py --discover` writes the roster and our channel, this week's outliers, title and script profiles,
  new candidate channels -> `~/RobloxStories_tmp/research/growth/<date>/GAPS.md` + `CHANNEL_LOG.md`.
- `tools/v6_selftest.sh` = the test cases: every gate must still pass the viral references and judge our latest episode.
- It self-updates measured thresholds, the roster, experiments and lessons, logging each in LESSONS + CHANGELOG with
  evidence. It proposes (never applies) SKILL.md, narrator, music, runtime, ending and caption changes.
- It writes the weekly white card to the Project as `knowledge/WEEKLY_<date>.md`.
- Honest pace: YPP tier 1 needs 500 subs + 3M qualified Shorts views in 90 days. From 27 subs, 2 weeks would need
  ~214k views a day, i.e. a breakout, so the loop maximises breakout chances (more gated uploads, the biggest gap
  closed each week, 2 follow-ups within 48 h of any Short above 5x our median) and never promises a date.

1. **Measure our reach (never invent a number).** Windsor.ai connector (`get_connectors` -> Instagram `17841479901972435`,
   YouTube `91882`; `get_fields` before `get_data`), YouTube Studio / Instagram Insights screenshots the person gives, and
   `yt-dlp -J` on our own Shorts. Per video: views 48 h and 7 d, reach, average watch time and % watched, 3-s skip or
   swiped-away, likes, comments, shares/sends, saves, follows. Append to `CHANNEL_LOG.md`. Re-verify the YPP and Instagram
   thresholds on the official help pages each cycle and report "X / target (%)" and the 90-day pace.
   **"Stayed to watch"** (Shorts feed: viewed vs swiped away) is the number that gets a Short recommended; Shorts have no
   thumbnail click-through in the feed. Windsor does not expose it: ask for the YouTube Studio Shorts screenshot, and use
   `engaged_views / views` as a proxy (2026-11-17: 54-72 %) plus Instagram `media_reel_skip_rate` (18-39 %).
2. **Is it good?** Compare each funnel stage with our median and the peers. Baseline 2026-11-17: IG skip 18-39 %, 33-42 %
   watched, ~0 shares and 0-1 comments per video, IG reach 1.1-1.4k, YT 28-1,426 views; peers in this niche reach 2-25M with
   tens of thousands of likes. Name the **one weakest stage** (stop, hold, share, talk, convert, volume). If any stage is
   below the peer level, go to steps 3-4 aimed at that stage (weak stop -> study first 3 s; weak hold -> beat maps and pace;
   no shares -> endings and emotional payoffs).
3. **Compare ourselves with the benchmark, side by side.** In the same Gemini task chat, give our two latest public
   Shorts and two benchmark Shorts as `/watch?v=` links and ask for: score /10 for each on first 3 s, premise, voice,
   pace/dead air, animation smoothness, faces, camera, overlays/captions, music/SFX, ending, title, look; the biggest gap
   with a timestamp from OUR video; the exact fix; the top 5 gaps ranked by views lost; and why viewers swipe in our
   first 3 s. If the answer is only a summary, ask it to "write the full result here in the chat". Check every claim you
   can by measurement (words/s and silences from `words.json`, cuts with ffmpeg scene detection, outro length, a 0-3 s
   frame strip you look at) and mark the rest "Gemini". 2026-11-17 result: `RESEARCH_2026-11-17_gap_vs_dripdyl.md`.
   To let Gemini judge our production code, give it the public raw GitHub URLs of the repo files
   (`https://raw.githubusercontent.com/Harishisonline/rblx-animates-skill/main/...`). Its Connected Folders did not reach
   the web chat, github.com pages made it ask for a sign-in, and on a later turn raw URLs were blocked too: then paste the
   key code excerpts into the chat.
4. **Find and learn from videos that already win it:** section 2 (outliers, yt-dlp numbers, Gemini Task chat). Write each
   finding as `rule | evidence (IDs + numbers) | level | test | decision rule`. Levels: proven (our own test won) > observed
   (3+ independent channels) > hypothesis. Only proven and observed rules become skill defaults; hypotheses become
   one-variable experiments in `EXPERIMENTS.md` (3 posts per arm, judged at 7 days, ~20 %+ gain on the primary metric with
   no loss on the guardrail; one viral post is noise).
5. **Update this skill with change control.** Show a white card per change: what changes | why (evidence + level) | how we
   test it | how we roll back. The person's decisions (runtime, ending, Alex voice, music, gates) never change on data alone.
   After a yes: edit the single source of truth (numbers in `FORMATS.json`, endings in `ENDING_RULE.md`, formats in their
   files, research in a dated file), propose the `SKILL.md` edit with the skill-update card, append to `LESSONS.md`, bump
   the kit version and `HANDOFF.md`.
6. **Ship** (`references/VIRAL_PLAYBOOK.md` sections 5-6; cadence decided 2026-11-18: as many 80-120 s Shorts as possible
   plus 2 compilations of ~20 minutes a week, built from finished `out/final.mp4` files only).
   Weekly batch of 5-7 premises scored on premise family, stake + clock in sentence 1, visual hook in frame 1,
   difference from our last 10 videos, cost; at least one follow-up to our best performer and one live experiment. Each goes
   through the normal gates. Package: 3 titles, a first frame that stops a scroll on mute, the same file to Shorts and Reels,
   the audience question answered truthfully. Log posts and schedule the 48 h check.

**Never:** invent or round up numbers; buy views or engagement; copy another creator's video, script, character or title;
use ripped music; mislabel made-for-kids; post without an explicit yes for that exact file; promise virality or a date.
Uniqueness matters for monetization: YouTube does not monetize near-identical template videos, so every video needs its
own story, visual hook, sets and cast.

---

## Reference map

| File | Read when |
|---|---|
| `references/BLOX_CITY.md`, `EPISODE_CATALOGUE.md` | Blox City topic/script |
| `references/INTOWN_FORMAT.md`, `FORMATS.json`, `STORY.md` | In-this-town scripts |
| `references/ENDING_RULE.md` | every script and finish |
| `references/MUSIC_PLAYBOOK.md`, `MUSIC_RESEARCH.md` | music question, research |
| `references/VOICE_SPEC.md`, `AUDIO.md`, `GEMINI_AUDIO_NOTES.md` | voice, mix, listening checks |
| `references/CLEAN_ANIMATION.md`, `ACTING.md`, `LOOK.md`, `REF_IG_*.md` | shots, acting, look |
| `references/DAILY_PIPELINE.md`, `TEAM_AGENTS.md` | the day plan, parallel agents |
| `references/LESSONS.md` | before any work: every mistake already paid for |
| `references/GROWTH_LOOP.md`, `CHANNEL_LOG.md`, `COMPETITORS.md`, `EXPERIMENTS.md` | growth loop, "check my reach", monetization |
| `RESEARCH_2026-11-17_dripdyl_gemini.md`, `RESEARCH_2026-11-17_gap_vs_dripdyl.md`, `RESEARCH_2026-11-17_viral_roblox_shorts.md` | viral research, gaps, Big Game format |
| `references/VIRAL_PLAYBOOK.md` | premises, scoring, script templates, endings, packaging, posting plan |
| `references/DRIPDYL_STYLE_GUIDE.md` | every shots.py, tts_script.txt and audio config (camera, motion, narration) |
| `BLOCKY_SHORTS_PIPELINE.md`, `NARRATION_REF_BvvcR_LJRuQ.md`, `VOICE_FIX_2026-11-18.md` | the approved "Laughs Charge You" build, its voice and what was learned |
| `RESEARCH_2026-11-19_miro_viral_roblox_shorts.md`, `RESEARCH_2026-11-19_voice_and_growth.md` | why our Shorts and narration underperform; the Adam voice, pace, 12 beats, originality, motion; the approved change list |
| `STYLE_EXAMPLES.md` | before writing any script (the owner's approved scripts = the style lock) |
| `~/RobloxStories/docs/VIRAL_V6.md`, `FORMATS.json` (in_this_world.script_v3 / narration_v3 / package_v6), `EXPERIMENTS.md`, `SKILL_ENHANCEMENT_PLAN_2026-11-19.md` | kit v6.0: every script, voice take, package and weekly loop; wins over older rules |
| `examples/EP2_*`, `examples/EP3_*` | scripts, cue files, shots, QA report of finished episodes |
| `kit/SKILL.md` (installed as `~/RobloxStories/SKILL.md`) | the kit's API in depth |