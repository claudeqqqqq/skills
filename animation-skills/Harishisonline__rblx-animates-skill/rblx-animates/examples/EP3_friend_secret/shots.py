"""friend_secret - EP3 Blox City Day 02 "I Told ONE Secret. By Lunch, Everyone Knew." (kit v4.2, 2026-11-16).
Alex alex_ep1 narration audio/voice.wav (words.json, 328 words); final mix audio/mix_nomusic.wav = 100.85 s.
Cast: Leo = cast host recoloured (green zip hoodie, dark hair, H patch hidden); Max = cast bestie recoloured (burnt-orange
jacket, black hair) + props3.limited_hat from the cafeteria on; Chase = rich kid (purple polo, slick blond hair, gold chain);
classmates = shotlib.extra kids. Sets: school hallway + exterior (town), NEW cafeteria, NEW bus interior, bedroom (town, night
with the duck night-light as key / morning), NEW camp (props3 tents, camp_ground, camp_lamp) night storm + morning.
Shot grammar: docs/CLEAN_ANIMATION.md (MCU to lens, OTS, straight-on inserts, aftermath; transitions hidden in cuts)."""
from shotkit import *
from rbx import story
from rbx.story import *
from rbx.shotlib import *
from rbx import props3 as P3, cast, town as T, motion as mo, signs as SG, crowd as C, chars, acting, pbr, qa, cams, look
from rbx.core import Cam, box, cyl, sphere, mat, hexc, light, F
import bpy, math, os
from mathutils import Vector

V = Video(__file__); story.bind(V)
install_snaps()
look.STYLE = "clean"; cast.CLEAN = True
V.end = math.ceil(100.85 * 30) / 30
SCR = os.path.join(V.dir, "screens")
scr = lambda n: os.path.join(SCR, n)

HX, HY = T.ORIGINS["school_hallway"][:2]
EX, EY = T.ORIGINS["school_exterior"][:2]
BX, BY = T.ORIGINS["bedroom"][:2]
CX, CY = 1000.0, 0.0          # cafeteria
UX, UY = 1150.0, 0.0          # bus interior
KX, KY = 1300.0, 0.0          # camp clearing centre
W = lambda i: V.w(i)


# ------------------------------------------------------------------ cast
def recolor(ch, mapping):
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


def leo(t0, t1, expr="neutral", loc=(0, 0, 0), rot=0):
    cast._hair_mat("harry", "#3a2416", band=(0.62, 0.86))
    h = cast.make("host", t0, t1, expr, loc=loc, rot=rot, cine=True, name="Leo")
    recolor(h, {"harry_jacket": "#2f7a5a", "harry_cream": "#2f7a5a", "harry_rib": "#235c44", "harry_snap": "#2f7a5a"})
    recolor(h, {"Leo_shirt": "#28684c"})                  # the open-jacket 'tee' becomes the hoodie front (MGR v2)
    for ob in list(h.coll.all_objects):                   # list(): hiding while iterating skipped objects
        if "patch" in ob.name or "_snap" in ob.name:      # no varsity H, no snaps: a PLAIN zip hoodie (BRIEF cast)
            force_hidden(ob)                              # (plain hide_render loses to the cast's visibility keys)
    zm = mat("leo_zip", hexc("#c9ccd1"), 0.3, 0.8); cord = mat("leo_cord", hexc("#f2efe6"), 0.6)
    box("Leo_zip", (0.07, 0.05, 1.78), (0, -0.56, 1.02), zm, 0.02, parent=h.hip, coll=h.coll)
    box("Leo_zippull", (0.12, 0.06, 0.2), (0, -0.59, 1.78), zm, 0.03, parent=h.hip, coll=h.coll)
    for sx in (-1, 1):
        box(f"Leo_cord{sx}", (0.06, 0.06, 0.55), (sx * 0.2, -0.575, 1.66), cord, 0.02, parent=h.hip, coll=h.coll)
    box("Leo_hood", (1.55, 0.5, 0.42), (0, 0.42, 2.08), mat("leo_hood", hexc("#2f7a5a"), 0.7), 0.16, parent=h.hip,
        coll=h.coll)
    return h


