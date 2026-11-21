# REF: instagram.com/p/Dfe8B5Hs3G6 (@kyreblx, "In This Town Every Clock Skips One Minute...", 2026-11-09)
Studied 2026-11-14 in the signed-in browser pane: 132.3 s, 1080x1920; colour sampled every 0.5 s (263 samples, in-page canvas); pictures: 133 stills at 1 per second via in-page contact sheets, 24 stills at 0.1 s steps, 8 full-res stills. No frames saved or copied; numbers only. We recreate the STYLE with original assets.
Legend: [seen] = observed/measured in the reel; [inferred] = my reading of how it was made.

## DO / DON'T (follow with no other context)
1. DO grade NEUTRAL-to-slightly-warm: mean B-R between -5 and +5 (8-bit) on day/interior shots; night may go B-R up to +12, never more. Ours was +35 at 0:10 (cyan cast). DON'T ship any shot with B-R > +15.
2. DO cut saturation roughly in half: target mean HSV-S 0.28-0.38 (ref 0.30; EP1 0.60).
3. DO lift blacks: 2nd-percentile luma 12-20 (ref 17; EP1 5.5). Milky, matte toe, no crushed pure black.
4. DO compress highlights: 98th-percentile luma 120-175 typical, >220 only for flashes/moon/sky (ref 124; EP1 212).
5. DO expose darker/moodier: median luma 40-60 (ref 49; EP1 83).
6. DO light with ONE motivated warm practical (window/porch/lamp, ~2700-3200 K) against a dim neutral-grey ambient; DON'T flood scenes with blue fill/rim.
7. DO use night exteriors that are grey-slate (moonlit, desaturated), not saturated indigo.
8. DO cut every ~2 s (ref ~30 shots/min, avg shot ~2.0 s); hold 4-6 s only on dread beats.
9. DO frame mostly eye-level MS/MCU, lens feel 35-50 mm, static or very slow push; use low-angle full shots for "standing outside the house" beats.
10. DO use a tight face ECU (face fills frame, eyes ~40 % of width) for emotional peaks (tear, shock).
11. DO use flashback = sepia/monochrome with heavy grain + vignette (seen at 1:54-1:57).
12. DO put inserts of the story prop (clock face ECU) as their own shots, prop fills frame.
13. DO captions (captions2 defaults): white heavy sans ALL CAPS, thin outline, 1-3 words, y 0.65, size 64, hard cut, ONE key word yellow #FFD21E (red #E0141E for threat words).
14. DO any "keep sleeve down / tug sleeve / hold X" beat with fingertips ON the cuff/object in a still checked at the START frame and mid frame (town.insert_sleeve_pull, contact < 0.05 m).
15. DON'T let a hand that the narration names hang free near the object: contact or don't mention it.
16. DO keep faces readable: warm skin key ~1 stop above background.
17. DO add soft vignette 0.25-0.35 and fine film grain (ref has visible compression-grain texture) [inferred].
18. DON'T use bloom glow halos beyond practicals; bloom <= 0.12.
19. DO run tools/grade_check.py (all PASS) on contact-sheet stills before any render goes to the user.
20. DON'T copy kyreblx characters, house, clock or frames; original cast/props only.

## Measured look spec (whole reel, 263 samples) [seen]
| metric (8-bit, 108x192 downsample) | REF | our EP1 | target |
|---|---|---|---|
| mean R / G / B | 54 / 55 / 57 | 97 / 87 / 94 | balanced, B-R in [-5,+5] (night <= +12) |
| B-R on a cool shot (EP1 0:10) | ref night street 0:10 = +15 | +35 (B 155 vs R 130 at 0:08) | <= +12 |
| mean saturation (HSV S) | 0.30 | 0.60 | 0.28-0.38 |
| black level p2 luma | 17 | 5.5 | 12-20 |
| median luma | 49 | 83 | 40-60 |
| highlight p98 luma | 124 | 212 | 120-175 |
Per-shot range: warm interiors/porch R>B by 10-30 (eg 0:36 R81 G64 B48; 1:56 R93 B69); nights B>R by 8-15 with S 0.4-0.5 but very dark (median 13-20). Sepia flashback ~1:54-2:02 (R>B ~+25). End white flash 2:10 (L 213).
Kit mapping (IMPLEMENTED 2026-11-14, UNRENDERED / visually untested): look.PRESETS ref_matte / ref_day / ref_night / ref_practical,
look.ref(...) tuner, look.REF_TARGETS, cast.LOOK_COOL (neutral character fill/rim), shotkit default look = ref_matte,
tools/grade_check.py. See CHANGELOG v3.6.
Light rig [inferred from stills]: one warm key from a practical (doorway / window / porch lamp, ~2800-3200 K), dim grey ambient,
weak or no coloured rim, heavy volumetric haze in interiors (staircase hall 1:12-1:33 is foggy grey) [haze seen], strong AO.
Night: weak grey-slate moon, big visible moon disc in frame, lit windows as the only warm accents [seen].

