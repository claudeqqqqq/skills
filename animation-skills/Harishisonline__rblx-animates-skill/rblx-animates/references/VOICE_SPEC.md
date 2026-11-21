# VOICE SPEC

> **v6.1 (owner 2026-11-20) - THE house narration "v3" for every video, no more samples:**
> `tools/ep_audio/narrate_house.py` reproduces the two takes the owner approved by ear
> (yawn_curfew/voice_test/YawnCurfew_hook_v3_withbed.mp3 and YawnCurfew_FULL_v3_withbed.mp3).
> - **Model:** eleven_v3 Creative (stability 0.0), style 0.35, one request per tts_script paragraph, performed as written:
>   "[emotion] [speaking quickly] text". Paragraphs with sound words, [yawns], [laughs] or [whispers] get no
>   [speaking quickly].
> - **Editing, per sentence:** trim; cap inner silences at 0.12 s; stretch to a 4.75 w/s speech pace (short lines =
>   long lines; sound-word sentences keep their length); 0.06 s joins; no extra beats.
> - **Voices:** In-this-town = Adam with the D alien FX on the whole take. Blox City = Alex, same method, no FX.
> - **Gate:** tools/ears_check.py.
> - **Do not use** narrate_v4.py: it auto-added [speaking quickly] to the yawn lines, and the owner heard the difference.

