# TEAM_AGENTS: making one episode with several agents in parallel (used on EP3, 2026-11-16)

Use this when a single agent would spend hours on shots (60+ shots, 100 s of video). On EP3 three Opus agents took
about 3 hours wall time and brought the low-res QA flags from 280 to 31 accepted ones. One agent writing everything in
order was the bottleneck; splitting by file ownership removed it without anyone overwriting anyone.

## Roles
| Agent | Owns (only this agent edits it) | Job |
|---|---|---|
| MANAGER (QA lead) | `shots.py` (shared helpers above the SHOT PARTS loader), kit files (`rbx/*`, `tools/*`), final verdict | triage flags by root cause, fix shared causes, send numbered issues, verify fixes, approve parts, render look-dev, write `out/QA_REPORT.md` |
| BLENDER A | `shots_a.py` (first half of the shots) | fix every flag in its range, readable inserts, contact, acting; post "PART A READY" |
| BLENDER B | `shots_b.py` (second half) | same for its range |
| NON-BLENDER (optional) | `audio/`, `sfx/`, `tools/ep_audio`, captions/end-card tools, docs | audio QA by measurement, captions/end-card tests, episode files, docs |

`shots.py` keeps imports, `V = Video(...)`, cast and set helpers, then execs the parts:
```python
_HERE = os.path.dirname(os.path.abspath(__file__))
for _part in ("shots_a.py", "shots_b.py"):
    _p = os.path.join(_HERE, _part)
    exec(compile(open(_p).read(), _p, "exec"), globals())
```
`tools/ep_final.sh` counts `@S(` across `shots.py` and `shots_[a-z].py`. `tools/ep_lo.py` writes to `$RBX_LO_LOG`
(e.g. `render_lo_A.log`) so the two low-res passes don't interleave; frame ranges never overlap.

## Protocol
- `BRIEF.md` (read first): episode, paths, what is done, hard rules, the owner's mistake list, cast.
- `BOARD.md`: append-only, `HH:MM | AGENT | DOING/DONE/BLOCKED | details`. Read before every step, append after it.
- `INBOX_A.md`, `INBOX_B.md`: Manager -> worker, numbered issues (shot, time, what is wrong, what good looks like,
  which kit tool fixes it). Worker marks `DONE hh:mm (what changed)`; Manager marks `VERIFIED` or `REOPENED: why`.
- `INBOX_MANAGER.md`: worker -> Manager (shared helper or kit change requests, "PART X READY").
- Workers never edit a file they do not own; new helpers go in their own part with an `a_` / `b_` prefix.
- Every kit change is backed up (`name.bak_mgr`) and announced on BOARD because it changes both halves; after it, re-run a
  quick import test (load shots.py in Blender: shot count right, `V.check()` empty).
- Nobody runs the final render. The person approves look-dev first.
- Workers poll their inbox (sleep 120 s between checks) until "APPROVED A/B" or "ALL APPROVED - STOP", with a time cap.

## What the Manager judges (beyond flags)
The owner's real complaints: levitating, characters cut off, objects floating instead of held, unreadable props, laughing
kids looking away or "dancing", glitching instead of kneeling, key actions not visible, fake screens. A flag can be
acceptable (a POV phone shot hides the holder's head on purpose); a main character cut off never is. Check continuity
across the A/B cut and that each shot shows what the narrator says at that moment.

## Lessons from EP3
- Image staging can break mid-run (expired desktop sign-in): agents then judge by logs and pixel stats only. Re-check the
  final contact sheet yourself before delivery.
- A worker may change a shot after its look-dev still was made: re-render that still before showing the person.
- Each agent costs real tokens (EP3: about 1.8 M across four agents). Use one Blender agent + Manager for short episodes.
