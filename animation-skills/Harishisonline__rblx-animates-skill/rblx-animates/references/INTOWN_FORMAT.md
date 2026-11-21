# In-this-town format spec (measured, 2026-11-14)

Source: the user's two reference reels only (R1 @kyreblx "missing minute" 132 s; R2 "I can't wait" 105 s).
Raw numbers + word-timestamp transcripts: `research/intown_refs/` (MEASUREMENTS.md, *_transcript.txt, *_stt.json).
Media was downloaded anonymously for analysis and deleted. Blox City / Blox Town branding is NOT used here
(Blox City = later storyline videos only).

## 1. What the format actually is (honest reading)
- A calm, fast, first-person **storyteller** monologue read by an AI TTS voice. It is NOT hype: 0 exclamation marks,
  0 spoken SFX, 0 ad-libs, 0 laughs/gasps, no whisper beats, no question CTA, no "like and follow".
- Speed comes from a dense script and almost no pauses (gaps 0.1-0.4 s, none > 0.6 s), not from excitement.
- Loudness is flat (mix LRA 0.8-1.9 LU, -14 LUFS). Pitch movement is moderate (10.6-17 st p5-p95).
- Emotional payoff, not a punchline: R1 ends on a family reveal, R2 on a sibling callback. Both are wholesome-twist stories
  wearing a mystery premise.

## 2. Script template (beat by beat; targets for a 100-130 s video, ~480-500 words)

> Superseded for this channel: with the Alex voice (~197 wpm) a 90-120 s video is 300-370 spoken words, and every video ends with references/ENDING_RULE.md (like/share/follow + a one-word two-option comment question).

| beat | time | words | what it does (pattern from refs) |
|---|---|---|---|
| 1 PREMISE | 0-4 s | 10-15 | "In this town, [ordinary thing] [one exact rule]." Precise numbers/times in the rule (a time, a phrase). First word at <=0.2 s. |
| 2 RULE MECHANICS | 4-15 s | 30-60 | 2-4 short sentences explaining how the rule works and its catch ("Nobody knows why." / "But if X, you never Y."). |
| 3 TOWN TEXTURE | 15-30 s | 30-70 | Either the locals' one strange rule, or 2-3 quick funny/odd examples of the rule hitting other people (relatives, coach, cousin), each 1-2 sentences, deadpan kicker of 2-5 words. |
| 4 PERSONAL STAKE | by 10-30 s | 15-30 | "I" + someone close (sister, twin) enters; the rule touches the narrator's life. |
| 5 INCITING EVENT | ~30-50 s | 40-80 | One night / one day something breaks the pattern. Concrete images, one action per sentence. |
| 6 ESCALATION LADDER | 50-95 s | 150-220 | 3-5 repeated attempts or repeated sightings, each a step closer ("The following night...", "Dad... Nothing. Mom... Nothing."). Number countdowns/counts are SPOKEN plainly in sequence (R2: 0, 3, 12, 40... 90, 97, 98, 99). |
| 7 TURN / DISCOVERY | 95-115 s | 50-90 | The object/clue that recontextualises everything (photograph, the tree, the clock). Quoted lines from other characters, short. |
| 8 REVEAL + CALLBACK | last 10-15 s | 30-50 | The twist in a 4-6 word sentence ("She was my little sister."), or a callback to the opening image ("It's always a tie."). End immediately, no CTA. |

Sentence length: median 9-10 words, mean 10-11, range 1-32; ~15 % are 1-5 word kickers ("Nothing.", "I got up.").
Sentences per video: 46-50. One idea per sentence. Past tense narration after the present-tense premise.
Dialogue: 4-7 short quoted lines total, read in the same narrator voice (no character voices).

## 3. Phrase / pattern bank (paraphrased patterns; short fragments only as evidence)
- Opening: "In this town, [every X] [does Y] [exact detail]." / "In this town, if you say '[phrase]', [consequence]."
- Rule clarifiers: "Nobody knows why." / "You see, the second you..." / "For you, it feels like..." / "But if it never..., you never..."
- Town-wide norm: "The locals have learned to live with it, but everyone follows one rule: never ..." / "So here we say ... instead."
- Example-with-kicker triplet: [person] did it -> [result] -> 2-5 word deadpan kicker ("We're still losing.").
- Doubt-then-proof: "I thought it was ridiculous until one night..."
- Time markers that drive escalation: "The following night", "One night", "In March", "After a month", "By August", "On our birthday".
- Repetition beats: "[attempt]. Nothing. [attempt]. Nothing."
- Countdown/count lines spoken as bare numbers, comma separated, accelerating.
- Rule restated at the turn with new meaning (R2 repeats "It counts what you meant").
- Ending: short declarative twist, or mirror of an early line. No question, no "comment below".
  Superseded for this channel: with the Alex voice (~197 wpm) a 90-120 s video is 300-370 spoken words, and every video ends with references/ENDING_RULE.md (like/share/follow + a one-word two-option comment question).

