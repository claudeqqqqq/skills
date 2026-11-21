# EP3 part A - owned ONLY by Blender agent A. Executed inside shots.py's namespace (all common helpers available).
# Shots 1-33 (hook, friends, bedroom, Blox Tea, phone, cafeteria, hat). Put new helpers for this part HERE, prefixed a_ . Do not edit shots.py (common) - ask the Manager via BOARD.md.
# v2 (agent A, 2026-11-16): exterior action moved IN FRONT of the student crowd (EY-6), POV phones hide the whole
# holder except the hands, handshake solved from the measured shoulders, bags/phones held below the face, laugh shots
# from Leo's POV (kids laugh at the lens), Max's head really down at his tray, framing solved (frame_on) everywhere.
# ================================================================== part-A helpers
A_DBG = {}          # debug handles for agent A's probes (harmless at render time)


def a_rz(rot, v):
    """Rotate a local (x, y, z) offset by a character root yaw `rot` (deg; rot 0 faces -Y, local +X = the left)."""
    r = math.radians(rot)
    return Vector((v[0] * math.cos(r) - v[1] * math.sin(r), v[0] * math.sin(r) + v[1] * math.cos(r), v[2]))


def a_face_dir(rot):
    r = math.radians(rot)
    return Vector((math.sin(r), -math.cos(r), 0))


def a_pov_phone(h, name, screen, t0, t1, height, dist=2.3, lens=32, tilt=50):
    """POV of the holder looking DOWN at the phone in his hands (v2 of shots.pov_phone): the WHOLE holder is hidden except
    arms/hands (hide_for_pov), so no hoodie or collar fills the lower half of the frame (baseline s01/s10/s21: green
    torso over half the screen, BLOCKED by Leo_collar). Camera on the screen normal; fists at the phone's sides."""
    ph = P3.phone(name, screens=scr(screen), facing="in")
    ph["piv"].rotation_mode = "ZYX"; ph["piv"].rotation_euler = (math.radians(tilt), 0, math.pi)
    a_hold(h, ph, t0, t1, height=height, fwd=0.95, approach=0.6)
    hide_head(h); hide_for_pov(h)
    prop_cam(t0, t1, ph, dist=dist, lens=lens, push=0.08, fstop=2.4)
    return ph


def a_insert_cam(t0, t1, center, normal, half_h, lens=45, push=0.06, fstop=2.4, name="Cam_ains", up_off=0.0):
    """Straight-on insert whose frame shows `half_h` studs above and below `center` (vertical, core.Cam sensor 24)."""
    n = Vector(normal).normalized()
    d = half_h * lens / 12.0
    c0 = Vector(center)
    p = c0 + n * d
    tgt = c0 + Vector((0, 0, up_off))
    c = Cam(name, lens)
    c.key(t0, tuple(p), tuple(tgt), lens, focus=tuple(c0), fstop=fstop)
    c.key(t1, tuple(p + (c0 - p) * push), tuple(tgt), lens, focus=tuple(c0), fstop=fstop, ease="EASE_IN_OUT")
    cams.micro(c, deg=0.15, loc=0.006, period=2.4)
    return c


def a_look(ch, t, target, max_head=65, dur=0.3):
    """Head turns to a target WITHOUT mo.strike (strike's anticipation keys hipz = -dip from 0, so a SEATED character
    drops ~1.5 studs into the seat for 4 frames on every look_at: EP3 s22 fists left the phone at t0-0.17..t0)."""
    rel, pitch = mo.aim(ch, t, target)
    hy = max(-max_head, min(max_head, rel))
    ch.pose(t - dur, head=mo.sample(ch, t - dur, ["head"])["head"])
    ch.pose(t, head=(hy, max(-30, min(30, pitch)), -hy * 0.08))
    return hy


def a_talk(ch, t0, t1, words, strip_arms=True, **kw):
    """talk_cadence for SEATED / prop-holding characters: no sway (it keys straight legs on a seated body) and, with
    strip_arms, the arm beats it adds are removed again (they pulled the fists off a held phone / hat)."""
    from rbx.core import fcurves
    obs = [ch.shL, ch.shR, ch.hpL, ch.hpR] + list(getattr(ch, "joints", {}).values())
    if not strip_arms:
        obs = [ch.hpL, ch.hpR] + [j for k, j in getattr(ch, "joints", {}).items() if "knee" in k]
    before = {}
    for o in obs:
        ad = o.animation_data
        if ad and ad.action:
            for fc in fcurves(ad.action):
                before[(o.name, fc.data_path, fc.array_index)] = {round(kp.co[0], 2): kp.co[1] for kp in fc.keyframe_points}
    kw["sway"] = False
    mo.talk_cadence(ch, t0, t1, words, **kw)
    for o in obs:
        ad = o.animation_data
        if not (ad and ad.action):
            continue
        for fc in fcurves(ad.action):
            old = before.get((o.name, fc.data_path, fc.array_index), {})
            for kp in reversed(list(fc.keyframe_points)):
                k = round(kp.co[0], 2)
                if k not in old:
                    fc.keyframe_points.remove(kp)
                elif abs(kp.co[1] - old[k]) > 1e-6:          # an existing key it OVERWROTE (contact key): restore
                    d = old[k] - kp.co[1]
                    kp.co[1] += d; kp.handle_left[1] += d; kp.handle_right[1] += d
            fc.update()
    return ch