> **v6.0 (owner 2026-11-19) - current for every format:** narrator = ElevenLabs premade "Adam - Dominant, Firm"
> `pNInz6obpgDQGcFmaJgB` + the "D" alien FX (`asetrate=44100*1.1892,aresample=44100,atempo=0.8409,vibrato=f=5.5:d=0.08`),
> generated per story section by `tools/ep_audio/narrate_v3.py` (route v2 / v3 / sts, the owner picks by ear), edited by
> `post.py` mode "flow", and gated by `tools/ears_check.py` (viral numbers: 4.05-4.65 w/s, ~0.18 s after a full stop,
> <= 3.5 pauses of 0.3-0.6 s a minute, pitch range >= 12 st). Character voices speak quoted lines (`{name}` lines, ids
> from the ElevenLabs list with the owner's OK). Rules and evidence: `docs/VIRAL_V6.md` section 2. Everything below is
> the history (Alex, eleven_v3) and stays valid only for re-renders of old episodes. Never change the narrator without
> playing a clip and getting a yes.

# Narration voice spec (user-supplied 2026-11-14)

> **CURRENT for In this town / In this world (user decision 2026-11-14): calm deadpan first-person AI storyteller, NO hype.**
> config voice_preset **"intown_v1"** (kit.py VOICE_PRESETS). The v3.7 HYPE rules and HYPE recipe below are SUPERSEDED for this
> format (kept selectable as voice_preset "hype_v3"; "legacy_liam" also kept).
## INTOWN recipe (intown_v1; measured 2026-11-14, videos/number_lies/voice_tests/intown/NOTES.md)
Reels (research/intown_refs/MEASUREMENTS.md): 229 / 285 wpm, F0 median 181 / 203 Hz, F0 range 17.0 / 10.6 st, sd 5.2 / 3.5,
RMS sd 7.0 / 7.4 dB, word gaps 0.1-0.4 s (none > 0.6), first word 0.10 / 0.16 s, mix -14.4 / -14.1 LUFS, LRA 1.9 / 0.8 LU.
1. Script: passes tools/intown_lint.py (hype_lint.py delegates to it for this format): 0 '!', 0 spoken SFX, 0 [tags], no CTA,
   premise + exact rule in sentence 1, median sentence 7-13 words, 470-530 words, >= 3 time markers, short twist/callback ending.
2. TTS: Alex yl2ZDV1MzN4HbQJbMihG, **eleven_multilingual_v2, stability 0.55, similarity 0.75, style 0.0, speed 1.15**, speaker
   boost, plain punctuation, no tags; takes of consecutive lines <= 900 chars (tts_take_split "paragraph"). Use the
   /with-timestamps endpoint when possible so gaps can be cut on the alignment.
3. Post: cut every word gap > 0.34 s to 0.30 s (alignment; v2 leaves ~1 s sentence pauses), atempo = 257 / raw_wpm
   (test: 1.235), highpass 70, acompressor threshold -12 dB ratio 1.5 attack 20 release 250, alimiter 0.89, 120 ms lead-in,
   **two-pass** loudnorm I=-14 TP=-1.5. NO presence EQ boost, no softclip, no heavy compression (2:1 @ -20 dB cut RMS sd to 4 dB).
   Reference implementation: videos/number_lies/voice_tests/intown/gen.py (post) + measure.py.
4. Check: intown_lint.py <slug> with words.json (225-290 wpm, first word <= 0.3 s, no gap > 0.6 s) and voice_metrics.py:
   f0 range 10-17 st, f0 sd 3.5-5.2, RMS sd >= 6 dB.
Test result (166-word original paragraph): C = this recipe, closeness 0.84 mean |z| vs the reels; v3 stability 0.5: 1.51;
v3 stability 1.0: 1.42; stock Will v3: 1.77. C: 257 wpm, 157 Hz, 12.9 st, sd 3.83, RMS sd 6.4 dB, gaps 0.22/0.29 s, LRA 1.5.
Known gap: Alex sits ~157 Hz vs reels 181-203 Hz (all models). UNVERIFIED: nobody has listened; atempo 1.24 artefacts on v2
not judged; post is not yet wired into eleven.py/voice_run.py (run the gen.py post steps by hand).

> (history) v3.7 HYPE rules - SUPERSEDED for In this town/world:

> **v3.7 CURRENT RULES (read first; older sections below are history):** narrator Alex yl2ZDV1MzN4HbQJbMihG on eleven_v3,
> per-beat takes (2-4 sentences, 60-250 chars, each opening with its tag), stability 0.0-0.3, similarity 0.75, **style
> 0.35-0.45** (was 0.25), speaker boost on. **Delivered pace 255-290 wpm** for In this world/town, horror, comedy
> (measured refs 262-293; `pacing.py --format`), spoken SFX per format (docs/research/NARRATION_HYPE.md, FORMATS.json).
> Script must pass `tools/hype_lint.py` (no FAIL) before any credit is spent. The "Adam" lines directly below are SUPERSEDED.
## HYPE recipe (SUPERSEDED for in_this_world by INTOWN recipe above; was default, measured 2026-11-14; config voice_preset "hype_v3", kit.py VOICE_PRESETS)
Why EP1 was flat (measured on audio/narration.mp3 + words.json): 184.7 wpm (refs 262-293), f0 range 13.9 st and f0 sd 4.4 st
(mosquito_town, which the user liked: 21.5 / 7.0), loudness per 10 s within 1.4 dB for 108 s (no energy curve), ONE 108 s take
(v3 decays to neutral), script with 0 "!" / 1 spoken SFX / 0 tags, style 0.25, and NO atempo in post ("decoded only").
Measured fact: v3 Alex reads ~180-191 wpm raw whatever the tags/stability; tags raise pitch and variation, not pace.
Recipe (test take B, voice_tests/B_beats_st0_sty45_post.mp3: 264 wpm, f0 med 188 Hz, range 20.0 st, sd 6.1 st):
1. Script: passes tools/hype_lint.py (no FAIL) incl. the "beat lines" row: one beat per line, 30-250 chars, most lines open with a
   tag ([excited] hook, [fast-paced] rule/list, [urgent] stakes, [gasps] reveal, [whispers] ONE line), "!" >= 1/10 s, spoken SFX as
   own word/sentence ("Click!", "SLAM"), CAPS on 1 word, ends on a one-word comment question.
2. TTS: Alex yl2ZDV1MzN4HbQJbMihG, eleven_v3, stability 0.0, similarity 0.75, style 0.45, speaker boost, NO speed param;
   ONE CALL PER LINE (eleven.py tts does this when tts_take_split = "line"); concat.
   (Single long take A: range 16.7 st; per-line st 0.3 take C: 179 wpm and f0 146 Hz = calmer. Both lost.)
3. Post: silenceremove=stop_periods=-1:stop_duration=0.22:stop_threshold=-38dB:stop_silence=0.12,
   atempo=270/raw_wpm (~1.35-1.42; measure raw wpm from with-timestamps alignment or words.json), highpass 80,
   equalizer 4 kHz +3 dB q1, acompressor thr -20 dB ratio 3 attack 5 release 80, asoftclip tanh, loudnorm I=-14 TP=-1.5.
   Then tools/voice.py as usual; pacing.py must read 255-290 wpm.
4. Check: engine/tools/voice_metrics.py <take> --words <words.json>: wpm 255-290, f0 range >= 18 st, f0 sd >= 6 st.
Old settings stay selectable: voice_preset "legacy_liam" (Liam, multilingual_v2, speed 1.12) or "" (loose tts_* keys).
UNVERIFIED: no human listen yet; atempo 1.41 artefacts on v3 not judged; Gemini before/after not obtained (consent dialog).

Target: the viral "Adam" narrator heard in ref 5 (E9TTaFj-YXU).
- Voice: premade Adam, id pNInz6obpgDQGcFmaJgB (also library "Adam - Dominant, Firm" eGSd0uV8dNQnZuEEX9lu).
- Model: eleven_multilingual_v2 (drama) or eleven_turbo_v2_5 (fast shorts cadence).
- Settings: stability 35-45%, similarity 75-80%, style 15-25%, speaker boost ON.
  NOTE: the MCP creative_generate_speech tool exposes no sliders; use the full ElevenLabs API/connector to apply them.
- Post: speed 1.10-1.15x (or trim micro-pauses), HPF 80 Hz, +3-5 kHz presence, light compression.
- SFX: pspsps / gasp / breath one-shots (ElevenLabs sound effects) layered by hand.
- Ref 5 audio (user supplied mp3): 100.9 s, 48 kHz stereo, ~-22.7 LUFS gating threshold, LRA 7.5, true peak +0.2 dBFS (hot, clipped master).
- Still: user may replace with their own voice; ask before spending credits on full narration.

## Ref 5 audio, measured with earshot (2026-11-14)
It is a FULL MIX, not a bare voice: continuous hip-hop / glitch-hop / future-bass bed with heavy sub bass and vocal chops
(9 sections, ~6.8 onsets/s, no steady grid), integrated -12.6 LUFS (loud, LRA 7.5), true peak +0.2 dBTP, brightness 2.6 kHz,
bands (dB): sub -20, low -8.5, lowmid -2.4, mid -6.9, presence -14.6, air -15.5.
Accents: impact hit at 0:33 (+40 dB over bed), 0.3 s stop-down gap at 0:41.6, sub drops at 0:38.8 and 1:23.5,
chat-message-pop UI dings at 0:52, 1:09, 1:27, 1:31, fast whoosh 0:12.7.
earshot cannot transcribe or judge a voice; the narrator itself is unverified by me.

## Ref 4 narrator match attempt (2026-11-14)
Ref 4 (zzu-VJTRlM8) = same viral beat bed + narrator. Voice isolated via ElevenLabs /v1/audio-isolation (stem still has beat bleed).
Crude proxies (pyin F0 median Hz / spectral centroid Hz / onsets per s): ref 188/1944/6.0.
Candidates (free preview clips): Alex "Young American Male" yl2ZDV1MzN4HbQJbMihG 203/1856/6.4 (closest);
Liam premade TX3LPaxmHKxFdv7VOQHJ 142/1693/5.8; Adam 112/2301/4.9 (far too low => why the first sample was wrong).
Credit state: 8395/10000 chars used at 2026-11-14; keep tests under ~100 chars. API key in ~/RobloxStories/.env (never print).

## DECISION (user, 2026-11-14): narrator voice
- NOW: Alex - Young American Male, id yl2ZDV1MzN4HbQJbMihG (in the user's account).
- LATER/backup: Adrian - Cinematic Deep Male, shared-library id BT6eaRWNcJkXzGwuFtu0 (add to account before use). Closest library sound-alike by measurement (173 Hz, 6.3 onsets/s, centroid 1903).
- Do NOT clone the ref narrator (public-link voice). Do not use Adam, designed voices, or Liam unless the user asks.
- Recipe (Alex, one take, ~270 chars for 15 s): model eleven_v3, stability 0.0, similarity 0.75, style 0.25, speaker boost on;
  tags [fast, urgent, breathless] hook/closer, [whispers] for eerie lines.
  Post: ffmpeg silenceremove=stop_periods=-1:stop_duration=0.22:stop_threshold=-38dB:stop_silence=0.14, atempo=1.08, highpass 80,
  +3 dB @4 kHz, acompressor thr -20 dB ratio 3, loudnorm I=-14 TP=-1.5. Pauses stay <= 0.14-0.4 s.
- API key lives in ~/RobloxStories/.env (Creator plan as of 2026-11-14). Library voices need a paid key; check /v1/user/subscription first.
- Credit rule: ~100-300 chars per test, user approves before full narration.

## FINAL VOICE DECISION (user, 2026-11-14, after hearing the tests)
The user rejected the hype tests (hype_v3), the In-this-town calm tests (intown_v1) and the stock-voice tests, and chose: **Alex "upbeat" exactly as in the EP1 narration / D_fix_m mix.**
Default preset = `alex_ep1`: eleven_v3, stability 0.0, similarity 0.75, style 0.25, speaker boost, light tags ([fast, urgent, breathless], [whispers]) as in the DECISION recipe above; post chain as in the DECISION recipe (silenceremove 0.22->0.14, atempo 1.08, HPF 80, +3 dB @ 4 kHz, compressor, loudnorm -14 LUFS / TP -1.5). Do not change the voice again unless the user asks.
The In-this-town research (INTOWN_FORMAT.md) still governs the SCRIPT STRUCTURE (premise sentence first, rule mechanics, close person, time-marked escalation, twist ending, dense short sentences); the voice stays Alex-upbeat.
