"""poor_boy_school - EP2 Blox City "The Poor Boy Who Bought the School".
Alex alex_ep1 narration (audio/voice.wav, 104.7 s, words.json from ElevenLabs alignment). Built 2026-11-15 with gates
waived by the user ('just start making the video, we will review it and learn').
Cast: Harry = cast host in a faded GREY HOODIE (recoloured, H patch hidden); Ryan = cast bestie recoloured red/black;
Milo = small chars.kid; principal = cast grandma (Pearl); Ryan's dad = cast mayor; Grandpa = grandpa.
Sets: town school_hallway / school_exterior (sign -> BLOX CITY HIGH) / main_street / bedroom(night) / kitchen(day),
custom auditorium (room + stage + podium + crowd extras). Music is NOT in the film (added in Instagram)."""
from shotkit import *
from rbx import story
from rbx.story import *
from rbx import cast, town as T, motion as mo, signs as SG, crowd as C, chars, pbr
from rbx.core import Cam, orbit_pos, box, cyl, mat, hexc, light, collection
from rbx import cams
from rbx import qa


def _curb_z(x, y):
    """Top of a low surface (sidewalk / curb / step, 0.05-0.6 high) under (x, y); 0 if none. CLEAN_ANIMATION 2: feet on it."""
    sc = bpy.context.scene; bpy.context.view_layer.update(); dg = bpy.context.evaluated_depsgraph_get()
    hit, loc, n, i, ob, m = sc.ray_cast(dg, Vector((x, y, 0.9)), Vector((0, 0, -1)), distance=1.0)
    return loc.z if hit and 0.05 <= loc.z <= 0.6 else 0.0


_cast_make = cast.make


def _make_snapped(role, t0, t1, *a, **kw):
    loc = kw.get("loc")
    if loc is not None and abs(loc[2]) < 1e-6:
        kw["loc"] = (loc[0], loc[1], _curb_z(loc[0], loc[1]))
    return _cast_make(role, t0, t1, *a, **kw)


cast.make = _make_snapped
_mo_walk = mo.walk


def _walk_snapped(ch, t0, t1, path, *a, **kw):
    path = [(p[0], p[1], _curb_z(p[0], p[1]) if abs(p[2]) < 1e-6 else p[2]) for p in path]
    return _mo_walk(ch, t0, t1, path, *a, **kw)


mo.walk = _walk_snapped
import bpy, math, os
from mathutils import Vector
V = Video(__file__); story.bind(V)
V.look = "ref_matte"
V.end = math.ceil((V.words[-1]["end"] + 0.6) * 30) / 30

HX, HY = T.ORIGINS["school_hallway"][:2]
EX, EY = T.ORIGINS["school_exterior"][:2]
AUD = (800.0, 0.0, 0.0)


# ------------------------------------------------------------------ helpers
def head(ch, t, dz=0.55):
    bpy.context.scene.frame_set(F(t))
    return tuple(ch.head.matrix_world.translation + Vector((0, 0, dz)))


def mcu_live(t0, t1, face, d=11, lens=50, yaw=20, arc=10, push=0.16, eyes=0.36, side=1, third=0.36, fstop=1.4, pitch=-7):
    c = cams._cine(Cam())
    c.cd.lens = lens
    f = Vector(face)
    hy = math.tan(c.cd.angle_y / 2) if c.cd.sensor_fit != "HORIZONTAL" else math.tan(c.cd.angle / 2) * 16 / 9
    hx = hy * 9 / 16
    k = min(0.30, push * max(0.0, t1 - t0))
    for tt, dd, yy, ez in ((t0, d, yaw - arc / 2, None), (t1, d * (1 - k), yaw + arc / 2, "EASE_IN_OUT")):
        p = Vector(orbit_pos(f, dd, yy, pitch))
        fwd = (f - p).normalized()
        right = fwd.cross(Vector((0, 0, 1))).normalized()
        aimp = f + right * (side * dd * hx * 2 * (0.5 - third)) - Vector((0, 0, dd * hy * 2 * (0.5 - eyes)))
        c.key(tt, tuple(p), tuple(aimp), lens=lens, focus=tuple(f), fstop=fstop, ease=ez)
    return cams.micro(c, deg=0.8, loc=0.045, period=1.7)


def mcu(t0, t1, ch, rot, label, off=30, d=7.4, eyes=0.42, side=1, push=0.06, arc=8, fstop=1.6, zone=0.2, pitch=3):
    return scam(t0, t1, head(ch, t0, -0.15), yaw=face_yaw(ch, t0 + 0.3) + side * 15, dist=d, pitch=pitch, lens=55, push=push, fstop=fstop,
                ignore=(ch.name,), name="Cam_mcu")


def still_cam(t0, t1, loc, tgt, lens=35, push=0.08, fstop=4.0, focus=None, name="Cam"):
    c = Cam(name, lens)
    lv, tv = Vector(loc), Vector(tgt)
    c.key(t0, tuple(lv), tuple(tv), lens, focus=tuple(focus or tv), fstop=fstop)
    c.key(t1, tuple(lv + (tv - lv) * push), tuple(tv), lens, focus=tuple(focus or tv), fstop=fstop, ease="EASE_IN_OUT")
    cams.micro(c, deg=0.4, loc=0.02, period=2.2)
    return c


def recolor(ch, mapping):
    """Recolour costume materials whose name contains a key (cine copies included)."""
    seen = set()
    for ob in ch.coll.all_objects:
        for sl in getattr(ob, "material_slots", []):
            m = sl.material
            if not m or m.name in seen:
                continue
            for k, hx in mapping.items():
                if k in m.name:
                    seen.add(m.name)
                    c = hexc(hx)
                    if m.use_nodes:
                        for n in m.node_tree.nodes:
                            if n.type == "BSDF_PRINCIPLED":
                                n.inputs["Base Color"].default_value = (*c[:3], 1)
                            elif n.type == "RGB":
                                n.outputs[0].default_value = (*c[:3], 1)
                    m.diffuse_color = (*c[:3], 1)


def harry(t0, t1, expr="neutral", loc=(0, 0, 0), rot=0):
    h = cast.make("host", t0, t1, expr, loc=loc, rot=rot, cine=True)
    recolor(h, {"harry_jacket": "#5d6168", "harry_cream": "#767a82", "harry_rib": "#4a4d53", "harry_snap": "#767a82"})
    for ob in h.coll.all_objects:
        if "patch" in ob.name:
            ob.hide_render = True; ob.hide_viewport = True
    return h


def ryan(t0, t1, expr="smirk", loc=(0, 0, 0), rot=0):
    r = cast.make("bestie", t0, t1, expr, loc=loc, rot=rot, prop=False, cine=True, name="Ryan")
    recolor(r, {"ty_navy": "#b3242b", "ty_roll": "#2b2b30", "ty_pull": "#f2c14e"})
    return r


def extra(name, t0, t1, expr="neutral", loc=(0, 0, 0), rot=0, shirt="#5aa0e0", pants="#2d3550", hair="short",
          hair_color="#2a1d16", skin="#f1d2b0", scale=1.0, face="kid"):
    """Background classmate built like the cast (hands, elbows/knees, stance, blinking face, cinematic finish)."""
    ch = chars.Char(name, skin=skin, shirt=shirt, pants=pants, hair=hair, hair_color=hair_color, face=face,
                    sleeves="short", scale=scale, seed=sum(map(ord, name)))
    cast._finish(ch, t0, t1, expr, loc, rot, True, True, "#888888")
    try:
        cast.cine_finish(ch)
    except Exception as e:
        print("extra cine", e)
    return ch


def milo(t0, t1, expr="worried", loc=(0, 0, 0), rot=0):
    return extra("Milo", t0, t1, expr, loc, rot, shirt="#f2c14e", pants="#3a5f9a", hair="messy", hair_color="#6b3a1e",
                 scale=0.78)


KIDS = [dict(shirt="#5aa0e0", hair="short", hair_color="#2a1d16"), dict(shirt="#9b59b6", hair="bob", hair_color="#9a6a4a", face="girl"),
        dict(shirt="#2ecc71", hair="messy", hair_color="#e0c060"), dict(shirt="#e67e22", hair="slick", hair_color="#151212"),
        dict(shirt="#e74c3c", hair="short", hair_color="#6b3a1e", skin="#c68c5a")]


def kid(k, t0, t1, expr="joy", loc=(0, 0, 0), rot=0):
    return extra(f"Kid{k}", t0, t1, expr, loc, rot, **KIDS[k % len(KIDS)])


def laughers(t0, t1, target, spots, start=0.0):
    """Classmates who POINT at target, then laugh (head back, belly bounce), staggered."""
    ks = []
    for k, (x, y, r) in enumerate(spots):
        c = kid(k, t0, t1, "toothy", loc=(x, y, 0), rot=r)
        mo.idle(c, t0, t1, 1.2)
        tp = t0 + start + 0.15 * k
        mo.point(c, tp, target, arm="armR" if k % 2 == 0 else "armL", hold=0.6, expr="laugh_smug")
        mo.laugh(c, tp + 0.7, t1, hz=3.5 + 0.4 * k, expr="joy")
        ks.append(c)
    return ks


def kneel(ch, t, expr=None):
    return mo.strike(ch, t, {"hipz": -1.25, "legL": (85, 0, 0), "kneeL": 95, "legR": (-15, 0, 0), "kneeR": 100,
                             "torso": (0, 14, 0)}, expr=expr)


def hand_pos(ch, t, arm="armR"):
    """World position of the fist at t. The fist empty is created lazily by mo.hand: refresh the depsgraph AFTER
    creating it, or a fresh empty reports the origin (lesson 2026-11-15: desk flew to y 0)."""
    hd = mo.hand(ch, arm)
    bpy.context.scene.frame_set(F(t))
    bpy.context.view_layer.update()
    return tuple(hd.matrix_world.translation)


def shoe_hole(h):
    """Big readable hole on the FRONT of Harry's LEFT sneaker: dark torn opening + white sock toe poking out.
    Built from the shoe's real world bounds and parented to the shoe so it follows the walk."""
    sh = bpy.data.objects.get(h.name + "_harry_shoe_legL")
    if sh is None:
        print("shoe_hole: no shoe"); return None
    bpy.context.view_layer.update()
    mw = sh.matrix_world
    ys = [(mw @ Vector(c)).y for c in sh.bound_box]; zs = [(mw @ Vector(c)).z for c in sh.bound_box]
    xs = [(mw @ Vector(c)).x for c in sh.bound_box]
    fy = min(ys); cz = (min(zs) + max(zs)) / 2 + 0.02; cx = (min(xs) + max(xs)) / 2
    hole = cyl("shoe_hole", 0.27, 0.06, (cx, fy - 0.01, cz), mat("hole_m", hexc("#0e0c0b"), 0.95), 24, rot=(90, 0, 0),
               coll=h.coll)
    hole.scale = (1.35, 1.0, 0.85)
    sock = bpy.ops.mesh.primitive_uv_sphere_add(radius=0.2, location=(cx + 0.03, fy - 0.06, cz - 0.02), segments=16,
                                               ring_count=10)
    sk = bpy.context.active_object; sk.name = "shoe_sock"; sk.scale = (1.15, 0.7, 0.8)
    sk.data.materials.append(mat("sock_m", hexc("#f4efe6"), 0.9))
    for o in (sk,):
        for c in o.users_collection: c.objects.unlink(o)
        h.coll.objects.link(o)
    for k, (dx, dz, r) in enumerate([(-0.33, 0.12, 20), (0.34, -0.1, -25), (0.05, 0.24, 80)]):
        th = box(f"shoe_fray{k}", (0.16, 0.03, 0.05), (cx + dx, fy - 0.03, cz + dz), mat("fray_m", hexc("#cfcac2"), 0.9), 0.0,
                 rot=(0, r, 0), coll=h.coll)
        th.parent = sh; th.matrix_parent_inverse = sh.matrix_world.inverted()
    for o in (hole, sk):
        o.parent = sh; o.matrix_parent_inverse = sh.matrix_world.inverted()
    return hole