def maxx(t0, t1, expr="happy", loc=(0, 0, 0), rot=0, hat=False):
    cast._hair_mat("tyler", "#1e1813", band=(0.55, 0.8))
    m = cast.make("bestie", t0, t1, expr, loc=loc, rot=rot, prop=False, cine=True, name="Max")
    recolor(m, {"ty_navy": "#d9622b", "ty_navy2": "#b04d1f", "ty_pull": "#ffffff"})
    if hat:
        P3.limited_hat(m)
    return m


def chase(t0, t1, expr="smug", loc=(0, 0, 0), rot=0):
    c = extra("Chase", t0, t1, expr, loc, rot, shirt="#6a3fb5", pants="#ece6d6", hair="slick", hair_color="#e8c35a",
              skin="#f3d3b3")
    gold = mat("chase_gold", hexc("#e6b422"), 0.2, 1.0)
    for k in range(11):                                   # gold chain over the polo (hip-local, torso front y -0.5)
        a = (k - 5) / 5.0
        sphere(f"Chase_chain{k}", 0.075, (a * 0.5, -0.54, 1.93 - 0.42 * (1 - a * a)), gold, (1.3, 0.8, 0.8), parent=c.hip,
               coll=c.coll, seg=10)
    cyl("Chase_medal", 0.17, 0.05, (0, -0.56, 1.36), gold, 20, rot=(90, 0, 0), parent=c.hip, coll=c.coll)
    box("Chase_collar", (1.2, 0.08, 0.16), (0, -0.52, 1.98), mat("chase_collar", hexc("#f4f1ea"), 0.6), 0.03,
        parent=c.hip, coll=c.coll)
    return c


KIDS = [dict(shirt="#5aa0e0", hair="short", hair_color="#2a1d16"), dict(shirt="#9b59b6", hair="bob", hair_color="#9a6a4a", face="girl"),
        dict(shirt="#2ecc71", hair="messy", hair_color="#e0c060"), dict(shirt="#e67e22", hair="slick", hair_color="#151212"),
        dict(shirt="#e74c3c", hair="short", hair_color="#6b3a1e", skin="#c68c5a"), dict(shirt="#f2c14e", hair="bob", hair_color="#2a1d16", face="girl"),
        dict(shirt="#19c2b0", hair="messy", hair_color="#5a3a20", skin="#8d5a3a"), dict(shirt="#f28cb8", hair="bob", hair_color="#d9b46a", face="girl")]


def kid(k, t0, t1, expr="neutral", loc=(0, 0, 0), rot=0, name=None):
    return extra(name or f"Kid{k}", t0, t1, expr, loc, rot, **KIDS[k % len(KIDS)])


def jay(t0, t1, expr="smug", loc=(0, 0, 0), rot=0):
    return extra("Jay", t0, t1, expr, loc, rot, shirt="#c0182f", pants="#2b2f3a", hair="spiky", hair_color="#151212",
                 skin="#e0ac7c")


def rig(chs, strength=1.0, t=None, warm=None, name="cr"):
    """Character light rig made in the shot (auto_light then skips). warm = key colour override (duck glow)."""
    out = cast.light_rig(chs, bpy.context.scene.camera, look=V.look, strength=strength, t=t, name=name)
    if warm and out.get("key"):
        out["key"].data.color = hexc(warm)
    return out


# ------------------------------------------------------------------ sets
def hallway(students=True):
    L = T.school_hallway(students=students)
    V.look = "ref_matte"; look.cinematic("ref_matte", focus=L["focus"])
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
    V.look = "ref_day"; look.cinematic("ref_day", focus=L["focus"])
    return L


