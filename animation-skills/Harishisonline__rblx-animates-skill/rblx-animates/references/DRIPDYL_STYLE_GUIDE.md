# DRIPDYL_STYLE_GUIDE.md: camera, motion and narration rules for the RBLX ANIMATES kit (v1, 2026-11-17)

Source: Gemini (Hydrogen, Task mode) read the public repo (SKILL.md, cams.py, shotlib.py, motion.py, core.py, tts.py,
post.py, gap report) and wrote this guide. Claude then checked every code claim against the kit on the Mac.
Tags: **[verified]** = matches the code; **[corrected]** = Gemini was wrong, the fix is ours; **[Gemini]** = a target or
opinion not yet proven on our channel (test it); **[decision]** = changes a choice the owner made, needs their yes.
Read this before writing any `shots.py`, `tts_script.txt` or audio config for a new video.

---

## 0. Why our videos looked like slop (root causes, checked against the code)

| Symptom | Cause in the kit | Fix |
|---|---|---|
| Characters stand and breathe while the narrator talks | EP4 `shots*.py`: 52 `mo.idle()`, 1 `mo.strike()`. `strike()` is the only helper with anticipation (ANTIC=4 f), overshoot (OVER=0.12, MOVE=4 f) and settle (SETTLE=5 f) **[verified]** | a `strike()` or keyed turn/gesture every 0.5-0.8 s (section 4) |
| Flat straight-on "mugshot" shots | `shotlib.frame_on`: yaw search starts at offset 0 from the face direction, `pitch=4` (camera slightly above, looking down), `lens=35` **[verified]**; 31 of 34 EP4 cameras | 3/4 angles and per-beat recipes (section 2) |
| Two-shots small and distant | `frame_on` fits **all** `chars` inside a 6 % margin **[verified]** | frame the speaker/reactor only; the other is a foreground shoulder |
| Both characters soft | `frame_on` focuses on `tgt` = centre of the bounding box of all subjects, f/2.8 **[verified]** | focus on the active character's head (`ch.head` world position); f/5.6 on two-shots |
| Camera barely moves | `frame_on` push=0.06, ease-in-out; `cams.PUSH_RATE=0.08`, `SLOW=0.15`, `LATE=0.12` **[verified]**. Gemini's "static for 57 % of each shot" is **[corrected]**: `frame_on` starts moving at t0, but ease-in-out over a 1.4 s shot reads as nearly still | bigger pushes (12-22 %), ease-out starts, beat recipes (crash_zoom, whip_pan, dutch, impact_shake) actually used |
| Blurry first frame | `core.setup_render(blur=True)` sets shutter 0.5 for every shot **[verified]** | `look.motion_blur(0.0)` by default; 0.35-0.5 only on fast moves (section 6). `look.motion_blur()` already exists, no new helper needed **[corrected]** |
| Flat "audiobook" voice | `tts.py` sends the whole script with one tag `[fast, urgent, breathless]` **[verified]** | per-beat requests with per-line tags (section 8) |
| Dead air and slow pace | `post.py`: silences > 0.22 s shrunk to 0.14 s, `PAUSE=0.45` per meme cue (17 in EP4), `TEMPO=1.08`, `adelay=100\|100` (0.1 s silence before word 1) **[verified]** | fewer, shorter meme pauses; voice from frame 0; faster take tested by ear |

---

## 1. First 3 seconds (stops the swipe)

- **0.00-0.40 s:** the voice starts on frame 0 (no lead silence) at the highest energy of the video, with a hit/whoosh SFX inside 0.2 s. The picture is the weirdest or highest-motion image of the story (the rule happening, the crash, the crowd reaction), shot with `cams.crash_zoom` or `cams.run_follow` (24-28 mm). Frame 0 is sharp: shutter 0.
- **0.4-1.5 s:** first cut at ~0.7-1.0 s to the consequence or reaction (`cams.dutch` or any camera + `cams.impact_shake`). The character does a `mo.strike()`.
- **1.5-3.0 s:** second cut at ~1.8-2.2 s to the rule payoff or the narrator MCU. **The twist word is spoken by 2.5 s.**
- On screen: captions only (1-2 words). No phone UI paragraph, no text wall, nothing static.
**[Gemini]** timings; they match the first-3-seconds checklist in SKILL.md section 3.

