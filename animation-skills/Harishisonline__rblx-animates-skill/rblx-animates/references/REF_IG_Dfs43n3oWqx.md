# REF: instagram.com/p/Dfs43n3oWqx ("MY TWIN SISTER VANISHED ON PURPOSE...", Ralph Story Guy) - DAYLIGHT + FACES
Studied 2026-11-14 in the signed-in browser pane: 105.4 s, 1080x1920. Canvas pixel stats every 0.5 s (211 samples, 54x96 and 108x192 downsample), ~90 stills viewed in timed grids (>= 1/s, more at cuts), 4 face-crop sequences at 0.125-0.2 s steps (7.0-9.3, 23.0-24.4, 45.5-48.0, 53.5-54.1, 92.5-93.1). No frames saved or downloaded; numbers + notes only. Audio NOT heard (pane has no audio path for me; Gemini could not open Instagram, see GEMINI_AUDIO_NOTES.md).
Legend: [seen] observed/measured; [inferred] my reading.

## DO / DON'T (follow with no other context)
1. DO daylight exteriors as bright, mildly warm-neutral noon: median luma 90-110, p2 30-45 (lifted, milky), p98 190-215; mean S 0.20-0.35. DON'T crush blacks (p2 < 15) in day shots.
2. DO a single hard-ish sun, ~45-55 deg elevation, from camera side/back-side, crisp-but-soft shadow edge (sun angle ~1.5-3 deg) on pavement; shadow side lit by a bright sky fill (shadow luma ~45-60 % of lit side, never black).
3. DO a saturated-but-light blue sky with big white cumulus; sky may push frame B-R to +30, but SKIN/ground must stay neutral-warm (B-R <= +5 on non-sky pixels).
4. DO interiors in daytime warm (B-R -15 to -45, R>B): yellow/green walls, window daylight + warm ceiling lamp.
5. DO cut every ~1.9 s (52 hard cuts detected + several whip/blur transitions in 105 s = ~33/min).
6. DO use whip-pan / motion-blur smears (11 s, 39 s, 53 s) and a white sparkle-puff flash (5, 13, 14, 17, 24.4, 87 s) as the "magic happens" transition.
7. DO swap faces as HARD decal swaps on beats (0-frame transition), not morphs. Hold each expression 0.2-1.0 s in reaction moments, 2-4 s in calm moments.
8. DO a reaction ladder on a surprise: base face -> wide round "shock" eyes (6-8 f) -> big laugh/scream -> shock again -> cut. (seen 23.0-24.4: smirk-laugh, shock, toothy grin, shock, puff)
9. DO eye darts in fear holds: pupils jump left/right every 4-5 frames inside wide white eyes (seen 46.2-47.2).
10. DO blinks as a 2-4 frame swap to a closed-eye cell (seen 7.75-7.88, closed "content" lines). ~1 blink per 2.5-4 s on held talking/idle shots.
11. DO single-tear face for sorrow: half-lidded droopy eyes + one tear drop from inner eye corner + small flat mouth, held 1-2 s on a push-in (53.9-54.1, 92.5-93.1).
12. DO angry/scream: squeezed angled brows, mouth wide open with red/pink tongue, hold 6-10 frames, then snap to "worried" (45.6 -> 46.2).
13. DON'T lip-sync the narrator to on-screen mouths: narration is first-person VO; characters' mouths hold one shape per beat (seen throughout). Only the speaking character in a quoted line gets 1-2 mouth swaps.
14. DO comedic "face erased" gag: plain dot eyes + tiny mouth face (8.38+) as a punchline.
15. DO captions: 1-3 words, white, heavy rounded sans, mixed/sentence case, thick black outline, centred ~y 70-75 % (lower than ours). No yellow emphasis seen.
16. DO set dressing dense and toy-like: flower beds, lamp posts, picket fences, bunting, chalked hopscotch/height marks, mailbox, pool, ice-cream truck; props sized big and readable.
17. DO lens mostly 24-35 mm eye-level MS/MCU with low/handheld-feel push-ins; ECUs of faces for emotional peaks (face fills 60-80 % width).
18. DO a night/dusk shot (57-58 s) only for the sad turn: dark (median 20-30), B-R +10.
19. DON'T leave hands near a prop the narration names without contact (seen: fridge magnets, cake, wheelchair wheels, height chart marker - all touched).
20. DON'T copy this creator's characters, sets or face decals; draw our own atlas cells in the same vocabulary.