def a_hold(ch, prop, t0, t1, **kw):
    """shotlib.hold + removes the 1-frame POP at the shot's first frame: the cast keys a rest pose on the arms at
    F(t0), and hold's 2-frame contact keys can miss that frame, so the fists jumped 1.6-1.8 off the phone on frame 1
    (lo pass v2: s09/s11/s13/s22 NOTOUCH 1.77 at t0). Deletes that arm key and re-keys the prop on the measured fists."""
    from rbx.core import fcurves
    hold(ch, prop, t0, t1, **kw)
    f0 = F(t0)
    obs = [ch.shL, ch.shR] + [j for k, j in getattr(ch, "joints", {}).items() if "elbow" in k]
    for o in obs:
        ad = o.animation_data
        if not (ad and ad.action):
            continue
        for fc in fcurves(ad.action):
            frs = {int(round(kp.co[0])) for kp in fc.keyframe_points}
            if not ({f0 - 1, f0 - 2} & frs and {f0 + 1, f0 + 2} & frs):
                continue                                   # no contact keys around t0: leave it
            for kp in reversed(list(fc.keyframe_points)):
                if int(round(kp.co[0])) == f0:
                    fc.keyframe_points.remove(kp)
            fc.update()
    style = kw.get("style") or prop["style"]
    r = prop["root"]
    for f in range(f0 - 2, f0 + 3):
        t = f / 30.0
        hl = Vector(hand_pos(ch, t, "armL")); hr = Vector(hand_pos(ch, t, "armR"))
        mid = (hl + hr) / 2
        r.rotation_euler = (0, 0, math.atan2(hl.y - hr.y, hl.x - hr.x))
        r.location = (mid.x, mid.y, mid.z) if style == "sides" else (mid.x, mid.y, mid.z + 0.24 + prop["h"] * 0.5)
        r.keyframe_insert("location", frame=f); r.keyframe_insert("rotation_euler", frame=f)
    return prop


def a_bag_sides(bag):
    """Coin bag held by its SIDES at the chest (fists on the sack's flanks, face clear). props3.coin_bag only has 'under'
    grips (below the sack: out of R6 reach at chest height), so QA measured the fists against the wrong points."""
    k = bag["w"] / 1.3
    hw = bag["w"] / 2 + 0.22
    b = dict(bag); b["style"] = "sides"; b["grips"] = {"L": (hw, 0, 0), "R": (-hw, 0, 0)}
    return b


def a_head_down(ch, t0, t1, pitch=30, lean=12, yaw=0):
    """Head really DOWN (looking at the tray in front, not turned away): neck pitch + a forward torso lean, held."""
    for t in (t0 - 0.6, t0, (t0 + t1) / 2, t1 + 0.2):
        ch.pose(t, head=(yaw, pitch, 0), torso=(0, lean, 0))


def a_handshake_pair(t0, t1, cheat=28, gap=2.3):
    """Leo and Max face each other (both cheated `cheat` deg toward the -Y camera) placed so their RIGHT shoulders are
    `gap` apart: the meeting point P (shoulder midpoint, 0.45 lower) is inside BOTH R6 arm reaches (1.52), so the fists
    really meet (baseline: NOTOUCH 0.44-0.82, the hands never touched). Returns h, m, pe (moving clasp point), P."""
    rl, rm = 90 - cheat, -90 + cheat
    L0 = Vector((EX - 1.4, EY - 6.0, 0))
    SL = L0 + a_rz(rl, (-1.5, 0, 0)) + Vector((0, 0, 3.55))
    u = (a_face_dir(rl) - a_face_dir(rm)).normalized()
    SM = SL + u * gap
    M0 = SM - a_rz(rm, (-1.5, 0, 0)) - Vector((0, 0, 3.55))
    h = leo(t0, t1, "grin", loc=(L0.x, L0.y, 0), rot=rl)
    m = maxx(t0, t1, "grin", loc=(M0.x, M0.y, 0), rot=rm)
    for c in (h, m):
        mo.idle(c, t0, t1, 0.6)
    P0 = (SL + SM) / 2 + Vector((0, 0, -0.5))
    pe = bpy.data.objects.new("hs_P", None); bpy.context.scene.collection.objects.link(pe)
    steps = [(0.0, 0.0), (0.18, 0.3), (0.36, -0.2), (0.54, 0.3), (0.72, -0.2), (0.9, 0.25), (1.1, 0.0), (1.3, 0.35), (1.6, 0.05)]
    t = t0 - 0.4
    while t < t1 + 0.4:
        for dt, dz in steps:
            if t + dt > t1 + 0.4:
                break
            pe.location = (P0.x, P0.y, P0.z + dz * 0.5); pe.keyframe_insert("location", frame=F(t + dt))
        t += 1.8
    hl = point_on(pe, tuple(-u * 0.1), "hs_leo"); hm = point_on(pe, tuple(u * 0.1), "hs_max")
    follow(h, t0, t1, hl, hand="r", step=1, approach=0.25, tol=0.4)
    follow(m, t0, t1, hm, hand="r", step=1, approach=0.25, tol=0.4)
    A_DBG.update(hs=(h, m, hl, hm))
    return h, m, pe, P0


