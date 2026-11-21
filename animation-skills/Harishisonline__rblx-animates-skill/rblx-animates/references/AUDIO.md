# Audio v3: original story sound (2026-11-14). READ THIS BEFORE FINISHING ANY VIDEO

The user does NOT want the repetitive house/viral track. Every video gets its OWN score, written from its beats, over a real
room tone, with SFX that are placed, not sprayed. Target feel: REF4 (https://www.youtube.com/shorts/zzu-VJTRlM8, see
`REF4_HORROR_STORY_AUDIO.md`) over the REF1 cinematic picture; master -14 LUFS / -1.5 dBTP.

## FORMAT RULE: In this world / In this town = the AI-world bed (user, 2026-11-14)
- Bed = `assets/music/inthisworld_bed.wav` (copy of videos/ai_world/audio/music.wav, 184.5 s) at **1.0x** (Option_B pace; the
  1.5x house speed of finish.py --music is wrong for this format). Start at 0 (shift the offset only if a loud hit of the track
  clashes with a cut), 0.3 s fade-in, ~2 s fade-out ending on the final flash, music stem ~-15 LUFS -> bed ~-19 LUFS in the
  -14 master, ~3.4 LU under the voice. Keep room tone + SFX + transition hits; NO generated score/beat/drone unless asked.
- number_lies/make_audio_preview.py `--bed FILE` (default this file, `--bed generated` = old score path, `--bed-offset S`).

## v3.7 VOICE-CLARITY option (mix D) - NOT the default yet (2026-11-14)
EP1's narrator sounded "dulled": the AI-world bed sat only 3.4 LU under the voice with no duck, and its 40-150 Hz band was 6.7 LU
LOUDER than the voice (bass-heavy bed, nearly empty above 500 Hz). Tested fix = docs/research/MUSIC_RESEARCH.md sec. 5 "mix D":
voice `highpass=f=80,equalizer=f=3000:t=o:w=1:g=2.5`; bed `highpass=f=35,lowshelf=f=120:g=-6` (+ `equalizer=f=2500:t=o:w=1.5:g=-4`
only for beds WITH mids, `--clarity-scoop`); bed static ~6.6 dB under the speech level; duck ~3.7 dB (keep 3-5).
Measured on EP1 stems (not by ear): bed -22.6 LUFS static / -26.3 under speech, bed lows ~= voice lows, +2.8 dB presence.
Use: `tools/mix.py --video <slug> --voice-clarity` or `tools/finish.py <slug> --voice-clarity` or config.json `"voice_clarity": true`.
STATUS: OPTION ONLY. The user was sent A/B clips `A_base_m` (EP1 style) vs `D_fix_m`; make it the default only after the user
says D sounds better. mix_report.json logs `voice_clarity` and `bed_under_voice_db_rms` (RMS approximation: confirm LUFS with
`tools/audio_qa.py`). Episode scripts that build their own bed (videos/number_lies/make_audio_preview.py) do NOT apply it yet.

## The recipe (follow in order)
1. **Lock the voice** (never generate narration here). Mark dramatic pauses as holds, then tighten/retempo: both keep holds now.
   Hold = `{"t": 41.2, "beat": "hold", "dur": 0.6}` in `audio/cues.json` (or `"hold": 0.6` on a word in words.json).
2. **Beat map** in `audio/cues.json` (or `audio/beats.json` with `"type"`), one cue where each beat starts:
   `hook rule plant dread reveal climax cliffhanger twist cta hold` (aliases warm/escalate/turn/name/callback/silence).
   No beat cues -> score.py builds the REF4 proportions and snaps them to sentences (fine for a draft, not for a final).
   Horror rules: monster/reveal after 50 %, twist in the last 18 %, 2-3 holds per video.
3. **Mood** in `videos/<slug>/story.json` `"mood"` or `finish.py --mood`: horror | mystery | comedy | emotional | adventure.
4. **Locations** for the room tone: `{"t": 0, "amb": "room"}`, `{"t": 18.2, "amb": "school_hallway"}` (room street
   school_hallway wind night_crickets kitchen_hum). Pick the best file per location with
   `earshot rank "quiet bedroom room tone at night" sfxlib/openverse/amb_room --top 3` and pin it if needed.