## Shot-by-shot, full coverage (1 still per second for 0-132 s via in-page contact sheets + 0.1 s steps at 57.6-59.9 s)
Timestamps are +-1 s: Instagram's stream seeks are not frame-exact (two sessions gave offsets of a few seconds).
Lens is judged from perspective [inferred]; everything else [seen] unless marked.
| t (s) | shot | framing / camera | acting, hands, face | set / light | caption (key word) |
|---|---|---|---|---|---|
| 0-1 | boy face, eyes closed (asleep) | ECU, face fills frame, static, ~50 mm | closed-eye decal, calm | red-orange lamp glow from side, dark | "PM" |
| 2-3 | same, eyes snap open + sweat drops | ECU, slight push | wide eyes, small 'o' mouth, sweat decals | same warm key | "ONE MINUTE" |
| 4-7 | bedroom: bed, books, clock 11:59 on sill, window | wide/MS, static ~28 mm, slight high angle | no character | cool-grey moonlight, red curtain, blue-grey walls | "NOBODY KNOWS" |
| 8 | boy lying in bed seen from side | MS, low | still | moonlight | "NOBODY KNOWS" |
| 9-12 | night street, lamp-post clock on a pole, picket fence | wide, low angle, static, deep focus | none | grey cloudy sky, warm windows | "EVERY NIGHT", "STRAIGHT FROM" |
| 13-21 | clock face, minute hand ticks 11:59 -> 12:01 | insert, clock fills 90 % width, slow push, ~85 mm | prop acting: hand jumps (skip) | flat ambient, warm cream dial | "11:59 TO", "12:01" |
| 22-23 | boy standing in street under clock, far | full shot, low angle | arms at sides | night | "12:01" |
| 24-27 | bedroom window from inside, alarm 11:59, desk | MS, static | none | moon disc in window | "WINDOW" |
| 28-33 | girl standing in street under moon | full -> MS (cut-in 29), low angle | arms down, blank stare | moon backlight, cool grey | "A LITTLE", "GIRL" |
| 34-38 | girl by bare tree, wider | wide, eye level | still | night fog | "PROBABLY AROUND", "SEVEN YEARS" |
| 39-43 | boy at bedside, standing up | MS low angle ~24 mm, slight handheld drift | stands, turns head, hand on bed edge (in contact) | moonlit room, very dark | "SHE WAS", "COMPLETELY", "STILL" |
| 44-51 | girl face | ECU (face = frame width), static | wide eyes, flat mouth, then frown at 49 | dim grey | "STARING DIRECTLY", "AT ME" (ME red) |
| 52-57 | boy peeks over window sill | MCU through window frame (frame-in-frame) | eyes wide, sweat, scared mouth | cool interior | "SOMETHING ABOUT", "HER FACE" |
| 57.6-59 | grandfather clock pendulum / dial | insert, static | prop | dark brass | "ITS PENDULUM", "WAS STILL", "SWINGING" (yellow) |
| 58-63 | girl under moon (re-establish) | MS, low | still | moon disc top right | "FELT FAMILIAR" (yellow), "BUT I", "OUT WHY" |
| 64-66 | boy face low in frame, behind sill | MCU, top-heavy headroom | eyes peeking | dark | "I IMMEDIATELY", "CHECKED MY" |
| 67-71 | window sill + red digital clock 11:59 | insert/MS, push to clock, ECU at 71 | prop | red LED glow | "CLOCK", "11:59" |
| 72-77 | dark staircase hall, small girl at far end; boy OTS | OTS with boy's head as big FG, girl small BG, ~35 mm | boy turns (73-74 face to camera) | heavy grey fog, dust | "GIRL'S VOICE" (VOICE red), "YOU STILL", "I TURNED" |
| 78-80 | girl ECU, tear | ECU static | brows knit, tear decal, wavy mouth | dim | "SHE JUST", "YOU PROMISED" (yellow), "FORGET" (red) |
| 81-87 | staircase; blond boy in vest appears; boy backs off | MS/OTS mix, cuts ~1.5 s | blond boy steps forward (arms swing), our boy backs away | fog, framed painting | "I HEARD", "BEHIND THE", "A LITTLE", "BOY STEPPED", "I BACKED" |
| 88-93 | hallway crowd of children appearing | wide, eye level | kids standing, sitting on stairs | fog | "CHILDREN BEGAN" (red), "THE HALLWAYS", "SITTING ON", "WHILE OTHERS" |
| 94-101 | striped-shirt kid ECU crying, boy MCU, redhead girl crying | ECU / MCU alternating | tears, worried brows | dim | "THEM FINALLY", "IN HERE", "CLOCK" (yellow), "GIRL LOOKED", "ANSWERING" |
| 102-108 | kids in room, toys, crowd | MS / wide | standing, rocking horse set dressing | fog | "PLACE WHERE", "CHILDREN CAN", "ONLY ONE", "UNDERSTAND" (yellow) |
| 109-111 | music box on floor, old photo | insert, high angle ~50 mm | prop | warm practical | "UNTIL AN", "HAD SLIPPED", "MUSIC BOX" |
| 112-113 | boy picks it up (low angle) | low MS | reaching down, hand to object | dark | "FLOOR", "IT UP" |
| 114-123 | SEPIA flashback: old house, rows of children | wide static -> slow push, grain + vignette | crowd standing | sepia, strong grain | "OF CHILDREN", "SAME HOUSE", "WAS ME" (ME red), "OR SEVEN", "BESIDE ME" |
| 119 | boy ECU (present, cool) inserted mid-flashback | ECU | shocked | dim | "YOUNGER" (yellow) |
| 124-127 | warm daylight flashback: kids run back to house, porch, two kids sitting | wide low angle, then MS | running, sitting, holding box (hands on box) | bright warm sun, long shadows, autumn leaves | "RUSHING BACK", "THE GAMES", "THE MUSIC", "THE PROMISES" (red) |
| 128 | crying girl ECU | ECU | tears | dim | "SHE WASN'T" |
| 129 | boy in hall, dark | MS | still | dark | - |
| 130-132 | clock face ECU white-hot, fade to white | insert, overexposed | prop | blown white | end |