## Daylight look spec (measured) [seen]
| metric (8-bit) | whole reel | day exteriors (0-3, 19.5-24.5, 32-37, 59-60, 80-85 s) | warm interiors (11-19, 25-31, 66-77 s) | our EP1 | REF Dfe8B5 (night/moody) |
|---|---|---|---|---|---|
| mean R / B | 108 / 97 | ~105-125 / 110-155 (sky-heavy) | 120-185 / 70-125 | 97 / 94 | 54 / 57 |
| B-R | -11 | -5 to +35 (sky-heavy frames high; street level -5..+12) | -15 to -65 | +35 cool | +3 |
| HSV S mean | 0.32 | 0.20-0.40 | 0.30-0.46 | 0.60 | 0.30 |
| p2 luma | 36 | 33-95 (very lifted) | 17-45 | 5.5 | 17 |
| median luma | 97 | 90-150 | 80-165 | 83 | 49 |
| p98 luma | 194 | 195-250 | 200-237 | 212 | 124 |
Examples (t: R,G,B S p2/med/p98): 0.0 street 115,111,107 .18 46/103/196; 20.0 field 109,140,115 .41 77/134/220; 23.0 pool 119,144,156 .39 61/145/222; 59.0 sidewalk 93,94,98 .22 33/92/172; 80.5 street 115,104,105 .26 39/98/222; 73.0 kitchen 183,145,121 .43 37/166/237; night 57.5 23,24,32 .34 3/24/60.
Read: bright, low-contrast, lifted blacks, moderate saturation; skin stays warm-neutral; colour lives in sky, grass and props, not in light colour.
Light rig to build [inferred]: look.PRESETS "ref_day" = day preset with sun strength ~3.0-3.5, colour (1.0,0.96,0.90), elevation 45-55, angle 2 deg; world sky strength 1.0-1.2 (brighter fill than now) so shadows sit at ~50 % of lit; NO blue fill light; grade sat x0.75, contrast 0.9, black lift 0.10-0.12, AgX Base Contrast; vignette 0.15 (lighter than night); bloom 0.06. Target the "day exteriors" column with ref_grade_check, measuring B-R on non-sky pixels.

## Shot table (approx; cut detector at 0.5 s + stills) [seen]
| t (s) | shot | camera | notes |
|---|---|---|---|
| 0-3.5 | street queue at ice-cream truck, daylight | WS high-ish, slow push to MS of blond kid | caption "In this town, if you say, wait," |
| 4-6.5 | truck window, kids, sparkle puff | MS, over-shoulder | wish "pops" with white sparkle cloud |
| 7-9 | blond kid MCU, smug -> blink -> face erased | static MCU | face-swap gag |
| 9.5-10.5 | MISSING poster insert | insert | |
| 11 | whip blur | transition | |
| 12-14.5 | living room twins on couch, mouth open; red couch ECU, sparkle | MS -> ECU | warm interior |
| 15-17 | grandpa armchair + twins | WS interior | |
| 17.5-19 | porch, delivery man w/ pizza boxes | MS, puff flash | |
| 19.5-22.5 | soccer field, folding chair with team photo | low WS | very bright day |
| 23-24.5 | cousin by pool, popsicle, reaction ladder | MCU | sky B-R +35 |
| 25-31 | Christmas room, kitchen fridge magnets | MS/insert of hand on fridge | hand contact |
| 32.5-38 | street w/ kite, twins walking | WS low, tracking | |
| 39-42 | oak tree, kite caught, branch snaps | whip, low WS | |
| 42.5-48 | bedroom: grandpa scolds, boy shouts, shuts curtain, worried eye darts | MS/MCU, dissolve at 47.3 | key face study |
| 48-54 | night bedroom, empty bed, purple light, ECU tear | MCU -> ECU | |
| 55-58 | doorway; night under oak, dad hugs | WS, very dark | only night beat |
| 59-64.5 | boy in wheelchair on sidewalk | WS -> MCU | daylight return |
| 65-66 | window POV, curtain opens to oak | POV | |
| 66-72.5 | street fair/bunting, landing, chalk numbers | high angles, inserts | |
| 73-75 | birthday cake kitchen, fridge | MS warm | |
| 76.5-86 | oak + chalk height numbers ("At ninety... ninety-eight"), autumn leaves | low MS, feet insert | countdown montage, cut every 1.5 s |
| 87 | sparkle flash "and a hand" | transition | |
| 88.5-95.5 | sister returns in pajamas, hands, tear ECU | WS -> ECU | |
| 96-98 | height chart insert, twins in kitchen | insert, MS | |
| 98.5-105 | dinner table, lamp, end | MS | |

## Character design [seen]
Classic blocky R15-ish avatars, cylinder-ish heads with flat 2D decal faces (black line art, white eye whites, small black pupils), hair as chunky modelled meshes, plain shirts/hoodies, white sneakers. Props big and simple. Wheelchair, folding chair, cake modelled, not textures.

