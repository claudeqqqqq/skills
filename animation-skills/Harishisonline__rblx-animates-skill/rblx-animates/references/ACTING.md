# ACTING — body language library (rbx/motion.py, re-exported by rbx/acting.py)

Times passed to functions are SECONDS (like the rest of the kit). Timings below are FRAMES @30 fps; `mo.fr(n)` converts.
`from rbx import motion as mo` or `acting.shock(ch, t)` — both work. Every preset works on any `chars.Char` (all cast.*).

## The rule: pose-to-pose, pose HITS on the word
`strike(ch, t, pose)` is the engine under every gesture. `t` is the HIT frame — put it on the stressed word / the cut.
| phase | frames | what |
|---|---|---|
| hold | t-8 | previous pose read from the F-curves (moves chain, no pops) |
| anticipation | t-4 | 15 % of the move reversed + hip dip 0.08; squash if `sq` |
| hit | t | 112 % of the move (overshoot 10-15 %), stretch; face swaps at t-1 |
| settle | t+5 | final pose; `hold=` keeps a moving hold (3 % drift), `release=` eases back to rest |
Head channel runs LEAD=2 f early (head leads body). Eyes swap 2 f before the head on looks/turns.
Constants: ANTIC 4, MOVE 4, SETTLE 5, OVER 0.12, LEAD 2, RUN_CYCLE 12, WALK_CYCLE 24.

## Pose units (Char.pose)
arms/legs `(fwd, out, twist)`. Arm forward ~90 → sideways aim/inward is the **twist** (negative = inward across the
body); arm raised >90 → positive `out` brings the hand IN toward the face. head/torso `(yaw, pitch_down, roll)`,
`hipz` hip offset (−1.5 = lying on the ground), `rot` root yaw (0 faces −Y = toward default camera).

## Presets
| call | use for | timing |
|---|---|---|
| `idle(ch, t0, t1, energy)` | ALWAYS, every character on screen. Additive noise: weight shifts, head drift, chest breath 75 f | energy .5 sad, 1, 1.6 nervous |
| `walk(ch, t0, t1, path, mood=)` | normal/happy/sad/sneak/confident; turns at corners, head looks into turns 3 f early | 24 f cycle |
| `run(ch, t0, t1, path)` | 12 f cycle, arms ±60, lean 13°, impact-low/flight-high bob. Legacy `run(ch,t0,t1,p0,p1)` still works | 12 f |
| `skid_stop(ch, t)` | end of a run (t = run end): lean back, slide 1.4 in 10 f, squash, overshoot | 10+6+8 f |
| `run_away(ch, t, path, t1)` | flee: crouch, whip-turn (head first), run, glance back at 40 % | |
| `turn(ch, t, yaw=/target=, expr=, expr_t=)` | eyes → head (3 f) → body, 8 % overshoot; expr on the stressed word | 8 f |
| `dread_turn(ch, t, yaw=, dur=1.6, reveal_t=)` | horror: eyes slide, head creeps, body late, sinks, pop + recoil on reveal | 48 f |
| `look_at(ch, t, target)` | head 75 % / torso 25 % to a Char/object/point, height-correct | 6 f |
| `shock(ch, t)` / `recoil(ch, t, dist)` | REF1 shock: 2 f hold, 4 f snap up, eyes pop on snap, stretch→squash; recoil steps back | 2+4+6 f |
| `gasp(ch, t)` | hand-to-mouth, 'o' mouth, small lean back | 3+3+6 f |
| `point(ch, t, target)` | torso 30 % of aim, head the rest, arm by elevation; holds 0.8 s | |
| `grab(ch, t)` | reach+lean (big anticipation) then pull to chest 10 f later | |
| `hold_phone(ch, t, prop=)` / `read(ch, t, prop=, dur, react=, react_t=)` | phone parented to the fist, head + eyes down, scroll ticks every 12 f, optional reaction preset | |
| `laugh(ch, t0, t1)` | head back 15°, eyes-closed arcs, 4 Hz decaying bounce, hands on belly | |
| `cry(ch, t0, t1)` | hands to face, head down, 3 Hz shudder + sniff jolts | |
| `stomp(ch, t, n)` | fists, knee up 6 f, slam 2 f + squash | 0.4 s apart |
| `shrug(ch, t)` | arms out, shoulders up, head tilt, hold, drop | |
| `nod(ch, t, n)` / `shake(ch, t, n)` | decaying beats | 5-6 Hz |
| `sit(ch, t, seat_h)` / `stand(ch, t)` | look down, lean, lower, settle / lean forward, push, overshoot | 12 f |
| `stumble(ch, t)` / `fall(ch, t, back=)` | trip + recover / lurch, 7 f drop, impact squash, bounce (t = impact) | |
| `embrace(a, b, t)` | a steps in, b opens arms, wrap, squeeze-squash, sway | ~44 f |
| `talk_cadence(ch, t0, t1, words, stress=, expr_on=)` | head bob per word onset, nod + hand beat on stressed words, expression swap on given words, mouth flaps via face system | |
| `emote(ch, t, "sad")` | EMOTION map: happy joy sad angry furious scared shocked smug bored confused love determined embarrassed nervous neutral → expr + body pose + idle energy | |
| `blocking(chars, t, "two"/"two_deep"/"three"/"line"/"triangle", center, spacing, cam_yaw, speaker=)` | stage 2-3 chars, bodies cheat 35° to camera, heads on the speaker | |
| `eyeline(chars, t, speaker)` | re-aim heads when the speaker changes (call on each line) | |
| `squash(ch, t, amt)`, `rest(ch, t)`, `sample(ch, t)`, `hand(ch, arm)`, `attach(ch, prop)` | building blocks | |
`PRESETS[name](ch, t)` gives one-call access (used by `read(react=...)`).