def caf_table(name, x, y, L=14.0, top=2.7, trays=()):
    lam = mat("cf_lam", hexc("#e9e3d4"), 0.35)
    met = mat("cf_metal", hexc("#7d848c"), 0.35, 0.8)
    box(name + "_top", (L, 3.0, 0.2), (x, y, top - 0.1), lam, 0.05)
    box(name + "_edge", (L + 0.05, 3.05, 0.08), (x, y, top - 0.24), mat("cf_edge", hexc("#2f5a8a"), 0.4), 0.02)
    for sx in (-1, 1):
        box(f"{name}_leg{sx}", (0.3, 2.0, top - 0.3), (x + sx * (L / 2 - 0.8), y, (top - 0.3) / 2), met, 0.03)
    for sy in (-1, 1):
        box(f"{name}_bench{sy}", (L, 1.3, 0.3), (x, y + sy * 2.3, 1.35), mat("cf_bench", hexc("#2f5a8a"), 0.45), 0.06)
        for sx in (-1, 1):
            box(f"{name}_bl{sy}{sx}", (0.25, 0.25, 1.2), (x + sx * (L / 2 - 0.8), y + sy * 2.3, 0.6), met, 0.02)
    out = []
    for k, (dx, side) in enumerate(trays):
        tr = P3.tray(f"{name}_tray{k}", loc=(x + dx, y + side * 0.65, top + 0.05))
        tr["root"].rotation_euler = (0, 0, math.radians(180 if side < 0 else 0))
        out.append(tr)
    return out


def cafeteria(day=True, line=True):
    """Blox City High cafeteria: tiled room, 4 long tables with blue benches (seat 1.5, top 2.7), serving counter with
    food pans, menu board, school banner, clock, ceiling panels. Tables at (CX+-10, 12) and (CX+-10, 24)."""
    T.room("cf", (CX, -2, 0), 46, 42, 13, "tile", ("plaster", "#ece4d2"), wainscot=("tile", "#6f9cc4"), fill=1.2)
    V.look = "ref_matte"; look.cinematic("ref_matte", focus=(CX, 12, 4))
    trays = {}
    for nm, x, y in (("tA", CX - 10, 12), ("tB", CX + 10, 12), ("tC", CX - 10, 24), ("tD", CX + 10, 24)):
        trays[nm] = caf_table(nm, x, y, trays=((-4.5, 1), (0.5, 1), (4.0, -1)) if nm != "tD" else ())
    st = mat("cf_steel", hexc("#c9ced6"), 0.25, 0.8)
    box("cf_counter", (26, 2.6, 3.0), (CX, 37.0, 1.5), st, 0.05)
    box("cf_glass", (26, 0.1, 1.6), (CX, 35.9, 4.0), mat("cf_glassm", hexc("#dfefff"), 0.05, alpha=0.25), 0.0)
    for i, col in enumerate(("#f2c14e", "#d9573b", "#7cb342", "#f4f1ea", "#a0522d", "#f2c14e")):
        box(f"cf_pan{i}", (3.4, 1.8, 0.35), (CX - 10 + i * 4, 37.0, 3.15), mat(f"cf_food{i}", hexc(col), 0.7), 0.1)
    SG.sign("cf_menu", "TODAY: PIZZA DAY", (CX, 39.6, 8.6), w=14, h=2.4, bg="#1f2f5a", fg="#f2c14e")
    SG.sign("cf_banner", "BLOX CITY HIGH", (CX - 14, 39.6, 10.4), w=10, h=1.6, bg="#c62828", fg="#ffffff")
    SG.poster("cf_p1", "EAT YOUR", "VEGGIES!", (CX + 15, 39.7, 7.5), w=3.0, h=3.8, accent="#2e8b57")
    SG.poster("cf_p2", "BAKE SALE", "Friday 3pm", (CX + 19.5, 39.7, 7.5), w=3.0, h=3.8, accent="#2f7bff")
    T.wall_clock("cf_clock", (CX + 8, 39.6, 10.4))
    for i, x in enumerate((-12, 0, 12)):
        for j, y in enumerate((8, 20, 32)):
            T.ceiling_panel(f"cf_cp{i}{j}", (CX + x, y, 12.8), power=700)
    if line:
        C.crowd("cf_line", (CX + 4, 33.5, 0), (14, 2.5), 5, face=(CX + 4, 40, 0), seed=21,
                variants=["student_a", "student_b", "c2", "c5", "c8"], min_gap=2.6)
    return trays


def seated(ch, t0, seat_h=1.5):
    return seat(ch, t0, seat_h=seat_h)


