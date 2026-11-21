# EP3 part B - owned ONLY by Blender agent B. Executed inside shots.py's namespace (all common helpers available).
# Shots 34-63 (bus, camp, storm, duck light, choice, morning tents, resolution, end card). Put new helpers for this part HERE, prefixed b_ . Do not edit shots.py (common) - ask the Manager via BOARD.md.
# v2 (B, 2026-11-16): every character shot is framed by b_frame (fit camera, absolute yaw); singles do not build the
# off-screen partner (no sliced foreground heads); standing kids are kept off the stone ring; the circle is staged so
# Chase sits at Leo's RIGHT and grabs Leo's RIGHT forearm with his LEFT hand (contact by construction).
from rbx import shotlib as _SL

# ------------------------------------------------------------------ B helpers
B_LEO = (-1.6, -3.6)                       # circle seats relative to (KX, KY); duck on the flat rock at the centre
B_CHASE = (0.95, -3.95)                    # Chase at Leo's right, 2.6 away, body turned a little toward Leo
B_JAY = (0.6, 3.8)
B_RING = [(3.9 * math.sin(math.radians(a)), 3.9 * math.cos(math.radians(a))) for a in (50, 95, 130, 240, 285, 325)]
B_MEET = (-8.0, -4.0)                      # morning: Max finds Leo by the tents (clear of the stone ring)
B_GROUP = (0.0, -6.5)
B_KNEEL = dict(KNEEL_POSE, hipz=-0.47)    # KNEEL_POSE put the down knee 0.29 under the camp grass (QA FLOAT)
B_MAXZ = 0.07
B_KNEEL2 = dict(hipz=-0.47, torso=(0, 8, 0), legL=(0, 0, 0), kneeL=90, legR=(0, 0, 0), kneeR=90)   # both knees down
B_PRE = 1.5     # build every character 1.5 s BEFORE the shot: cast._finish keys the 'stand' stance (arms, legs, neck,
                # hip yaw) at its t0, which overwrote every pre-shot pose (seat legs, look_at at t0-0.3, kneel, hold
                # reach) AT the first frame: seated legs went straight down into the ground, eyelines snapped back.                              # Max's sad slump dips his hip 0.08: lift the root so the soles stay on the grass                      # storm kids huddle here (clear of the stone ring, radius <= 2.1)


def b_rot_to(dx, dy):
    """cast rot (deg) that faces the direction (dx, dy): rot r faces (sin r, -cos r)."""
    return math.degrees(math.atan2(dx, -dy))


def b_chase_rot():
    to_c = Vector((-B_CHASE[0], -B_CHASE[1], 0)).normalized()
    to_l = Vector((B_LEO[0] - B_CHASE[0], B_LEO[1] - B_CHASE[1], 0)).normalized()
    d = to_c * 0.65 + to_l * 0.35
    return b_rot_to(d.x, d.y)


def b_hide(*prefixes):
    for o in list(bpy.context.scene.objects):
        if o.name.startswith(prefixes):
            force_hidden(o)


def b_hide_trees(p, r=11.0, seg_to=None):
    """Hide camp trees near the camera position p (and, with seg_to, any tree standing between p and seg_to)."""
    p = Vector(p)
    for i in range(20):
        t = bpy.data.objects.get(f"camp_tree{i}_t")
        if t is None:
            continue
        q = Vector((t.location.x, t.location.y, 0)); pp = Vector((p.x, p.y, 0))
        near = (q - pp).length < r
        if seg_to is not None and not near:
            a = pp; b = Vector((seg_to[0], seg_to[1], 0)); ab = b - a
            k = max(0.0, min(1.0, (q - a).dot(ab) / max(1e-6, ab.length_squared)))
            near = (a + ab * k - q).length < 6.5 and k < 0.98
            if not near and ab.length < 12.0:              # singles: no canopy directly BEHIND the head (green 'helmet')
                k2 = (q - a).dot(ab) / max(1e-6, ab.length_squared)
                near = 1.0 < k2 < 9.0 and (a + ab * k2 - q).length < 4.0 + 1.2 * k2
        if near:
            b_hide(f"camp_tree{i}_")


def b_pts(ch, times, shot):
    """_frame_points (top, low, +-width along the character's own left/right) PLUS a ring around the head and the
    chest: _frame_points' width runs along the character's side axis, which is the DEPTH axis in a profile shot, so
    profile two-shots sliced both heads at the frame edges (s56 v3)."""
    out = []
    rr = {"mcu": (0.95, 1.25), "med": (1.0, 1.7), "cowboy": (1.0, 1.7), "full": (1.0, 1.7)}[shot]
    for t in times:
        out += _SL._frame_points(ch, t, shot)
        hd = ch.head.matrix_world.translation.copy()
        for k in range(8):
            a = math.radians(45 * k)
            out.append(hd + Vector((math.cos(a) * rr[0], math.sin(a) * rr[0], 0.55)))
            out.append(hd + Vector((math.cos(a) * rr[1], math.sin(a) * rr[1], -1.6)))
    return out


