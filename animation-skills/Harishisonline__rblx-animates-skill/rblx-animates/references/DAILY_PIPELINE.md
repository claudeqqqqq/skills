# DAILY PIPELINE: one episode per day at EP2/EP3 quality (kit v4.0 2026-11-15, audio v4.2 2026-11-16, single final v4.3)

EP2 "The Poor Boy Who Bought the School" is the quality bar the channel owner set ("I want all of my future outputs to be like
this"); EP3 "I Told ONE Secret. By Lunch, Everyone Knew." was made with the same line plus a parallel agent team.
Everything that produced them lives in the kit (`~/RobloxStories`), not in one episode folder.

## Kit pieces
| piece | what |
|---|---|
| `rbx/shotlib.py` | shot helpers: cameras (still_cam, scam, med, mcu, two_face, safe_pos, face_yaw, frame_on), contact (hand_pos, carry, hold, aim_prop, pencil, fit_desk_to_hands, seat_and_type, night_desk, kneel, kneel_down, stool), acting (belly_laugh, crowd_laugh), physics (drop, books), sets (car_door, appear, shoe_hole, game_screen, extra, install_snaps) |
| `rbx/props3.py` | held props with grips: pizza_box, book_stack, keyboard, laptop, tray, phone, duck_light, coin bag, hat... |
| `rbx/qa.py` | FLOAT / CLIP / HALF / CUTOFF / TINY / NOTOUCH / PROPFLOAT / EYELINE checks, declared in shots |
| `rbx/look.py` STYLE="clean", `rbx/cast.py` CLEAN=True | crisp look (defaults) |
| `rbx/signs.py` fit_text | text always inside its board |
| `tools/ep_lo.py` | low-res animated pass + QA log: `Blender -b --factory-startup -P tools/ep_lo.py -- <slug> all` (`RBX_LO_LOG` = log name) |
| `tools/ep_final.sh <slug> [samples] [ids]` | full-quality render, one shot per Blender run, lock + disk guard; counts shots in shots.py and shots_[a-z].py |
| `tools/ep_eta.py <ep dir>` | ETA from screen time (about 1.3-1.7 min of render per second of shot) |
| `tools/ep_captions.py <ep> test t:<sec> ...` | caption/end-card overlay test on a blank 1080x1920 frame (or real frames) |
| `tools/ep_endcard.py` | finds Like / share / follow / Comment + the two option words in words.json |
| `tools/ep_finish.sh <ep dir>` | captions + end card + audio -> `out/final.mp4`, loudness logged |
| `tools/ep_audio/` | tts, words, post (meme pauses + voice chain), sfxgen (sfx_jobs.json), bed (music), mix (mix_cfg.json), qa_audio |
| `templates/EP2_poor_boy_school_shots.py` | worked example of every rule |

## ep_audio (per episode, config files in <ep>/audio/)
- `tts.py` reads `tts_script.txt` (TTS spelling "Blocks"); captions use `script.txt` ("Blox").
- `post.py` reads `meme_cues.json` (`{"line", "after_word", "sfx"}`; optional `"nth"` picks the n-th occurrence of a
  repeated word in the line).
- `sfxgen.py` reads `sfx_jobs.json`: `{"name": {"sfx": prompt, "dur": s}}` (ElevenLabs sound generation, our own recreation),
  `{"name": {"tts": "[deadpan] Bruh."}}` (short Alex take), `{"name": {"copy": path}}` (reuse, no credits). Existing files are skipped.
- `bed.py [file|--none]`: the person's music, else `assets/music/default_bed.wav` (their licensed copy of the default), else an
  original score from `tools/score.py`. Writes `MUSIC_LICENSE.txt`.
- `mix.py` reads `mix_cfg.json`: `files` {LABEL: [[path, ffmpeg_filter, offset_s]]} with tokens `{K}` kit sfx/, `{S}` episode sfx/,
  `{A}` episode audio/, `{RB}` kit root; `gain` per label; `extra` [[path, word index or "t:sec", gain]]; `bed`
  {file, from_word, to_word, under_db, duck_db, fade_out}. Ending pops + follow click are placed from the words. The bed dips
  -8 dB for 1.2 s under each meme hit. Out: `mix_final.wav` (with the bed) and `mix_nomusic.wav`.
- `qa_audio.py`: prints AUDIO QA PASS/FAIL (hits inside word gaps, tails <= -10 dB under the voice, -14 LUFS / TP <= -1.5,
  bed under the voice).
- Lesson: mix.py peak-normalises each sound, so dense files (a phone buzz) come out much louder than sparse ones at the same
  gain. Fade long tails in mix_cfg and lower the gain; check with qa_audio.py.

## The day, with measured times
| step | who | time |
|---|---|---|
| 1. Topic + script; approval (white card) | Claude | 20-30 min |
| 2. Music question | person | 1 min |
| 3. Voice + timing (tts -> words -> post); voice gate | Claude + ElevenLabs | 10 min, ~1,800 characters |
| 4. SFX + bed + mix (sfx_jobs -> sfxgen, bed, mix_cfg -> mix, qa_audio) | Claude | 10-20 min |
| 5. shots.py with the CLEAN_ANIMATION grammar | Claude (or a team, TEAM_AGENTS.md) | 60-90 min |
| 6. ep_lo pass, fix every QA flag, look at 2 fps sheets | Blender + Claude | 15 min render + fixes |
| 7. Look-dev strip (6 full-quality stills); look gate | Blender | 3 min |
| 8. `ep_final.sh <slug> 32` | Blender | ~1.4 min per second of video (100 s = ~2 h 10 min on an M-series Mac mini) |
| 9. `ep_finish.sh <ep dir>` (test the overlay first) | computer | 90 s |
| 10. 1 fps contact sheet of the final; deliver `out/final.mp4` | Claude | 5 min |
About 5 h wall time, of which about 2.5 h is unattended rendering. The person posts after their own yes.

## Rules (full list in CLEAN_ANIMATION.md)
1. Shot grammar: wide, MCU to the lens, OTS / POV, prop insert, aftermath.
2. Contact by construction: IK the fists, measure them, build the prop under them; sit before the shot; car exits through
   car_door + appear (3 cuts).
3. Cameras: frame_on / face_yaw; clearance; stay inside rooms.
4. Look: clean style and clean cast are the defaults. Never judge the look from low-res frames.
5. Text: fit_text; straight-on inserts; real UI on screens.
6. Ending: pop-ups in the middle on the words, cursor clicks Follow, two-option comment buttons.
7. Run long jobs on the computer, detached.

## Still open
- Faces come from the kit atlases; some characters reuse another's face cells.
- Feet: one frame when a character steps from the road onto the sidewalk.
- Audio levels are checked by measurement only; the person judges the mix by ear.