---

## 2. Per-beat camera recipes (real kit functions; start every move on frame 0 of the shot)

| Beat | Call | Lens / yaw / pitch | Move | Shot length, cut |
|---|---|---|---|---|
| Hook | `cams.crash_zoom` or `cams.run_follow`, then `cams.impact_shake(cam, t_hit)` | 24-28 mm, yaw 20-35, pitch -10..+8 | 25-35 % fast ease-out push, or tracking | 0.6-1.0 s; cut on the impact or the stressed word |
| Rule ("In this town...") | `cams.push_in` or `frame_on([ch], ..., yaw=22, pitch=-4, lens=35, push=0.15)` | 35 mm, yaw 20-25, pitch -4 | 15 % push | 1.2-1.8 s; cut on the consequence word |
| World examples (gag montage) | alternate `cams.whip_pan` -> `cams.truck` / `cams.ground_low` / `cams.overhead` | 24-35 mm, yaw alternating -25 / +25 | 15-20 % truck or whip | 0.8-1.3 s each; cut on the whip blur peak |
| "And me?" | `cams.dolly_zoom` or `frame_on([me], ..., yaw=15, pitch=10, lens=50, push=0.18)` | 50 mm, high angle (feels small) | 18 % push | 1.3-1.8 s |
| Reaction | `cams.mcu` / `cams.ecu`, or `cams.dutch(roll=8-14)` for panic | 65-85 mm, yaw 18-25 | 12-18 % fast ease-out snap | 0.6-1.2 s; cut 1-2 f after the face settles |
| Dialogue | `shotlib.ots` or `frame_on([speaker], ...)` (speaker only) | 45-50 mm, yaw +25..35 / reverse -25..35, pitch 0 | 12 % push | 1.0-1.8 s; cut on the speaker change |
| Action | `cams.run_follow`, `cams.track_side`, `cams.hero_low` + `impact_shake` | 21-28 mm, low (-18) or overhead (+20) | tracking | 0.6-1.2 s; cut mid-motion on the peak |
| Reveal | `cams.pull_reveal`, `cams.crane`, `cams.aerial_dive` | 24 mm for scale, 50 mm for an insert | 30-50 % pull or crane | 1.5-2.2 s; hold 0.3 s on the full reveal |
| Punchline | `cams.crash_zoom` (snap) or a dead-still `shotlib.still_cam` (deadpan) | 50-65 mm, yaw 12-18 | snap 20 % in 4 f, or locked | 0.9-1.4 s; cut 0.15-0.25 s after the word |
| Ending | `cams.dolly_zoom` (cliffhanger) or `cams.pull_reveal` (callback) | 28-50 mm | keeps moving through the last frame | 1.2-2.0 s; hard cut on the last word |

Never the same recipe twice in a row (cams.py rule, still valid). **[Gemini]** values; tune on the low-res contact sheet.

**`frame_on` in kit v5** already defaults to yaw +/-22 (alternating), pitch -4, 45 mm, 15 % push from frame 1, f/2.8 solo
or 5.6 two-shot and focus on `chars[0]`'s head. Pass only the active character(s) in `chars`, the speaker first.

---

## 3. Framing for 9:16 (1080x1920)

- The main character's eyes sit 35-42 % from the top (y 670-805 px). **[Gemini]**
- **Caption band [corrected]:** our captions are drawn centred at **y = 0.65 x 1920 = 1248 px** (0.68 during the end
  card) by `ep_captions.py`, not at the bottom. Keep faces, props and in-world text out of roughly **y 1120-1400 px**.