def caf_kids(spots, t0, t1, exprs=None, start=10):
    """Seated classmates (far bench faces -Y) at the cafeteria: spots = [(x, y, rot)]."""
    ks = []
    for k, (x, y, r) in enumerate(spots):
        c = kid(start + k, t0, t1, (exprs or ["neutral"])[k % len(exprs or ["neutral"])], loc=(x, y, 0), rot=r,
                name=f"CK{start + k}")
        seated(c, t0); mo.idle(c, t0, t1, 0.8)
        ks.append(c)
    return ks


def bus():
    """School bus interior (front = -Y): cream walls with window strips (bright sky outside), green vinyl bench seats
    (cushion top 1.5, back to 3.2 = seated shoulder height, MGR v2), centre aisle, ceiling light strip. Row r at y = UY + 4.6 * r; left bench x UX-5.6."""
    from rbx.core import world
    V.look = "ref_matte"; look.cinematic("ref_matte", focus=(UX - 5.6, UY + 4.6, 4.2))
    world((0.75, 0.8, 0.85), 0.5)
    wall = mat("bus_wall", hexc("#efe8d6"), 0.6)
    box("bus_floor", (24, 60, 0.3), (UX, UY + 15, -0.15), mat("bus_floor_m", hexc("#3a3d42"), 0.85), 0.0)
    box("bus_ceil", (24, 60, 0.3), (UX, UY + 15, 9.4), wall, 0.0)
    sky = mat("bus_sky", hexc("#bfe3ff"), 0.5, emit=hexc("#d8eeff"), estr=1.6)
    for s in (-1, 1):
        x = UX + s * 11.0
        box(f"bus_wlo{s}", (0.4, 60, 4.2), (x, UY + 15, 2.1), wall, 0.0)
        box(f"bus_whi{s}", (0.4, 60, 2.2), (x, UY + 15, 8.3), wall, 0.0)
        box(f"bus_sky{s}", (0.1, 60, 3.2), (x + s * 0.4, UY + 15, 5.8), sky, 0.0)
        for k in range(14):
            box(f"bus_post{s}{k}", (0.45, 0.5, 3.2), (x, UY - 14 + k * 4.6, 5.8), mat("bus_post_m", hexc("#c9b98f"), 0.5), 0.03)
        box(f"bus_trim{s}", (0.5, 60, 0.3), (x - s * 0.05, UY + 15, 4.25), mat("bus_trim_m", hexc("#f2b632"), 0.5), 0.02)
    vin = mat("bus_seat", hexc("#2f6b4a"), 0.35, coat=0.3)
    for r in range(-2, 8):
        y = UY + 4.6 * r
        for s in (-1, 1):
            x = UX + s * 5.6
            box(f"bus_cu{r}{s}", (8.6, 2.2, 0.5), (x, y, 1.25), vin, 0.15)
            box(f"bus_bk{r}{s}", (8.6, 0.5, 2.1), (x, y + 1.3, 2.15), vin, 0.2)      # top 3.2 = seated shoulders
            box(f"bus_fr{r}{s}", (8.6, 0.3, 1.0), (x, y - 0.9, 0.5), mat("bus_frame", hexc("#555a60"), 0.4, 0.6), 0.03)
    light("bus_strip", "AREA", (UX, UY + 15, 9.0), 2600, hexc("#fff6e6"), 2.0, size_y=50, rot=(0, 0, 0))
    for s in (-1, 1):
        light(f"bus_win{s}", "AREA", (UX + s * 10.4, UY + 15, 5.8), 3000, hexc("#eaf4ff"), 3.0, size_y=50,
              rot=(0, -s * 90, 0))
    return dict(seat=lambda r, s: (UX + s * 5.6, UY + 4.6 * r))