# ================================================================== SHOTS
@S(1, 0, 7, "HOOK POV: Leo's phone in his hands - BLOX TEA post: drawing of him hugging a duck, 200 comments")
def s01(t0, t1):
    hallway(students=True)
    h = leo(t0, t1, "worried", loc=(HX, HY + 2, 0), rot=0)
    mo.idle(h, t0, t1, 0.8)
    a_pov_phone(h, "ph1", "tea_post.png", t0, t1, 3.6)


@S(2, 7, 13, "MCU: Leo in the hallway, two kids behind him point and laugh at him - 'By lunch, the whole school knew.'")
def s02(t0, t1):
    hallway(students=True)
    h = leo(t0, t1, "worried_dart", loc=(HX, HY - 2, 0), rot=0)
    mo.idle(h, t0, t1, 1.0)
    acting.dart(h, t0 + 0.2, t1)
    ks = [kid(k, t0, t1, "laugh_smug", loc=(HX + x, HY + y, 0), rot=r) for k, (x, y, r) in
          enumerate(((-2.2, 3.4, 30), (2.1, 4.0, -26)))]    # built FACING Leo (A-1: belly_laugh's turn is overridden)
    crowd_laugh(ks, t0, t1, h)
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    xs = [tuple(k.head.matrix_world.translation + Vector((dx, 0, dz))) for k in ks for dx, dz in ((0, 0.9), (-0.9, 0), (0.9, 0))]
    frame_on([h], t0, t1, "mcu", yaw=8, lens=40, extra=xs)


@S(3, 13, 19, "MED: Max grins at the lens, holding up a burlap coin bag tagged 500 at his chest - 'And he got paid for it.'")
def s03(t0, t1):
    hallway(students=True)
    m = maxx(t0, t1, "grin", loc=(HX + 0.5, HY + 2.0, 0), rot=-10, hat=False)
    mo.idle(m, t0, t1, 0.8)
    bag = a_bag_sides(P3.coin_bag("bag3", s=0.85))
    a_hold(m, bag, t0, t1, style="sides", height=2.95, fwd=0.9)          # fists ON the sack's sides at the chest, face clear
    acting.ladder(m, t0 + 0.4, ["grin", "toothy", "smug_up"])
    frame_on([m], t0, t1, "med", lens=40, yaw=8)


@S(4, 19, 28, "COWBOY: Max and Leo shoulder to shoulder in front of the school, Max's arm over Leo's shoulder - best friends since kindergarten")
def s04(t0, t1):
    exterior(students=True)
    h = leo(t0, t1, "joy", loc=(EX - 1.2, EY - 6.0, 0), rot=0)
    m = maxx(t0, t1, "joy", loc=(EX + 1.1, EY - 5.0, 0), rot=-6)       # half a step behind Leo: his arm goes OVER the shoulder
    mo.idle(h, t0, t1, 0.6); mo.idle(m, t0, t1, 0.6)
    shp = point_on(h.hip, (0.62, 0.25, 2.3), "leo_shoulder")             # top of Leo's left shoulder, next to his neck
    for t in (t0 - 0.6, t0, (t0 + t1) / 2, t1 + 0.3):                    # lean toward Leo, keyed FIRST (contact solves on it)
        m.pose(t, torso=(-8, 4, -5))
    pole = (-0.9, 0.4, 0.7)                                              # elbow out and UP behind Leo's shoulder (not a wave)
    mo.reach(m, t0 - 0.35, shp, hand="r", pole=pole)
    mo.contact(m, t0 - 0.3, t1, shp, hand="r", pole=pole, step=1)
    qa.touch(m, "armR", shp, t0, t1, tol=0.45)
    A_DBG.update(h=h, m=m, tgt=shp)
    acting.ladder(h, t0 + 0.6, "surprise_laugh")
    mo.look_at(h, t0 + 1.2, m, torso_share=0.0)
    frame_on([h, m], t0, t1, "med", lens=42, pitch=3)              # med: no empty ground in the bottom quarter


