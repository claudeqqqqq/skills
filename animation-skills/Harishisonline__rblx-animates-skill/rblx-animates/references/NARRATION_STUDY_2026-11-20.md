# NARRATION STUDY 2026-11-20: how the viral narrators actually deliver (sentence level), vs Shadow Chores

**Owner's verdict on Shadow Chores (v2):**
- "pace / pauses" and "robotic / flat"
- "Study the way they say things: their pauses, their tone, their pace."

**Method:**
- Same 4 viral Shorts (Gneef J0OQXSo1chk 34M and RVszt4A-ucc 31M, Baseplate AYdbna6xYrU 19M, VoidCast TAYxdugYgzg 16M) vs
  Shadow Chores and Laughs Charge You v2.
- Pipeline: vocals separated (demucs), word timings (faster-whisper), pitch (Praat), per sentence and per 10 % of the video.
- Code + data: Mac `~/RobloxStories_tmp/research/prosody/` (`prosody_deep.py`, `out/*.json`, `SUMMARY.md`).
- Numbers only; listening is the owner's.

**Limit:** the energy-based pause detector reads 0 on the viral tracks, because separated vocals keep music bleed and reverb.
Pause counts therefore come from the word-gap measure (VIRAL_V6): viral 0.3-0.6 s pauses 1.9-3.1/min; Shadow Chores 5.3/min.

## What differs (measured)

| | Viral (4) | Shadow Chores | What it sounds like |
|---|---|---|---|
| Average pace | 4.07-4.41 w/s | 4.43 | same; the average is not the problem |
| Pace in the first 10 s | 4.3-4.8 | **4.9** | our hook is rushed |
| Short sentences (<= 5 words) vs long (>= 10) | 4.6-5.5 vs 4.5-5.2: **the same speed** | **6.2 vs 5.0** | we RUSH the short punchy lines ("Snap, done.", "Never hit 300.") |
| Pitch over the story (10 bins, st vs own median) | **rises at the turn/climax**: J0 -1.8 -> +2.5; RV +4 to +5 mid-story; AY +2.9 mid | **falls at the climax** (-2.8, -3.0 in the last bins) | ours loses energy exactly when theirs gets excited |
| Sentence pitch variety (sd of sentence means) | 3.1-5.9 st | 3.4 | at the low end: sentences sound alike |
| Sentence end vs start (median) | -1.1 to -3.5 st; some setup lines END UP (+2.3, +2.4, +3.0) | -3.7, with deep drops of -8 to -10 st on the first lines | "announcer" falls on every sentence |
| Stressed last word | 5-13 % of sentences | 2 % | we never punch the payoff word |
| Pauses of 0.3-0.6 s | 1.9-3.1/min | 5.3/min (11 in 125 s; 3 were planned beats) | stop-start |
| Whisper heard | clean | "pointed the dishes", "2 .99" | numbers and small words get blurred at 1.12x |

## Rules for the next voice (Yawn Curfew)
1. **Same speed for short and long lines.** Generate per sentence. Time-stretch only short sentences (<= 5 words) back to
   the speaker's long-sentence pace. Never let a punch line run faster than about 5 w/s.
2. **Hook at 4.3-4.5 w/s,** not 4.9.
3. **Energy arc.** Setup at neutral pitch. From the trigger ("Then, last Friday...") through the climax, each section gets a
   higher-energy direction (v3 tags [excited] / [urgent], or v2 style +0.15). Measure the per-10 % pitch arc: it must RISE
   by at least 2 st from the setup to the climax, like the viral four.
4. **Not every sentence falls.**
   - Setup and "and then" sentences end level or up: write them as one flowing sentence with "and" / "so", not two stops.
   - Deep falls are kept for the rule line, the twist and the last line.
5. **Punch the payoff word** at the end of the key lines ("forever", "Pip doesn't do yawns", "jail"): CAPS in the TTS
   script.
6. **Numbers written as words** in the TTS script ("forty-six times a day", "two a.m.") so they are pronounced clearly.
7. **Pauses:** at most 3 planned beats; every other gap ~0.1-0.18 s.
8. **Gate:**
   - ears_check 0 FAIL
   - prosody arc rise >= 2 st
   - short/long pace ratio <= 1.1
   - first-10-s pace <= 4.6
   - then the owner's ear on a 20-s sample. Numbers are necessary, not sufficient.