def bedroom(night=True, duck_on=True, max_room=False, duck_t=None, duck=True):
    """Town bedroom (Leo's; max_room=True = Max's with an orange blanket + skate posters). Night: the DUCK night-light on
    the nightstand is the key light (warm), faint moon at the window, desk lamp low. Returns dict(duck, bed_seat, ...)."""
    L = T.bedroom(morning=not night, night=night)
    for o in bpy.context.scene.objects:
        if o.name.startswith(("bd_bag", "bd_note", "bd_mug")):
            o.hide_render = True; o.hide_viewport = True
    if night:
        V.look = "ref_night"; look.cinematic("ref_night", focus=(BX - 6, BY + 14, 4.5))
        lp = bpy.data.objects.get("bd_lampL")
        if lp: lp.data.energy = 90
        night_dim()
    else:
        V.look = "ref_matte"; look.cinematic("ref_matte", focus=(BX - 6, BY + 14, 4.5))
    wood = pbr.get("planks", tint="#c89a68", tile=3)
    box("ns_body", (2.3, 2.5, 3.1), (BX - 2.6, BY + 16.1, 1.55), wood, 0.06)
    box("ns_drawer", (1.9, 0.05, 0.9), (BX - 2.6, BY + 14.83, 1.9), pbr.get("planks", tint="#a87a4c", tile=3), 0.03)
    if max_room:
        recolor_bl = mat("bd_bed_bl_max", hexc("#d9622b"), 0.8)
        b = bpy.data.objects.get("bd_bed_bl")
        if b: b.data.materials.clear(); b.data.materials.append(recolor_bl)
        SG.poster("mx_p1", "SKATE", "or die", (BX - 7, BY + 19.75, 7.4), w=2.4, h=3.2, accent="#d9622b")
    d = None
    if duck and not max_room:
        d = P3.duck_light("duck", s=0.9, loc=(BX - 2.05, BY + 16.6, 3.1 + 0.63), on=duck_t, power=650 if night else 300,
                          lit=duck_on, glow=1.5 if night else 0.9)
        d["root"].rotation_euler = (0, 0, math.radians(-25))
        qa.rest(d["root"], 0, 999)
    return dict(duck=d, bed=(BX - 7, BY + 15.6), bed_h=3.0, L=L)


NIGHT_ROOM = {"bd_fill": 0.12, "bd_castK": 0.2, "bd_castF": 0.2, "bd_floorW": 0.25, "bd_ceilB": 0.1,
              "look_key": 0.3, "look_fill": 0.5, "look_rim": 0.12}
_NIGHT_RIG = {}
_auto_light0 = cast.auto_light


def _auto_light(look=None):
    """MGR v3: in a duck-lit night room the character rig is a LOW warm rig (strength from _NIGHT_RIG), so the duck
    stays the key (look-dev 1: the old rig + room fills lit the 'night' bedroom like day)."""
    s = _NIGHT_RIG.pop("strength", None)
    if s is None:
        return _auto_light0(look)
    cast.settle_stance()                      # kit v4.3: the original auto_light does this first
    sc = bpy.context.scene
    if not cast.AUTO_LIGHT or sc.camera is None or any(o.type == "LIGHT" and o.name.startswith(("cl_", "cr_"))
                                                       for o in bpy.data.objects):
        return None
    chs = cast._live_chars()
    if not chs:
        return None
    out = cast.light_rig(chs, sc.camera, look=look, strength=s, t=(sc.frame_start + sc.frame_end) / 2 / sc.render.fps)
    if out.get("key"):
        out["key"].data.color = hexc("#ffc27a")
    for k in ("rim", "top", "fill"):
        if out.get(k):
            out[k].data.energy *= 0.4
    return out


cast.auto_light = _auto_light


def night_dim(rig=0.35):
    """Duck-lit night room (MGR v3, look-dev vs REF Dfe8B5Hs3G6 night: ONE warm practical, dark surroundings): scale the
    bedroom's day-ish fills and the look rig down, turn the window glass into a dark night pane, and ask for a low warm
    character rig. Shots may still add rig(...) themselves (then the auto rig is skipped)."""
    for o in bpy.context.scene.objects:
        if o.type == "LIGHT" and o.name in NIGHT_ROOM:
            o.data.energy *= NIGHT_ROOM[o.name]
    g = bpy.data.objects.get("bd_win_gl")
    if g:                                   # a NEW material (the glass one may be shared by other windows)
        nm = mat("bd_win_night", hexc("#1c2748"), 0.3, emit=hexc("#1c2748"), estr=0.5)
        for sl in g.material_slots:
            sl.material = nm
    _NIGHT_RIG["strength"] = rig


def on_bed(ch, t0):
    return seat(ch, t0, seat_h=3.0)