def _blocked(a, b, ignore=()):
    """True if something (not in ignore names) sits between points a and b."""
    sc = bpy.context.scene; dg = bpy.context.evaluated_depsgraph_get()
    a, b = Vector(a), Vector(b); d = b - a; L = d.length
    if L < 1e-4:
        return False
    hit, loc, nrm, idx, ob, mtx = sc.ray_cast(dg, a, d.normalized(), distance=L)
    if not hit:
        return False
    return not any(ob.name.startswith(p) for p in ignore)


def _clear(p, r=0.8):
    """Camera needs free space around it (not inside/against a wall, locker or door)."""
    sc = bpy.context.scene; dg = bpy.context.evaluated_depsgraph_get(); p = Vector(p)
    for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        hit = sc.ray_cast(dg, p, Vector(d), distance=r)[0]
        if hit and d != (0, 0, -1):
            return False
    return True


def safe_pos(target, yaw=-15, dist=9.0, pitch=4, ignore=()):
    """Camera position around target (yaw 0 = in front along -Y, + = to the right), pulled in or swung round until
    the line of sight is clear. Avoids the 'camera inside a wall / behind a head' black frames."""
    bpy.context.view_layer.update()
    t = Vector(target)
    for dy in (0, 20, -20, 40, -40, 65, -65):
        for k in (1.0, 0.8, 0.62, 0.48):
            dd = dist * k
            ya, pa = math.radians(yaw + dy), math.radians(pitch)
            p = t + Vector((math.sin(ya) * math.cos(pa), -math.cos(ya) * math.cos(pa), math.sin(pa))) * dd
            if not _blocked(t + (p - t).normalized() * 0.9, p, ignore) and _clear(p, 0.8):
                return p
    return t + Vector((0, -dist * 0.5, 1.0))


def scam(t0, t1, target, yaw=-15, dist=9.0, pitch=4, lens=40, push=0.10, fstop=2.8, ignore=(), name="Cam_s"):
    p = safe_pos(target, yaw, dist, pitch, ignore)
    tv = Vector(target)
    c = Cam(name, lens)
    c.key(t0, tuple(p), tuple(tv), lens, focus=tuple(tv), fstop=fstop)
    c.key(t1, tuple(p + (tv - p) * push), tuple(tv), lens, focus=tuple(tv), fstop=fstop, ease="EASE_IN_OUT")
    cams.micro(c, deg=0.4, loc=0.02, period=2.2)
    return c


def face_yaw(ch, t):
    """Camera yaw (safe_pos convention) that looks straight at the character's FACE at time t."""
    bpy.context.scene.frame_set(F(t))
    f = ch.head.matrix_world.to_quaternion() @ Vector((0, -1, 0))
    return math.degrees(math.atan2(f.x, -f.y))


def desk_cam(t0, t1, lens=28):
    """Bedroom desk: camera above the desk's right end, beside the monitor, looking back at Harry's face (3/4 front).
    The desk lamp is hidden because it sits on that sight line."""
    for o in bpy.context.scene.objects:
        if o.name.startswith(("bd_lamp", "bd_mug")):
            o.hide_render = True; o.hide_viewport = True
    return still_cam(t0, t1, (612.0, 19.0, 6.0), (608.0, 14.0, 5.2), lens=lens, push=0.08, fstop=2.8)


def stool():
    """Desk chair so Harry sits at a real desk height (he sank to chin level before)."""
    box("chair_seat", (2.4, 2.2, 0.4), (608, 13.4, 2.3), mat("chair_m", hexc("#3a3f4a"), 0.6), 0.06)
    box("chair_back", (2.4, 0.35, 3.2), (608, 12.2, 4.1), mat("chair_m", hexc("#3a3f4a"), 0.6), 0.08)
    cyl("chair_post", 0.18, 2.1, (608, 13.4, 1.05), mat("chair_p", hexc("#222222"), 0.4, 0.6), 12)


def two_face(t0, t1, a, b, favor=None, lens=30, extra=6.0, pitch=5, up=-1.0, ignore=()):
    """Two-shot that sees BOTH faces: camera on the open (-Y) side of the line between the two heads,
    swung 20 deg toward the favoured character's face."""
    pa, pb = Vector(head(a, t0 + 0.3, up)), Vector(head(b, t0 + 0.3, up))
    mid = (pa + pb) / 2; dv = pb - pa
    n = Vector((-dv.y, dv.x, 0)).normalized()
    if n.y > 0: n = -n
    yaw = math.degrees(math.atan2(n.x, -n.y))
    if favor is not None:
        fy = face_yaw(favor, t0 + 0.3)
        yaw += max(-25, min(25, (fy - yaw + 540) % 360 - 180))
    dist = max(9.0, dv.length * 1.5 + extra)
    return scam(t0, t1, tuple(mid), yaw=yaw, dist=dist, pitch=pitch, lens=lens, ignore=(a.name, b.name) + tuple(ignore))


def med(t0, t1, ch, yaw=-12, d=9.0, lens=40, pitch=4, up=-0.8):
    off = yaw if abs(yaw) <= 60 else -12
    return scam(t0, t1, head(ch, t0, up), yaw=face_yaw(ch, t0 + 0.3) + off, dist=d, pitch=pitch, lens=lens,
                ignore=(ch.name,))


def _rot_of(ch):
    try:
        return -math.degrees(ch.root.rotation_euler.z)
    except Exception:
        return 0.0


def principal(t0, t1, expr="neutral", loc=(0, 0, 0), rot=0):
    p = cast.make("grandma", t0, t1, expr, loc=loc, rot=rot, prop=False, cine=True, name="Principal")
    return p


def rdad(t0, t1, expr="grin", loc=(0, 0, 0), rot=0):
    return cast.make("mayor", t0, t1, expr, loc=loc, rot=rot, prop=False, cine=True, name="RyanDad")


def hallway(students=True):
    L = T.school_hallway(students=students)
    look.cinematic("ref_matte", focus=L["focus"])
    return L


def exterior(students=True):
    _sign = T.S.sign
    def sign2(name, body, *a, **k):
        return _sign(name, "BLOX CITY HIGH" if "SCHOOL" in body else body, *a, **k)
    T.S.sign = sign2
    try:
        L = T.school_exterior(students=students)
    finally:
        T.S.sign = _sign
    V.look = "ref_day"
    look.cinematic("ref_day", focus=L["focus"], blur=0.4)
    return L


def drop(obs, t_fall, push=(0, -1, 0), power=3.6, seed=0, rest=0.14):
    """Real fall (CLEAN_ANIMATION 4): each object flies on a gravity arc from where it is at t_fall, tumbles, lands
    flat, bounces once, slides and settles. Small stagger per object."""
    import random
    rnd = random.Random(7 + seed)
    P = Vector(push); P.z = 0
    P = P.normalized() if P.length > 0 else Vector((0, -1, 0))
    side = Vector((-P.y, P.x, 0)); n = len(obs)
    for k, b in enumerate(obs):
        b.rotation_mode = "XYZ"
        f0 = F(t_fall) + k
        bpy.context.scene.frame_set(f0)
        p = Vector(b.matrix_world.translation)
        v = P * (power * rnd.uniform(0.8, 1.2)) + side * ((k - (n - 1) / 2) * 1.4) + Vector((0, 0, rnd.uniform(1.0, 2.5)))
        rot = Vector(b.rotation_euler)
        w = Vector((rnd.uniform(-9, 9), rnd.uniform(-7, 7), rnd.uniform(-6, 6)))
        b.keyframe_insert("location", frame=f0); b.keyframe_insert("rotation_euler", frame=f0)
        dt = 1 / 30.0; landed = 0; f = f0
        rz = rest + 0.02 * k
        while f < f0 + 45:
            f += 1
            v.z -= 32 * dt
            p += v * dt
            if landed == 0:
                rot += w * dt
            if p.z <= rz:
                p.z = rz
                if landed == 0:
                    v = Vector((v.x * 0.45, v.y * 0.45, -v.z * 0.22)); landed = 1
                    rot = Vector((0, 0, rot.z)); w = Vector((0, 0, 0))
                else:
                    v = Vector((v.x * 0.6, v.y * 0.6, 0))
            b.location = p; b.rotation_euler = rot
            b.keyframe_insert("location", frame=f); b.keyframe_insert("rotation_euler", frame=f)
    return obs


def books(name, loc, t_fall=None, n=3, floor=(0, 0, 0.1), seed=0, hold=None, push=(0, -1, 0), power=3.6):
    """School books. hold=(ch, t_from): ride in ch's hands (keyed every 2 f) until t_fall; then drop()."""
    cols = ["#2f6db3", "#c0392b", "#2e8b57", "#d4a017"]
    obs = []
    for k in range(n):
        m = mat(f"{name}_m{k}", hexc(cols[(k + seed) % 4]), 0.6)
        b = box(f"{name}{k}", (1.4, 1.0, 0.28), (loc[0], loc[1], loc[2] + k * 0.3), m, 0.04)
        obs.append(b)
    if hold is not None and t_fall is not None:
        ch, ta = hold
        for f in range(F(ta), F(t_fall) + 1, 2):
            hl = Vector(hand_pos(ch, f / 30.0, "armL")); hr = Vector(hand_pos(ch, f / 30.0, "armR"))
            c = (hl + hr) / 2
            for k, b in enumerate(obs):
                b.location = (c.x, c.y - 0.55, c.z - 0.25 + k * 0.28)
                b.keyframe_insert("location", frame=f)
    if t_fall is not None:
        drop(obs, t_fall, push, power, seed)
    return obs


def shoe_set(loc, pencil_t=None):
    """ECU prop: Harry's worn left sneaker with a hole at the toe; optional pencil pushed through at pencil_t."""
    x, y, z = loc
    coll = collection("shoe")
    sh = mat("shoe_m", hexc("#cfcac0"), 0.8)
    sole = mat("shoe_sole", hexc("#8d877c"), 0.9)
    box("shoe_body", (1.9, 3.6, 1.1), (x, y, z + 0.75), sh, 0.25, coll=coll)
    box("shoe_sole", (2.0, 3.8, 0.3), (x, y, z + 0.15), sole, 0.08, coll=coll)
    box("shoe_toe", (1.85, 1.0, 0.8), (x, y - 1.6, z + 0.55), sh, 0.3, coll=coll)
    for k in range(4):
        box(f"shoe_lace{k}", (1.2, 0.12, 0.06), (x, y - 0.6 + k * 0.4, z + 1.33), mat("lace", hexc("#efece6"), 0.7), 0.02, coll=coll)
    hole = cyl("shoe_hole", 0.32, 0.2, (x - 0.3, y - 2.08, z + 0.6), mat("hole_m", hexc("#151311"), 0.95), 24,
               rot=(90, 0, 0), coll=coll)
    box("shoe_dirt", (1.6, 0.05, 0.4), (x + 0.2, y - 2.11, z + 0.35), mat("dirt", hexc("#7a6a55"), 1.0), 0.0, coll=coll)
    box("floor_tile", (30, 30, 0.2), (x, y + 6, z - 0.1), pbr.get("concrete", tint="#d8d2c6"), 0.0, coll=coll)
    leg = box("shoe_leg", (1.3, 1.3, 9.0), (x, y + 0.6, z + 5.6), mat("jeans", hexc("#2d3550"), 0.85), 0.12, coll=coll)
    sock = cyl("shoe_sock", 0.2, 0.05, (x - 0.3, y - 2.0, z + 0.6), mat("sock", hexc("#e9e2d2"), 0.9), 20, rot=(90, 0, 0), coll=coll)
    if pencil_t is not None:
        pm = mat("pencil_m", hexc("#f2c14e"), 0.5)
        p = cyl("pencil", 0.12, 4.0, (x - 0.3, y - 4.2, z + 0.6), pm, 6, rot=(90, 0, 0), coll=coll)
        tip = cyl("pencil_tip", 0.12, 0.3, (0, 0, 2.1), mat("wood", hexc("#e6c79a"), 0.6), 6, parent=p, coll=coll)
        p.keyframe_insert("location", frame=F(pencil_t))
        p.location = (x - 0.3, y - 1.7, z + 0.6)
        p.keyframe_insert("location", frame=F(pencil_t + 0.35))
    light("shoe_key", "AREA", (x - 4, y - 6, z + 6), 900, hexc("#ffd9a8"), 3, target=(x, y - 1, z + 0.6))
    light("shoe_fill", "AREA", (x + 5, y - 4, z + 3), 250, hexc("#f2eee8"), 4, target=(x, y, z + 0.6))
    return (x - 0.3, y - 2.1, z + 0.6)