@S(5, 28, 31, "MED: same lunch table - Leo and Max seated side by side behind their trays, laughing")
def s05(t0, t1):
    trays = cafeteria(line=True)
    h = leo(t0, t1, "joy", loc=(CX - 13.2, 14.3, 0), rot=0)
    m = maxx(t0, t1, "joy", loc=(CX - 9.0, 14.3, 0), rot=0)
    trays["tA"][0]["root"].location.x = CX - 13.2; trays["tA"][1]["root"].location.x = CX - 9.0     # a tray in front of each
    for c in (h, m):
        seated(c, t0); mo.idle(c, t0, t1, 1.0)
    a_look(h, t0 - 0.1, m); a_look(m, t0, h)
    acting.ladder(h, t0 + 0.3, "surprise_laugh")
    caf_kids([(CX + 8, 14.3, 0), (CX + 12, 14.3, 0)], t0, t1, ["happy"])
    frame_on([h, m], t0, t1, "mcu", lens=35, pitch=8, extra=[(CX - 13.2, 12.65, 2.8), (CX - 9.0, 12.65, 2.8)])


@S(6, 31, 34, "MCU two-shot: same bus seat - Leo (window) and Max side by side, filmed from the aisle over the seat in front")
def s06(t0, t1):
    B = bus()
    x, y = B["seat"](2, -1)
    h = leo(t0, t1, "happy", loc=(x - 2.0, y, 0), rot=0)
    m = maxx(t0, t1, "joy", loc=(x + 2.0, y, 0), rot=0)
    for c in (h, m):
        seated(c, t0); mo.idle(c, t0, t1, 1.0)
    a_look(m, t0 - 0.1, h)
    frame_on([h, m], t0, t1, "mcu", lens=30, yaw=45, pitch=13)


@S(7, 34, 37, "COWBOY: Leo and Max start their secret handshake, grinning at each other")
def s07(t0, t1):
    exterior(students=True)
    h, m, pe, P = a_handshake_pair(t0, t1)
    acting.face(h, t0 + 0.4, "joy"); acting.face(m, t0 + 0.5, "joy")      # bodies cheated 3/4 to the lens, no head turn
    frame_on([h, m], t0, t1, "cowboy", lens=40)


@S(8, 37, 40, "INSERT: the two right hands clasped - shake, pump, pump (eleven steps)")
def s08(t0, t1):
    exterior(students=False)
    h, m, pe, P = a_handshake_pair(t0, t1)
    a_insert_cam(t0, t1, (P.x, P.y, P.z), (0.0, -0.6, 0.8), 1.05, lens=35, push=0.05, fstop=3.2)
    light("hs_fill", "AREA", (P.x, P.y - 2.2, P.z + 3.0), 120, hexc("#fff4e6"), 1.5, target=(P.x, P.y, P.z))   # both fists lit


@S(9, 40, 46, "WIDE: one night - Leo sits on his bed, phone in hand, the yellow duck night-light glowing beside him")
def s09(t0, t1):
    D = bedroom(night=True, duck_on=True)
    h = leo(t0, t1, "content", loc=(D["bed"][0], D["bed"][1], 0), rot=0)
    on_bed(h, t0); mo.idle(h, t0, t1, 0.7)
    ph = P3.phone("ph9", screens=scr("call_max.png"), facing="in")
    ph["piv"].rotation_mode = "ZYX"; ph["piv"].rotation_euler = (math.radians(25), 0, math.pi)
    a_hold(h, ph, t0, t1, height=4.3, fwd=0.95, approach=0.6)
    a_look(h, t0 - 0.1, ph["root"])
    d = D["duck"]["root"].matrix_world.translation
    frame_on([h], t0, t1, "med", lens=32, yaw=35, pitch=8, extra=[(d.x + 0.6, d.y, d.z + 1.0), (d.x + 0.6, d.y, d.z - 0.7)])


@S(10, 46, 53, "POV INSERT: the call screen - MAX, best friend, on call")
def s10(t0, t1):
    D = bedroom(night=True, duck_on=True)
    h = leo(t0, t1, "content", loc=(D["bed"][0], D["bed"][1], 0), rot=0)
    on_bed(h, t0); mo.idle(h, t0, t1, 0.5)
    a_pov_phone(h, "ph10", "call_max.png", t0, t1, 4.45)


@S(11, 53, 62, "MCU: Leo on the bed, phone in hands, embarrassed, glances at the duck - 'I can't sleep without my night-light.'")
def s11(t0, t1):
    D = bedroom(night=True, duck_on=True)
    h = leo(t0, t1, "worried", loc=(D["bed"][0], D["bed"][1], 0), rot=0)
    on_bed(h, t0); mo.idle(h, t0, t1, 0.6)
    ph = P3.phone("ph11", screens=scr("call_max.png"), facing="in")
    ph["piv"].rotation_mode = "ZYX"; ph["piv"].rotation_euler = (math.radians(25), 0, math.pi)
    a_hold(h, ph, t0, t1, height=4.3, fwd=0.95, approach=0.6)
    a_look(h, t0 + 0.9, D["duck"]["root"], dur=0.35)
    qa.look(h, D["duck"]["root"], t0 + 1.4, t1, tol=40)
    acting.face(h, t0 + 0.9, "sad")
    acting.face(h, t1 - 0.6, "content")
    frame_on([h], t0, t1, "mcu", lens=50, yaw=40)