def camp(night=True, dark=None, lightning=(), flicker=None, lamps=True, tents=True):
    """CAMP BLOX clearing at (KX, KY): ring of trees, stone circle (no fire), tents facing the centre, light poles.
    night: ref_night + lamps on; dark=t: every light dies at t (storm power cut) except the duck/rim; after the cut only
    a faint moon. lightning: times of flashes. Day (night=False): ref_day, blue sky, sun."""
    P3.camp_ground((KX, KY, 0), night=night)
    if night:
        V.look = "ref_night"; look.cinematic("ref_night", focus=(KX, KY + 2, 3))
        T.sky("night")
    else:
        V.look = "ref_day"; look.cinematic("ref_day", focus=(KX, KY + 2, 3))
        T.sky("day"); T.sun(4.0, "#fff1dc", 40, 35)
    tl = []
    if tents:
        for k, (x, y, col) in enumerate(((-15, 9, "#e8742a"), (0, 15, "#2f7bff"), (15, 9, "#2e8b57"), (-19, -5, "#c0392b"),
                                         (20, -4, "#f2c14e"))):
            yaw = math.degrees(math.atan2(-x, y))          # door (local -Y) toward the clearing centre
            tl.append(P3.tent(f"tent{k}", (KX + x, KY + y, 0), rot=yaw, col=col))
    lp = []
    if lamps:
        for k, (x, y) in enumerate(((-8, 6), (9, 5), (-10, -8), (11, -9))):
            lp.append(P3.camp_lamp(f"lamp{k}", (KX + x, KY + y, 0), power=700 if night else 0, off=dark if night else None,
                                   flicker=flicker if night else None))
            if not night:
                lp[-1]["light"].data.energy = 0
    if night and dark is not None:
        for o in bpy.context.scene.objects:
            if o.type == "LIGHT" and o.name.startswith(("look_key", "look_fill", "look_rim", "look_sun")):
                e = o.data.energy
                o.data.keyframe_insert("energy", frame=F(dark) - 1)
                o.data.energy = e * (0.25 if "sun" in o.name else 0.06)
                o.data.keyframe_insert("energy", frame=F(dark))
    if night:
        moon = light("camp_moon", "SUN", (KX, KY, 40), 0.25, hexc("#b8c4dc"), 1.0, rot=(48, 0, 150))
    for t in lightning:
        flash(t)
    return dict(tents=tl, lamps=lp)


def flash(t, power=9.0):
    """Lightning: a cold sun that pops on for 2 + 3 frames (double strike)."""
    lt = light(f"lightning_{F(t)}", "SUN", (KX, KY, 50), 0.0, hexc("#e4ecff"), 2.0, rot=(35, 0, 200))
    for f, v in ((1, 0.0), (F(t) - 1, 0.0), (F(t), power), (F(t) + 1, power * 0.25), (F(t) + 2, power * 0.9),
                 (F(t) + 3, power * 0.5), (F(t) + 5, 0.0)):
        lt.data.energy = v; lt.data.keyframe_insert("energy", frame=f)
    from rbx.props3 import _constant
    _constant(lt.data)
    return lt


def ground_kids(spots, t0, t1, exprs=("worried",), start=20):
    """Classmates sitting ON THE GROUND (seat 0.05) around the duck: spots = [(x, y)] relative to the camp centre,
    each turned to face the centre."""
    ks = []
    for k, (x, y) in enumerate(spots):
        yaw = math.degrees(math.atan2(x, -y)) + 180          # face the centre
        c = kid(start + k, t0, t1, exprs[k % len(exprs)], loc=(KX + x, KY + y, 0), rot=yaw, name=f"GK{start + k}")
        seat(c, t0, seat_h=0.05); mo.idle(c, t0, t1, 0.7)
        ks.append(c)
    return ks


# circle layout (relative to KX, KY): duck at the centre; Leo south-west facing the duck, Chase shoulder to shoulder at Leo's RIGHT
DUCK_C = (0.0, 0.0)
LEO_C = (-1.6, -3.6)
CHASE_C = (0.5, -3.9)          # MGR v2: 2.15 studs from Leo on the circle (was 3.0 = out of reach, s46 NOTOUCH 4.3)
JAY_C = (0.6, 3.8)
CIRCLE = [(-3.8, 0.6), (-2.8, 2.9), (2.9, 2.6), (3.9, -0.3), (-3.6, -2.2), (3.4, -2.6)]