def auditorium(crowd=True, banner=None):
    x, y, z = AUD
    coll = collection("aud")
    T.room("aud", AUD, w=64, d=46, h=22, floor="woodfloor", wall=("plaster", "#8a3b34"), coll=coll, fill=0.6)
    stage = box("aud_stage", (44, 12, 2.6), (x, y + 38, z + 1.3), pbr.get("planks", tint="#8a5a32", tile=4), 0.05, coll=coll)
    T.curtains("aud_cur", (x, y + 45.6, z + 2.6), 44, 18, "#7d1f24", coll=coll)
    box("aud_pod", (3.2, 2.2, 3.0), (x - 6, y + 36, z + 2.6 + 1.5), pbr.get("planks", tint="#5e3b22", tile=2), 0.06, coll=coll)
    cyl("aud_mic", 0.06, 1.6, (x - 7.2, y + 35.6, z + 2.6 + 3.6), mat("micm", hexc("#2a2a2a"), 0.3, 0.6), 8, rot=(25, 0, 0), coll=coll)
    cyl("aud_micH", 0.22, 0.5, (x - 7.2, y + 35.3, z + 2.6 + 4.4), mat("micm", hexc("#2a2a2a"), 0.3, 0.6), 12, coll=coll)
    SG.sign("aud_name", "BLOX CITY HIGH ASSEMBLY", (x, y + 43.6, z + 18.0), w=16, h=2.0, bg="#1f2f5a", fg="#f2c14e", coll=coll)
    if banner:
        SG.sign("aud_banner", banner, (x, y + 43.4, z + 12.0), w=13, h=4.2, bg="#f2c14e", fg="#1f2f5a", coll=coll)
    for k in range(5):
        light(f"aud_spot{k}", "SPOT", (x - 16 + k * 8, y + 22, z + 20), 9000, hexc("#ffe2b8"), 0.6, target=(x - 16 + k * 8, y + 38, z + 3))
    if crowd:
        C.crowd("aud_kids", (x, y + 12, z), (46, 12), 45, mode="scatter", face=(x, y + 38, 5), seed=4, coll=coll,
                variants=["student_a", "student_b", "c1", "c2", "c4", "c6"], min_gap=2.6, poses=("stand", "stand", "cross", "pocket"))
    light("aud_stagekey", "AREA", (x, y + 20, z + 16), 26000, hexc("#ffe6c4"), 30, target=(x, y + 36, z + 4))
    box("aud_backwall", (64, 1.0, 22), (x, y - 0.6, z + 11), mat("aud_bw", hexc("#7a3530"), 0.9), 0.0, coll=coll)
    for k in range(3):
        box(f"aud_door{k}", (4.0, 0.3, 7.0), (x - 16 + k * 16, y - 0.05, z + 3.5), mat("aud_dm", hexc("#3b2a20"), 0.6), 0.04, coll=coll)
    look.cinematic("ref_matte", focus=(x, y + 34, 6))
    return dict(stage_z=z + 2.6, pod=(x - 6, y + 34.5, z + 2.6), focus=(x, y + 34, 6))


def screen_insert(t0, t1, lines, header="BLOX SCHOOL TYCOON", push=0.12):
    o = (900.0, 0.0, 0.0)
    coll = collection("scr")
    box("scr_desk", (20, 10, 0.4), (o[0], o[1] + 2, o[2] + 2.8), pbr.get("planks", tint="#6e4a2e", tile=3), 0.05, coll=coll)
    SG.screen("scr", lines, (o[0], o[1] + 3.0, o[2] + 5.6), w=6.4, h=3.6, bg="#0f1830", header=header,
              header_bg="#2f7bff", coll=coll, size=0.42)
    box("scr_back", (40, 1, 20), (o[0], o[1] + 14, o[2] + 8), mat("bgwall", hexc("#2a2622"), 0.9), 0.0, coll=coll)
    light("scr_lamp", "POINT", (o[0] + 5, o[1] - 1, o[2] + 7), 600, hexc("#ffb867"), 1.0)
    look.cinematic("ref_practical", focus=(o[0], o[1] + 3, o[2] + 5.6))
    return still_cam(t0, t1, (o[0] + 0.6, o[1] - 7.2, o[2] + 6.0), (o[0], o[1] + 3, o[2] + 5.5), lens=40, push=push, fstop=2.8)


# ================================================================== v2 SHOTS (2026-11-15 redo: acting first)
HP = (HX - 6, HY - 2, 0)      # Harry's hallway mark


def car_door(cx, cy, t_open=None, name="bdoor"):
    """Side door on the camera (-Y) side of a T.car(rot=90) parked at (cx, cy): dark opening + door that swings OUT
    (hinge at the front end). Characters stand OUTSIDE the body (y <= cy-7.2) and step away: nobody walks through
    the car (CLEAN_ANIMATION 2). t_open None = already open."""
    body = mat("tw_car_door", hexc("#141416"), 0.25, 0.3)
    box(name + "_gap", (2.3, 0.05, 1.8), (cx + 0.4, cy - 2.53, 2.55), mat("door_gap", hexc("#050506"), 0.9), 0.0)
    pv = bpy.data.objects.new(name + "_hinge", None); bpy.context.scene.collection.objects.link(pv)
    pv.location = (cx + 1.6, cy - 2.6, 0)
    d = box(name, (2.4, 0.16, 2.0), (-1.2, -0.02, 2.5), body, 0.08, parent=pv)
    box(name + "_win", (1.8, 0.04, 0.9), (-1.2, -0.12, 3.25), mat("door_win", hexc("#22303c"), 0.1, 0.2), 0.02, parent=pv)
    pv.rotation_mode = "XYZ"
    if t_open is None:
        pv.rotation_euler = (0, 0, math.radians(72))
    else:
        pv.rotation_euler = (0, 0, 0); pv.keyframe_insert("rotation_euler", frame=F(t_open))
        pv.rotation_euler = (0, 0, math.radians(80)); pv.keyframe_insert("rotation_euler", frame=F(t_open + 0.35))
        pv.rotation_euler = (0, 0, math.radians(72)); pv.keyframe_insert("rotation_euler", frame=F(t_open + 0.55))
    return pv


def appear(ch, t):
    """Character hidden until t (e.g. behind a closed car door)."""
    for o in ch.coll.all_objects:
        o.hide_render = True; o.keyframe_insert("hide_render", frame=1)
        o.hide_render = False; o.keyframe_insert("hide_render", frame=F(t))


def H_pov_spot():
    """OTS layout in the hallway: Harry with his back to camera (foreground), bullies facing the lens."""
    return (HX - 2.0, HY - 9.0, 0)


@S(1, 0, 3, "OTS: Harry's shoulder blurred in front; Ryan + 2 kids face us, POINT at Harry's shoes and LAUGH")
def s01a(t0, t1):
    L = hallway(students=True)
    hp = H_pov_spot()
    h = harry(t0, t1, "sad", loc=hp, rot=180)
    mo.idle(h, t0, t1, 0.6)
    shoes = (hp[0], hp[1], 0.4)
    r = ryan(t0, t1, "laugh_smug", loc=(HX - 6.0, HY - 3.6, 0), rot=0)
    mo.turn(r, t0, target=h, dur=2)
    mo.point(r, t0 + 0.1, shoes, hold=0.9, expr="laugh_smug")
    mo.laugh(r, t0 + 1.2, t1 + 0.5, hz=4.0, expr="joy")
    ks = laughers(t0, t1, shoes, [(HX - 7.6, HY - 2.0, 25), (HX - 3.8, HY - 1.8, -25)], start=0.25)
    for c in [r] + ks:
        qa.look(c, h, t0 + 0.3, t0 + 1.0, tol=45)
    still_cam(t0, t1, (HX - 0.4, HY - 15.5, 6.4), (HX - 5.6, HY - 3.0, 3.6), lens=34, push=0.08, fstop=2.8)
    sfx(t0 + 0.4, "kids_laugh", 0.6)


@S(2, 3, 5, "INSERT: Harry's two feet - right sneaker fine, LEFT one with a torn hole and the sock showing")
def s01b(t0, t1):
    L = hallway(students=False)
    h = harry(t0, t1, "sad", loc=HP, rot=0); shoe_hole(h)
    mo.idle(h, t0, t1, 0.3)
    c = Cam("Cam_feet0", 38)
    c.key(t0, (HX - 5.9, HY - 7.6, 0.8), (HX - 5.95, HY - 2.4, 0.45), 38, focus=(HX - 5.5, HY - 2.6, 0.3), fstop=2.4)
    c.key(t1, (HX - 5.8, HY - 6.4, 0.7), (HX - 5.8, HY - 2.4, 0.4), 44, focus=(HX - 5.5, HY - 2.6, 0.3), fstop=2.2,
          ease="EASE_IN_OUT")
    cams.micro(c, deg=0.25, loc=0.01, period=2.0)


@S(3, 5, 8, "MCU: Harry looks down, sad, a tear - 'for three years'")
def s01c(t0, t1):
    L = hallway(students=True)
    h = harry(t0, t1, "sad", loc=HP, rot=-10)
    mo.idle(h, t0, t1, 0.5)
    acting.face(h, t0 + 0.6, "sad_tear")
    scam(t0, t1, head(h, t0 + 0.3, -0.7), yaw=face_yaw(h, t0 + 0.3) + 12, dist=9.5, pitch=3, lens=45, push=0.10,
         ignore=("Harry",))


@S(4, 8, 11, "WIDE: establishing - Blox City High on a Monday morning, kids arriving")
def s02_est(t0, t1):
    L = exterior(students=True)
    still_cam(t0, t1, (EX + 2, EY - 34, 7.0), (EX + 2, EY - 4, 6.0), lens=26, push=0.06, fstop=8.0)




