# GEMINI AUDIO NOTES (2026-11-14) - one model's opinion, for MUSIC_RESEARCH / NARRATION_HYPE merge
Method: gemini.google.com (existing signed-in session, model "Auto") in the built-in browser. Only public URLs given; nothing private pasted, no media downloaded or uploaded. One chat, two prompts.
Prompt 1: "analyse ONLY its audio" of youtube npdxivww0Xk: narrator pace (wpm), energy curve, hype, pauses, ad-libs, spoken SFX w/ timestamps; music genre/mood/BPM/instruments/structure/level/ducking/track ID w/ confidence; SFX types/density/sync; voice processing; "say clearly if you cannot access the audio".
Prompt 2: quote the first two narrator sentences verbatim with timestamps + state whether the waveform or only transcript was processed; then same analysis marked HEARD vs INFERRED for E9TTaFj-YXU, zzu-VJTRlM8, IG Dfs43n3oWqx, IG Dfe8B5Hs3G6.

## Access result
- YouTube: Gemini claims it processed audio+video tokens. Its verbatim opening quote for npdxivww0Xk was an "In this world everyone swaps bodies with the person they'll marry..." hook (plausible for the format; NOT verified by us).
- Instagram (both reels): Gemini says it cannot open Instagram URLs. No audio findings for Dfs43n3oWqx or Dfe8B5Hs3G6.

## My confidence
- HIGH-ish: format-level claims that match what we see (no dead air, hard SFX sync to cuts, dry close-mic voice, ~6-12 SFX/min).
- LOW: numeric claims. All three videos came back ~115-125 BPM, ~215-235 wpm, music "-18 to -24 dB / ~-20 dB under voice", "~70-75 % stock cue" - suspiciously uniform/templated. Treat as hypotheses; measure with earshot if we ever get the audio legitimately.
- No track/artist IDs (Gemini only said "stock/custom cue"). Do not invent names (see LESSONS 2026-11-14).

## Per video (paraphrased)
### YT npdxivww0Xk ("You went back in time to save her...")
- Narrator: fast, ~210-235 wpm; brisk mysterious open -> steady climb ~0:35-1:10 -> peak urgency ~1:47-2:20; micro-pauses only (~0:25, ~1:28); no ad-libs/fillers; human or very good neural voice.
- Music: cinematic ambient-electronic / dramatic synth underscore; melancholic-tense; ~115-125 BPM; pads, pulsing sub-bass, ticking percussion, soft piano arps; drone open -> pulse ~0:35 -> drop-outs on tension -> swell at final countdown ~1:47; sidechain-ducked well under voice.
- SFX: impacts, whooshes on swaps, train rumble (~0:30, ~1:40), alarms (~1:10, ~2:06), magic shimmer; 6-10/min; hard-synced to cuts and caption pops.
- Voice: presence boost 2-5 kHz, low roll-off, heavy compression, dry (no reverb).
### YT E9TTaFj-YXU ("His Cat CRAWLED Closer To His Face Every NIGHT")
- Narrator ~220 wpm, even/mysterious -> tension -> dramatic climax; spoken "pspsps" SFX ~0:14 and ~1:07 (ad-lib style).
- Music dark ambient minor synth pads, sub drones, clock ticks, ~120 BPM; drops out for beats, swells at climax; ~-20 dB ducked.
- SFX purrs/meows, impacts, wood creaks, monster groan; 8-10/min.
- Voice compressed, bright, dry, human.
### YT zzu-VJTRlM8 ("The Crows GATHERED Outside His Window Every MORNING")
- Narrator ~215 wpm, eerie-conversational -> high urgency at the creature sequence.
- Music dark cinematic/orchestral tension bed, string pads, synth bass, metallic hits, ~115 BPM, progressive swell; ducked.
- SFX crow caws/flutter, pot clang (~0:27), scratching/sliding, thuds; 8-12/min.
- Voice compressed, presence EQ, dry, human.
### IG Dfs43n3oWqx / IG Dfe8B5Hs3G6
- Gemini: cannot access. Nothing recorded.

## Takeaways for the kit (cross-checked against our visual measurements)
1. Narration in YT refs runs faster (~210-230 wpm, Gemini) than our "natural pace"; the IG refs' captions suggest ~150-190 wpm [inferred]. Keep natural pace for IG, allow faster for YT-style hype.
2. Music: dark/tense synth bed with drop-outs on reveal beats and a swell into the climax; ducked hard under voice (try -18 to -22 dB below VO, sidechain).
3. SFX on every cut / caption pop / magic transition (whoosh + shimmer for "puff" transitions; 6-12 per minute).
4. Voice chain: HPF ~80-100 Hz, +2-3 dB at 3 kHz, compression 4:1, no reverb.

## Session 2 (2026-11-14, narration hype) - one model's opinion
Q1 (URLs only, refs npdxivww0Xk, E9TTaFj-YXU, zzu-VJTRlM8, lrueeOM4VKg, 7SPMY6zHgsE): per-video voice report (wpm, energy/10 s, pitch,
pauses, hype 1-10, techniques w/ timestamps, processing, HEARD vs INFERRED) + 10-point checklist vs a flat ~185 wpm narrator.
A (paraphrased): claims HEARD for all five. Hype 8.2-9.0; energy curves rise 6.5-7 -> 8.5-9 every 10 s (never drops); sentence gaps
0.1-0.3 s; whisper/hushed lines before reveals (E9TTaFj "the next night...", zzu "At midnight..."); spoken SFX "pspsps" (E9TTaFj),
"Poof!" (7SPMY6); character-voice/tone shifts on quotes; energy resets at every new night/wish/scene; processing = heavy
compression + HPF + presence/high-mid boost + limiter, dry (little/no room). Checklist: hook in 2 s, punch key nouns, micro-pauses
before twists, whisper contrast, spoken SFX, energy reset per beat, conversational ad-libs ("Yeah", "So..."), forward compressed voice.
Confidence: qualitative techniques MEDIUM (they match transcripts + earlier earshot). Its wpm (178-190 for all five) CONTRADICTS our
transcript measurement (262-293 for these same videos) -> Gemini's pace numbers are WRONG/unreliable; timestamps were empty. LOW.
Q2 (upload OUR EP1 narration + hype test B for a before/after report): NOT DONE. Gemini's file attach needs either the native file
picker or "+ > Drive", which shows a consent dialog ("Creating content from images and files", Agree/Cancel). Accepting terms needs the
user's explicit yes, so it was cancelled. Both mp3s are already in the user's Drive root (ep1_narration_original.mp3, ep1_hype_test_B.mp3).