@S(12, 62, 67, "INSERT: the duck night-light glowing on the nightstand, straight-on - 'It's shaped like a duck.'")
def s12(t0, t1):
    D = bedroom(night=True, duck_on=True)
    d = D["duck"]
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    c = d["root"].matrix_world @ Vector((0, 0, 0.75))
    prop_cam(t0, t1, d, dist=5.0, lens=50, push=0.1, fstop=1.8, center=tuple(c), up=0.5)


@S(13, 67, 74, "MCU: Max in his room at night, phone in his hands, warm smile - 'Your secret's safe with me.'")
def s13(t0, t1):
    D = bedroom(night=True, max_room=True)
    m = maxx(t0, t1, "smile", loc=(BX - 7, BY + 9.3, 0), rot=0)
    on_bed(m, t0); mo.idle(m, t0, t1, 0.6)
    ph = P3.phone("ph13", screens=scr("call_max.png"), facing="in")
    ph["piv"].rotation_mode = "ZYX"; ph["piv"].rotation_euler = (math.radians(25), 0, math.pi)
    a_hold(m, ph, t0, t1, height=4.3, fwd=0.95, approach=0.6)
    a_talk(m, W(67), W(74), V.words, stress=("safe",), expr_on={"me,\"": "smile"}, hands=False, energy=0.6)
    light("mx_screen", "AREA", (BX - 7, BY + 7.6, 4.6), 60, hexc("#9cc4ff"), 1.0, target=(BX - 7, BY + 9.3, 5.2))
    frame_on([m], t0, t1, "mcu", lens=42, yaw=10, margin=0.14, pitch=12)     # a bit above: face clears the phone


@S(14, 74, 78, "WIDE: Blox City High on a sunny morning, students arriving")
def s14(t0, t1):
    L = exterior(students=True)
    a, b, lens = L["cams"]["wide"]
    still_cam(t0, t1, a, b, lens=lens, push=0.05, fstop=8)


@S(15, 78, 84, "INSERT: Chase shows his phone - the BLOX TEA app, SEND A SECRET, GET PAID 500 (straight-on, fills the frame)")
def s15(t0, t1):
    hallway(students=True)
    c = chase(t0, t1, "smug", loc=(HX, HY + 2, 0), rot=0)
    mo.idle(c, t0, t1, 0.5)
    ph = P3.phone("ph15", screens=scr("tea_app.png"), facing="out")
    a_hold(c, ph, t0, t1, height=2.55, fwd=0.85, approach=0.4)          # phone below his chin: the frame shows only phone + fists
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    ctr = ph["piv"].matrix_world.translation.copy()
    a_insert_cam(t0, t1, tuple(ctr), (0, -1, 0), 0.95, lens=45, push=0.03, fstop=2.2, up_off=-0.12)


@S(16, 84, 90, "MCU: Chase in the hallway, gold chain, smug smile - 'Chase runs it. Chase is rich.'")
def s16(t0, t1):
    hallway(students=True)
    c = chase(t0, t1, "smug", loc=(HX - 1.0, HY + 1, 0), rot=15)
    mo.idle(c, t0, t1, 0.9)
    acting.ladder(c, W(87), ["smug", "smug_up", "laugh_smug"])
    frame_on([c], t0, t1, "mcu", lens=45, yaw=-10)


@S(17, 90, 96, "MED: Chase holds a burlap coin bag tagged 500 at his chest, grinning - 'Chase pays five hundred coins'")
def s17(t0, t1):
    hallway(students=True)
    c = chase(t0, t1, "grin", loc=(HX, HY + 1, 0), rot=0)
    mo.idle(c, t0, t1, 0.9)
    bag = a_bag_sides(P3.coin_bag("bag17", s=0.85))
    a_hold(c, bag, t0, t1, style="sides", height=2.95, fwd=0.9)
    acting.ladder(c, W(93), ["grin", "toothy"])
    frame_on([c], t0, t1, "med", lens=40)


@S(18, 96, 102, "OTS (a kid's shoulder FG): Chase leans in, hand cupped at his ear - 'for every secret you send him'")
def s18(t0, t1):
    hallway(students=True)
    c = chase(t0, t1, "smug_up", loc=(HX + 0.5, HY + 3.5, 0), rot=10)
    k = kid(2, t0, t1, "neutral", loc=(HX - 0.8, HY - 0.5, 0), rot=190)
    mo.idle(c, t0, t1, 0.8); mo.idle(k, t0, t1, 0.6)
    ear = point_on(c.head, (-0.9, -0.05, -0.05), "chase_ear")
    follow(c, t0, t1, ear, hand="r", body={"torso": (0, 10, 6), "head": (-8, 4, -10)}, step=2, approach=0.3, tol=0.5)
    mo.look_at(c, t0 + 0.2, k)
    ots(t0, t1, k, c, lens=40, back=2.6, side=2.4, up=1.6, aim_dz=-0.5)