@S(5, 11, 15, "LOW: flash-forward - a black car pulls up at the gates, Harry steps out with a smirk")
def s02(t0, t1):
    L = exterior(students=True)
    car = T.car("bcar", (EX + 34, EY - 4, 0), 90, "#141416")
    car.keyframe_insert("location", frame=F(t0)); car.location.x = EX + 8; car.keyframe_insert("location", frame=F(t0 + 1.0))
    dv = car_door(EX + 8, EY - 4, t_open=t0 + 1.0)
    for o in [dv] + [o for o in bpy.data.objects if o.name == "bdoor_gap"]:
        x1 = o.location.x
        o.location.x = x1 + 26; o.keyframe_insert("location", frame=F(t0))
        o.location.x = x1; o.keyframe_insert("location", frame=F(t0 + 1.0))
    h = harry(t0, t1, "smug_up", loc=(EX + 8.0, EY - 7.4, 0), rot=0)
    appear(h, t0 + 1.2)
    mo.walk(h, t0 + 1.25, t1, [(EX + 8.0, EY - 7.4, 0), (EX + 6.5, EY - 9.0, 0)])
    mo.strike(h, V.w(12), {"head": (0, -6, 6)}, expr="smug_up")
    still_cam(t0, t1, (EX + 1, EY - 18, 2.0), (EX + 6.5, EY - 6, 3.8), lens=30, push=0.12, fstop=4.0)


@S(6, 15, 24, "WALK: Harry walks up to BLOX CITY HIGH, two kids whisper and point")
def s03(t0, t1):
    L = exterior(students=True)
    h = harry(t0, t1, "sad", loc=(EX - 4, EY - 14, 0), rot=180)
    mo.walk(h, t0, t1, [(EX - 4, EY - 16, 0), (EX - 2, EY - 6, 0)], mood="sad")
    k0 = kid(0, t0, t1, "smug", loc=(EX + 3, EY - 9, 0), rot=-120)
    k1 = kid(1, t0, t1, "laugh_smug", loc=(EX + 5, EY - 8, 0), rot=-110)
    mo.point(k0, t0 + 0.8, h, hold=1.0); mo.laugh(k1, t0 + 1.0, t1, hz=3.5)
    still_cam(t0, t1, (EX - 10, EY - 30, 6.5), (EX, EY - 4, 6), lens=30, push=0.10, fstop=5.6)


@S(7, 24, 28, "MED: Harry tugs his faded hoodie, looks down at his shoes")
def s04(t0, t1):
    L = hallway(students=True)
    h = harry(t0, t1, "worried", loc=HP, rot=-20)
    mo.idle(h, t0, t1, 1.0)
    mo.reach(h, t0 + 0.2, (HP[0] + 0.4, HP[1] - 0.7, 2.3), hand="l", expr="worried")
    mo.strike(h, V.w(26), {"head": (0, 20, 0)}, expr="sad_tear")
    med(t0, t1, h, yaw=-20, d=9.5)


@S(8, 28, 33, "LOW: Harry's real feet - one fine sneaker, the left one with a hole at the toe")
def s05(t0, t1):
    L = hallway(students=False)
    h = harry(t0, t1, "sad", loc=HP, rot=0); shoe_hole(h)
    mo.idle(h, t0, t1, 0.5)
    c = Cam("Cam_feet", 40)
    c.key(t0, (HX - 7.4, HY - 9.5, 1.0), (HX - 6.2, HY - 2.4, 0.9), 40, focus=(HX - 5.8, HY - 2.6, 0.4), fstop=2.2)
    c.key(t1, (HX - 6.6, HY - 7.6, 0.8), (HX - 5.8, HY - 2.6, 0.5), 50, focus=(HX - 5.8, HY - 2.6, 0.4), fstop=2.0, ease="EASE_IN_OUT")
    cams.micro(c, deg=0.3, loc=0.01, period=2.0)


def pencil(name="pencil"):
    """Real pencil (pink eraser, metal band, yellow hex body, sharpened wood tip, graphite point), built along
    local +Z from the eraser end so the whole prop can be aimed with one rotation."""
    root = bpy.data.objects.new(name, None); bpy.context.scene.collection.objects.link(root)
    parts = [("_er", 0.075, 0.075, 0.12, 0.06, "#e88a9a", 0.7, 0.0), ("_fe", 0.08, 0.08, 0.08, 0.16, "#c9c9c9", 0.3, 0.9),
             ("_bd", 0.075, 0.075, 0.95, 0.675, "#f2b632", 0.5, 0.0), ("_wd", 0.075, 0.022, 0.2, 1.25, "#e3c08f", 0.8, 0.0),
             ("_gr", 0.022, 0.002, 0.07, 1.385, "#2b2b2b", 0.4, 0.0)]
    for suf, r1, r2, ln, zc, col, rough, met in parts:
        cyl(name + suf, r1, ln, (0, 0, zc), mat(name + suf + "_m", hexc(col), rough, met), 6 if suf == "_bd" else 16,
            parent=root, r2=r2)
    return root


def aim_prop(ob, t0, t1, grip, dir_fn, hold=0.45, step=2):
    """Key a prop every `step` frames: grip point from grip(t), pointing along dir_fn(t)."""
    for f in range(F(t0), F(t1) + 1, step):
        t = f / 30.0
        g = Vector(grip(t)); d = Vector(dir_fn(t)).normalized()
        ob.location = g - d * hold
        ob.rotation_mode = "QUATERNION"
        ob.rotation_quaternion = d.to_track_quat("Z", "Y")
        ob.keyframe_insert("location", frame=f); ob.keyframe_insert("rotation_quaternion", frame=f)


@S(9, 33, 38, "INSERT: ECU of the torn sneaker - a yellow pencil slides into the hole and pokes through")
def s06a(t0, t1):
    L = hallway(students=False)
    h = harry(t0, t1, "sad", loc=HP, rot=0); hole = shoe_hole(h)
    mo.idle(h, t0, t1, 0.2)
    bpy.context.view_layer.update()
    hp = hole.matrix_world.translation.copy()
    pen = pencil()
    d = Vector((0.25, 1.0, -0.35)).normalized()          # from front-right, slightly downward into the hole
    t_in = V.w(38)
    for f in range(F(t0), F(t1) + 1, 1):
        t = f / 30.0
        k = max(0.0, min(1.0, (t - (t_in - 0.6)) / 0.6))
        k = k * k * (3 - 2 * k)
        tip = hp - d * (1.0 - 1.1 * k)
        pen.location = tip - d * 1.42
        pen.rotation_mode = "QUATERNION"; pen.rotation_quaternion = d.to_track_quat("Z", "Y")
        pen.keyframe_insert("location", frame=f); pen.keyframe_insert("rotation_quaternion", frame=f)
    qa.prop(pen)
    c = Cam("Cam_pencil", 50)
    c.key(t0, (hp.x - 1.6, hp.y - 4.2, 1.0), (hp.x + 0.1, hp.y, hp.z + 0.1), 50, focus=tuple(hp), fstop=2.0)
    c.key(t1, (hp.x - 1.3, hp.y - 3.4, 0.9), (hp.x + 0.1, hp.y, hp.z + 0.1), 55, focus=tuple(hp), fstop=1.8,
          ease="EASE_IN_OUT")
    cams.micro(c, deg=0.2, loc=0.01, period=2.0)
    sfx(t_in, "boing", 0.8)


@S(10, 38, 40, "MCU: Ryan, crouched at shoe level, laughs up at Harry (POV from Harry)")
def s06b(t0, t1):
    L = hallway(students=True)
    r = ryan(t0, t1, "toothy", loc=(HX - 6.0, HY - 2.0, 0), rot=0)
    kneel(r, t0 - 0.2, expr="toothy")
    mo.laugh(r, t0 + 0.15, t1 + 0.4, hz=4.5, expr="joy")
    hd = Vector(head(r, t0 + 0.2, 0.0))
    eye = (hd.x + 0.6, hd.y - 6.5, hd.z + 2.6)              # Harry's eyes, looking down at him
    mo.look_at(r, t0, eye)
    qa.look(r, eye, t0 + 0.1, t0 + 0.2, tol=40)
    still_cam(t0, t1, eye, (hd.x, hd.y, hd.z - 0.3), lens=40, push=0.10, fstop=2.0)


@S(11, 40, 45, "MED: Ryan stands, points at Harry and shouts to the hallway")
def s07(t0, t1):
    L = hallway(students=True)
    h = harry(t0, t1, "worried", loc=HP, rot=-30)
    r = ryan(t0, t1, "smug_up", loc=(HX - 3.6, HY - 4.2, 0), rot=40)
    mo.idle(r, t0, t1, 1.0)
    mo.point(r, t0 + 0.2, h, hold=1.6, expr="angry_shout")
    mo.turn(r, V.w(43), yaw=-10, expr="laugh_smug")
    mo.strike(h, t0 + 0.5, {"head": (0, 16, 0), "torso": (0, 6, 0)}, expr="worried_dart")
    cams.two_shot(t0, t1, HP, (HX - 3.6, HY - 4.2, 0), lens=30, d=11, h=4.4, yaw=-10)


@S(12, 45, 48, "MED: Harry hugs his books to his chest, glances nervously to the side")
def s08a(t0, t1):
    L = hallway(students=True)
    h = harry(t0, t1, "worried", loc=HP, rot=-10)
    mo.strike(h, t0, {"armL": (62, -8, 0), "armR": (62, -8, 0), "elbowL": 55, "elbowR": 55})
    bk = books("bkA", (0, 0, 0), t_fall=t1 + 2, hold=(h, t0))
    mo.look_at(h, t0 + 0.8, (HX - 1.0, HY - 6, 4.5))
    still_cam(t0, t1, (HX - 7.4, HY - 14.0, 4.4), (HX - 6.0, HY - 2.0, 3.6), lens=34, push=0.08, fstop=3.0)


@S(13, 48, 50, "MCU POV: Ryan's hand SWIPES at the lens (at Harry's books), angry grin")
def s08b(t0, t1):
    L = hallway(students=True)
    r = ryan(t0, t1, "angry_shout", loc=(HX - 6.0, HY - 2.0, 0), rot=0)
    hd = Vector(head(r, t0, 0.0))
    eye = (hd.x - 0.4, hd.y - 6.0, hd.z - 0.3)
    books_pt = (hd.x - 0.2, hd.y - 2.2, hd.z - 2.2)
    mo.look_at(r, t0, books_pt)
    mo.reach(r, t0 + 0.25, books_pt, hand="r", body={"torso": (-14, 10, 0)}, expr="angry_shout")
    mo.strike(r, t0 + 0.42, {"armR": (60, 55, 0), "elbowR": 10, "torso": (20, 6, 0)}, expr="laugh_smug")
    still_cam(t0, t1, eye, (hd.x, hd.y, hd.z - 0.6), lens=34, push=0.04, fstop=2.2)
    sfx(t0 + 0.3, "bonk", 0.9)


@S(14, 50, 55, "LOW INSERT: the books tumble into frame and slap onto the hallway floor; Harry's shoes behind")
def s08c(t0, t1):
    L = hallway(students=False)
    h = harry(t0, t1, "sad", loc=(HX - 6.0, HY + 1.0, 0), rot=0); shoe_hole(h)
    mo.idle(h, t0, t1, 0.3)
    bk = books("bkB", (HX - 6.6, HY - 2.6, 5.2), t_fall=t0 + 0.05, push=(0.6, -1.0, 0), power=2.2)
    c = Cam("Cam_floor", 30)
    c.key(t0, (HX - 5.0, HY - 9.0, 0.9), (HX - 6.0, HY - 2.0, 0.8), 30, focus=(HX - 6.2, HY - 3.4, 0.3), fstop=3.2)
    c.key(t1, (HX - 5.0, HY - 8.4, 0.85), (HX - 6.0, HY - 2.0, 0.7), 32, focus=(HX - 6.2, HY - 3.4, 0.3), fstop=3.0,
          ease="EASE_IN_OUT")
    cams.micro(c, deg=0.3, loc=0.01, period=2.0)
    sfx(t0 + 0.55, "thud", 0.7)