## FACIAL EXPRESSION SPEC
### Vocabulary seen (eyes / mouth) -> our kit
| seen expression | eyes | mouth | have in kit? | build |
|---|---|---|---|---|
| smug / unimpressed (7.0) | half-lidded ovals, pupils pushed UP, straight upper lid, thin angled brows | asymmetric wavy line | partial: smug=(half, smirk) | ADD eye cell `half_up` (lid line + pupils at top) and mouth `wavy_side` |
| content blink (7.75) | closed upward-curved lines | small "w" cat smile | relief=(closed, smile) | ADD mouth `cat_w`; blink cell `closed_happy` |
| face erased (8.38) | two dots | tiny dash | no | ADD eye `dots`, mouth `dash`; EXPR "blank" |
| shock (23.4, 24.2) | big round whites, tiny centred pupils, no brows | tiny "o"/flat | gasp=(wide,o) close | ADD eye `ring` (thick outline, small pupil); EXPR "pop_shock"=(ring, o_small) |
| laugh smug (23.0) | half-lidded, droopy | open grin with top teeth | partial | ADD mouth `grin_top` |
| toothy grin (24.0) | closed happy arcs | huge open grin, two rows of teeth | grin=(happy, grin) ok | check teeth rows in atlas |
| angry shout (45.6-45.9) | squeezed, brows sharply down-in, eyes small | wide open, red tongue | furious=(angry, scream) | ensure scream cell has red tongue |
| worried w/ darts (46.2-47.2) | large white ovals, small pupils that jump L/R, brows up-in | small wobbly frown | worried=(worried, frown); side_l/side_r exist | ADD `worried_l`, `worried_r` eye cells (same lids, pupils shifted) for darts |
| sad tear (53.9, 92.5) | half-lid droopy, brows up-in, tear drop under inner eye | small flat/down | cry=(cry, ah) too loud | ADD eye `tear1`, EXPR "sad_tear"=(tear1, flat) |
| neutral worried open (53.7) | big ovals, no pupils highlight | slightly open | | use wide + o_small |
Mouth set needed (11): flat, dash, o_small, o, wavy, wavy_side, cat_w, frown_wobble, grin_top, grin_full, scream_tongue. Talking (only for quoted lines): flat <-> o_small <-> grin_top, 3-4 swaps/s, no phoneme mapping. [seen: no per-phoneme sync anywhere; mouths hold per beat]
### Timing numbers (30 fps) [seen unless marked]
- Expression swap: 0 frames (hard cut of decal), coincides with a beat word or the SFX/puff frame.
- Reaction ladder steps: 6-8 f each (0.2-0.27 s); total 1.2-1.5 s then cut.
- Anger hold 9-12 f, then hard swap to worried (no in-between).
- Eye darts: pupils jump every 4-5 f, alternating L/R, 3-5 darts per hold, rest centre 6-8 f between bursts.
- Blink: 2-4 f closed; interval 2.5-4 s on held shots; no blink during reaction ladders. (only 1 blink caught in the sampled windows; rate [inferred])
- Tear hold 1.5-2 s with slow push-in, no blink.
- Head: small tilt/turn accompanies a swap (5-10 deg) [seen at 46.2-47.2 slight head turn]; anticipation on body gestures 2-3 f, overshoot small. [inferred]
- On cuts: the next shot often opens on a NEW expression (expression change is "hidden" in cuts ~50 % of the time).
### How to build in our kit
- acting.EYE add: half_up, closed_happy, dots, ring, worried_l, worried_r, tear1. MOUTH add: dash, o_small, cat_w, wavy_side, frown_wobble, grin_top, scream_tongue (tools/make_faces_layered.py / make_cast_v3_faces.py atlases: grow 4x4 to 5x5 cells).
- EXPR add: blank=(dots,dash), pop_shock=(ring,o_small), sad_tear=(tear1,flat), worried_dart=(worried,frown_wobble), smug_up=(half_up,wavy_side), content=(closed_happy,cat_w).
- New helpers: `dart(ch,t0,t1,every=4/30)` alternating worried_l/worried_r keyed CONSTANT; `ladder(ch,t,[expr...],step=7/30)`; `blink()` default every=(2.5,4.0), closed 3 f, and skip windows where ladder/dart are active.
- Keep face keys CONSTANT interpolation (they are already atlas swaps); align swap frames to caption word onsets.
- Do NOT call talk() on the narrator-POV character during VO; use one mouth per beat.

## Hands / props [seen]
Hand on fridge magnet (30-31), hand on cake/table (73), hands on wheelchair rims (59-63), two hands meeting at oak (94 "at our hands"), marker on height chart (96). Contact is real in every named action.

## Narration / audio
Not heard. From burned-in captions [seen]: first-person, past tense, short clauses, numbers as a countdown device ("At ninety... At ninety-seven... Ninety-eight"), quoted dialogue in captions with quote marks. Caption density ~1 caption per 0.5-0.8 s of 1-3 words -> pace roughly 150-190 wpm [inferred]. Gemini could not open this Instagram URL (see GEMINI_AUDIO_NOTES.md); no Gemini-sourced claims here.