@S(19, 102, 106, "MCU: next morning - Leo sits up in bed, sleepy, turns to the buzzing nightstand")
def s19(t0, t1):
    D = bedroom(night=False, duck_on=False)
    h = leo(t0, t1, "sleepy", loc=(D["bed"][0], D["bed"][1], 0), rot=0)
    on_bed(h, t0); mo.idle(h, t0, t1, 0.5)
    a_look(h, t0 + 0.5, (BX - 3.1, BY + 16.0, 3.2), max_head=45)   # glance, face stays 3/4 to the lens
    acting.face(h, t0 + 0.6, "confused")
    frame_on([h], t0, t1, "mcu", lens=50, yaw=50)


@S(20, 106, 110, "INSERT: the phone on the nightstand buzzing non-stop, lock screen full of BLOX TEA notifications")
def s20(t0, t1):
    D = bedroom(night=False, duck_on=False)
    ph = P3.phone("ph20", screens=scr("lock_buzz.png"), facing="out")
    r = ph["root"]; r.rotation_mode = "XYZ"
    z0 = 3.1 + 0.065
    base = Vector((BX - 3.15, BY + 16.0, z0))
    t, k = t0 - 0.2, 0
    while t < t1 + 0.1:
        buzz = (k % 10) < 6
        a = 1 if k % 2 == 0 else -1
        r.location = base + Vector((0.025 * a if buzz else 0, 0.015 * a if buzz else 0, 0))
        r.rotation_euler = (math.radians(-90), 0, math.radians(-8 + (2.5 * a if buzz else 0)))
        r.keyframe_insert("location", frame=F(t)); r.keyframe_insert("rotation_euler", frame=F(t))
        t += 1 / 30 * 1.5; k += 1
    qa.rest(r, t0, t1, tol=0.15)
    prop_cam(t0, t1, ph, dist=3.8, lens=45, push=0.08, fstop=2.2, normal=(0.05, -0.18, 1.0))


@S(21, 110, 121, "POV INSERT: the BLOX TEA post - a drawing of Leo hugging a duck - 'Guess who sleeps with a DUCK night-light?'")
def s21(t0, t1):
    D = bedroom(night=False, duck_on=False)
    h = leo(t0, t1, "shock", loc=(D["bed"][0], D["bed"][1], 0), rot=0)
    on_bed(h, t0); mo.idle(h, t0, t1, 1.0)
    a_pov_phone(h, "ph21", "tea_post.png", t0, t1, 4.45)


@S(22, 121, 124, "MCU: Leo's jaw drops at the screen - 'Two hundred comments.'")
def s22(t0, t1):
    D = bedroom(night=False, duck_on=False)
    h = leo(t0, t1, "pop_shock", loc=(D["bed"][0], D["bed"][1], 0), rot=0)
    on_bed(h, t0); mo.idle(h, t0, t1, 1.2)
    ph = P3.phone("ph22", screens=scr("tea_post.png"), facing="in")
    ph["piv"].rotation_mode = "ZYX"; ph["piv"].rotation_euler = (math.radians(42), 0, math.pi)      # tilted flatter: top edge under the chin
    a_hold(h, ph, t0, t1, height=4.3, fwd=0.95, approach=0.6)
    a_look(h, t0 - 0.1, ph["root"])
    acting.ladder(h, t0 + 0.15, ["shock", "pop_shock", "worried_dart"])
    frame_on([h], t0, t1, "mcu", lens=50, yaw=15, pitch=14)     # slightly above: the open mouth reads over the phone


@S(23, 124, 129, "WIDE (side): lunch - Leo walks in along the tables, every seated kid turns to stare at him")
def s23(t0, t1):
    cafeteria(line=True)
    h = leo(t0, t1, "worried", loc=(CX - 9.0, 7.0, 0), rot=56)
    mo.walk(h, t0 - 0.3, t1, [(CX - 9.0, 7.0, 0), (CX - 5.2, 4.4, 0)])     # diagonal toward the lens: face 3/4 visible
    mo.idle(h, t0, t1, 0.6)
    target = (CX - 7.0, 5.6, 4.6)
    ks = caf_kids([(CX - 13, 14.3, 0), (CX - 9.3, 14.3, 0), (CX - 5.6, 14.3, 0), (CX + 7.5, 14.3, 0),
                   (CX - 12, 26.3, 0), (CX - 3.0, 26.3, 0)], t0, t1, ["neutral", "sus", "smug"])
    for k, c in enumerate(ks):
        a_look(c, t0 + 0.3 + 0.12 * k, target, dur=0.25)
        acting.face(c, t0 + 0.5 + 0.12 * k, ["toothy", "laugh_smug", "smug"][k % 3])
    still_cam(t0, t1, (CX - 6.5, -9.5, 6.8), (CX - 6.5, 10.0, 3.8), lens=26, push=0.05, fstop=5.0)
    qa.frame(h, t0, t1, "full")