@S(15, 55, 64, "MED: Ryan points down at Harry's shoes 'Maybe buy real shoes...'")
def s09(t0, t1):
    L = hallway(students=True)
    r = ryan(t0, t1, "smug_up", loc=(HX - 3.4, HY - 4.0, 0), rot=30)
    mo.idle(r, t0, t1, 1.0)
    mo.talk_cadence(r, t0, t1, V.words, stress=("real", "Harry."), expr_on={"real": "laugh_smug", "Harry.": "toothy"}, hands=True)
    mo.point(r, V.w(58), (HP[0], HP[1], 0.3), hold=1.0, expr="laugh_smug")
    med(t0, t1, r, yaw=20, d=9.5)


@S(16, 64, 66, "WIDE: the whole hallway points and laughs")
def s10(t0, t1):
    L = hallway(students=True)
    h = harry(t0, t1, "sad_tear", loc=HP, rot=0)
    laughers(t0, t1, h, [(HX - 2.5, HY - 7, 40), (HX - 9.5, HY - 7, -40), (HX - 1.5, HY + 1, 90), (HX - 10.5, HY + 1.5, -90), (HX - 4, HY + 4, 160)], start=-0.6)
    still_cam(t0, t1, (HX - 6, HY - 20, 6.5), (HX - 6, HY - 1, 3.8), lens=28, push=0.10, fstop=5.0)
    sfx(t0, "kids_laugh", 0.8)


@S(17, 66, 68, "LOW: Harry alone on his knees picking up books, kids walk past (crickets)")
def s11(t0, t1):
    L = hallway(students=False)
    h = harry(t0, t1, "sad", loc=HP, rot=10)
    kneel(h, t0, expr="sad_tear")
    books("bk2", (HP[0] - 0.3, HP[1] - 1.6, 0.15), floor=(HP[0], HP[1] - 1.5, 0))
    mo.reach(h, t0 + 0.2, (HP[0] - 0.3, HP[1] - 1.6, 0.3), hand="r", body={"hipz": -1.25, "torso": (0, 26, 0)})
    k = kid(3, t0, t1, "bored", loc=(HX - 2, HY - 6, 0), rot=90)
    mo.walk(k, t0, t1, [(HX - 1, HY + 2.5, 0), (HX - 11, HY + 2.5, 0)])
    cams.ground_low(t0, t1, (HP[0], HP[1], 1.6), lens=20, d=7, yaw=-20)


def carry(obs, ch, t0, t1, up=0.12, fwd=-0.25, step=2):
    """Objects ride between the character's two fists (tray, box, books) - keyed every `step` frames."""
    base = [Vector(o.location) for o in obs]
    for f in range(F(t0), F(t1) + 1, step):
        hl = Vector(hand_pos(ch, f / 30.0, "armL")); hr = Vector(hand_pos(ch, f / 30.0, "armR"))
        c = (hl + hr) / 2
        for o, b0 in zip(obs, base):
            o.location = (c.x + b0.x, c.y + fwd + b0.y, c.z + up + b0.z)
            o.keyframe_insert("location", frame=f)


@S(18, 68, 77, "MED: Milo, smallest kid in sixth grade, carries his lunch tray in both hands")
def s12(t0, t1):
    L = hallway(students=True)
    m = milo(t0, t1, "content", loc=(HX - 6, HY - 1, 0), rot=0)
    mo.idle(m, t0, t1, 1.0)
    mo.strike(m, t0 - 0.4, {"armL": (62, -6, 0), "armR": (62, -6, 0), "elbowL": 45, "elbowR": 45})
    tr = box("tray", (2.2, 1.0, 0.12), (0, -0.15, 0), mat("tray_m", hexc("#e04a3a"), 0.4), 0.03)
    fd = box("tray_food", (0.8, 0.6, 0.35), (-0.4, 0, 0.22), mat("fd0", hexc("#f2c14e"), 0.7), 0.1)
    ml = box("tray_milk", (0.4, 0.4, 0.6), (0.6, 0.1, 0.35), mat("milk_m", hexc("#f4f4f4"), 0.6), 0.05)
    carry([tr, fd, ml], m, t0, t1, fwd=-0.6)
    qa.prop(tr, holder=m, arm="arm")
    acting.face(m, t0 + 0.2, "happy"); acting.face(m, V.w(72), "joy")
    still_cam(t0, t1, (HX - 7.0, HY - 12.5, 3.6), (HX - 6.0, HY - 1.0, 2.6), lens=34, push=0.10, fstop=3.0)


@S(19, 77, 80, "LOW INSERT: the lunch tray flips and the food splats onto the floor")
def s13a(t0, t1):
    L = hallway(students=False)
    m = milo(t0, t1, "pop_shock", loc=(HX - 6, HY + 0.5, 0), rot=0)
    mo.idle(m, t0, t1, 1.2)
    tr = box("trayF", (2.2, 1.4, 0.12), (HX - 6.2, HY - 2.6, 5.0), mat("tray_m", hexc("#e04a3a"), 0.4), 0.03)
    food = [box(f"foodF{k}", (0.5, 0.5, 0.3), (HX - 6.7 + k * 0.5, HY - 2.6, 5.25), mat(f"fdF{k}",
            hexc(["#f2c14e", "#7cb342", "#a0522d"][k]), 0.7), 0.1) for k in range(3)]
    drop(([tr] + food), t0 + 0.05, push=(0.3, -1.0, 0), power=1.8)
    c = Cam("Cam_tray", 30)
    c.key(t0, (HX - 5.0, HY - 9.0, 0.9), (HX - 6.0, HY - 2.0, 0.9), 30, focus=(HX - 6.2, HY - 3.4, 0.3), fstop=3.2)
    c.key(t1, (HX - 5.0, HY - 8.5, 0.85), (HX - 6.0, HY - 2.0, 0.8), 32, focus=(HX - 6.2, HY - 3.4, 0.3), fstop=3.0,
          ease="EASE_IN_OUT")
    cams.micro(c, deg=0.3, loc=0.01, period=2.0)
    sfx(t0 + 0.5, "splat", 0.9)


@S(20, 80, 82, "MCU: Milo looks down at his lunch on the floor, lip wobbling, a tear")
def s13b(t0, t1):
    L = hallway(students=True)
    m = milo(t0, t1, "sad_tear", loc=(HX - 6, HY - 1, 0), rot=0)
    mo.idle(m, t0, t1, 0.5)
    floor_pt = (HX - 6.2, HY - 3.6, 0.2)
    mo.look_at(m, t0, floor_pt)
    scam(t0, t1, head(m, t0 + 0.2, -0.6), yaw=face_yaw(m, t0 + 0.2) + 10, dist=8.5, pitch=-2, lens=42,
         ignore=("Milo",))


@S(21, 82, 88, "MED: Harry kneels beside Milo, hand on his shoulder")
def s14(t0, t1):
    L = hallway(students=False)
    m = milo(t0, t1, "sad_tear", loc=(HX - 5, HY - 1.5, 0), rot=30)
    h = harry(t0, t1, "worried", loc=(HX - 7.6, HY - 2.2, 0), rot=-40)
    mo.walk(h, t0, t0 + 1.0, [(HX - 9.5, HY - 3, 0), (HX - 7.6, HY - 2.2, 0)])
    kneel(h, V.w(83), expr="smile")
    sh = head(m, V.w(85), -1.25)
    mo.reach(h, V.w(85), (sh[0] - 0.6, sh[1], sh[2]), hand="l", body={"hipz": -1.25, "torso": (0, 10, 0)}, expr="smile")
    mo.turn(m, V.w(86), target=h, expr="worried")
    two_face(t0, t1, m, h, favor=h)


@S(22, 88, 93, "MCU: Harry 'It's okay. I've got you.' warm smile")
def s15(t0, t1):
    L = hallway(students=False)
    h = harry(t0, t1, "smile", loc=(HX - 7.6, HY - 2.2, 0), rot=-40)
    kneel(h, t0, expr="smile")
    mo.talk_cadence(h, t0, t1, V.words, stress=("okay.", "you.\""), expr_on={"okay.": "content", "you.\"": "smile"}, hands=False)
    scam(t0, t1, head(h, t0 + 0.4, -0.6), yaw=face_yaw(h, t0 + 0.4) + 15, dist=9.5, pitch=2, lens=45, push=0.06, ignore=("Harry",))


@S(23, 93, 102, "MED: Ryan grins and points 'Look. The poor kid found a pet.' kids laugh (bruh)")
def s16(t0, t1):
    L = hallway(students=True)
    r = ryan(t0, t1, "toothy", loc=(HX - 3.4, HY - 4.0, 0), rot=30)
    mo.idle(r, t0, t1, 1.0)
    acting.ladder(r, t0 + 0.1, "surprise_laugh")
    mo.talk_cadence(r, V.w(95), t1, V.words, stress=("poor", "pet.\""), expr_on={"pet.\"": "laugh_smug"}, hands=True)
    mo.point(r, V.w(96), (HX - 7, HY - 2, 1.5), hold=1.2, expr="laugh_smug")
    k = kid(1, t0, t1, "joy", loc=(HX - 0.8, HY - 1.5, 0), rot=60)
    mo.laugh(k, V.w(99), t1, hz=4)
    med(t0, t1, r, yaw=20, d=10)


@S(24, 102, 109, "TRUCK: dusk, Harry walks home alone (fast-forward whoosh)")
def s17(t0, t1):
    L = T.main_street(closed=False, extras=False, cops=False)
    V.look = "ref_day"
    look.cinematic("ref_day", focus=(-3, 20, 3), blur=0.4)
    h = harry(t0, t1, "sad", loc=(-3, 10, 0), rot=180)
    mo.walk(h, t0, t1, [(-3, 10, 0), (-3, 22, 0)], mood="sad")
    cams.truck(t0, t1, (-3, 16, 4.0), d=12, h=4.2, lens=30, heading=-20, tilt=-2)
    sfx(t0, "whoosh", 0.8)


@S(25, 109, 114, "MED: Harry hands a pizza box to Grandma Pearl at her door, she smiles")
def s18(t0, t1):
    L = T.main_street(closed=False, extras=False, cops=False)
    V.look = "ref_day"
    look.cinematic("ref_day", focus=(-10, 22, 3))
    h = harry(t0, t1, "happy", loc=(-8.5, 20, 0), rot=-110)
    g = cast.make("grandma", t0, t1, "smile", loc=(-11.5, 21.2, 0), rot=70, prop=False, cine=True)
    mo.turn(h, t0, target=(-11.5, 17.0, 4), dur=2); mo.turn(g, t0, target=(-8.5, 17.0, 4), dur=2)
    pz = box("pizza", (2.0, 2.0, 0.35), (0, 0, 0), mat("pz", hexc("#d9a35a"), 0.8), 0.03)
    mo.attach(h, pz, "armR", offset=(0, -1.1, -0.15), rot=(0, 0, 0))
    mo.strike(h, t0 + 0.1, {"armR": (80, 0, 0), "elbowR": 15}, expr="happy")
    mo.reach(g, V.w(112), (-9.9, 20.4, 3.4), hand="r", expr="joy")
    still_cam(t0, t1, (-10, 9.8, 4.6), (-10, 20.6, 3.8), lens=30, push=0.08, fstop=3.5)


@S(26, 114, 120, "MED: Harry fixes a neighbour's laptop at the kitchen table, Dad gives a thumbs-up")
def s19(t0, t1):
    L = T.kitchen(night=False)
    look.cinematic("ref_matte", focus=L["focus"])
    sp = L["cast_spots"]
    h = harry(t0, t1, "determined", loc=sp[0][:3], rot=sp[0][3])
    d = cast.make("dad", t0, t1, "smile", loc=sp[1][:3], rot=sp[1][3], prop=False, cine=True, name="Neighbour")
    lap = SG.laptop("lap", (sp[0][0] - 0.2, sp[0][1] - 2.4, 3.3), 180, title="Settings", posts=["Wi-Fi: CONNECTED", "Fixed!"])
    mo.reach(h, t0 + 0.2, (sp[0][0] - 0.2, sp[0][1] - 2.3, 3.6), hand="r", expr="determined")
    mo.strike(d, V.w(118), {"armR": (100, 10, 0), "elbowR": 80}, expr="joy")
    acting.face(h, V.w(119), "happy")
    loc, tgt, lens = L["cams"]["wide"]
    still_cam(t0, t1, loc, tgt, lens=lens, push=0.10, fstop=4.0)