def b_cam_fit(t0, t1, pts, yaw, pitch=4.0, lens=35, margin=0.06, headroom=0.04, push=0.06, fstop=2.8, tgt=None,
              name="Cam_b", micro=True, scale=1.03):
    """Camera that fits every point in pts inside the 9:16 frame, looking from world direction yaw/pitch (deg;
    yaw 0 = camera at -Y of the target, 90 = at +X). Distance solved by bisection (same math as frame_on)."""
    pts = [Vector(p) for p in pts]
    mn = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    mx = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    tgt = Vector(tgt) if tgt is not None else (mn + mx) / 2
    ty = 12.0 / lens; tx = ty * 9 / 16
    lim_x, lim_y = tx * (1 - 2 * margin), ty * (1 - 2 * margin)
    ya, pa = math.radians(yaw), math.radians(pitch)
    dirv = Vector((math.sin(ya) * math.cos(pa), -math.cos(ya) * math.cos(pa), math.sin(pa)))

    def fits(p):
        f = (tgt - p).normalized(); r = f.cross(Vector((0, 0, 1))).normalized(); u = r.cross(f)
        for q in pts:
            v = q - p; z = v.dot(f)
            if z <= 0.3 or abs(v.dot(r) / z) > lim_x or abs(v.dot(u) / z) > lim_y - headroom:
                return False
        return True
    lo, hi = 1.0, 120.0
    for _ in range(36):
        mid = (lo + hi) / 2
        if fits(tgt + dirv * mid): hi = mid
        else: lo = mid
    pe = tgt + dirv * hi * scale                     # the push ENDS at the fitted distance (nothing cut at t1)
    p = tgt + (pe - tgt) / (1.0 - push)
    c = Cam(name, lens)
    c.key(t0, tuple(p), tuple(tgt), lens, focus=tuple(tgt), fstop=fstop)
    c.key(t1, tuple(pe), tuple(tgt), lens, focus=tuple(tgt), fstop=fstop, ease="EASE_IN_OUT")
    if micro:
        cams.micro(c, deg=0.3, loc=0.015, period=2.2)
    if bpy.data.objects.get("camp_tree0_t"):            # camp: no tree between the lens and the subject
        b_hide_trees(p, 16.0, seg_to=tgt)
    return c, p, tgt


def b_frame(chars, t0, t1, shot="med", yaw=0.0, pitch=4.0, lens=35, extra=(), times=None, register=True, **kw):
    """frame_on with an ABSOLUTE camera yaw and points sampled over the shot (moving subjects stay in frame)."""
    times = times or [t0 + 0.3, (t0 + t1) / 2, max(t0 + 0.3, t1 - 0.1)]
    pts = [p for ch in chars for p in b_pts(ch, times, shot)] + [Vector(e) for e in extra]
    c, p, tgt = b_cam_fit(t0, t1, pts, yaw, pitch, lens, **kw)
    if register:
        for ch in chars:
            qa.frame(ch, t0, t1, shot)
    return c, p, tgt


def b_head_pt(xy, seated=True, z=None):
    """Where a circle member's face is (look target for singles whose partner is off screen)."""
    return (KX + xy[0], KY + xy[1], z if z is not None else (3.12 if seated else 4.6))


def b_look(ch, t, pt, **kw):
    """mo.look_at a POINT. mo.aim assumes the looker's head is at root + 4.6 (standing); for seated (root on the ground,
    head at 3.12) the point is lifted by the same 1.48 so the pitch is right (EYELINE 44 deg in v2 without this)."""
    sat = ch.name in qa.REG["sit"]
    p = Vector(pt) + Vector((0, 0, 1.48 if sat else 0.0))
    return mo.look_at(ch, t, tuple(p), **kw)


def b_unkey_t0(ch, t0, parts=("shL", "shR", "elbowL", "elbowR")):
    """cast.make keys a stance on the arms at exactly F(t0); hold()'s contact keys every 2nd frame, so on odd parity
    the stance key wins at the first frame of the shot (fist drops 1.4 and the prop, baked from the fists, dips with
    it = NOTOUCH at frame t0). Remove those arm keys BEFORE hold() so the hold is continuous through the cut."""
    from rbx.core import fcurves
    f0 = F(t0)
    for n in parts:
        ob = bpy.data.objects.get(ch.name + "_" + n)
        if ob is None or not ob.animation_data or not ob.animation_data.action:
            continue
        for fc in fcurves(ob.animation_data.action):
            for k in list(fc.keyframe_points):
                if abs(k.co[0] - f0) < 0.5:
                    fc.keyframe_points.remove(k)
                    break


def b_unpop(*chars):
    """KIT BUG workaround (motion.strike): the anticipation key writes hipz = prev.get('hipz', 0.0) - dip when the pose
    has no hipz, i.e. a SEATED (-1.45) or KNEELING (-0.47) character pops up to standing height for one frame on every
    look_at / reach / follow approach. Clamp hip z keys that jump > 0.35 above the held low pose back down to it.
    Call at the END of a shot for every seated/kneeling character."""
    from rbx.core import fcurves
    for ch in chars:
        hip = bpy.data.objects.get(ch.name + "_hip")
        if hip is None or not hip.animation_data or not hip.animation_data.action:
            continue
        for fc in fcurves(hip.animation_data.action):
            if fc.data_path != "location" or fc.array_index != 2:
                continue
            ks = sorted(fc.keyframe_points, key=lambda k: k.co[0])
            low = None
            for k in ks:
                v = k.co[1]
                if low is not None and v > low + 0.35:
                    k.co[1] = low - 0.02; k.handle_left[1] = k.co[1]; k.handle_right[1] = k.co[1]
                elif v < 1.75:
                    low = v
            fc.update()


def b_hands_face(ch, t0, t1):
    """Both fists ON the cheeks (scream): targets are empties parented to the head, so the contact holds."""
    sc = bpy.context.scene; sc.frame_set(F(t0)); bpy.context.view_layer.update()
    hm = ch.head.matrix_world; q = hm.to_quaternion()
    c = hm.translation; fw = q @ Vector((0, -1, 0)); rt = q @ Vector((-1, 0, 0))
    for hand, sgn in (("r", 1), ("l", -1)):
        p = c + rt * (0.66 * sgn) + fw * 0.22 + Vector((0, 0, -0.22))
        e = point_on(ch.head, tuple(hm.inverted() @ p), f"b_cheek_{hand}")
        follow(ch, t0, t1, e, hand=hand, body=None, step=1, approach=0.25, tol=0.4)