5. **SFX**: one impact per act, omen/diegetic sounds real (real-sfx / Kenney / Openverse, `earshot realness`). A cue with
   `"through": true` keeps playing inside a hold (the single important sound: the tapping).
6. **Finish**: `$PY tools/finish.py <slug>` (or `--audio-only` before frames exist). It runs
   `score.py` -> audio/score.wav + score.json + score_stems/ (copied to music.wav), `ambience.py render` -> ambience.wav,
   `mix.py` (voice peak -1.5 dBFS, score as is at -24 LUFS, side-chain duck `--duck-db -5`, room tone ducked 2 dB, holds cut
   music + sfx with a 30 ms out / 250 ms in), then a two-pass linear loudnorm to -14 LUFS.
   Same take again: `--score-seed <seed from score.json>`. Different take: just re-run (new key/motif/tempo).
7. **QA (mandatory)**: `$PY tools/audio_qa.py <slug>` -> out/audio_report.md. Pass = -14 +-1 LUFS, TP <= -1 dBTP, horror
   melodic music <= 45 % of runtime (REF4 says ~35 %: the bed/drone does not count), score escalation +3..+9 LU (first 18 %
   vs 70-88 %; REF4 4-6), no digital silence, holds at voice + room tone level, earshot critique without critical rows.
   The critique profile is LAUNCH films: "sparse onsets" and "music presence < 62 %" are expected for horror; say so.
8. Report: numbers above + "I cannot hear it; listen with sound on, especially the music level under the voice".

## Tools
- `tools/score.py <slug> [--mood m] [--seed n] [--lufs -24]`; standalone: `--beats b.json --dur 85 --out x.wav --lufs -14 --stems DIR`;
  `--demo-beats 85` prints a template map. numpy only (STFT time-varying filters, FFT convolution reverb with a per-run IR,
  slow RMS bus compressor, tanh glue). Layers: drone, sub, pad (horror: only on plant/reveal/twist/cta), cluster, bowed metal
  (horror/mystery dread swells), air (+ tape-like top hiss), pulse (heart / clock tick / oom-pah bassoon+pizz / toms), motif
  (musicbox / celesta / marimba / piano / horn; horror max 4 placements, reveal = half speed, -45 cents), riser + hit into
  reveal/climax, holds. Escalation is applied after the compressor so it survives.
- `tools/ambience.py list | render <slug> | make <name> --dur 20 --out x.wav [--procedural] | fetch`.
  Library: 16 CC0 recordings (Openverse/Freesound) in `<workspace>/sfxlib/openverse/amb_*`, each credited in
  `sfxlib/openverse/ATTRIBUTION.md` (CC0: credit not required, logged anyway). Procedural fallback for every name.
- `tools/mix.py`: `--music-level asis|peak`, `--duck-db`, `--amb-db`, `--no-beat-auto`; beat gains for plain music files
  (hook -3, rule -4, plant -2, dread 0, reveal/climax +2, cliffhanger +1, twist/cta -3 dB, 0.8 s glides).
- `tools/holds.py`: hold reading + time shifting of cues.json/beats.json (used by tighten.py and retempo.py).
- `finish.py --music path` (a file, old behaviour) and `--music-source house` still work but are not the default.

## Measured (earshot, 85 s demo beat map, 2026-11-14)
See the CHANGELOG entry for the scorecards. Short version: horror score matches "a horror film score" (plausible, z ~+2.6)
and reads code-synthesized (p_real ~0.2-0.3; expected for a synth score). Under a fast kid narrator the bed is mostly masked
(earshot hears music in ~50 % of 5 s windows): raise `--lufs -22` or `--duck-db -4` for REF1-style continuous music.

---

# Audio: earshot + real-sfx (installed 2026-11-13, use in every video)

Two skills handle what an agent cannot hear. Both live in `~/.claude/skills/` (`earshot`, `real-sfx`); earshot's engine is in
`~/earshot` (Python 3.11 venv, local CPU, models ~1.1 GB cached after `earshot doctor --fetch`).