def night_desk():
    """Harry's bedroom desk set at REAL seated heights (CLEAN_ANIMATION 2): chair seat 1.5, desk top 2.8,
    old beige CRT monitor with a glowing screen, keyboard on the front edge. Hides the room's tall desk."""
    L = T.bedroom(morning=False, night=True)
    V.look = "ref_night"
    look.cinematic("ref_practical", focus=(608, 16, 4))
    for o in bpy.context.scene.objects:
        if o.name.startswith(("bd_desk", "bd_lamp", "bd_mug", "bd_note")):
            o.hide_render = True; o.hide_viewport = True
    wood = mat("dk_wood", hexc("#7a5636"), 0.7)
    box("dk_top", (6.0, 3.2, 0.2), (608, 17.0, 2.7), wood, 0.04)
    for sx in (-1, 1):
        for sy in (-1, 1):
            box(f"dk_leg{sx}{sy}", (0.25, 0.25, 2.6), (608 + sx * 2.8, 17.0 + sy * 1.4, 1.3), wood, 0.03)
    beige = mat("crt_m", hexc("#d8ccb0"), 0.7)
    box("crt_body", (2.8, 2.4, 2.3), (608, 17.9, 4.0), beige, 0.12)
    box("crt_neck", (1.2, 0.8, 0.3), (608, 17.9, 2.95), beige, 0.05)
    SG.screen("crt", [("build_school()", "#7cff9a"), ("+1 brick", "#ffffff")], (608, 16.68, 4.05), w=2.2, h=1.7,
              bg="#0b1020", size=0.26, bezel="#cdbf9f", glow=3.0)
    kb = box("kbd", (2.4, 0.8, 0.12), (608, 15.85, 2.86), mat("kbd_m", hexc("#e6e0d0"), 0.6), 0.03)
    seat = mat("chair_m", hexc("#3a3f4a"), 0.6)
    box("ch_seat", (2.2, 2.0, 0.3), (608, 14.3, 1.35), seat, 0.06)
    box("ch_back", (2.2, 0.3, 2.6), (608, 13.25, 2.8), seat, 0.08)
    cyl("ch_post", 0.16, 1.2, (608, 14.3, 0.6), mat("ch_p", hexc("#222222"), 0.4, 0.6), 12)
    light("crt_glow", "AREA", (608, 16.4, 4.1), 450, hexc("#9cc4ff"), 2.0, target=(608, 14.3, 4.4))
    light("crt_rim", "AREA", (611, 11.5, 7), 300, hexc("#ffb36b"), 3, target=(608, 14.3, 4.4))
    return dict(seat=(608, 14.3, 1.5), kbdL=(607.45, 15.8, 2.95), kbdR=(608.55, 15.8, 2.95), screen=(608, 16.6, 4.05))


def fit_desk_to_hands(h, t, D):
    """CONTACT BY CONSTRUCTION: R6 arms are short (1.55) and the reach solver clamps, so instead of hoping the fists
    reach a guessed keyboard, pose the typing arms first, MEASURE where the fists are, then move the keyboard/desk/
    monitor so the keys sit right under the fists (fist bottom ~0.22 below its centre)."""
    hl = Vector(hand_pos(h, t, "armL")); hr = Vector(hand_pos(h, t, "armR"))
    mid = (hl + hr) / 2
    kb = bpy.data.objects["kbd"]
    dz = (mid.z - 0.24 - 0.06) - kb.location.z
    dy = mid.y + 0.05 - kb.location.y
    for o in bpy.context.scene.objects:
        if o.name.startswith(("dk_top", "kbd", "crt")) and o.parent is None:
            o.location.z += dz; o.location.y += dy
        elif o.name.startswith("dk_leg"):
            o.location.y += dy
            o.scale.z = (2.6 + dz) / 2.6; o.location.z = (2.6 + dz) / 2
    kb.scale.x = max(1.0, (abs(hr.x - hl.x) + 0.9) / 2.4)
    D["kbdL"] = (hl.x, hl.y, mid.z - 0.24); D["kbdR"] = (hr.x, hr.y, mid.z - 0.24)
    D["screen"] = (D["screen"][0], D["screen"][1] + dy, D["screen"][2] + dz)
    return D


def seated_harry(t0, t1, D, expr="determined", typing_until=None):
    h = harry(t0, t1, expr, loc=(D["seat"][0], D["seat"][1] - 0.15, 0), rot=180)
    mo.sit(h, t0 - 0.7, seat_h=1.5)       # seated and settled BEFORE the shot starts (sit keys arms at t+6 f)
    qa.sit(h)
    # typing: IK the fists to reachable points in front of the belly, keep them there with a small typing wobble,
    # THEN build the keyboard under where the fists actually are (contact by construction)
    body = {"torso": (0, 10, 0)}
    root = Vector((D["seat"][0], D["seat"][1] - 0.15, 0))
    tL = (root.x - 0.6, root.y + 1.25, 2.95); tR = (root.x + 0.6, root.y + 1.25, 2.95)
    tu = typing_until if typing_until is not None else t1
    mo.reach(h, t0 - 0.25, tL, hand="l", body=body); mo.reach(h, t0 - 0.25, tR, hand="r", body=body)
    mo.contact(h, t0 - 0.1, tu, tL, hand="l", body=body, wobble=0.05, seed=1)
    mo.contact(h, t0 - 0.1, tu, tR, hand="r", body=body, wobble=0.05, seed=2)
    fit_desk_to_hands(h, t0 + 0.3, D)
    qa.touch(h, "armL", D["kbdL"], t0 + 0.1, tu, tol=0.45); qa.touch(h, "armR", D["kbdR"], t0 + 0.1, tu, tol=0.45)
    mo.look_at(h, t0, D["screen"])
    qa.look(h, D["screen"], t0 + 0.2, t1, tol=35)
    return h


@S(27, 120, 127, "OTS: midnight - over Harry's shoulder, the old CRT glows with code; he types")
def s20a(t0, t1):
    D = night_desk()
    h = seated_harry(t0, t1, D, "determined")
    acting.face(h, V.w(124), "sleepy"); acting.face(h, V.w(126), "determined")
    still_cam(t0, t1, (610.0, 10.6, 5.6), (608.0, 16.6, 4.1), lens=34, push=0.08, fstop=2.2)


@S(28, 127, 133, "MCU (from the screen): Harry's face lit blue, typing, determined -> small smile")
def s20b(t0, t1):
    D = night_desk()
    for o in bpy.context.scene.objects:
        if o.name.startswith(("crt", "Crt")) and o.type != "LIGHT":
            o.hide_render = True; o.hide_viewport = True
    h = seated_harry(t0, t1, D, "determined")
    acting.face(h, V.w(131), "content")
    hd = Vector(head(h, t0 + 0.3, 0.0))
    still_cam(t0, t1, (608.8, 19.5, hd.z + 0.3), (hd.x, hd.y, hd.z - 0.9), lens=30, push=0.06, fstop=2.4)


@S(29, 133, 138, "INSERT: the game on screen, a school built brick by brick")
def s21(t0, t1):
    screen_insert(t0, t1, [("BUILD YOUR SCHOOL", "#ffffff"), ("+1 BRICK   +1 BRICK", "#f2c14e"), ("v0.1", "#7a8aa8")])


@S(30, 138, 144, "MCU (from the screen): Harry grins at his game, quick fist pump, back to the keys")
def s22(t0, t1):
    D = night_desk()
    for o in bpy.context.scene.objects:
        if o.name.startswith(("crt", "Crt")) and o.type != "LIGHT":
            o.hide_render = True; o.hide_viewport = True
    h = seated_harry(t0, t1, D, "content", typing_until=V.w(140))
    mo.strike(h, V.w(141), {"armR": (120, 10, 0), "elbowR": 95}, expr="joy")
    mo.strike(h, V.w(141) + 0.8, {"armR": (62, -4, -6), "elbowR": 38}, expr="content")
    hd = Vector(head(h, t0 + 0.3, 0.0))
    still_cam(t0, t1, (608.8, 19.5, hd.z + 0.3), (hd.x, hd.y, hd.z - 1.0), lens=28, push=0.05, fstop=2.4)


@S(31, 144, 157, "INSERT: PLAYERS ONLINE 10 -> 10,000 -> 4,000,000 (pop, pop)")
def s23(t0, t1):
    c = screen_insert(t0, t1, [("PLAYERS ONLINE", "#ffffff"), (" ", "#ffffff")], push=0.25)
    o = (900.0, 0.0, 0.0)
    nums = [("10", "#7cff9a", t0, V.w(150)), ("10,000", "#f2c14e", V.w(150), V.w(154)), ("4,000,000", "#ff5a3c", V.w(154), t1 + 1)]
    for k, (txt, col, a, b) in enumerate(nums):
        ob = SG.label(f"cnt{k}", txt, (o[0], o[1] + 2.9, o[2] + 5.0), 0.75, col, "bold", 2.0, rot=(90, 0, 0))
        for obj in [ob] + list(getattr(ob, "children", [])):
            obj.hide_render = True; obj.keyframe_insert("hide_render", frame=1)
            obj.hide_render = False; obj.keyframe_insert("hide_render", frame=F(a))
            obj.hide_render = True; obj.keyframe_insert("hide_render", frame=F(b))
    sfx(V.w(149), "pop", 0.8); sfx(V.w(153), "pop", 0.8)


@S(32, 157, 166, "MED: jaw-drop Harry, then drops coins into his SCHOOL FUND jar (cha-ching)")
def s24(t0, t1):
    L = T.bedroom(morning=False, night=True)
    V.look = "ref_night"
    look.cinematic("ref_practical", focus=(608, 16, 5))
    h = harry(t0, t1, "pop_shock", loc=(607, 13.8, 0), rot=200)
    acting.ladder(h, t0 + 0.05, "surprise_laugh")
    T.jar("jar", (609.5, 16.2, 3.55), "SCHOOL FUND", fill="#d4a017", h=1.6, r=0.6)
    coin = cyl("coin", 0.2, 0.05, (0, 0, 0), mat("coin_m", hexc("#f2c14e"), 0.2, 1.0), 16)
    mo.attach(h, coin, "armR", offset=(0, -0.4, -0.1))
    mo.reach(h, V.w(163), (609.5, 16.0, 5.4), hand="r", expr="content")
    med(t0, t1, h, yaw=160, d=9.0)
    sfx(V.we(157), "cashier", 0.9); sfx(V.w(164) + 0.3, "coin", 0.7)


@S(33, 166, 171, "MED: kitchen, Harry opens a letter, reads it")
def s25(t0, t1):
    L = T.kitchen(night=False)
    look.cinematic("ref_matte", focus=L["focus"])
    sp = L["cast_spots"][0]
    h = harry(t0, t1, "neutral", loc=sp[:3], rot=sp[3])
    letter = box("letter", (1.6, 0.04, 2.1), (0, 0, 0), mat("paper", hexc("#f4ecd6"), 0.8), 0.01)
    mo.read(h, t0 + 0.2, prop=letter, dur=t1 - t0 - 0.4, react="shock", react_t=V.w(170))
    med(t0, t1, h, yaw=-10, d=8.5)
    sfx(t0 + 0.2, "paper", 0.7)