def b_hold(ch, prop, t0, t1, **kw):
    """hold(). Call AFTER every body pose of the shot (look_at / pose), because the prop path is baked from the fists
    at call time. No talk_cadence on a holder (it keys the body): use acting.talk (mouth only). The character must be
    built with t0 - B_PRE (else its stance key at t0 drops the fists on the first frame)."""
    return hold(ch, prop, t0, t1, **kw)


def b_pov_phone(h, name, screen, t0, t1, height):
    """pov_phone (shots.py) with b_hold (no first-frame drop)."""
    ph = P3.phone(name, screens=scr(screen), facing="in")
    ph["piv"].rotation_mode = "ZYX"; ph["piv"].rotation_euler = (math.radians(50), 0, math.pi)
    b_hold(h, ph, t0, t1, height=height, fwd=0.95)
    hide_head(h)
    prop_cam(t0, t1, ph, dist=2.5, lens=30, push=0.1, fstop=2.0)
    return ph


def b_kid_at(k, t0, t1, expr, xy, rot, name):
    return kid(k, t0, t1, expr, loc=(KX + xy[0], KY + xy[1], 0), rot=rot, name=name)


def b_circle_set(t_on=None):
    """Night camp + the duck on its flat rock (narrowed to r 0.62 so a kneeling hand reaches the duck's head);
    the stone ring is hidden (seated legs would cross it)."""
    d = circle_duck(t_on=t_on)
    b_hide("camp_stone")
    fl = bpy.data.objects.get("camp_flat")
    if fl:
        fl.scale = (0.62, 0.62, 1.8); fl.location.z = 0.45      # flat stone 0.9 high: duck head top at 2.47
        d["root"].location.z += 0.4
    return d


def b_leo_ground(t0, t1, expr="neutral", idle=0.5):
    h = leo(t0 - B_PRE, t1, expr, loc=(KX + B_LEO[0], KY + B_LEO[1], 0), rot=face_centre(*B_LEO))
    seat(h, t0, seat_h=0.05)
    if idle:
        mo.idle(h, t0, t1, idle)
    return h


def b_chase_ground(t0, t1, expr="worried", idle=0.0):
    c = chase(t0 - B_PRE, t1, expr, loc=(KX + B_CHASE[0], KY + B_CHASE[1], 0), rot=b_chase_rot())
    seat(c, t0, seat_h=0.05)
    if idle:
        mo.idle(c, t0, t1, idle)
    return c


def b_jay(t0, t1, expr="smug"):
    j = jay(t0 - B_PRE, t1, expr, loc=(KX + B_JAY[0], KY + B_JAY[1], 0), rot=face_centre(*B_JAY))
    seat(j, t0, seat_h=0.05)
    return j


def b_jay_phone(t0, t1, expr="smug", height=1.75, fwd=1.25, pre=None):
    j = b_jay(t0, t1, expr)
    if pre:
        pre(j)
    ph = P3.phone("phj", screens=scr("tea_camp.png"), facing="out")
    b_hold(j, ph, t0, t1, height=height, fwd=fwd)
    return j, ph


def b_sleeve(h, c, t0, t1):
    """Leo's RIGHT forearm rests forward over his knee (IK to a reachable point); Chase's LEFT fist rides an empty
    parented to Leo's right forearm (sleeve), so the contact holds by construction. qa.touch registered."""
    sc = bpy.context.scene
    sc.frame_set(F(t0)); bpy.context.view_layer.update()
    M = h.root.matrix_world
    rest_pt = M @ Vector((-0.9, -1.25, 1.45))          # local: -X = Leo's right, -Y = forward
    mo.reach(h, t0 - 0.6, tuple(rest_pt), hand="r")
    mo.contact(h, t0 - 0.55, t1 + 0.2, tuple(rest_pt), hand="r", step=3)
    lo = bpy.data.objects.get(h.name + "_sleeve_armR_lo") or bpy.data.objects.get(h.name + "_armR_lo")
    sc.frame_set(F(t0)); bpy.context.view_layer.update()
    bb = [lo.matrix_world @ Vector(cn) for cn in lo.bound_box]
    ctr = sum(bb, Vector()) / 8
    top = ctr + Vector((0, 0, 0.32))
    tg = point_on(lo, tuple(lo.matrix_world.inverted() @ top), "b_sleeve_tg")
    follow(c, t0, t1, tg, hand="l", body=None, step=1, approach=0.35, tol=0.4)
    return tg


def b_ground_kids(t0, t1, spots, exprs=("worried",), start=20, sit_from=None, gap=0.38):
    """Classmates sitting ON THE GROUND around the duck, facing it. sit_from=t: they sit down one by one from t."""
    ks = []
    for k, (x, y) in enumerate(spots):
        c = b_kid_at(start + k, t0 - B_PRE, t1, exprs[k % len(exprs)], (x, y), face_centre(x, y), f"GK{start + k}")
        mo.idle(c, t0, t1, 0.6)
        if sit_from is None:
            seat(c, t0, seat_h=0.05)
        else:
            mo.sit(c, sit_from + gap * k, seat_h=0.05); qa.sit(c)
        ks.append(c)
    return ks


def b_morning(t0, t1, who=("leo", "max"), mexpr="sad", lexpr="neutral", gap=1.45, cheat=0.0, lcheat=None):
    """Morning by the tents (day look). Leo at B_MEET - gap (faces +X), Max at B_MEET + gap (faces -X)."""
    camp(night=False)
    b_hide("lamp")                        # morning: lamps are off; their poles cut through the frames (B13, B18)
    out = {}
    if "leo" in who:
        out["leo"] = leo(t0 - B_PRE, t1, lexpr, loc=(KX + B_MEET[0] - gap, KY + B_MEET[1], 0), rot=90 - (cheat if lcheat is None else lcheat))
        mo.idle(out["leo"], t0, t1, 0.5)
    if "max" in who:
        out["max"] = maxx(t0 - B_PRE, t1, mexpr, loc=(KX + B_MEET[0] + gap, KY + B_MEET[1], B_MAXZ), rot=-90 + cheat, hat=True)
    return out


