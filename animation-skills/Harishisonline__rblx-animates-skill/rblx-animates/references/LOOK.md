# Look: lighting, grade, environments (rbx/look.py)

v1 frames looked flat because everything used one flat sky + one sun and no grade. The references all use the same
four ingredients. v2 builds them in:

1. **Warm/cool contrast.** Key light warm (or cyan for neon) from the camera side, cool/colour rim from behind, fill low.
2. **A rim light** that outlines the subject so it separates from the background (cheap, huge effect).
3. **Depth of field.** Every camera recipe sets `fstop` (2.0-3.5 on people, 5-8 on wides) and focuses the subject.
4. **Bloom + grade.** Compositor: Glare(bloom) -> saturation/contrast -> split tone (cool shadows, warm lights). Applied to every
   shot automatically at the end of `Video.build` using `V.look` (v3.6+ default "ref_matte": neutral matte, NOT blue;
   day exteriors "ref_day", night "ref_night", lamp-lit rooms "ref_practical"; all UNRENDERED until a look-dev pack passes
   `tools/grade_check.py --format <name>`). Per-format look: docs/FORMATS.json. Old presets below stay selectable.

```python
V = Video(__file__); V.look = "neon"          # grade for the whole video: day dusk night interior neon horror
look.rig("night", focus=(0, -28, 4), cam_yaw=0)   # lights one shot (key + fill + rim + sun), see PRESETS in look.py
look.fog(0.008)                                # light atmosphere under spotlights / sun
look.hdri("dresden_station_night_1k.hdr")      # real reflections/ambient (assets/hdri, fetched by tools/assets.py)
```
Choosing: day = playful/comedy, dusk = emotional, night = secrets/tension, interior = warm lamp rooms, neon = AI/cyberpunk,
horror = dark with one warm practical light. Mix per scene by calling `look.rig(<other preset>)` in that shot, but keep
one grade per video so the cuts feel like one film.

## Environment rules
- Never re-use one landmark in every location. Each location needs its own 6-10 distinct props (shelves, signs, lamps).
- Fill the sky and floor: gradient sky + clouds (day), emissive windows/lane strips (neon), contact shadows under props.
- `P.ai_city()` is the sci-fi city; `W.town()` the school town; `W.classroom_day()`; `sets.bedroom()`; `W2.cabin()`, etc.
- Keep faces readable: if a face is dark, add a small warm/cool point light in front (see the hideout shot in videos/ai_lookdev).
- Windows: use `P.lit_building_mat` (grid + per-cell random mask). Never use a noise texture directly for windows (it grains).

## Exposure checklist (every contact sheet)
Faces visible; background not pure black; skin never green/purple (balance key colour: use warm-ish fills, saturation <= 1.25);
nothing blown out; bloom only on lights/screens.

## v2.1 sci-fi sets (rbx/aiworld.py)
`A.street()`, `A.hideout()`, `A.core_hall()`, `A.core_room()` each bring their own practical lights and 6-10 prop types.
Use `A.face_light(head_pos)` on any close/medium shot where the face is dark, `look.exposure(0.3)` for a per-shot lift,
and `A.wrist_macro()` + `cams.macro()` for readable small-object inserts. Worked example: `videos/ai_world/shots.py`.