## 1. earshot: measure and judge sound (always)
Never say how audio sounds without a reading behind it. After `finish.py`:
```
$PY tools/audio_qa.py <slug>            # loudness, true peak, listening transcript, sync to picture/cues, scorecard
$PY tools/audio_qa.py <slug> --quick    # loudness only, no models (seconds)
```
Read `videos/<slug>/out/audio_report.md`. Targets: about -14 LUFS integrated, true peak <= -1 dBTP, no SFX more than 40 ms
off its cue frame, the voice clearly above the music, no dead silence between sentences. Fix with `finish.py --music-db/--sfx-db`,
`sfx/pack.json` (`lead`/`gain`), or by moving cues, then re-run.
Also useful while building: `earshot rank "<description>" folder/ --top 5` (pick the best candidate sound),
`earshot find FILE "<description>"` (best trim of a long recording), `earshot realness FILE` (recorded vs synthesized),
`earshot ab A B` (compare two mixes). Prefer one Python script / MCP over many CLI calls (each CLI call reloads models, 20-40 s).

## 2. real-sfx: replace synthesized SFX with real recordings (when a real library exists)
real-sfx never synthesizes: it places REAL recorded sounds from the user's libraries (and the CC0 uisfx pack for UI cues) on
the exact frames of a finished video and returns a new MP4 + a separate SFX WAV. Status (2026-11-13): a starter library is registered: Kenney audio packs (CC0, ~470 sounds, ~9 MB) in `~/RobloxStories/sfxlib/kenney`
(`tools/sfx_library.py kenney` fetches them). Main tier = real recordings: impact-sounds (130), rpg-audio (52: foley, footsteps, doors,
cloth). Extra tier = synthesized UI/sci-fi/digital packs. Check: `python ~/.claude/skills/real-sfx/scripts/setup.py check`.
Gaps: almost no whooshes, risers, crowds or room ambiences (indexed roles: hit 117, foley 54, ambience 29, click 13, paper 8, glass 6,
glitch 4...). For those add a bigger real library, e.g. a Sonniss GDC bundle (royalty-free, 7-50 GB per year, read its licence first)
or Freesound CC0 packs (needs the user's API key), then `setup.py add-library NAME PATH --tier main --index`.
The kit's own `sfx/` pack is synthesized/generated, so real-sfx is the upgrade path:
1. Get a real library (user's own, or free CC0/licensed: Freesound CC0 filter, Sonniss GDC bundles, Mixkit, Pixabay; read each licence).
2. `python ~/.claude/skills/real-sfx/scripts/setup.py add-library NAME PATH --tier main --index`
3. Export our cue list as the project event list: `videos/<slug>/audio/cues.json` (kit format) -> `from_cues.py`, then `mix.py`.
   Do not double: render the film without the kit SFX (finish with `--sfx-db -60` or an SFX-less mix) and let real-sfx add the sounds,
   or use real-sfx only for the sounds it improves (whooshes, hits, risers, UI).
4. Verify with earshot (`audio_qa.py`) and report what was checked by measurement and what the user must listen to.
Ask the user before installing anything or calling a paid tool (real-sfx's own rule).

## Report wording
"Audio checked by measurement with earshot (LUFS x, true peak y, sync z ms; critique verdict ...). I cannot hear it:
please listen with sound on, especially the voice level against the music and the loudest hits."

## Fix round 2026-11-14 (test_seq integration findings)
- **SFX level**: `SFX_DB` -12 -> **-6** (finish `--sfx-db -6`); every pack sound is peak-normalised first; cue `vol` is
  softened with `vol**0.5` (0.3 -> 0.55) so quiet cues still clear the bed; whoosh/riser/flash/boom/thud get +4 dB (low crest).
- **Peak alignment**: whoosh/swish/whip/rise/flash/boom/thud cues are placed so the sound's PEAK lands on the cue time
  (pack.json `"align": "peak"|"start"` overrides). `fx.whip_out` now cues the whoosh ON the cut. Fixed '7.22 whoosh no hit'.
- **Side-chain**: music dips -7 dB and room tone -3 dB under every SFX hit (5 ms in, ~180 ms out): `SC_MUSIC_DB`, `SC_AMB_DB`.
- **Room tone never drops out**: 15 ms anti-click in, tail only to -12 dB. audio_qa ignores the first 0.45 s of
  ebur128 momentary (its 400 ms window is empty = false "2.4 % near-silence").
- **Score (mystery/horror)**: RESTS - pad + pulse + motif drop out 1.3-2 s every 4-6.5 s (horror 1.5-2.5 s every 3-5 s),
  drone/air/cluster dip -9 dB there, plus a 0.9 s breath before each reveal/climax hit. Timbre: `glass` motif (soft
  attack, inharmonic 2.76x partial), bowed-glass sine pad (no saw buzz), drone with 3 harmonics, no pizz on the tick
  (earshot had tagged the old score "house music?, electric guitar"). Score level -24 -> **-20 LUFS** (config `score_lufs`).
- **Bug fixed**: ambience cues `{"t","amb"}` inside beats.json were parsed as "dread" beats (every section was dread).
- `audio_qa.py --film=out/x.mp4` checks another render.
- Still open: cue hits that fall under running narration cannot reach +12 dB over the bed; earshot critique says
  "music heard in 0 % of 5 s windows" for the quiet glass/drone score (texture does not read as "music" to AST).

## Whip / whoosh onset and the mystery palette (2026-11-14, D7)
- Peak-aligned sounds (whoosh, swish, whip, rise, flash, boom, thud): mix.py keeps the PEAK on the cue (= the cut) but
  trims the pre-roll to `PRE_MAX` 0.17 s (pack.json `"pre"` overrides) and reshapes it into a ramp that starts 9 dB
  under the peak with a 4 ms attack: an audible onset where the whip motion starts. earshot on test_seq: the 0:07.30
  whip cut went from "no onset, level peak +130 ms" to an onset at -11 ms.
- score.py mystery: root MIDI 33-40, 58-70 bpm, BOWED motif (220 ms swell, no strike) instead of glass/celesta, motif
  only on plant/reveal/cliffhanger/twist, max 3, one rep per section; bowed-metal layer under every section; muffled
  400-900 Hz "lowclock" pulse + low thump instead of 1.8/2.4 kHz ticks (earshot tagged those "chat message pop").
  test_seq: melodic share 85 % -> 47 %, "celesta" gone from the section tag, AST music 0.34 -> 0.51. Voice-agnostic.
- (round 2) mystery motif now ALSO on the hook (max 4) and no rest before 3.5 s: a drone-only hook is not heard as
  music under the VO (earshot "music presence" critical, 5 s windows). Re-check `music presence` in audio_qa for every
  video; horror still fails it (known). Sync the kit with `setup.py ~/RobloxStories --update --no-pip --no-music --no-test`.

## Round 3 (2026-11-14): transitions, stereo, dynamics, ducking, captions
- **Transition sound design (mix.py `TRANS`)**: a cue tagged `{"cut": true, "kind": "whip|flash|push", "pan": [p0, p1]}`
  (set by `fx.whip_out`, `fx.flash`, `fx.push_through(mode="in")`, `cams.whip_pan`, `cams.crash_zoom`, the window
  fly-through) is built from REAL CC0 recordings in `sfxlib/openverse`: an air layer (recorded whoosh/swoosh, its natural
  swell peaking ON the cut, no hard 4 ms onset: that read as a "chat message pop"), a low hit (pack thud / recorded
  impact) whose ATTACK is on the cut, a riser tail for a flash, and a 50 ms suck-in (-14 dB) just before the cut. The
  air layer auto-pans p0 -> p1 with the camera move (yaw +deg = turn left = right->left). The pack "sparkle" (glock
  chime) is no longer used for flashes. Without sfxlib the pack whoosh + thud are used (warning printed).
  Old cue files still work: a plain "whoosh" cue is treated as a whip cut.
- **Music dips** (`DIP_*`): the music falls -12 dB over 0.15 s from 0.45 s before every transition cut and comes back ON
  the cut (plain music files also before reveal/climax; the generated score rests there by itself).
- **Ducking**: `speaking()` gates 25 dB under the voice's p90 level, bridges < 120 ms gaps, 40 ms look-ahead, ~60 ms
  release: the bed now opens in the 150-300 ms phrase gaps (old gate never re-opened: voice "active" 100 %).
  `audio/mix_report.json` logs the applied duck (`duck_db_applied`, target -3..-6) and the measured music level.
- **Stereo**: SFX bus is stereo (cue `"pan"` -1..1 for point sounds); beds are widened (`BED_SIDE_DB`, decorrelated
  high-passed Haas side when a source is near mono, mono-compatible), plus a -15 dB decorrelated early-reflection side
  on the voice. test_seq: side -21.8 -> -10.9 dB under mid (target -14..-8, REF1 -14.5..-5).
- **Macro dynamics** (`BEAT_RIDE_DB`, `--no-ride` to skip): the whole mix rides the beat map like a fader (hook +1, plant
  -3..-4.5, dread -6.5 rising to -3, reveal -1..-2, climax +1). test_seq LRA 1.5 -> 4.4 LU with the ending under the body.
- **Score (mystery)**: dark low STRING pad (filtered detuned saws), cello PIZZ ostinato (3+2+1+2 eighths) instead of the
  clock tick, bowed motif in the cello/viola range, modal chord paths (i-iv-i-VI, i-bII-i-iv, i-VI-iv-i) instead of the
  i-VI-III-v "corporate" loop. earshot match "inspirational corporate background music" z 1.4 -> 0.4-0.65 on 3 seeds.
  Music presence fixes: no rest before 5 s (`FIRST_REST_S`) or in the last 3 s, a 0.5 s pre-hit rest (was 0.9), the
  hook exempt from most of the escalation dip (`HOOK_ESC_DB`), a 0.35 s end fade (was 1.5 s: it emptied the last 5 s
  window), score level -20 -> **-19 LUFS** (finish default; config `score_lufs`). AST music presence on a 12 s excerpt
  with wall-to-wall narration stays borderline (0.2-0.45 per window, threshold 0.3): always read audio_qa's critique.
- **Bug fixed**: mix.py picked `audio/music.json` (score sidecar) as the music file when it sorted before music.wav.
- **audio_qa.py** now prints "Mix checks": stereo side/mid, LRA, the duck, the dips and, per transition, the attack
  within one frame of the cut (>= 6 dB / 20 ms). A word onset right on a cut masks the hit (test_seq flash: the voice
  starts "Every" 60 ms before the cut): move the cut or the line, not the sound.
- **Captions** (captions2.py): groups switch on the frame NEAREST the word (was up to 1 frame late), group starts are
  snapped to speech onsets heard in voice.wav when words.json is off (test_seq "Every" was 100 ms late), the last
  caption holds to the end of the sound, and `out/caption_report.json` is written on every finish (group onset, words
  on screen while spoken, words.json vs voice; target <= 1 frame).
- **finish.py tail guard**: frames shorter than the mix are held on the last frame (never a player's black), trailing
  black frames beyond 6 are cut together with the mix; `out/tail_report.json`.
- **pacing.py**: wpm is measured over the spoken span; with a PLACEHOLDER voice in audio/ the wpm row is "info" (the
  `say` take reads 203 wpm; re-check with the real voice).

## Round 4 (R3-1..R3-4)
- score.py: rests now gate the motif too; a rest budget (MELODIC_MAX - 6 %) is guaranteed with breaths before section
  boundaries/cuts, then mid-run rests. A reveal/climax hit in the last 2.5 s is -4 dB with a 0.4 s sub tail.
- mix.py `end_guard`: the last max(1.25 s, 10 %) may sit at most +1 dB (RMS) over the body median; smooth ride down otherwise.
- finish.py: a `.keep_frames` file in the video folder disables auto_clean_frames (test_seq has one).

## Round 5 rules (bed continuity, sub, whip)
- Mystery has no pulse layer (pizz plucks read as celesta/'chat message pop'): dark string pad + drone + bowed motif.
- Melodic rests never empty the bed: per mood `rest_bed_db` (default -9, mystery 0) + `rest_swell_db` (mystery +3). A rest
  under a voice phrase gap must stay within ~8 dB of the talking level (earshot reports a 'drop' otherwise).
- The sub stem always sits in 36-56 Hz at -11 dB and swells `reveal_sub_db` under reveal/climax/dread/twist sections.
  Full-mix sub band target: REF1 -16.2..-4.1 dB share (test_seq: -9.4).
- Whip transitions are pure air: two high-passed (350 Hz) recorded whooshes, no thud, +4 dB, voice tucked -6 dB around the
  cut. Write scripts so a whip lands in a voice pause when possible: a whoosh under a running word is masked.