def b_meet_head(who, gap=1.45):
    s = -1 if who == "leo" else 1
    return (KX + B_MEET[0] + s * gap, KY + B_MEET[1], 4.62)


# ------------------------------------------------------------------ shots
@S(34, 175, 183, "MED: two weeks - Leo alone on the bus seat by the window, the seat beside him empty")
def s34(t0, t1):
    B = bus()
    x, y = B["seat"](2, -1)
    b_hide("bus_cu1-1", "bus_bk1-1", "bus_fr1-1", "bus_cu0-1", "bus_bk0-1", "bus_fr0-1")   # the camera stands there
    h = leo(t0 - B_PRE, t1, "sad", loc=(x - 2.0, y, 0), rot=0)
    seated(h, t0); mo.idle(h, t0, t1, 0.4)
    mo.look_at(h, t0 - 0.3, (x - 11, y - 5, 5.2))          # out of the window, away from the empty seat
    b_frame([h], t0, t1, "med", yaw=30, pitch=7, lens=24, extra=[(x + 2.8, y - 0.4, 1.4)], fstop=2.8, push=0.08)
    rig([h], strength=0.4)
    b_unpop(h)


@S(35, 183, 189, "WIDE: the class camping trip - CAMP BLOX sign, tents in a clearing, sunny afternoon")
def s35(t0, t1):
    camp(night=False)
    kids = [kid(k, t0 - B_PRE, t1, "happy", loc=(KX + x, KY + y, 0), rot=r, name=f"DK{k}") for k, (x, y, r) in
            enumerate(((-7, -2.5, 20), (-3.5, 4.0, -10), (3.5, -3.0, 30), (6.0, 4.5, -40)))]
    for k, c in enumerate(kids):
        mo.idle(c, t0, t1, 1.0)
    cp, tg = (KX - 6, KY - 21, 8.5), (KX - 7.5, KY + 8, 3.2)          # inside the tree ring; CAMP BLOX sign upper left
    b_hide_trees(cp, 12, seg_to=tg)
    still_cam(t0, t1, cp, tg, lens=22, push=0.06, fstop=8)


@S(36, 189, 194, "WIDE NIGHT: camp at night, lamps on - a lightning flash on 'storm'")
def s36(t0, t1):
    camp(night=True, lightning=(W(192) + 0.05,))
    gx, gy = B_GROUP
    kids = [kid(k, t0 - B_PRE, t1, "worried", loc=(KX + gx + x, KY + gy + y, 0), rot=r, name=f"NK{k}") for k, (x, y, r) in
            enumerate(((-5, 1.0, 30), (-1.8, -0.5, 0), (2.0, -0.2, -20), (5.2, 1.2, -40)))]
    for c in kids:
        mo.idle(c, t0, t1, 1.2)
        mo.look_at(c, W(192) + 0.15, (KX, KY + 10, 20))
    pts = [p for c in kids for p in b_pts(c, [t0 + 0.3, t1 - 0.1], "full")]
    pts += [(KX - 8, KY + 6, 7.2), (KX + 9, KY + 5, 7.2), (KX, KY + 15, 6.0)]     # lamps + the blue tent behind
    cam, p, tg = b_cam_fit(t0, t1, pts, yaw=4, pitch=10, lens=26, margin=0.05, fstop=6, push=0.05)
    b_hide_trees(p, 10, seg_to=tg)


@S(37, 194, 199, "MED: the light pole by the tents flickers and DIES on 'camp.' - kids look up at it")
def s37(t0, t1):
    camp(night=True, dark=W(198), flicker=(W(196), W(198)), lightning=(t0 + 0.1,))
    lamp_top = (KX - 8, KY + 6, 6.6)
    kids = [kid(k, t0 - B_PRE, t1, "worried", loc=(KX + x, KY + y, 0), rot=r, name=f"NK{k}") for k, (x, y, r) in
            enumerate(((-5.6, 2.2, 200), (-3.2, 3.4, 215)))]
    for c in kids:
        mo.idle(c, t0, t1, 1.0)
        mo.look_at(c, t0 - 0.2, lamp_top)
        acting.face(c, W(198) + 0.1, "scared")
    kc = (Vector(kids[0].root.location) + Vector(kids[1].root.location)) / 2
    ry = b_rot_to(lamp_top[0] - kc.x, lamp_top[1] - kc.y)       # camera beyond the lamp, low, looking up at them
    b_hide("tent0")                                                  # the camera stands where tent0 is
    b_frame(kids, t0, t1, "mcu", yaw=ry + 14, pitch=-10, lens=24, extra=[lamp_top], fstop=3.5)
    rig(kids, strength=0.3)


@S(38, 199, 201, "MED: pitch black - three kids huddle, only their faces and wide eyes faintly lit")
def s38(t0, t1):
    camp(night=True, dark=-5, lamps=True)
    gx, gy = B_GROUP
    ks = [kid(k, t0 - B_PRE, t1, "terror", loc=(KX + gx + x, KY + gy + y, 0), rot=r, name=f"BK{k}") for k, (x, y, r) in
          enumerate(((-1.95, 0.5, 18), (0, -0.25, 0), (1.95, 0.5, -18)))]
    for c in ks:
        mo.idle(c, t0, t1, 1.4)
        acting.dart(c, t0, t1)
    b_frame(ks, t0, t1, "mcu", yaw=0, pitch=6, lens=35, fstop=2.8)
    rig(ks, strength=0.28)


@S(39, 201, 203, "MCU: a lightning flash lights a girl screaming, hands on her cheeks - 'Somebody screamed.'")
def s39(t0, t1):
    camp(night=True, dark=-5, lightning=(t0 + 0.05,))
    gx, gy = B_GROUP
    g = kid(1, t0 - B_PRE, t1, "scream", loc=(KX + gx, KY + gy, 0), rot=0, name="Mia")
    b_hands_face(g, t0, t1)
    b_frame([g], t0, t1, "mcu", yaw=0, pitch=3, lens=50)
    rig([g], strength=0.4)