@S(24, 129, 134, "POV (Leo): the front table QUACKS at him - beaks open, elbows flapping like wings, eyes on Leo (the lens)")
def s24(t0, t1):
    cafeteria(line=False)
    ks = caf_kids([(CX - 13.4, 14.3, 0), (CX - 10.0, 14.3, 0), (CX - 6.6, 14.3, 0)], t0, t1, ["toothy"], start=30)
    frame_on(ks, t0, t1, "mcu", lens=32, pitch=6, yaw=40, margin=0.03)        # diagonal: the 3 kids overlap, heads ~10 %
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    target = tuple(bpy.context.scene.camera.matrix_world.translation)
    for k, c in enumerate(ks):
        mock_quack(c, t0, t1, target, hz=2.4 + 0.3 * (k % 2), stagger=0.07 * k, turn=False)


@S(25, 134, 136, "POV (Leo): three kids stand at the table, point and laugh at Leo (the lens) - 'Everyone laughed.'")
def s25(t0, t1):
    cafeteria(line=False)
    ks = [kid(k, t0, t1, "joy", loc=(CX - 10 + x, y, 0), rot=0, name=f"LK{k}")       # staggered trio: middle kid a step back
          for k, (x, y) in enumerate(((-2.5, 7.0), (0.0, 8.3), (2.5, 7.0)))]
    cam = frame_on(ks, t0, t1, "mcu", lens=32, pitch=3, margin=0.03)
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    cp = bpy.context.scene.camera.matrix_world.translation.copy()
    away = Vector((cp.x - (CX - 10), cp.y - 7.0, 0)).normalized()
    hp = cp + away * 1.2
    h = leo(t0, t1, "sad", loc=(hp.x, hp.y, 0), rot=180)
    mo.idle(h, t0, t1, 0.5)
    crowd_laugh(ks, t0, t1, h)


@S(26, 136, 140, "MCU: Max at his table, head DOWN at his tray, does NOT look up - a shiny gold LIMITED hat on")
def s26(t0, t1):
    cafeteria(line=True)
    m = maxx(t0, t1, "worried", loc=(CX + 10, 26.3, 0), rot=0, hat=True)
    seated(m, t0); mo.idle(m, t0, t1, 0.4)
    tr = P3.tray("mtray", loc=(CX + 10, 24.85, 2.75)); qa.rest(tr["root"], t0, t1)
    tray_pt = (CX + 10, 24.85, 2.9)
    a_head_down(m, t0, t1, pitch=26, lean=10)
    qa.look(m, tray_pt, t0 + 0.1, t1, tol=40)
    acting.dart(m, t0 + 0.2, t1)
    caf_kids([(CX + 4.5, 26.3, 0), (CX + 15, 26.3, 0)], t0, t1, ["joy"], start=40)
    frame_on([m], t0, t1, "mcu", lens=50, yaw=-12, pitch=11, extra=[(CX + 10, 24.6, 2.8)])     # Leo's standing eye line: head-down reads


@S(27, 140, 145, "MCU: Leo by the table end, eyes narrowing on Max - 'Then I saw his head.'")
def s27(t0, t1):
    cafeteria(line=True)
    h = leo(t0, t1, "sus", loc=(CX + 10.5, 20.2, 0), rot=170)
    mo.idle(h, t0, t1, 0.6)
    tgt = (CX + 10, 26.3, 5.2)
    mo.look_at(h, t0 - 0.3, tgt); qa.look(h, tgt, t0 + 0.1, t1, tol=40)
    acting.face(h, t0 + 0.5, "sus")
    frame_on([h], t0, t1, "mcu", lens=50, yaw=15)


@S(28, 145, 150, "CLOSE-UP: Max's head, the shiny gold LIMITED hat filmed level with its band (LIMITED readable), slow push in")
def s28(t0, t1):
    cafeteria(line=False)
    m = maxx(t0, t1, "worried", loc=(CX + 10, 26.3, 0), rot=0, hat=True)
    seated(m, t0); mo.idle(m, t0, t1, 0.3)
    a_head_down(m, t0, t1, pitch=6, lean=4)
    acting.dart(m, t0 + 0.3, t1)
    tr = P3.tray("mtray", loc=(CX + 10, 24.85, 2.75)); qa.rest(tr["root"], t0, t1)
    bpy.context.scene.frame_set(F(t0 + 0.3)); bpy.context.view_layer.update()
    hc = m.head.matrix_world.translation.copy()
    band = m.head.matrix_world @ Vector((0, -0.6, 0.55))
    ctr = hc + Vector((0, -0.2, 0.32))                       # whole head + hat in frame (band readable, no slice)
    c = Cam("Cam_hat", 60)
    p = ctr + Vector((0.6, -7.0, -0.3))
    c.key(t0, tuple(p), tuple(ctr), 60, focus=tuple(band), fstop=2.4)
    c.key(t1, tuple(p + (ctr - p) * 0.05), tuple(ctr), 60, focus=tuple(band), fstop=2.4, ease="EASE_IN_OUT")
    cams.micro(c, deg=0.15, loc=0.008, period=2.0)
    light("hat_glint", "AREA", tuple(Vector(band) + Vector((-2.5, -3.0, 2.5))), 260, hexc("#fff3d6"), 1.0, target=tuple(band))
    qa.frame(m, t0, t1, "mcu")