@S(34, 171, 176, "INSERT: the letter - BLOX CITY HIGH WILL CLOSE (frontal, fully in frame)")
def s26(t0, t1):
    o = (980.0, 0.0, 0.0)
    cz = 6.0
    # wooden backboard behind the letter (vertical), letter pinned flat on it, camera straight on
    box("lt_board", (14, 0.4, 16), (o[0], o[1] + 2.0, cz), pbr.get("planks", tint="#b88a5a", tile=3), 0.05)
    box("lt_paper", (4.4, 0.04, 5.8), (o[0], o[1] + 1.75, cz), mat("lt_pap", hexc("#f6efdc"), 0.85), 0.0)
    box("lt_hdr", (4.4, 0.05, 0.9), (o[0], o[1] + 1.72, cz + 2.45), mat("lt_hdrm", hexc("#1f3a6b"), 0.7), 0.0)
    SG.label("lt_h", "BLOX CITY HIGH", (o[0], o[1] + 1.68, cz + 2.33), 0.42, "#ffffff", "bold", 0, rot=(90, 0, 0))
    SG.label("lt_n", "OFFICIAL NOTICE", (o[0], o[1] + 1.70, cz + 1.45), 0.30, "#333333", "bold", 0, rot=(90, 0, 0))
    SG.label("lt_b1", "THIS SCHOOL", (o[0], o[1] + 1.70, cz + 0.55), 0.52, "#111111", "bold", 0, rot=(90, 0, 0))
    SG.label("lt_b2", "WILL CLOSE", (o[0], o[1] + 1.70, cz - 0.25), 0.62, "#7a0000", "bold", 0, rot=(90, 0, 0), extrude=0.01)
    SG.label("lt_b3", "LAND SOLD:\nFUTURE PARKING LOT", (o[0], o[1] + 1.70, cz - 1.35), 0.30, "#1d1d1d", "bold", 0,
             rot=(90, 0, 0), spacing=1.15)
    SG.label("lt_sig", "- The Principal", (o[0] + 0.9, o[1] + 1.70, cz - 2.40), 0.24, "#333333", "hand", 0, rot=(90, 0, 0))
    light("lt_k", "AREA", (o[0] - 3, o[1] - 7, cz + 4), 700, hexc("#ffe2b8"), 4, target=(o[0], o[1] + 1.7, cz))
    light("lt_f", "AREA", (o[0] + 4, o[1] - 7, cz - 1), 250, hexc("#ffffff"), 4, target=(o[0], o[1] + 1.7, cz))
    look.cinematic("ref_matte", focus=(o[0], o[1] + 1.7, cz))
    still_cam(t0, t1, (o[0], o[1] - 11.5, cz), (o[0], o[1] + 1.7, cz), lens=36, push=0.10, fstop=8.0)


@S(35, 176, 185, "WIDE: SOLD - FUTURE PARKING LOT sign, Ryan and his dad laugh in front of the school")
def s27(t0, t1):
    L = exterior(students=False)
    sx0, sy0, sz0 = EX + 2, EY - 1.5, 6.6
    SG.sign("sold", " ", (sx0, sy0, sz0), w=7.4, h=3.2, bg="#c62828", fg="#ffffff")
    SG.label("sold_a", "SOLD!", (sx0, sy0 - 0.2, sz0 + 0.55), 1.25, "#ffffff", "bold", 0, rot=(90, 0, 0))
    SG.label("sold_b", "FUTURE PARKING LOT", (sx0, sy0 - 0.2, sz0 - 0.85), 0.85, "#ffffff", "bold", 0, rot=(90, 0, 0))
    for k in (-1, 1):
        box(f"sold_post{k}", (0.3, 0.3, sz0), (sx0 + k * 3.2, sy0 + 0.2, sz0 / 2 - 0.8), mat("postm", hexc("#5a4632"), 0.8), 0.02)
    r = ryan(t0, t1, "laugh_smug", loc=(EX + 5.2, EY - 7, 0), rot=-15)
    d = rdad(t0, t1, "grin", loc=(EX - 1.4, EY - 7.5, 0), rot=12)
    mo.point(r, t0 + 0.4, (sx0, sy0, sz0), hold=1.0); mo.laugh(r, t0 + 1.6, t1)
    mo.stance(d, t0, "hands_hips"); mo.laugh(d, V.w(183), t1, hz=3)
    still_cam(t0, t1, (EX + 2, EY - 29, 4.6), (EX + 2, EY - 4, 4.8), lens=26, push=0.10, fstop=4.0)


@S(36, 185, 193, "LOW: Ryan's dad rubs his hands, evil grin (dun dun dunnn)")
def s28(t0, t1):
    L = exterior(students=False)
    d = rdad(t0, t1, "grin", loc=(EX + 2, EY - 6, 0), rot=20)
    mo.idle(d, t0, t1, 0.6)
    mo.strike(d, t0 + 0.2, {"armL": (60, -12, 0), "armR": (60, -12, 0), "elbowL": 70, "elbowR": 70}, expr="smug_up")
    mo.strike(d, V.w(191), {"head": (0, -10, 0)}, expr="toothy")
    scam(t0, t1, head(d, t0, -1.6), yaw=10, dist=9.5, pitch=-6, lens=28, ignore=("RyanDad",))
    sfx(V.we(192), "rise", 0.6)


@S(37, 193, 202, "WIDE: Monday, a black car pulls up at the gates, students turn and stare")
def s29(t0, t1):
    L = exterior(students=False)
    car = T.car("bcar", (EX + 36, EY - 4, 0), 90, "#141416")
    car.keyframe_insert("location", frame=F(t0)); car.location.x = EX + 8; car.keyframe_insert("location", frame=F(V.w(198) + 0.4))
    for k, (x, y, r) in enumerate([(EX - 1, EY + 0.5, 150), (EX + 3, EY + 1.5, 170), (EX + 7, EY + 1.0, -170)]):
        c = kid(k, t0, t1, "neutral", loc=(x, y, 0), rot=r)
        mo.turn(c, V.w(198) + 0.2 * k, target=(EX + 8, EY - 4, 2), expr="pop_shock")
    still_cam(t0, t1, (EX + 2, EY - 24, 4.5), (EX + 6, EY - 3, 3.0), lens=30, push=0.08, fstop=5.0)


@S(38, 202, 209, "LOW: Harry steps out - same hoodie, same shoes - calm smile")
def s30(t0, t1):
    L = exterior(students=True)
    T.car("bcar", (EX + 8, EY - 4, 0), 90, "#141416"); car_door(EX + 8, EY - 4)
    h = harry(t0, t1, "content", loc=(EX + 6, EY - 8.5, 0), rot=0); shoe_hole(h)
    mo.walk(h, t0, t0 + 1.3, [(EX + 8.0, EY - 7.4, 0), (EX + 6, EY - 8.5, 0)])
    mo.reach(h, V.w(205), (EX + 6.4, EY - 9.1, 2.3), hand="l", expr="smug_up")
    scam(t0, t1, head(h, t0 + 1.3, -1.5), yaw=face_yaw(h, t0 + 1.4) - 10, dist=10, pitch=3, lens=28, ignore=("Harry",))


@S(39, 209, 223, "TWO-SHOT: Grandpa follows with a blue folder under his arm, gives Harry a wink")
def s31(t0, t1):
    L = exterior(students=True)
    T.car("bcar", (EX + 8, EY - 4, 0), 90, "#141416"); car_door(EX + 8, EY - 4)
    h = harry(t0, t1, "content", loc=(EX + 2, EY - 9, 0), rot=10)
    g = cast.make("grandpa", t0, t1, "smile", loc=(EX + 6, EY - 9.5, 0), rot=-10, prop=False, cine=True)
    fo = box("folder", (1.6, 0.2, 2.0), (0, 0, 0), mat("fold", hexc("#2f7bff"), 0.6), 0.03)
    mo.attach(g, fo, "armR", offset=(0, -0.3, -0.2), rot=(0, 0, 0))
    mo.walk(g, t0, t0 + 1.6, [(EX + 8.0, EY - 7.4, 0), (EX + 6, EY - 9.5, 0)])
    mo.turn(g, V.w(215), target=h, expr="wink")
    mo.nod(h, V.w(220), 2)
    cams.two_shot(t0, t1, (EX + 2, EY - 9, 0), (EX + 6, EY - 9.5, 0), lens=28, d=12, h=4.4, yaw=-8)


@S(40, 223, 233, "MED: the principal rushes up, stares 'Harry? ...ownership meeting?'")
def s32(t0, t1):
    L = exterior(students=False)
    p = principal(t0, t1, "pop_shock", loc=(EX + 2, EY - 6, 0), rot=-10)
    mo.idle(p, t0, t1, 1.0)
    mo.gasp(p, V.w(225))
    mo.talk_cadence(p, V.w(226), t1, V.words, stress=("Harry?", "ownership"), expr_on={"Harry?": "pop_shock", "ownership": "confused"}, hands=True)
    med(t0, t1, p, yaw=-8, d=9.5)


@S(41, 233, 237, "MCU: Ryan freezes, jaw drops 'Ownership... what?' (record scratch, FAHHH)")
def s33(t0, t1):
    L = exterior(students=True)
    r = ryan(t0, t1, "smug", loc=(EX - 2, EY - 6, 0), rot=10)
    mo.shock(r, V.w(234), expr="pop_shock")
    acting.dart(r, V.w(234) + 0.4, V.w(235))
    mo.talk_cadence(r, V.w(235), t1, V.words, stress=("what?\"",), expr_on={"what?\"": "shock"}, hands=True)
    mo.strike(r, V.w(236), {"armL": (150, 20, 0), "armR": (150, 20, 0), "elbowL": 120, "elbowR": 120}, expr="scream")
    med(t0, t1, r, yaw=10, d=8.0, lens=45)


@S(42, 237, 245, "WIDE: auditorium full of kids, the principal taps the mic")
def s34(t0, t1):
    A_ = auditorium(crowd=True)
    p = principal(t0, t1, "neutral", loc=(A_["pod"][0] + 0.4, A_["pod"][1] + 1.6, A_["stage_z"]), rot=0)
    mo.idle(p, t0, t1, 0.6)
    mo.reach(p, V.w(242), (AUD[0] - 7.2, AUD[1] + 35.3, A_["stage_z"] + 4.4), hand="r", expr="neutral")
    still_cam(t0, t1, (AUD[0] + 1, AUD[1] + 4, 11), (AUD[0] - 4, AUD[1] + 36, 6.5), lens=48, push=0.12, fstop=6.0)
    sfx(V.w(242), "thud", 0.5)


@S(43, 245, 256, "MED: principal at the podium 'Blox City High has a new owner...'")
def s35(t0, t1):
    A_ = auditorium(crowd=False)
    p = principal(t0, t1, "smile", loc=(A_["pod"][0] + 0.4, A_["pod"][1] + 1.6, A_["stage_z"]), rot=0)
    mo.idle(p, t0, t1, 0.6)
    mo.talk_cadence(p, t0, t1, V.words, stress=("owner.", "game"), expr_on={"owner.": "happy"}, hands=True)
    med(t0, t1, p, yaw=0, d=10, up=-0.6)


