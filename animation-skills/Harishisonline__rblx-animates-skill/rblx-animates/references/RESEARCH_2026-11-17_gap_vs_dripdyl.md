# RBLX ANIMATES vs @DripDyl: gap report (2026-11-17)

Our Shorts compared: EP4 "My Bully Begged Me For Help" (x_Jv9GBD8Oc) and EP3 "I Told ONE Secret" (ump5uhwk8LM).
Benchmark: @DripDyl "Throw Food" (HY7SkIAdiNw) and "World's Biggest Floor Is Lava Game" (V0H8tJ17HaA).
Sources: **M** = measured (Windsor.ai, yt-dlp, ffmpeg, our words.json), **G** = Gemini Hydrogen, Task mode, same research
chat (gemini.google.com/u/1/app/c8316334d7f00e08), **C** = Claude looked at the 0-3 s frame strips.

## 1. Measured side by side

| Measure | Us | @DripDyl | Source |
|---|---|---|---|
| Subscribers | 25 (YT) | 477k | M yt-dlp |
| Uploads | 6 Shorts in total | ~33 per week (152 since 16 Oct) | M |
| Views per Short | 38-1,500 YT; IG reach 110-1,410 | 148 of 152 over 100k; Throw Food 3.06M in 2 days | M |
| Like rate | ~1.2 % (EP1 16/1,295) | ~1.0 % (30.8k/3.06M) | M: like rate is NOT our gap |
| Average watched | YT 40.6 % (EP1); IG 31.8-45.9 s of 96-109 s (33-42 %) | not public | M Windsor |
| Stayed past first seconds | YT engaged/views 54-72 %; IG 3-s skip 18-39 % (EP4 24.5 %, EP3 33.4 %) | not public | M Windsor (proxy; Studio "stayed to watch" needs a screenshot) |
| Shares | 0 on 5 of 6 reels (EP3: 20) | n/a | M |
| Runtime | 96-109 s | 135-165 s | M |
| Words per second | EP3 3.28, EP4 3.45 overall (3.6-3.75 speech only) | 3.7-4.2 | M words.json / captions |
| Silences | 17-18 meme pauses, ~8 s of the video | "almost no dead air" | M / G |
| Shot length | ~1.4 s (EP4 69 shots in 96 s; EP3 63 in 100 s) | 1.5-3 s | M / G: cutting speed is NOT our gap |
| CTA outro | 5.2 s (EP4), 5.8 s (EP3) | none | M |
| Twist word lands at | ~4 s (EP4 "knocked on my door at midnight"; EP3 "the whole school knew" just after 3 s) | ~1.5-2 s | M words.json |
| Frame 0 | EP4 blurred close-up, then a static legs/books shot; EP3 a static phone UI for 2 s | mid-action (firefighters blasting, banana thrown) | C / G |
| Title | 52-98 characters, caps, hashtags, "PART 2" | 2-6 words + 1 emoji | M |

## 2. Gemini 12-point scores (us / dripdyl, out of 10)

| Area | Us | Dyl | Biggest gap (G) | Fix |
|---|---|---|---|---|
| First 3 s + frame 0 | 5 | 9.5 | passive setup, no motion | open on the weirdest/highest-motion shot |
| Premise + structure | 5.5 | 9.5 | predictable moral arcs; side facts that don't feed the hook | one visual rule or twist; cut world facts that don't power it |
| Narrator voice | 5 | 9.5 | same flat energy for drama and calm; quotes in narrator voice | emotion tags per line, higher pitch range, 0.25 s beats; (character voices = decision) |
| Pacing / dead air | 4.5 | 9.5 | 0.4-0.8 s gaps + outro | cut silences > 0.15 s except deliberate beats |
| Animation smoothness | 5.5 | 9 | squared-off upper bodies, linear moves, props hovering | counter-rotation, anticipation, overshoot, props parented to hands |
| Faces + acting | 6.5 | 9.5 | mouths gentle/repetitive, body still | 20-30 % bigger mouths + head/shoulder pop |
| Camera | 5 | 9.5 | flat eye-level mediums | 5-8 % push-ins, 3/4 low/high angles, whip pans |
| Overlays + captions | 6.5 | 9 | 2-4-word captions clash with UI; end buttons | 1-2 words at bottom 22 %, UI in top 60 % |
| Music + SFX | 4.5 | 9.5 | one flat bed; few micro-SFX | SFX on every cut/face swap; bed changes with the story |
| Ending | 3.5 | 9.5 | CTA outro | end on the last story line |
| Title + packaging | 6 | 9.5 | long caps titles, PART 2 | 2-6 words, Title Case, 1 emoji |
| Lighting + sets | 8 | 8.5 | some indoor scenes dark on phones | +10-15 % exposure on indoor scenes (look-dev test) |

Gemini's timestamps for floating props (EP4 0:11 books, 1:05 keyboard, 1:23 paycheck; EP3 0:10 handshake, 0:15 phone,
1:23 money bag) are not yet checked against our contact sheets.

## 3. Top 5 gaps (Gemini's ranking by views lost, with our measurements)

1. **CTA outro** (5.2-5.8 s, measured). Cheapest fix: end on the last story line. *User decision: ending rule.*
2. **Flat voice + dead air** (~8 s of pauses, 3.3-3.45 words/s, measured). Fix: emotion tags, fewer meme pauses, faster take.
3. **Static frame 0 + backstory first sentence** (twist word at ~4 s in EP4, measured). Fix: open on the weirdest shot;
   sentence 1 = rule or absurd consequence.
4. **Flat music + few micro-SFX.** Fix: whoosh/pop on every cut and face swap, risers and drop-outs; music change per act
   (*music is a user decision*).
5. **Static eye-level camera + hovering props.** Fix: eased push-ins and angles; `hold()` on every held prop.

Not gaps: cutting speed (ours is already ~1.4 s per shot), like rate, lighting.
Structural gap outside the video: volume (6 Shorts total vs ~33 a week) and a 25-subscriber audience.

## 4. First-3-seconds checklist ("stayed to watch")
- Frame 0 has motion or the strangest picture of the video; never a static phone screen, text wall or standing character.
- Sentence 1 is a world rule or an absurd consequence; the twist word lands by 2.5 s.
- A sharp SFX inside 0.5 s; voice at full energy from the first frame.
- One thing to read: 1-2-word captions, no UI paragraph.
- 2-3 cuts or one big camera move before 3 s.
- The stakes are clear on mute.

## 5. Decisions waiting for the user (not changed in the skill)
Drop or shorten the like/share/follow outro; distinct side-character voices; faster narration take; music that changes
per act; Big Game runtime 130-165 s; 60 fps.
