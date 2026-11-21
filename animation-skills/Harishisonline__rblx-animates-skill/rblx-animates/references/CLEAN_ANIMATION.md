# CLEAN ANIMATION: rules every shot must pass (v4.0, 2026-11-15)

Sources:
- the user's frame-by-frame QA of EP2 v1/v2 (wrong shoe, letter, signs, pencil, books, levitating chair);
- craftee_films reels studied frame by frame on 2026-11-15 (Dfu0GKLh60_ 917K views, DfuNAV7ukVC);
- body-mechanics and staging basics (cursa.app body-mechanics and beginner-mistakes chapters; prolificstudio staging).

## 1. Design shots the kit can do cleanly (the craftee method)
Craftee almost never shows complex physical choreography in one continuous wide. A story beat is told as a CUT
SEQUENCE of simple shots, about 1-2.5 s each, one per key word:
1. **Establishing wide** of the place, held 1-2 s (house, street, gym, crowd). No acting needed.
2. **Single MCU/medium reaction**: ONE character, centred or on a third, facing the lens or 3/4 to it, clear
   expression, a small gesture. This is about 60 % of all shots.
3. **OTS / dirty single**: the partner's head and shoulder blurred in the foreground and the speaker facing the lens.
   This replaces a two-shot "both in profile".
4. **Prop insert (ECU)**: the object ALONE or in one giant foreground hand, very shallow DOF (polaroid, door knob,
   cup, wristband). Every story-critical object gets an insert. Never rely on a wide to show a small object.
5. **Aftermath instead of physics**: show the result (cup lying on the floor, books spread out) and the reaction.
   If an object must fly, it gets its own low insert with real gravity, 0.3-0.6 s.
6. **Seated = framed chest-up behind the table.** The chair and legs are never shown. The table top sits at chest
   height in frame.
=> A "Ryan slaps the books" beat is: Ryan MCU swipe at the lens -> low insert, books hit the floor -> Harry MCU shock.
   NOT one wide where everything has to line up.

## 2. Contact (most visible errors)
- **Feet on the ground** (or on the seat while sitting). No hovering, no sinking. QA flag `FLOAT`: lowest foot point
  more than 0.15 above the surface under it, or more than 0.15 below it.
- **Hands touch what they use.** Keyboard, door, tray, books, shoulder: use `mo.reach`/`mo.contact`, never a pose
  guess. QA flag `NOTOUCH`: a declared contact with fist-to-target over 0.35.
- **Props are gripped, not glued.** A prop rides the fist (`mo.attach` / `rig.grip`), points the way the forearm
  points, and NEVER passes through a body. QA flag `CLIP`: a prop mesh intersects a character mesh.
- **Sitting:** the seat top is at the hips (Roblox seat 1.5), the knees are forward, the feet are on the floor, and
  the desk top is below the chest (2.6-2.9 for a seat of 1.5). Use `mo.sit(ch, t, seat_h)` on a real chair model.