@S(40, 203, 206, "MED: then everybody screams - four kids, arms up, panicking in the dark (lightning)")
def s40(t0, t1):
    camp(night=True, dark=-5, lightning=(t0 + 0.4, t1 - 0.6))
    gx, gy = B_GROUP
    ks = [kid(k, t0 - B_PRE, t1, "scream", loc=(KX + gx + x, KY + gy + y, 0), rot=r, name=f"SK{k}") for k, (x, y, r) in
          enumerate(((-3.3, 0.6, 15), (-1.1, -0.4, 5), (1.1, -0.2, -5), (3.3, 0.7, -15)))]
    for k, c in enumerate(ks):
        mo.idle(c, t0, t1, 1.2)
        acting.panic(c, t0 + 0.05 * k, t1)
    b_frame(ks, t0, t1, "med", yaw=0, pitch=5, lens=32)
    rig(ks, strength=0.35)


@S(41, 206, 211, "LOW MED: in the dark Leo kneels by his open backpack and lifts out the duck night-light (off)")
def s41(t0, t1):
    camp(night=True, dark=-5)
    b_hide("camp_stone")
    lx, ly = -5.5, -5.0
    h = leo(t0 - B_PRE, t1, "determined", loc=(KX + lx, KY + ly, 0), rot=b_rot_to(0.6, 1.0))
    h.pose(t0 - 0.6, **B_KNEEL); h.pose(t1 + 0.3, **B_KNEEL)
    mo.idle(h, t0, t1, 0.3)
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    fw = h.root.matrix_world.to_quaternion() @ Vector((0, -1, 0)); fw.z = 0; fw.normalize()
    bp = Vector(h.root.matrix_world.translation) + fw * 2.0
    yaw = math.atan2(fw.y, fw.x) + math.pi / 2
    pk = box("leo_pack", (1.6, 1.0, 1.4), (bp.x, bp.y, 0.7), mat("pack_m", hexc("#c0392b"), 0.7), 0.25)
    fl = box("leo_pack_flap", (1.5, 0.25, 0.9), (bp.x, bp.y, 1.0), mat("pack_m2", hexc("#962d22"), 0.7), 0.1)
    pk.rotation_euler = (0, 0, yaw); fl.rotation_euler = (math.radians(-35), 0, yaw)
    fl.location = bp - fw * 0.62 + Vector((0, 0, 1.15))          # flap hangs open toward Leo's knees
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    b_look(h, t0 - 0.2, tuple(Vector(h.root.matrix_world.translation) + fw * 1.3 + Vector((0, 0, 2.2))))
    d = P3.duck_light("duck", s=0.75, lit=False)
    b_hold(h, d, t0, t1, height=2.45, fwd=1.05)
    b_frame([h], t0, t1, "med", yaw=math.degrees(math.atan2(fw.x, -fw.y)) + 35, pitch=-2, lens=32,
            extra=[tuple(bp + Vector((0, 0, 0.1)))], fstop=2.4)
    rig([h], strength=0.34)
    b_unpop(h)


@S(42, 211, 215, "MCU: Leo's finger clicks the duck's switch - it glows warm and lights his face")
def s42(t0, t1):
    camp(night=True, dark=-5)
    t_on = W(214)                     # the glow pops on 'duck.' (the tap lands on screen, not in the first frames)
    d = b_circle_set(t_on=t_on)
    dd = Vector(B_LEO).normalized() * 1.2
    h = leo(t0 - B_PRE, t1, "determined", loc=(KX + dd.x, KY + dd.y, 0), rot=face_centre(dd.x, dd.y))
    h.pose(t0 - 0.6, **B_KNEEL2); h.pose(t1 + 0.3, **B_KNEEL2)
    b_look(h, t0 - 0.3, (KX, KY, 1.5))
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    sh = bpy.data.objects[h.name + "_shL"].matrix_world.translation.copy()
    top = d["root"].matrix_world @ Vector((d["head_top"][0], d["head_top"][1], d["head_top"][2] + 0.18))
    tw = top - Vector((top.x - sh.x, top.y - sh.y, 0)).normalized() * -0.0
    tw = top + Vector((sh.x - top.x, sh.y - top.y, 0)).normalized() * 0.38      # the side of the head facing Leo
    sw = point_on(d["root"], tuple(d["root"].matrix_world.inverted() @ tw), "duck_tap")
    follow(h, t0 + 0.05, t_on + 0.35, sw, hand="l", body=None, step=1, approach=0.25, tol=0.4)
    h.pose(t_on + 0.8, armL=(20, -4, 0), elbowL=30)
    acting.face(h, t_on + 0.15, "content")
    bpy.context.scene.frame_set(F(t0)); bpy.context.view_layer.update()
    yaw = face_centre(dd.x, dd.y) + 62                     # side-front: the fist ON the duck's head reads in profile
    b_frame([h], t0, t1, "mcu", yaw=yaw, pitch=6, lens=40, extra=[(KX, KY, 1.6), (KX, KY, 0.9)],
            times=[t0 + 0.3, t1 - 0.1], fstop=2.4, push=0.06)
    rig([h], strength=0.3, warm="#ffd66b")
    b_unpop(h)


