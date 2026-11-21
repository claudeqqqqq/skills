# EP3 friend_secret - QA REPORT (Manager / QA lead), 2026-11-16 20:20-23:25 (VM clock)

## Verdict
- PART A (shots 1-33, agent A): **APPROVED** 23:07.
- PART B (shots 34-63, agent B): **APPROVED** 23:22.
- Look-dev: 6 full-quality stills rendered (1080x1920, 32 samples, same V.build path as the finals). **Waiting for the user's look-dev approval. The final render (tools/ep_final.sh) was NOT started.**

## Flag counts (render_lo QA), baseline v1 -> final
| type | baseline v1 (63 shots) | final A (1-33) | final B (34-63) | final total |
|---|---|---|---|---|
| HALF | 141 | 5 | 15 | 20 |
| NOTOUCH | 49 | 0 | 2 | 2 |
| CUTOFF | 33 | 0 | 0 | 0 |
| AWAY | 16 | 9 | 0 | 9 |
| EYELINE | 16 | 0 | 0 | 0 |
| FLOAT | 14 | 0 | 0 | 0 |
| BLOCKED | 6 | 0 | 0 | 0 |
| TINY | 5 | 0 | 0 | 0 |
| **total** | **280** | **14** | **17** | **31** |
Logs: render_lo_A.log (v6, current kit), render_lo_B.log ('=== B v4 pass' + 'B v4b (53,62)'), baseline out/render_lo_v1_full.log.

## Accepted flags (and why)
- AWAY x9, s01/s10/s21: POV phone shots. The holder's head is hidden on purpose (the camera is his eyes); the check still sees the hidden head facing away.
- HALF x5, s30: Max's hat is the soft foreground corner of the OTS ("Leo sits down across from him"); Max is not the subject.
- HALF x15, s49/s59/s61: straight-on phone inserts; the holder's head is above the frame by design, the screen fills the frame.
- NOTOUCH x2, s56 (last 2 QA frames): Max's right fist 0.49 from the bag grip (tolerance 0.45) after the push-back; the bag is still visibly in his hands.

## Verdict per shot range (looked at 2 fps sheets, probes and stills, not only flags)
- 1-8 hook/friends: POV phone readable (was 60 % green torso), Max's coin bag at belly (was over his face), s04 hand on Leo's shoulder, s06 bus chest-up over the seat, s07/s08 handshake readable. OK.
- 9-13 night call: night look fixed (duck is the key light, dark room); faces 3/4 (s11 no longer the back of the head). OK.
- 14-22 Blox Tea / next morning: inserts readable; s22 jaw drop visible (phone lowered). OK.
- 23-33 cafeteria / hat: quack table and laughing kids closer, eyes on Leo; LIMITED hat readable in the CU; Max's face readable under the brim. OK.
- 34-42 bus / storm: empty bus seat reads; s37 lamp dies (was a flat dark-red frame = camera inside a tent); s41 Leo kneeling with the duck readable; s42 fist on the duck, glow on. OK.
- 43-52 duck circle: high wide reads; Chase's fist ON Leo's sleeve with both faces 3/4; Jay's phone at chest; Chase MCU with no FG. OK.
- 53-63 morning / resolution / end card: no lamp pole bar, push-back two-shot reads, phone inserts fill the frame, 4 ducks on a dark night sill, end card calm. OK.
- A/B cut 33 -> 34 (cafeteria "limited, bro" -> bus two weeks later, alone): clean time jump, Leo's hoodie consistent. Beat map: every shot's picture matches its words (checked against audio/words.json).

## Shared fixes made by the Manager (backups *.bak_mgr)
- shots.py: pov_phone hides the whole holder except the arms; Leo = plain zip hoodie (no H patch/snaps; zip, drawstrings, hood); bus seat backs to shoulder height; night bedroom look night_dim() (fills/look rig down, dark window pane, duck 650 W + glow 1.5, low warm character rig via an auto_light wrapper); CHASE_C/sleeve_grab rework (part B uses its own b_ layout).
- rbx/shotlib.py: frame_on -> clear_fg() (hides non-subject characters/crowd instances in front of the subjects); belly_laugh keeps its body turn; hold()/follow() key contact on frame t0; seat_and_type measures fists after look_at.
- rbx/motion.py: strike() anticipation dip from the sampled hipz (seated hips no longer pop); talk_cadence(arms=False) and no leg sway when seated.
- rbx/cast.py: build/stance keys at t0 - PRE_KEY (1.5 s) + settle_stance() hold keys at t0 for untouched channels (pre-shot sit/turn/hold survive frame 1).
- rbx/props3.py: limited_hat band/text bigger (LIMITED readable).
- Regression: ~/RobloxStories_tmp/shotlib_test after every kit change = baseline flags (kneel FLOAT fixed, desk clean, TINY in the crowd-laugh test pre-existing).
- Kit TODO (not changed mid-episode): motion._head_world ignores hipz (seated look_at pitch); 'torso' body key = hip rotation. Both parts have workarounds.

## Look-dev (out/lookdev/)
ld1_bedroom_night_duck.png (s09), ld2_cafeteria_quack.png (s24), ld3_limited_hat_cu.png (s28), ld4_camp_storm_dark.png (s38),
ld5_duck_circle_sleeve.png (s46), ld6_morning_coinbag_push.png (s56); side-by-side: out/lookdev/lookdev_strip.jpg. Script: out/lookdev/lookdev.sh.
Measured (108x192): ld1 med 44 / B-R -12; ld2 med 121 / B-R -19; ld3 med 151 / B-R -52; ld4 med 54 / B-R +17; ld5 med 55 / B-R -18 / S 0.50; ld6 med 130 / p98 227 / B-R -21.
vs refs: night stills (ld1/ld4/ld5) sit in the REF Dfe8B5Hs3G6 median band 40-60 with one warm practical; day ld6 is a bit brighter/hotter than REF Dfs43n3oWqx (median 130 vs 90-110, p98 227 vs 195-215). Blacks are crushed (p2 0) on purpose: the v4.0 CLEAN look follows the user's crisp refs, not the old matte spec. ld4 is slightly blue (B-R +17 vs <= +12) - the storm sky; ld5 is warm/saturated from the duck. Only the user can judge the look by eye.

## Final render ETA (after look-dev approval)
tools/ep_final.sh friend_secret 32 (detached on the Mac): about 1.4 min per second x 100.85 s = about 141 min (2 h 21 min), plus ep_finish about 2 min.

## Not verified / caveats
- From 23:00 the desktop sign-in went stale, so I could not stage images: part B's last pass was verified by log, numeric frame stats and the 3 B look-dev stills (viewed as a small thumbnail), not by a full 2 fps sheet of the final B frames.
- EEVEE prints "Shadow buffer full (2326/2048)" in the cafeteria: possible missing shadows there in the finals; look at the cafeteria shots in the final sheet.
- lo frames are 34 % / 6 samples: sharpness and mood are only judged from the look-dev stills.