def face_centre(x, y):
    return math.degrees(math.atan2(x, -y)) + 180


def circle_duck(t_on=None, s=0.95):
    rock = mat("p3_rock", hexc("#8d8f93"), 0.8)
    cyl("camp_flat", 1.0, 0.5, (KX + DUCK_C[0], KY + DUCK_C[1], 0.25), rock, 24, bev=0.1)
    d = P3.duck_light("duck", s=s, loc=(KX + DUCK_C[0], KY + DUCK_C[1], 0.5 + 0.7 * s), on=t_on, power=520)
    d["root"].rotation_euler = (0, 0, math.radians(200))
    qa.rest(d["root"], 0, 999)
    return d


def leo_ground(t0, t1, expr="neutral"):
    h = leo(t0, t1, expr, loc=(KX + LEO_C[0], KY + LEO_C[1], 0), rot=face_centre(*LEO_C))
    seat(h, t0, seat_h=0.05); mo.idle(h, t0, t1, 0.6)
    return h


def chase_ground(t0, t1, expr="worried"):
    c = chase(t0, t1, expr, loc=(KX + CHASE_C[0], KY + CHASE_C[1], 0), rot=face_centre(*CHASE_C))
    seat(c, t0, seat_h=0.05)
    return c


def sleeve_grab(lo, ch, t0, t1):
    """Chase's LEFT fist ON Leo's RIGHT sleeve (forearm, just above the cuff). Chase sits at CHASE_C = Leo's right,
    shoulder to shoulder, so his left hand is the near one. Leo's right forearm rests forward on his knee; the target
    empty rides the forearm (contact by construction); registers qa.touch. MGR v2 (baseline: wrong side, 3 studs away)."""
    lo.pose(t0 - 0.5, armR=(38, -2, 0), elbowR=45)
    lo.pose(t1 + 0.5, armR=(38, -2, 0), elbowR=45)
    fist = mo.hand(lo, "armR")
    bpy.context.view_layer.update()
    sp = point_on(fist, (0.0, 0.0, 0.55), "leo_sleevept")       # up the forearm from the fist (sleeve)
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    side = Vector(ch.root.matrix_world.translation) - Vector(lo.root.matrix_world.translation); side.z = 0
    side.normalize()
    tg = bpy.data.objects.new("leo_sleeve_top", None); bpy.context.scene.collection.objects.link(tg)
    for f in range(F(t0 - 0.6), F(t1) + 2):
        bpy.context.scene.frame_set(f); bpy.context.view_layer.update()
        p = sp.matrix_world.translation + side * 0.3 + Vector((0.0, 0.0, 0.42))
        tg.location = p; tg.keyframe_insert("location", frame=f)
    follow(ch, t0, t1, tg, hand="l", body=SLEEVE_BODY, step=1, approach=0.3, tol=0.45)
    return tg


SLEEVE_BODY = {"torso": (12, 8, 0)}


def pov_phone(h, name, screen, t0, t1, height):
    """POV of the holder looking DOWN at the phone in his hands: screen tilted 50 deg up to the eyes, camera on the
    screen normal at eye height (head hidden), so the UI is frontal and fills the frame with the fists at the edges."""
    ph = P3.phone(name, screens=scr(screen), facing="in")
    ph["piv"].rotation_mode = "ZYX"; ph["piv"].rotation_euler = (math.radians(50), 0, math.pi)
    hold(h, ph, t0, t1, height=height, fwd=0.95)
    hide_for_pov(h)              # MGR v2: hide_head left the collar/torso filling 60 % of the frame (s01/s10/s21)
    prop_cam(t0, t1, ph, dist=2.5, lens=30, push=0.1, fstop=2.0)
    return ph



# ================================================================== SHOT PARTS (split 2026-11-16 for parallel agents)
# Common helpers above are owned by the MANAGER agent. Shots live in shots_a.py (agent A) and shots_b.py (agent B).
_HERE = os.path.dirname(os.path.abspath(__file__))
for _part in ("shots_a.py", "shots_b.py"):
    _p = os.path.join(_HERE, _part)
    exec(compile(open(_p).read(), _p, "exec"), globals())