- Top ~12 % (0-230 px) and bottom ~20 % are covered by Shorts/Reels UI: nothing important there.
- Two characters: frame the active one; the other is a cropped foreground shoulder, never both shrunk to fit.

## 4. Motion (30 fps)

- **At least one clear pose change every 0.5-0.7 s** (about 1.5-2 keyed body/head/arm actions per second; 2.5 per second
  in the first 3 s). **[Gemini target - measure it in `shots.py` and compare]**
- Use `mo.strike(ch, t, pose, ...)` with the hit `t` on the stressed word or the cut. Normal gesture: antic 3-4 f, move
  3-4 f, over 0.12-0.15, settle 4-5 f (the kit defaults 4/4/0.12/5 are fine). Comedy snap: antic 2, move 3, over 0.18,
  settle 3.
- `mo.idle()` stays on as the base layer, but an **idle-only shot** is allowed in at most 10-15 % of shots (dread, quiet
  realisation, a deadpan freeze), never two in a row.
- Every pose asymmetric: 5-12 deg torso twist, uneven shoulders and elbows. Limbs move in arcs, not straight lines.
- Follow-through: head leads by 2 f (`LEAD=2`), arms and props settle 2-3 f after the torso.
- Every shock or laugh pairs the face swap with an upper-body pop: head back 10-15 deg + shoulders up through `strike()`.
- Walks/runs: `mo.walk` with bigger arm swing and bob; runs already use `RUN_CYCLE = 12` f **[verified]**.
- Props: `hold()` for every held prop; NOTOUCH / PROPFLOAT flags block the render.

## 5. Focus and depth of field

- Focus on the active character's head (`ch.head` world position at t), never between two characters.
- Solo MCU/ECU/prop macro: f/2.8-4. Two-shots, OTS, medium: f/5.6-8. Wides and aerials: f/11 or DoF off.

## 6. Motion blur

- Default `look.motion_blur(0.0)` per shot; frame 0 of the video always sharp.
- 0.35-0.5 only for whip pans, crash zooms, throws, runs and ragdoll flights (`whip_pan` already sets its own shutter).

## 7. Face swaps

- Stepped (constant) keys, never cross-faded. Swap 1-2 frames before the body hit and before the audio transient
  (`strike()` already swaps 1 f before the hit **[verified]**).
- Use high-contrast expressions on emotional words (wide-eyed shock, grimace, smug half-lid) instead of neutral.

## 8. Narration (ElevenLabs eleven_v3, voice Alex unchanged)

- **One request per line** of `tts_script.txt` (kit v5 `tts.py`; write one beat of 1-3 sentences per line). The chunks
  and their alignments are stitched into `raw.wav` + `alignment_raw.json`. `previous_text`/`next_text` are not used (not
  verified for eleven_v3); listen for joins between lines at the voice gate.
- **A tag on every line** for its emotion, for example:
  1. `[excited, fast] In this town, every lie makes you SHRINK one inch.`
  2. `[deadpan] The mayor is the size of a pencil.`
  3. `[urgent] Until one night, I woke up to smoke.`
  4. `[whispers] "Don't let them see."`
  5. `[shouting] "RUN!"`
- **Pauses:** 0 s before the first word (today `adelay=100|100` adds 0.1 s); shrink speech gaps to ~0.08 s (today 0.14);
  a deliberate 0.22-0.28 s beat only before a punchline or twist; at most 4-8 meme pauses of 0.20-0.28 s (today 17 x 0.45 s).
- **Pace:** 3.8-4.2 words per second overall (EP3/EP4: 3.3-3.45). Get there with shorter sentences and fewer pauses first;
  a higher `TEMPO` (1.12-1.15 instead of 1.08) is a test for the voice gate, decided by ear.
- Stress numbers and key nouns (capitals or tags). Side-character voices or pitch/EQ presets: **[decision]**.

## 9. Sound effects on the picture