Cut rhythm [seen]: ~65 shots in 132 s => ~30 cuts/min, avg ~2.0 s; caption groups change every 0.4-0.8 s, ~2 words each.
Transitions [seen]: hard cuts throughout; flashback in/out by hard cut to the sepia grade; ending blows out to white. No whips,
no speed lines, no impact frames, no crash zooms seen in 1 s or 0.1 s sampling. SFX-visual sync: clock tick = minute hand jump
(13-21 s) [seen picture; audio inferred, muted].
Faces vs ours [seen]: same decal family (big white glossy eyes with highlight, thick brows, small mouth), but they lean HARD on
extra decals: sweat drops, tear streaks, knitted brows, wavy 'crying' mouth; ECUs where the face fills the frame width.
Hands [seen]: rarely shown; when shown they touch the thing (bed edge, box, music box). Their way to avoid hand errors: shoot faces/inserts.

## Gaps and the exact kit change
| gap | change |
|---|---|
| EP1 blue/cyan cast (B-R +35 at 0:10) | cine_room/cine_day fill (0.62,0.77,0.91) + rim (0.75,0.85,1.0) + shadows B 1.03 push blue; add PRESETS ref_matte/ref_night (above); default V.look -> "ref_matte" |
| 2x saturation | ref_matte sat 0.72 multiplier (or desat 0.4 in _grade_extra) |
| crushed blacks + hot whites | add black lift + highlight gain in look._grade_extra (new keys lift=0.06, roll=0.85); AgX Base Contrast |
| too bright | look.exposure(-0.6) on ref presets |
| no automated check | DONE tools/grade_check.py (EP1: 6 of 7 rows FIX, 34/92 cool frames) |
| hand-sleeve gap at 0:10-0:11 | DONE town.CUFF_TOL=0.05 (pinch + sleeve_pull) + town.hand_on_prop(hand, prop, t0, t1) guard printing start-frame gap |
| cut rhythm | DONE pacing.py row 'cuts/min vs REF_IG' (26-40/min = ok; EP1 35/min ok) |