## 3. Eyelines and acting
- Every character looks AT what they react to (the target's face, or the object). Use `mo.look_at` / `mo.eyeline` /
  `mo.stage(chars, t, cam)`. QA flag `EYELINE`: head forward more than 35 deg off the declared target.
- Pointing and laughing: arm aimed at the target, head toward the target, then the head turns to the lens or the
  partner on the laugh.
- Faces carry the beat. A single MCU with a clear expression change beats a wide with tiny faces.
- Backs to camera only for walk-aways and crowds (QA `AWAY`).

## 4. Physics and timing
- Falling objects: gravity (32 studs/s^2), a tumble in flight, land flat, one small bounce, slide, settle. Start on
  the hit frame; the body commits before the object moves.
- Keys: anticipation, hit, settle. Holds use a moving hold (`idle`). No linear motion except mechanical things.

## 5. Readability
- Text (signs, letters, screens) must fit its board (`signs.fit_text`) and be filmed straight on in an insert.
- Ink colours survive the matte grade (dark red #7a0000, not #c62828).
- One idea per shot. Silhouette test: pause on any frame; a new viewer must know what is happening.

## 6. Cameras
- Aim from the subject's FACE direction (`face_yaw`), never a guessed absolute yaw.
- Cameras need line of sight AND free space (`safe_pos` + `_clear`), and must stay inside rooms.
- 9:16 is narrow: two people side by side only in a wide; otherwise use OTS or singles.

## 7. QA gate (automatic + eyes)
`render_lo.py` logs BLOCKED, AWAY, FLOAT, CLIP, NOTOUCH and EYELINE. A shot is not shown to the user until:
(a) the log is clean, or every remaining flag is explained in the shot desc;
(b) a 2-fps contact sheet of the shot has been LOOKED at against sections 1-5;
(c) the story beat reads with the sound off.

## 8. CLEAN LOOK (v4.0): the user's look references are crisp, not matte
References: instagram.com/p/Dfe8B5Hs3G6 (night/interior, @kyreblx) and instagram.com/p/Dfs43n3oWqx (day).
- **Crisp plastic.** Smooth surfaces with no grain, noise or fabric weave. `cast.CLEAN = True` (default) drops the cine
  micro-normal bumps.
- **Real shadows and natural colour.** `look.STYLE = "clean"` (default) removes the black lift, distance haze and
  desaturation, uses AgX Medium High Contrast, a light vignette and tiny bloom. The old matte look is `look.STYLE = "matte"`.
- **Day exteriors:** saturated blue sky, sunlit and green. Night/interiors: one warm or screen practical key with dark
  surroundings, kept clean (no fog).
- **Never judge the look from render_lo** (34 %, 6 samples). Look-dev = `tools/render.py <slug> still:T <shot> 24` on 5-6
  shots (MCU interior, desk, exterior day, wide, insert), tiled next to reference frames.
- **Finals** are 1080x1920 with 32 samples and full-res raytracing. Instagram re-encodes, so anything soft at 1080 looks
  like 360p.

## 9. Contact by construction (v4.0)
- When a hand must rest ON a prop (keyboard, table, door handle), first pose the hand with IK to a REACHABLE point,
  MEASURE the fist, then build or move the prop under it (`fit_desk_to_hands`). Never place the prop first and hope the
  R6 arm reaches it.
- Read a fist position only after `bpy.context.view_layer.update()`. mo.hand creates the empty lazily, and a fresh empty
  reports the world origin.
- `mo.sit` keys the arms at t+6 f: sit BEFORE the shot (t0 - 0.7) and pose the arms after it.
- Vehicles: characters start OUTSIDE the body next to an opened door (`car_door` + `appear`). Nobody walks out of a
  closed car.

## 10. POST-MORTEM of the POSTED EP2 (user review 2026-11-15): the 4 repeat failures and the fixes now in the kit (v4.1)
| failure the user saw | root cause | kit fix (v4.1) | automatic check |
|---|---|---|---|
| 0:03: Harry stands in the air beside the road before the car arrives | `appear()` was overridden by the cast's own visibility keys; the exit was staged as one continuous shot | `appear()` keys over the cast keys. **VEHICLE rule:** a 3-cut sequence: (A) car arrives, stops, door opens, NO character built in that shot; (B) low insert of the hero's shoe stepping down beside the open door; (C) hero standing beside the door | FLOAT |
| 0:10-0:14, 1:21: Harry, Ryan and his dad cut in half by the frame edge | still_cam positions were guessed per shot; nothing checked that the subjects were in frame | **`frame_on(chars, t0, t1, shot)`** solves the camera so every subject's head (with headroom) and body down to the shot size (mcu/med/cowboy/full) is inside 9:16 with a margin. It uses the real camera FOV (core.Cam: sensor_fit VERTICAL, 24 mm) and swings around walls. Use it for EVERY character shot; still_cam only for inserts and sets | **CUTOFF** (declared subject's head or torso outside), **HALF** (any character's head sliced by the edge), **TINY** (subject head < 6 % of frame height) |
| 0:12 books "in the air", 0:33 pizza box unreadable and held wrong, 0:38 typing on a white slab, pencil/shoe weak | props were plain boxes placed near the hands; the prop was narrower than the fist gap, so the hands never touched it | **`rbx/props3.py`** props that read at phone size (pizza box with lid + logo, book stack with page blocks + spines, keyboard with keycaps, laptop with keyboard + UI screen, tray with food), each with GRIP points. **`hold(ch, prop, t0, t1)`** IKs the fists to the grips and rides the prop on the MEASURED fists every frame ('sides' for books/tray, 'under' for pizza/cake) | NOTOUCH on both grips (auto), CLIP, **PROPFLOAT** (`qa.rest(ob)`: unheld props must sit on a surface; `drop()` registers it automatically) |
| 0:19 kids look away and "dance"; 0:24 Harry "glitches" instead of kneeling | `mo.laugh` reset head yaw to 0 and bounced the hips at 4 Hz; kneel = an 8-frame strike with 12 % overshoot and hipz -1.25 (legs through the floor) | **`belly_laugh / crowd_laugh(chars, t0, t1, target)`**: body turned to the target BEFORE the shot, eyes ON the target all shot, point first, then fist to belly, head back 10 deg, small 2.4 Hz shoulder shake. **`kneel_down(ch, t)`**: weight shift, lower, knee lands at hipz -0.62 with correct leg mechanics, no overshoot. Big transitions are best hidden in the cut (start the shot in the pose; `KNEEL_POSE`) | EYELINE (auto), FLOAT |
| 0:34 laptop fix not visible; 0:38 "the game" was plain numbers | no insert of the object being worked on; screens showed text only | **`game_screen()`**: a monitor that shows a real game (a lit mini 3D school assembling brick by brick + avatars + UI bar). `props3.laptop()` with readable UI. Rule: every "X is doing something with an object" beat = MCU of the face + INSERT of the hands on the object + INSERT of the screen/result | eyes on the contact sheet |

## 11. Object interaction checklist (every shot where a character touches or holds something)
1. The prop comes from `props3` (or is built with the same standard: identifying details plus GRIP points).
2. Hold with `hold()`, sit and type with `seat_and_type()` + a visible `props3.keyboard`, and drop with `drop()`. Never place a prop
   "near the hands".
3. An insert shows the hands on the object at least once per interaction beat.
4. QA log: no NOTOUCH, CLIP or PROPFLOAT.

## 12. Framing checklist
1. Every character shot uses `frame_on([...], t0, t1, "mcu|med|cowboy|full")`. Two people talking: cowboy two-shot, or OTS + singles.
2. The subject whose line it is must be fully in frame: no HALF or CUTOFF on that character, ever.
3. 9:16 is narrow. More than 2 people in a medium shot = a wide; otherwise cut to singles.

## 13. Body animation checklist
1. No big pose change inside a short shot unless a preset exists (`kneel_down`, `mo.sit`, `mo.turn`, `mo.walk`). Otherwise start the shot in the pose.
2. Reactions face the subject: `belly_laugh`, `mo.look_at`, `mo.turn` BEFORE t0; EYELINE is clean.
3. Look at every reaction shot at 2 fps: if a pose reads as "dancing" or "glitching", replace it with a preset or a held pose.

## 14. Regression test (run after ANY kit change)
`~/RobloxStories_tmp/shotlib_test` (`Blender -b --factory-startup -P test.py`) covers six shots: books hold, pizza two-shot, kneel, crowd laugh, desk + keyboard, game screen.
Expected: no CUTOFF/HALF, no NOTOUCH, no CLIP; LOOK at out/test_strip.