## 4. Voice delivery spec (numbers)
- Voice: AI TTS, light / young-sounding register, F0 median 180-205 Hz (p10 128-165, p90 260-270), neutral US accent.
  AudioSet "speech synthesizer" 0.82-0.86 on both - viewers accept an obviously AI voice.
- Pace: 225-290 wpm over the spoken span (R1 229, R2 285); articulation rate 250-290 wpm.
- Pauses: between sentences 0.10-0.40 s (target median 0.25 s); within sentence none audible; never > 0.6 s.
- Pitch: range 10-17 st p5-p95, sd 3.5-5.2 st. Energy: RMS sd ~7 dB, mix LRA <= 2 LU (heavily compressed/limited).
- Tone: calm, sincere, slightly wistful; questions inside quotes get a natural rise; no shouting, no stylised whisper.
- TTS direction: steady storyteller settings (no [excited]/[fast-paced] tags); reach pace with a tight script and pause
  trimming (silenceremove to <= 0.3 s) plus mild atempo only if raw pace < 225 wpm. Master to -14 LUFS.

### 4b. Voice preset intown_v1 (measured 2026-11-14, default in config/kit.py)
Alex on eleven_multilingual_v2, stability 0.55, similarity 0.75, style 0.0, speed 1.15, no tags, paragraph takes; post =
gap cap 0.30 s on the alignment, atempo to 257 wpm, HPF 70, 1.5:1 comp, limiter, 120 ms lead-in, loudnorm -14.
Closest of 4 test takes (mean |z| 0.84; v3 takes 1.42-1.51, stock Will 1.77): 257 wpm, F0 157 Hz (reels 181-203: Alex is
lower, open item), range 12.9 st, sd 3.83, RMS sd 6.4 dB, gaps 0.22-0.29 s. Details: docs/VOICE_SPEC.md INTOWN recipe,
videos/number_lies/voice_tests/intown/NOTES.md. Not listened to yet.

## 5. Music / SFX / captions tied to narration
- R1: continuous soft piano/strings bed ("warm / inspirational"), loud: in voice-quiet frames only ~2 dB under voice; no ducking swings.
- R2: almost no bed (-19 dB under voice in gaps); light foley/tick accents only.
- => one constant bed for the whole video, no drops/risers on every line; real SFX sparingly on physical events. Never spoken SFX.
- Captions: follow narration word timing; no extra hype captions needed (not measured visually here).

## 6. Lint spec - IMPLEMENTED as tools/intown_lint.py (hype_lint.py delegates for this format); both reels PASS, number_lies FAILS 8 rows
FAIL: any spoken SFX word; any "!" in narration; a question CTA in the last 2 sentences; a gap > 0.6 s; wpm < 205 or > 310;
first word after 0.5 s; "Blox City"/"Blox Town" in the script.
FIX: wpm outside 225-290; words in first 15 s outside 50-75; median sentence length outside 7-13; no "In this town/world" premise in
sentence 1; fewer than 3 escalation steps; final sentence > 8 words.
PASS otherwise. (FORMATS.json in_this_world.narration holds the numeric bands; hype_lint sfx/exclam minimums are now 0.)

## 7. How our earlier work differs (measured)
| | refs | EP1 narration | hype tests (B post) |
|---|---|---|---|
| wpm | 229-285 | 185 (too slow) | 264 (ok) |
| tone | calm storyteller | flat, low (F0 134 Hz, deep) | hyped, 20-21.6 st swings (too animated) |
| spoken SFX / "!" | 0 / 0 | - | lint demanded 0.6/10 s and 1/10 s (wrong) |
| CTA | none | - | "X or Y?" question (wrong) |
| voice register | 181-203 Hz light | 134 Hz | 171-188 Hz |
Wrong assumptions: "hype", spoken SFX, exclamations, whisper beat, question CTA, f0 range >= 18 st, 262-293 wpm as THE band
(it fits R2 only; R1 is 229). Right: high pace vs EP1, tight pauses, constant music bed, first-person.

## 8. Gemini cross-check
Not obtained this round: the built-in browser cannot hand a local file to Gemini's upload control (native file picker; no
file-injection tool), and the consent dialog was never reached. Measurements above are ours only.