## Habits (match REF1 / craftee)
- One readable silhouette pose per shot, held 0.4-1.2 s, transitions 3-5 f. Never stand still: `idle` on everyone.
- Hit on the stressed word: `mo.shock(ch, V.w(V.find("dead")))`. Expression swap lands there too (the preset does it).
- Listeners react too: `eyeline` to the speaker + a small `nod` or `emote(..., strength=0.5)`.
- Locomotion: walk = calm, run = 12 f, always end runs with `skid_stop` or a `turn`.
- Legacy `act(t, gesture)` now routes through `strike` (3 f anticipation); `act(..., antic=0)` is the old pop.
- Props parented with `attach` stay in the hand for the rest of the shot (each shot is its own scene).

## v3.1 (2026-11-14): joints, IK reach, key poses, camera-aware blocking

**Rig.** Every cast member now has ELBOWS and KNEES (`ch.joints`). Limb blocks are cut at the joint (upper piece
overlaps 0.14 so there is no seam); straight limbs keep the exact R6 silhouette. `Char.pose()` takes
`elbowL/elbowR/kneeL/kneeR` = flex in degrees (+ = natural bend). `motion.sample/strike/rest/idle` know them, walk/run
cycles flex knees and elbows. Old calls work unchanged.

**Hands must reach things.** Never mime in the air:
- `mo.reach(ch, t, target, hand="r", body={...})` - two-bone IK; the fist LANDS on target (object, Char, point) at
  t+settle; `body` (torso/hipz/head) is solved together so lean + reach agree. `reach_pose(...)` returns the dict to mix.
- `mo.contact(ch, t0, t1, target, hand, wobble=0.05)` - keeps the fist on a moving target (re-solves every 3 f);
  wobble = fiddly hand work (buttoning, adjusting).
- presets: `present_cuff(harry, t, "armL", toward=mom, cam=cam)` (v3.3 FK "show me your watch": upper arm hangs on
  the torso, elbow 88, forearm level at belly height, whole arm swung toward the partner by the shoulder twist (max
  45); chest twisted back to within 25 deg of the lens; head upright, yaw to the cuff, pitch 12), then
  `button_cuff(mom, t, harry, "armL", cam=cam)` (world-space solve of BOTH characters: reads Harry's posed cuff
  point `mo.cuff_point(harry, "armL")`, turns Mom toward it cheated 0.4 to camera, places her so the cuff sits at her
  right-hand WORK point out in front-right of her body (never in front of her own chest), right fist on top of the cuff
  (fist on the lens-side/top face of the forearm, surface gap < 0.2), left arm relaxed; `ch._contact` = measured
  (max, mean) surface gap, RBX_DEBUG=1 prints it),
  `tug_sleeve(ch, t)` (fists OVERLAP at the body midline - centres 0.84 apart, hip-local z ~1.2, a clasped grip), `hand_to_face(ch, t, "r",
  "chin"|"mouth"|"forehead"|"cheek")`, `lean_on(ch, t, wall_point, "r")` (hand flat on wall, feet planted, ankle crossed,
  free hand in pocket), `hold_phone_ik(ch, t, prop=phone)`. Registry: PRESETS phone/tug_sleeve/hand_to_face/think/
  sad_slump/confident/arms_crossed.