@S(44, 256, 262, "MED: front row - Ryan and his dad lean forward, kids whisper")
def s36(t0, t1):
    A_ = auditorium(crowd=True)
    r = ryan(t0, t1, "confused", loc=(AUD[0] - 2, AUD[1] + 20, 0), rot=180)
    d = rdad(t0, t1, "smug", loc=(AUD[0] - 5.5, AUD[1] + 20, 0), rot=180)
    k = kid(2, t0, t1, "gasp", loc=(AUD[0] + 2, AUD[1] + 20.5, 0), rot=150)
    mo.strike(r, t0 + 0.3, {"torso": (0, 14, 0)}, expr="confused")
    mo.hand_to_face(k, t0 + 0.4, "r", "mouth", expr="gasp")
    still_cam(t0, t1, (AUD[0] - 2, AUD[1] + 31, 6.5), (AUD[0] - 2.5, AUD[1] + 20, 4.5), lens=32, push=0.1, fstop=3.0)


@S(45, 262, 266, "MCU: Harry at the side of the stage, she looks at him, he gives a small nod")
def s37(t0, t1):
    A_ = auditorium(crowd=False)
    h = harry(t0, t1, "content", loc=(AUD[0] + 8, AUD[1] + 36, A_["stage_z"]), rot=-30)
    mo.idle(h, t0, t1, 0.6)
    mo.nod(h, t0 + 0.6, 1)
    mcu(t0, t1, h, -30, "s37", d=8.6)


@S(46, 266, 269, "WIDE: 'Harry built it.' - the whole auditorium gasps (boom)")
def s38(t0, t1):
    A_ = auditorium(crowd=True)
    h = harry(t0, t1, "smile", loc=(AUD[0] + 4, AUD[1] + 36, A_["stage_z"]), rot=0)
    for k, (x, y) in enumerate([(-6, 22), (-2, 21), (3, 22), (7, 21)]):
        c = kid(k, t0, t1, "neutral", loc=(AUD[0] + x, AUD[1] + y, 0), rot=180)
        mo.gasp(c, V.we(268) - 0.1 + 0.05 * k)
        acting.face(c, V.we(268), "pop_shock")
    still_cam(t0, t1, (AUD[0] + 2, AUD[1] + 8, 9), (AUD[0] + 3, AUD[1] + 36, 6), lens=28, push=0.2, fstop=5.0)
    sfx(V.we(268), "boom", 0.9); sfx(V.we(268) + 0.05, "gasp", 0.8)


@S(47, 269, 276, "MED: Ryan's dad deflates, Ryan facepalms (sad trombone)")
def s39(t0, t1):
    A_ = auditorium(crowd=True)
    d = rdad(t0, t1, "pop_shock", loc=(AUD[0] - 5.5, AUD[1] + 20, 0), rot=170)
    r = ryan(t0, t1, "pop_shock", loc=(AUD[0] - 2, AUD[1] + 20, 0), rot=190)
    mo.strike(d, t0 + 0.4, {"head": (0, 18, 0), "torso": (0, 12, 0), "armL": (0, 2, 0), "armR": (0, 2, 0)}, expr="sad_tear")
    mo.hand_to_face(r, V.w(272), "r", "forehead", expr="worried")
    still_cam(t0, t1, (AUD[0] - 3.5, AUD[1] + 30, 6.2), (AUD[0] - 3.8, AUD[1] + 20, 4.8), lens=32, push=0.12, fstop=3.0)


@S(48, 276, 283, "TWO-SHOT: later, Ryan walks up to Harry by the lockers, rubbing his neck")
def s40(t0, t1):
    L = hallway(students=False)
    HA, RA = (HX - 7.6, HY - 3.0, 0), (HX - 3.6, HY - 3.0, 0)
    h = harry(t0, t1, "neutral", loc=HA, rot=-50)
    r = ryan(t0, t1, "worried", loc=RA, rot=50)
    mo.walk(r, t0, t0 + 1.4, [(HX - 0.6, HY - 4.5, 0), RA], mood="sad")
    mo.turn(r, t0 + 1.45, target=(HX - 7.6, HY - 6.5, 4))
    mo.turn(h, t0 + 0.6, target=(HX - 3.6, HY - 6.5, 4))
    mo.hand_to_face(r, t0 + 1.9, "r", "cheek", expr="worried_dart")
    still_cam(t0, t1, (HX - 5.4, HY - 15.5, 4.6), (HX - 5.6, HY - 3, 3.8), lens=32, push=0.10, fstop=3.5)


@S(49, 283, 289, "MED: Ryan, eyes darting 'So... are you kicking me out?'")
def s41(t0, t1):
    L = hallway(students=False)
    r = ryan(t0, t1, "worried", loc=(HX - 3.4, HY - 4.0, 0), rot=40)
    acting.dart(r, t0, V.w(285))
    mo.talk_cadence(r, V.w(284), t1, V.words, stress=("kicking",), expr_on={"kicking": "sad_tear"}, hands=False)
    med(t0, t1, r, yaw=25, d=9.0)


@S(50, 289, 300, "TWO-SHOT: Ryan's books slip, Harry kneels and picks them up for him (aww)")
def s42(t0, t1):
    L = hallway(students=False)
    HA, RA = (HX - 7.6, HY - 3.0, 0), (HX - 3.6, HY - 3.0, 0)
    h = harry(t0, t1, "smile", loc=HA, rot=-50)
    r = ryan(t0, t1, "worried", loc=RA, rot=50)
    mo.turn(r, t0, target=(HX - 7.6, HY - 6.5, 4), dur=2); mo.turn(h, t0, target=(HX - 3.6, HY - 6.5, 4), dur=2)
    mo.strike(r, t0 + 0.1, {"armL": (62, -8, 0), "armR": (62, -8, 0), "elbowL": 55, "elbowR": 55})
    hl = Vector(hand_pos(r, t0 + 0.3, "armL")); hr = Vector(hand_pos(r, t0 + 0.3, "armR")); mid = (hl + hr) / 2
    tf = V.w(291)
    bk = books("bk3", (mid.x, mid.y - 0.3, mid.z + 0.1), t_fall=tf, seed=1, hold=(r, t0), push=(-0.6, -1, 0), power=1.6)
    mo.strike(r, tf + 0.05, {"armL": (20, 10, 0), "armR": (20, 10, 0)}, expr="pop_shock")
    kneel(h, V.w(296), expr="content")
    bpy.context.scene.frame_set(F(tf + 1.5)); landed = tuple(bk[0].matrix_world.translation)
    mo.reach(h, V.w(297), landed, hand="r", body={"hipz": -1.25, "torso": (0, 24, 0)}, expr="smile")
    acting.face(r, V.w(299), "sad_tear")
    still_cam(t0, t1, (HX - 5.6, HY - 15, 3.6), (HX - 5.6, HY - 3, 2.8), lens=30, push=0.08, fstop=3.5)
    sfx(tf + 0.5, "thud", 0.5)


@S(51, 300, 311, "MED: Harry stands, hands Ryan his books 'No. But from today...'")
def s43(t0, t1):
    L = hallway(students=False)
    h = harry(t0, t1, "content", loc=HP, rot=-40)
    r = ryan(t0, t1, "sad_tear", loc=(HX - 3.4, HY - 4.0, 0), rot=50)
    bk = books("bk4", (0, 0, 0), n=2)
    for b in bk:
        mo.attach(h, b, "armR", offset=(0, -0.6, -0.1), rot=(0, 0, 0))
    mo.reach(h, t0 + 0.3, r.hip if hasattr(r, "hip") else (HX - 3.6, HY - 4.2, 2.6), hand="r", expr="content")
    mo.talk_cadence(h, t0, t1, V.words, stress=("No.", "nobody"), expr_on={"nobody": "determined"}, hands=False)
    acting.face(r, V.w(306), "relief")
    still_cam(t0, t1, (HX - 4.6, HY - 15.0, 4.6), (HX - 5.0, HY - 2.6, 3.8), lens=32, push=0.08, fstop=3.0)


@S(52, 311, 317, "WIDE: Harry waves Milo up onto the stage, Milo hurries over")
def s44(t0, t1):
    A_ = auditorium(crowd=True)
    z = A_["stage_z"]
    h = harry(t0, t1, "happy", loc=(AUD[0] + 4, AUD[1] + 36, z), rot=-20)
    m = milo(t0, t1, "pop_shock", loc=(AUD[0] + 12, AUD[1] + 36, z), rot=40)
    mo.strike(h, t0 + 0.2, {"armR": (160, 25, 0), "elbowR": 20}, expr="joy")
    mo.walk(m, V.w(313), t1, [(AUD[0] + 12, AUD[1] + 36, z), (AUD[0] + 7, AUD[1] + 35.5, z)])
    acting.face(m, V.w(314), "joy")
    still_cam(t0, t1, (AUD[0] + 6, AUD[1] + 14, 7), (AUD[0] + 6, AUD[1] + 36, 5.5), lens=30, push=0.1, fstop=4.0)


@S(53, 317, 328, "WIDE: FREE LUNCH + NEW SHOES banner drops, kids cheer, Milo jumps (cheer)")
def s45(t0, t1):
    A_ = auditorium(crowd=True, banner="FREE LUNCH\n+ NEW SHOES")
    z = A_["stage_z"]
    h = harry(t0, t1, "joy", loc=(AUD[0] - 1.2, AUD[1] + 36, z), rot=0)
    m = milo(t0, t1, "joy", loc=(AUD[0] + 2.0, AUD[1] + 35.5, z), rot=-10)
    acting.act(m, V.w(318), "cheer", expr="joy"); acting.act(h, V.w(320), "cheer", expr="joy")
    for k, (x, y) in enumerate([(-6, 22), (-2, 21), (3, 22), (7, 21)]):
        c = kid(k, t0, t1, "joy", loc=(AUD[0] + x, AUD[1] + y, 0), rot=180)
        acting.act(c, V.w(318) + 0.1 * k, "cheer", expr="joy")
    still_cam(t0, t1, (AUD[0] + 0.4, AUD[1] + 13, 9.5), (AUD[0] + 0.4, AUD[1] + 36, 9.0), lens=28, push=0.12, fstop=6.0)
    sfx(V.w(318), "cheer", 0.7)


@S(54, 328, 338, "TILT: Harry's feet - the hole is still there - then up to his proud smile (ding)")
def s46(t0, t1):
    L = hallway(students=False)
    h = harry(t0, t1, "content", loc=HP, rot=0); shoe_hole(h)
    mo.idle(h, t0, t1, 0.6)
    acting.face(h, V.w(334), "happy")
    c = Cam("Cam_tilt", 40)
    c.key(t0, (HX - 6.6, HY - 9.0, 0.9), (HX - 5.9, HY - 2.5, 0.5), 40, focus=(HX - 5.8, HY - 2.6, 0.4), fstop=2.4)
    c.key(V.w(333), (HX - 6.6, HY - 9.0, 1.0), (HX - 5.9, HY - 2.5, 0.6), 40, focus=(HX - 5.8, HY - 2.6, 0.4), fstop=2.4)
    c.key(t1, (HX - 6.4, HY - 11.5, 5.4), (HX - 6.0, HY - 2.0, 5.6), 40, focus=(HX - 6, HY - 2, 5.6), fstop=2.8, ease="EASE_IN_OUT")
    cams.micro(c, deg=0.3, loc=0.01, period=2.0)


@S(55, 338, None, "END CARD: Harry waves, points at the pop-ups (heart/share/follow click/comment added in post)")
def s47(t0, t1):
    L = hallway(students=False)
    h = harry(t0, t1, "happy", loc=HP, rot=-15)
    mo.idle(h, t0, t1, 0.8)
    mo.strike(h, V.w(338), {"armR": (150, 20, 0), "elbowR": 30}, expr="joy")
    mo.point(h, V.w(341), (HP[0] + 3, HP[1] - 6, 5.5), arm="armL", hold=1.0, expr="happy")
    acting.face(h, V.w(346), "smug_up")
    med(t0, t1, h, yaw=-10, d=14, up=-1.4, lens=35)