@S(43, 215, 225, "HIGH WIDE (from behind the duck): one by one the whole class sits down on the ground around the glowing duck")
def s43(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    h = b_leo_ground(t0, t1, "content")
    c = b_chase_ground(t0, t1, "worried")
    ks = b_ground_kids(t0, t1, B_RING, exprs=("worried", "relief"), sit_from=t0 + 0.2, gap=0.45)
    for k, kk in enumerate(ks):
        acting.face(kk, t0 + 0.6 + 0.45 * k, "relief")
    pts = []
    for ch in [h, c] + ks:
        pts += b_pts(ch, [t0 + 0.2 + 0.5 * k for k in range(int((t1 - t0) / 0.5))] + [t1 - 0.1, t1], "full")
    cam, p, tg = b_cam_fit(t0, t1, pts, yaw=172, pitch=32, lens=20, margin=0.04, fstop=5.0, push=0.05)
    for ch in [h, c]:
        qa.frame(ch, t0, t1, "full")
    rig([h, c] + ks, strength=0.3, warm="#ffd66b")
    b_unpop(h, c)


@S(44, 225, 227, "MCU: even Chase sits in the circle - scared, lit by the duck - 'Even Chase.'")
def s44(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    c = b_chase_ground(t0, t1, "worried", idle=1.0)
    acting.dart(c, t0, t1)
    b_look(c, t0 - 0.2, (KX, KY, 1.6))
    b_frame([c], t0, t1, "mcu", yaw=b_chase_rot() - 12, pitch=4, lens=50, extra=[(KX, KY, 1.6)])
    rig([c], strength=0.3, warm="#ffd66b")
    b_unpop(c)


@S(45, 227, 230, "MED: Chase hugs himself and shakes, eyes darting into the dark - 'Chase was shaking.'")
def s45(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    c = b_chase_ground(t0, t1, "scared")
    shiver(c, t0, t1, amp=1.8, hz=9)
    b_frame([c], t0, t1, "med", yaw=b_chase_rot() + 10, pitch=5, lens=40)
    rig([c], strength=0.3, warm="#ffd66b")
    b_unpop(c)


@S(46, 230, 235, "TWO-SHOT: Chase, scared, holds Leo's hoodie sleeve with his left hand - both sitting in the duck glow")
def s46(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    h = b_leo_ground(t0, t1, "content", idle=0)
    c = b_chase_ground(t0, t1, "scared")
    sc = bpy.context.scene; sc.frame_set(F(t0)); bpy.context.view_layer.update()
    rest = h.root.matrix_world @ Vector((-0.9, -1.25, 1.45))
    b_look(h, t0 - 0.3, tuple(rest + Vector((0, 0, 0.3))))        # Leo glances down at the hand on his sleeve
    b_look(h, W(232) + 0.1, tuple(rest + Vector((0, 0, 0.3))))
    tg = b_sleeve(h, c, t0, t1)
    acting.dart(c, t0, t1)
    mid = Vector(((B_LEO[0] + B_CHASE[0]) / 2, (B_LEO[1] + B_CHASE[1]) / 2, 0))
    yaw = math.degrees(math.atan2(-mid.x, mid.y)) - 12   # camera on the centre side, a bit toward Leo's front
    b_frame([h, c], t0, t1, "mcu", yaw=yaw, pitch=16, lens=30, fstop=2.4, push=0.05, extra=[tuple(Vector(tg.matrix_world.translation))])
    rig([h, c], strength=0.3, warm="#ffd66b")
    b_unpop(h, c)


@S(47, 235, 240, "MED: Jay, across the circle, holds up his phone with a smirk - 'Someone held up a phone.'")
def s47(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    j, ph = b_jay_phone(t0, t1, "smug")
    acting.ladder(j, t0 + 0.4, ["smug", "smug_up"])
    b_frame([j], t0, t1, "med", yaw=face_centre(*B_JAY) - 28, pitch=6, lens=45)
    rig([j], strength=0.3, warm="#ffd66b")
    b_unpop(j)


@S(48, 240, 243, "MCU: Jay grins, phone out toward Leo - 'Post it, Leo.'")
def s48(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    j, ph = b_jay_phone(t0, t1, "grin")
    acting.talk(j, W(240), W(243), V.words)
    b_frame([j], t0, t1, "mcu", yaw=face_centre(*B_JAY) + 26, pitch=6, lens=50)
    rig([j], strength=0.3, warm="#ffd66b")
    b_unpop(j)


@S(49, 243, 248, "INSERT: Jay's phone, straight-on - photo of Chase holding Leo's sleeve: 'Chase is SCARED of the DARK?!' POST +500")
def s49(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    j, ph = b_jay_phone(t0, t1, "grin")
    prop_cam(t0, t1, ph, dist=3.2, lens=45, push=0.06, fstop=2.0, up=0.9)
    b_unpop(j)


@S(50, 248, 252, "MCU: Leo turns his head from Jay to Chase - 'I looked at Chase.'")
def s50(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    h = b_leo_ground(t0, t1, "neutral")
    cpt = b_head_pt(B_CHASE)
    b_look(h, t0 - 0.3, b_head_pt(B_JAY))
    b_look(h, W(249) + 0.1, cpt)
    acting.face(h, W(251), "sad")
    qa.look(h, cpt, W(249) + 0.5, t1, tol=35)
    b_frame([h], t0, t1, "mcu", yaw=118, pitch=4, lens=50, extra=[(KX - 0.4, KY - 2.2, 1.6)])
    rig([h], strength=0.3, warm="#ffd66b")
    b_unpop(h)


@S(51, 252, 258, "MCU (Leo's eyeline): Chase looks back at him, scared, a tear - 'I knew exactly how that felt.'")
def s51(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    c = b_chase_ground(t0, t1, "sad_tear", idle=0.6)
    lpt = b_head_pt(B_LEO)
    b_look(c, t0 - 0.3, lpt)
    qa.look(c, lpt, t0 + 0.1, t1, tol=35)
    acting.face(c, t0 + 0.8, "sad_tear")
    b_frame([c], t0, t1, "mcu", yaw=-112, pitch=4, lens=50)
    rig([c], strength=0.32, warm="#ffd66b")
    b_unpop(c)


@S(52, 258, 263, "MCU: Leo, calm small smile, shakes his head - 'Nah. Secrets aren't for sale.'")
def s52(t0, t1):
    camp(night=True, dark=-5)
    d = b_circle_set()
    h = b_leo_ground(t0, t1, "determined")
    b_look(h, t0 - 0.3, b_head_pt(B_JAY))
    mo.shake(h, W(258) + 0.05, n=2, amp=12)
    mo.talk_cadence(h, W(258), W(263), V.words, stress=("Nah.", "sale.\""), expr_on={"sale.\"": "content"}, hands=False)
    b_frame([h], t0, t1, "mcu", yaw=face_centre(*B_LEO) - 15, pitch=4, lens=50, extra=[(KX - 0.6, KY - 1.4, 1.5)])
    rig([h], strength=0.32, warm="#ffd66b")
    b_unpop(h)


@S(53, 263, 272, "WIDE MORNING: sunlit camp, blue sky - Max walks up to Leo by the tents")
def s53(t0, t1):
    P = b_morning(t0, t1, who=("leo",), lexpr="neutral")
    h = P["leo"]
    mx0 = (KX + B_MEET[0] + 3.4, KY + B_MEET[1] - 1.0, B_MAXZ)
    mx1 = (KX + B_MEET[0] + 1.45, KY + B_MEET[1], B_MAXZ)
    m = maxx(t0 - B_PRE, t1, "sad", loc=mx0, rot=-80, hat=True)
    mo.walk(m, t0 + 0.2, W(270), [mx0, mx1])
    mo.turn(m, W(270), target=h)
    mo.look_at(h, W(267), m)
    b_frame([h, m], t0, t1, "full", yaw=-22, pitch=7, lens=30, times=[t0, t0 + 0.3, W(266), W(268), W(270), t1 - 0.1], fstop=5.6)
    p = bpy.context.scene.camera.matrix_world.translation
    b_hide_trees(p, 10)


@S(54, 272, 278, "MED: Max holds out the 500 coin bag toward Leo with both hands, eyes down - 'He held out five hundred coins.'")
def s54(t0, t1):
    P = b_morning(t0, t1, who=("max",), mexpr="sad")
    m = P["max"]
    mo.idle(m, t0, t1, 0.2)
    lpt = b_meet_head("leo")
    mo.look_at(m, t0 - 0.3, (lpt[0], lpt[1], lpt[2] - 0.8))
    acting.face(m, t0 + 1.2, "sad")
    bag = P3.coin_bag("bag54", s=0.72)
    b_hold(m, bag, t0, t1, style="under", height=2.7, fwd=0.95)
    b_frame([m], t0, t1, "med", yaw=-90 + 42, pitch=20, lens=35, fstop=2.4, push=0.1)


@S(55, 278, 282, "CU: Max, sorry eyes, bag held up - 'I'm sorry. Take it.'")
def s55(t0, t1):
    P = b_morning(t0, t1, who=("max",), mexpr="sad")
    m = P["max"]
    mo.idle(m, t0, t1, 0.15)
    mo.look_at(m, t0 - 0.3, b_meet_head("leo"))
    acting.talk(m, W(278), W(282), V.words)
    acting.face(m, W(279) + 0.1, "sad_tear")
    bag = P3.coin_bag("bag55", s=0.72)
    b_hold(m, bag, t0, t1, style="under", height=2.7, fwd=0.95)
    b_frame([m], t0, t1, "mcu", yaw=-90 + 24, pitch=16, lens=55, fstop=2.0)


@S(56, 282, 286, "TWO-SHOT (both cheated open to the lens): Leo's hands on the coin bag push it back into Max's hands - 'I pushed it back.'")
def s56(t0, t1):
    P = b_morning(t0, t1, mexpr="sad", lexpr="determined", gap=1.0, cheat=32, lcheat=36)
    h, m = P["leo"], P["max"]                       # no look_at: it would turn the cheated heads back to profile
    acting.face(m, W(284), "shock")
    bag = P3.coin_bag("bag56", s=0.72)
    r = bag["root"]
    tp = W(283) + 0.05
    sc = bpy.context.scene; sc.frame_set(F(t0)); bpy.context.view_layer.update()
    m0 = Vector(m.root.matrix_world.translation)
    dl = Vector(h.root.matrix_world.translation) - m0; dl.z = 0; dl.normalize()
    m1 = m0 - dl * 0.35                                 # the push: Max is pushed back half a step, bag stays in his hands
    m.pose(tp, loc=tuple(m0)); m.pose(tp + 0.5, loc=tuple(m1))
    r.rotation_euler = (0, 0, math.atan2(dl.x, -dl.y))       # the tag face looks straight at Leo (bodies are cheated)
    keys = []
    for tk in (t0 - 0.6, tp, tp + 0.5, t1 + 0.5):
        sc.frame_set(F(tk)); bpy.context.view_layer.update()
        keys.append((tk, tuple(m.root.matrix_world @ Vector((0, -0.95, 3.8)))))
    path_key(r, keys)
    sc.frame_set(F(t0)); bpy.context.view_layer.update()
    rinv = r.matrix_world.inverted(); mm = m.root.matrix_world
    gl = point_on(r, tuple(rinv @ (mm @ Vector((0.42, -0.85, 3.2)))), "b56_gL")     # grips in MAX's frame (he is cheated 32 deg)
    gr = point_on(r, tuple(rinv @ (mm @ Vector((-0.42, -0.85, 3.2)))), "b56_gR")
    follow(m, t0, t1, gl, hand="l", body=None, step=1, approach=0.25, tol=0.35)
    follow(m, t0, t1, gr, hand="r", body=None, step=1, approach=0.25, tol=0.35)
    fl = point_on(r, (0.2, -0.62, 0.0), "b56_fL"); fr = point_on(r, (-0.46, -0.44, 0.08), "b56_fR")
    follow(h, tp - 0.4, t1, fl, hand="r", body=None, step=1, approach=0.3, tol=0.35)
    follow(h, tp - 0.4, t1, fr, hand="l", body=None, step=1, approach=0.3, tol=0.35)
    qa.prop(r)
    bpy.context.scene.frame_set(F(tp)); bpy.context.view_layer.update()
    bc = Vector(r.matrix_world.translation)
    pts = b_pts(h, [t0 + 0.2, tp, t1 - 0.05], "mcu") + [bc + Vector((dx, dy, dz)) for dx in (-0.8, 0.8) for dy in (-0.8, 0.8) for dz in (-1.0, 0.9)]
    pts += b_pts(m, [t0 + 0.2, tp, t1 - 0.05], "mcu")
    b_cam_fit(t0, t1, pts, yaw=0, pitch=12, lens=35, margin=0.04, fstop=2.8, push=0.05)   # two-shot, both cheated 25 deg open
    qa.frame(h, t0, t1, "mcu")
    qa.frame(m, t0, t1, "mcu")


@S(57, 286, 293, "MCU: Leo, a calm savage smile - 'Keep it. You'll need it to buy...'")
def s57(t0, t1):
    P = b_morning(t0, t1, who=("leo",))
    h = P["leo"]
    mo.look_at(h, t0 - 0.2, b_meet_head("max"))
    acting.face(h, t0 - 0.1, "smug")                      # calm, savage: no talk_cadence shock-eyes
    acting.talk(h, W(286), W(293), V.words)
    acting.face(h, W(288), "smug_up")
    b_frame([h], t0, t1, "mcu", yaw=90 - 26, pitch=3, lens=50)


@S(58, 293, 297, "MCU: Max deflates - jaw drop, then sad - '...a new best friend.' (FAHHH)")
def s58(t0, t1):
    P = b_morning(t0, t1, who=("max",), mexpr="pop_shock")
    m = P["max"]
    mo.look_at(m, t0 - 0.3, b_meet_head("leo"))
    m.pose(t0 + 0.9, torso=(0, 8, 0), head=(0, 14, 0))
    acting.ladder(m, t0 + 0.1, ["pop_shock", "shock", "sad"])
    bag = P3.coin_bag("bag58", s=0.72)
    b_hold(m, bag, t0, t1, style="under", height=2.6, fwd=0.85)
    b_frame([m], t0, t1, "mcu", yaw=-90 + 26, pitch=20, lens=50)


@S(59, 297, 301, "INSERT: Chase's phone, straight-on - @bloxtea ACCOUNT DELETED - 'That week, Chase deleted...'")
def s59(t0, t1):
    hallway(students=True)
    c = chase(t0 - B_PRE, t1, "content", loc=(HX, HY + 2, 0), rot=0)
    mo.idle(c, t0, t1, 0.4)
    ph = P3.phone("ph59", screens=scr("deleted.png"), facing="out")
    b_hold(c, ph, t0, t1, height=3.7, fwd=1.0)
    prop_cam(t0, t1, ph, dist=4.2, lens=45, push=0.1, fstop=2.0)


@S(60, 301, 304, "MCU: Chase lowers the phone and smiles, relieved - '...Blox Tea himself.'")
def s60(t0, t1):
    hallway(students=True)
    c = chase(t0 - B_PRE, t1, "relief", loc=(HX, HY + 2, 0), rot=0)
    mo.idle(c, t0, t1, 0.6)
    acting.face(c, t0 + 0.5, "content")
    frame_on([c], t0, t1, "mcu", lens=50, yaw=-12)


@S(61, 304, 309, "INSERT: a classmate's phone - Duck Night-Light ORDERED! #1 in Blox City")
def s61(t0, t1):
    hallway(students=True)
    k = kid(5, t0 - B_PRE, t1, "joy", loc=(HX + 1, HY + 2, 0), rot=0)
    mo.idle(k, t0, t1, 0.5)
    ph = P3.phone("ph61", screens=scr("order.png"), facing="out")
    b_hold(k, ph, t0, t1, height=3.7, fwd=1.0)
    prop_cam(t0, t1, ph, dist=4.2, lens=45, push=0.1, fstop=2.0)


@S(62, 309, 311, "INSERT: four duck night-lights glowing in a row on a dark windowsill")
def s62(t0, t1):
    D = bedroom(night=True, duck=False)
    box("sill", (9.0, 1.6, 0.3), (BX + 2, BY + 18.9, 3.85), pbr.get("planks", tint="#e8dcc8", tile=3), 0.05)
    for k in range(4):
        d = P3.duck_light(f"dk{k}", s=0.7, loc=(BX + 2 + (k - 1.5) * 1.15, BY + 18.8, 4.0 + 0.49), power=150)
        d["root"].rotation_euler = (0, 0, math.radians(-15 + 10 * k))
        qa.rest(d["root"], t0, t1)
    b_hide("bd_win_gl")                                  # the dark pane MIRRORED the 4 ducks (8 duck shapes); the night sky box shows behind
    still_cam(t0, t1, (BX + 2.0, BY + 8.6, 6.4), (BX + 2, BY + 18.8, 5.4), lens=25, push=0.05, fstop=2.8)


@S(63, 311, None, "END CARD: Leo on his bed hugging the glowing duck, smiling to the lens (centre kept calm for pop-ups)")
def s63(t0, t1):
    D = bedroom(night=True, duck=False)
    h = leo(t0 - B_PRE, t1, "content", loc=(D["bed"][0], D["bed"][1], 0), rot=0)
    on_bed(h, t0); mo.idle(h, t0, t1, 0.6)
    d = P3.duck_light("duck2", s=0.85, power=320)
    hold(h, d, t0, t1, height=4.25, fwd=0.95)
    acting.face(h, t0 + 0.3, "smile"); acting.face(h, W(325), "content"); acting.face(h, W(327) + 0.4, "smile")
    frame_on([h], t0, t1, "med", lens=45, yaw=-10)
    b_unpop(h)