**R6 reach envelope (read before writing any IK target).** Shoulders sit 1.5 studs off the midline, the arm is 1.55
long, the torso is 2 wide. So: two fists can only TOUCH at the midline at belly/low-chest height (hip-local z 0.85-1.0)
with near-straight arms; a fist cannot cross the midline (no true crossed arms); a fist under the chin lands ~0.55 to
its own side. `mo.solve_arm` now runs every target through `mo.reachable(arm, p)`: height and depth are kept and the
target slides toward the arm's own side until it is reachable, and fists are pushed out of the torso. Before v3.2 an
out-of-reach target straightened the arm toward it and the fist landed in mid-air (wings, Mom's hands at her chin in
s04, tug_sleeve hands that never met). FK arm "out" values in POSES are the hang relative to GRAVITY: key_pose_dict
cancels the hip roll so contrapposto never lifts an arm into a wing.

**Key poses** (`mo.POSES`, `mo.key_pose(ch, t, name, expr=, mirror=)`, `mo.stance(ch, t, name)` = instant): stand,
relaxed, confident, hands_hips, sad_slump, thinking, arms_crossed, shy, excited, point. All asymmetric, weight on one
leg (hip roll + legs compensated so feet stay planted, free knee flexed), head tilt, soft elbows. Every cast member is
built in `stand` (mirrored per name) - never a T/I-pose. Read-at-a-glance test: squint at the still; if the beat
(button / tug / lean / phone) is not obvious from the silhouette, push the pose further or turn the body.

**Camera-facing blocking** (`mo.stage(chars, t, cam, bias=0.25-0.5)`): call AFTER the camera exists. Each body turns
3/4: blend of facing the lens and facing the partner (bias 0 = full front, 1 = profile); heads then take the eyeline.
Rules for two-shots:
1. The character whose HANDS do the beat stands on the far side of the action (as seen from camera) and faces it 3/4
   to lens (button_cuff(cam=...) does this). The receiving character is 3/4 front (bias ~0.25), presenting the prop /
   cuff toward the partner, below chin height.
2. Never put a raised arm between lens and a face: in MCUs keep gestures below the chest line (talk_cadence(
   hands=False) or a key pose) - a near-lens forearm at f/2 becomes a big blurred block.
3. Hand contact must be visible: the contact point sits in the frame centre third, not behind a body.
4. Backs to camera are only for OTS shots.

**Character light rig.** `cast.light_rig(chars, cam, look=...)`: key / fill / rim / top / bounce, light-LINKED to the
characters only (no wedges on walls), placed from the camera and the framed heads, strength per look (`cast.LOOK_RIG`).
`shotkit` calls `cast.auto_light()` after every shot containing a cast member unless the shot already called
`cast.cine_light` (lights named `cl_*`) or set `cast.AUTO_LIGHT = False` (or `V.auto_char_light = False` for a video).

## v3.2 (R3, 2026-11-14): no wings, faces that change, presented cuffs
- Hanging arms: REST/POSES hang slightly IN (out -2..-3); `mo.clamp_hang(pose)` keeps any hanging FK arm in out -6..+3.
  Never write `armX=(0, 4+)` for a resting arm - that is the A-pose wing.
- `talk_cadence` now acts the face by itself: opening look, swap on every stressed word (or the longest word), settle,
  eye dart; `mood=` picks the TALK_ARC row (default = current eyes), `faces=False` / `sway=False` to opt out.
  hands=False = low belly-height gesture beat (MCU safe), hands=True = chest-height beat.
- `present_cuff(ch, t, arm, toward=partner, cam=cam)` presents into the gap between the bodies; `button_cuff` does it for
  you (present=True) and stores the measured span contact in `ch._contact` (max, mean).
- `tug_sleeve`: fists meet face to face at the midline at belly height (only place R6 allows), elbows tucked.
- `lean_on`: hand clamps to shoulder height, free fist in its own hip pocket.
- Blinks follow expression swaps (no more blink undoing a face).