- A soft whoosh (-18 to -14 dB) on every whip pan and big cut; a pop (-16 dB) on shock faces, phone alerts, callouts;
  a heavy hit (-8 to -6 dB) on the exact impact frame with the bed ducked 8 dB.
- Music changes at the act 2 turn and the climax **[decision: music choices]**.

## 10. Pre-render checklist (scriptable pass/fail)

| Check | Pass | Today (EP4) |
|---|---|---|
| frame 0 motion blur | 0.0 | 0.5 |
| idle-only shots | <= 15 % of shots | 25 of 69 (36 %) |
| keyed actions per second | >= 1.5 overall, >= 2.5 in 0-3 s | ~0.4 (rough: 1 strike + 15 look_at + 3 walk + 3 nod + 4 laughs + 9 hold in 96 s) |
| cuts or one big camera move before 3.0 s | >= 2 cuts, or 1 crash_zoom / run_follow | see 0-3 s strip |
| twist word time (words.json) | <= 2.5 s | ~4 s |
| first word start | <= 0.05 s | ~0.19 s |
| words per second | 3.7-4.3 | 3.45 |
| longest silence in voice.wav | <= 0.30 s | 0.45 s (x17) |
| shots at yaw offset 0 | <= 20 % | up to 91 % (31 of 34 cameras were frame_on with no yaw) |
| shots focused between characters | 0 | every multi-character frame_on |
| in-world text inside the caption band (y 1120-1400) | 0 | not measured |
| like/share/follow outro | **[decision]** | 5.2 s |

## 11. Kit changes (applied in kit v5.0, 2026-11-17, tested without rendering; see kit CHANGELOG)

Done in v5: the `frame_on` defaults below (alternating +/-22 yaw, pitch -4, 45 mm, 15 % push from frame 1, f/2.8 solo /
5.6 two-shot, focus on the main head); motion blur off by default in `shotkit`; `mo.NORMAL` / `mo.SNAP` strike presets;
`tts.py` one request per line with its tags; `post.py` pause 0.24, gap 0.08, lead 0 (TEMPO unchanged, voice gate);
`tools/ep_viral_check.py` = the section 10 gate. Not built (existing tools cover them): `snap_pose` (= `mo.strike(...,
**mo.SNAP)`), `two_shot_active` (= `shotlib.ots` + frame_on on the speaker), `react_pop` (= `mo.shock` / `mo.gasp`).

Gemini's original proposals, for reference:
- `shotlib.snap_pose(ch, t, pose, antic=3, move=3, over=0.14, settle=4, face=None)`: everyday gesture on top of `mo.strike`
  with built-in asymmetry.
- `shotlib.two_shot_active(speaker, listener, t0, t1, yaw=24.0, lens=45.0, push=0.15)`: MCU on the speaker, listener's
  shoulder in the foreground, focus on the speaker's head at f/5.6.
- `motion.react_pop(ch, t, face, tilt_deg=12.0, dir="back")`: face swap 1 f early + 3-frame head/shoulder pop.
- `ep_audio/tts.py` beat chunking with per-line tags (and stitching of alignments).
- `qa.qa_dripdyl(...)`: the section 10 gates, run after the low-res pass.
- Not needed **[corrected]**: `set_shot_blur` (use the existing `look.motion_blur(shutter)` per shot).

Defaults changed in v5 (old -> new): `frame_on` yaw None/0 -> +/-22, pitch 4 -> -4, lens 35 -> 45, push 0.06 -> 0.15,
fstop 2.8 -> 5.6 with focus on the main head; motion blur 0.5 -> off (shotkit);
`post.py` PAUSE 0.45 -> 0.24, gap 0.14 -> 0.08, adelay 100 -> 0; TEMPO stays 1.08 (1.12-1.15 is a voice-gate test).
`cams.PUSH_RATE` was NOT changed (recipes keep their own rates; frame_on carries the new push).
