---
name: short
description: Turn a one-line idea into a finished vertical Roblox story Short (single narrator, Three.js render) - writes stories/<slug>/story.json, lints, previews once, renders, and fills the publish package (SEO title, description, tags, caption). Use when the user gives a video idea ("in this town...", "what if...") or asks to make, remake or continue a Short.
---

# /short: idea -> video

Follow AGENTS.md (already the full guide: workflow, compact notation, vocabulary). Nothing else needs to be read.

1. Pick `genre` (in_this_world = viral long story, default for emotional/family ideas | in_this_town | what_if) and a slug. Copy `stories/_template_world/story.json` for in_this_world (read `config/formats/in_this_world/FORMAT.md` first), else `stories/_template/story.json`.
2. Write the story in compact notation with cast and loc presets; fill `publish`. If a scene needs something that doesn't exist (object, animation, face, asset), do not substitute: download or create it per "Creative fidelity" in AGENTS.md. Never use a solid block/untextured primitive as an object: source a low-poly but detailed model (Roblox Creator Store > web/kits > Blender as last resort), see "Visual quality of models" in AGENTS.md.
3. `--lint` until `lint: OK` -> `--preview` once, look at preview.jpg -> fix -> `--preview --only <scenes>` if needed.
4. Full render in the background. Report in 3-4 lines. Continuation only if asked: new slug `<slug>_p2`, one-line recap first.
