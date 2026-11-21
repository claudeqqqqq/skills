# EP3 BRIEF (read first, every agent) - 2026-11-16
Episode: Blox City Day 02. Title (approved): "I Told ONE Secret. By Lunch, Everyone Knew."  slug: friend_secret
Folder: Mac ~/RobloxStories_tmp/friend_secret  (= ~/RobloxStories/videos/friend_secret symlink; VM: $HOME/mnt/RobloxStories_tmp/friend_secret)
Kit: Mac ~/RobloxStories (VM $HOME/mnt/RobloxStories), kit v4.1 (+ v4.2 audio: tools/ep_audio/sfxgen.py and mix.py are now per-episode/config driven).
Read first: kit SKILL.md, docs/LESSONS.md, docs/CLEAN_ANIMATION.md (or Project knowledge/CLEAN_ANIMATION.md), templates/EP2_poor_boy_school_shots.py.
Script + beat map + SFX cue sheet: Project doc scripts/EP3_friend_sold_secret_script.md (captions text = script.txt here).

## Done (coordinator)
- Script approved by the user. Music: user said "same music as in this town" = assets/music/inthisworld_bed.wav ("Numbers", TEMPOREX) for the WHOLE video,
  copied to audio/inthisworld_bed.wav. Posted file = out/final_nomusic.mp4 (user adds the song in Instagram); out/final_preview.mp4 has the bed.
- Voice: audio/voice.wav (Alex alex_ep1, 100.05 s, 197 wpm, 18 meme pauses), audio/words.json (328 words, start/end s), audio/pauses.json.
- SFX: sfx/*.mp3 (own recreations, ElevenLabs SFX + EP2 copies) + kit sfx/. audio/mix_cfg.json, audio/mix_nomusic.wav + mix_preview.wav
  (-14.1 LUFS, peak -4.5 dBFS, 100.85 s). audio/sfx_cues_placed.json = cue times.
- Ending words: Like=311 share=312 follow=314 Comment=324, options TRUST=325 BLOCK.=327.

## Hard rules
- NEVER print or copy the ElevenLabs key (~/RobloxStories/.env). Never post anything anywhere. Never delete user files
  (EP2 posted files, Drive). Only write inside the friend_secret folder and the kit; back up a kit file before editing it (name.bak_ep3).
- No final full-quality render (tools/ep_final.sh) until the coordinator says the user approved the look-dev stills.
- VM background jobs die when the call ends: run long Blender jobs on the Mac, detached, via the Blender MCP
  execute_blender_code_for_cli (blend_file = /Applications/Blender.app/Contents/Resources/5.3/scripts/startup/bl_app_templates_system/Video_Editing/startup.blend)
  with subprocess.Popen([...], start_new_session=True, stdout=log). Blender binary: /Applications/Blender.app/Contents/MacOS/Blender.
- The VM cannot follow symlinks into Google Drive (videos/, assets/, music/); use the Mac (Blender MCP python) for those paths.
- After any fix: append a dated lesson line to docs/LESSONS.md (format: date | symptom | cause | fix | check).

## The user's EP2 mistake list (must NOT happen again; kit v4.1 tools exist for each)
levitating out of a car (use car_door + appear + 3-cut rule); characters cut off by frame (frame_on + CUTOFF/HALF/TINY QA);
objects floating instead of held (hold() + props3, qa.touch/qa.prop); unreadable small props (straight-on inserts, big enough);
laughing kids looking away / "dancing" (belly_laugh / crowd_laugh with target, head stays on target);
glitching instead of kneeling (kneel_down); key actions not visible (insert shots); typing on a table / a "game" shown as numbers
(real keyboard/laptop/phone screen content readable). Look: clean, like IG refs Dfe8B5Hs3G6 (night) and Dfs43n3oWqx (day). Full 1080x1920.

## Cast
Leo (narrator, 14, plain hoodie), Max (best friend; gets a shiny "limited" hat), Chase (rich kid, runs "Blox Tea"; afraid of the dark), classmates, camp teacher (no lines).