## v3.3 (R4, 2026-11-14): readable heads, no forearm blocks, warm faces, real cuff contact
- **Readable-head clamp** (`acting.clamp_head`, applied to EVERY keyed head pose): pitch -20..+16 (down), roll +-10.
  A cylinder head pitched further down shows the top of its hair; a roll > 10 reads as a broken neck. Drive eyelines
  with yaw and the eye cells ("down", "side_l/r"). `ch.head_free = True` opts out (falls, gags).
- **Straight resting arms**: REST elbows 5, stance elbows <= 14. A flexed elbow throws the forearm forward; from a low
  MCU lens that is the "horizontal block / wing" next to the torso.
- `talk_cadence` v3.3: mood also read from the MOUTH (dot eyes + smile mouth = smile line), smile lines flap through
  smile shapes (`TALK_MOUTH`), the stressed word holds its face for the whole word (talk() no longer flaps over it),
  words ending in ?/! count as stressed, contrapposto per phrase (torso roll + yaw, legs counter-rotate, free knee),
  head counter-tilt 6-9 deg, hands=False beat = forearm lifts UP beside the chest, upper arm on the torso (never a forearm at the lens).
- `present_cuff`/`button_cuff` rebuilt (see presets above): presenter's upper arm abduction <= 10, chest 3/4 to lens.

## v3.7 (2026-11-14): natural faces cheat sheet (REF_IG_Dfs43n3oWqx FACIAL EXPRESSION SPEC) - UNRENDERED
Data/parameter additions only; nothing here has been rendered yet. Test without Blender: `python -I tools/face_dryrun.py`.
- New eye cells: `half_up closed_happy dots ring worried_l worried_r tear1` (EYE 16-22). New mouth cells: `dash o_small cat_w
  wavy_side frown_wobble grin_top grin_full scream_tongue` (MOUTH 16-23). They need a 5x5 atlas: add
  `assets/faces/<style>_<layer>.json` = `{"grid": 5}` next to the regenerated PNG. Without it the atlas is the old 4x4 and
  every new name FALLS BACK (`acting.EYE_FALLBACK` / `MOUTH_FALLBACK`: ring->wide, tear1->cry, worried_l->side_l, dots->normal,
  scream_tongue->scream, grin_top->open_smile, cat_w->smile, wavy_side->smirk, frown_wobble->wavy, dash->flat, o_small->o).
- New EXPR: `blank`(dots,dash) face-erased gag, `pop_shock`(ring,o_small), `sad_tear`(tear1,flat) 1.5-2 s on a push-in, no blink,
  `worried_dart`(worried,frown_wobble), `smug_up`(half_up,wavy_side), `content`(closed_happy,cat_w), `laugh_smug`, `toothy`,
  `angry_shout`; cast aliases `tear`, `erased`, `dart`.
- `ch.ladder(t, exprs="surprise_laugh", step=7/30, hold_last=None) -> t_end`: reaction ladder, HARD swaps 6-8 f each
  (presets `acting.LADDERS`: surprise_laugh smug->pop_shock->toothy->pop_shock, surprise_scream, anger_to_worry). Put t on the
  beat word / SFX frame; cut at t_end. Blinks inside the window are removed.
- `ch.dart(t0, t1, every=4.5/30, seed=None, mouth="frown_wobble") -> plan`: fear-hold eye darts, pupils jump L/R every 4-5 f,
  3-5 per burst, rest centre 6-8 f. Pure plan: `acting.dart_plan(t0, t1, ...)`.
- `ch.blink(t0, t1, every=(2.5, 4.0), closed=3/30)`: default interval was 1.8-3.6 s; skips ladder/dart windows. Pure plan:
  `acting.blink_schedule(t0, t1, every, closed, skip, seed)`.
- `acting.resolve_cell(layer, name, grid)`, `acting.atlas_grid(style, layer)`: name -> atlas index with fallback.
- Rules: swaps are 0-frame decal cuts aligned to caption word onsets; ~50 % of expression changes hide in a cut (open the next
  shot on the new face); anger hold 9-12 f then hard swap to worried; small 5-10 deg head tilt with a swap; NEVER `talk()` the
  narrator-POV character during VO (one mouth per beat; only a quoted line gets 1-2 mouth swaps: flat <-> o_small <-> grin_top).
- Per-format expression sets: `cast.FACE_SET` / docs/FORMATS.json `expressions`.