@S(29, 150, 153, "MCU: Leo realises - shock to anger - 'Five hundred coins.'")
def s29(t0, t1):
    cafeteria(line=True)
    h = leo(t0, t1, "pop_shock", loc=(CX + 10.5, 20.2, 0), rot=170)
    mo.idle(h, t0, t1, 1.0)
    tgt = (CX + 10, 26.3, 5.2)
    mo.look_at(h, t0 - 0.3, tgt); qa.look(h, tgt, t0 + 0.1, t1, tol=40)
    acting.ladder(h, t0 + 0.1, "anger_to_worry")
    acting.face(h, t0 + 0.9, "angry")
    frame_on([h], t0, t1, "mcu", lens=55, yaw=-10)


@S(30, 153, 159, "OTS (Max's hat FG edge): Leo drops onto the bench across the table from Max, glaring at him")
def s30(t0, t1):
    cafeteria(line=True)
    m = maxx(t0, t1, "worried", loc=(CX + 10, 26.3, 0), rot=0, hat=True)
    seated(m, t0); mo.idle(m, t0, t1, 0.4)
    a_head_down(m, t0, t1, pitch=26, lean=10)
    tr = P3.tray("mtray", loc=(CX + 10, 24.85, 2.75)); qa.rest(tr["root"], t0, t1)
    h = leo(t0, t1, "angry", loc=(CX + 10, 21.7, 0), rot=180)
    mo.sit(h, t0 - 0.05, seat_h=1.5); qa.sit(h); mo.idle(h, t0, t1, 0.6)     # lands on the cut: we see the settle
    a_look(h, t0 + 0.6, m)
    ots(t0, t1, m, h, lens=45, back=2.8, side=1.45, up=1.0, aim_dz=-0.7, shot="mcu")      # Max's hat = soft FG corner


@S(31, 159, 165, "MCU: Leo seated, hurt and angry - 'Was I worth five hundred coins?'")
def s31(t0, t1):
    cafeteria(line=True)
    h = leo(t0, t1, "angry", loc=(CX + 10, 21.7, 0), rot=180)
    seated(h, t0); mo.idle(h, t0, t1, 0.8)
    a_look(h, t0 - 0.1, (CX + 10, 26.3, 4.7))
    a_talk(h, W(159), W(165), V.words, strip_arms=False, stress=("worth", "coins?\""), expr_on={"coins?\"": "sad"}, hands=False)
    frame_on([h], t0, t1, "mcu", lens=50, yaw=12)


@S(32, 165, 170, "MCU: Max stares down at his tray, guilty, eyes darting - 'He stared at his tray.'")
def s32(t0, t1):
    cafeteria(line=True)
    m = maxx(t0, t1, "worried_dart", loc=(CX + 10, 26.3, 0), rot=0, hat=True)
    seated(m, t0); mo.idle(m, t0, t1, 0.4)
    tr = P3.tray("mtray", loc=(CX + 10, 24.85, 2.75)); qa.rest(tr["root"], t0, t1)
    tray_pt = (CX + 10, 24.85, 2.9)
    a_head_down(m, t0, t1, pitch=20, lean=8)
    qa.look(m, tray_pt, t0 + 0.1, t1, tol=40)
    acting.dart(m, t0, t1)
    frame_on([m], t0, t1, "mcu", lens=50, yaw=15, pitch=2, extra=[(CX + 10, 24.6, 2.8)])      # low: eyes visible under the brim


@S(33, 170, 175, "MCU: Max shrugs, palms up, head tilted, sheepish grin - 'It was a limited, bro.'")
def s33(t0, t1):
    cafeteria(line=True)
    m = maxx(t0, t1, "smug", loc=(CX + 10, 26.3, 0), rot=0, hat=True)
    seated(m, t0); mo.idle(m, t0, t1, 0.6)
    tr = P3.tray("mtray", loc=(CX + 10, 24.85, 2.75)); qa.rest(tr["root"], t0, t1)
    rest = mo.sample(m, t0, ["armL", "armR"])
    ts = W(171)
    m.pose(t0, head=(0, 6, 0), torso=(0, 0, 0), armL=rest["armL"], armR=rest["armR"])
    m.pose(ts - 0.12, armL=rest["armL"], armR=rest["armR"], head=(0, 6, 0))
    shrug = dict(armL=(38, 40, -20), armR=(38, 40, -20), head=(0, 2, 13), torso=(0, -2, 4))   # mo.shrug pose, no strike/hipz dip
    m.pose(ts + 0.12, **shrug)
    for t in (W(173), t1 + 0.2):
        m.pose(t, **shrug)
    a_talk(m, W(170), W(175), V.words, stress=("limited,",), expr_on={"bro.\"": "smug_up"}, hands=False)
    frame_on([m], t0, t1, "mcu", lens=45, yaw=-12, pitch=6, margin=0.12)     # wider MCU: shoulders + raised forearms of the shrug
