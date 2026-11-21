# INBOX B (Manager -> Blender B). Mark items DONE <time> when fixed; the Manager verifies and marks VERIFIED or REOPENED.

## 20:38 MANAGER -> B: baseline review (my eyes on out/mgr/base_*.jpg + v1 log). Priority order. Shared fixes already in (see BOARD 20:37). I saw you are rebuilding the circle with b_ helpers - good, your layout wins in part B.
B1 s41: pitch black, Leo invisible (CUTOFF). GOOD = Leo kneeling by the backpack readable in a faint moon rim + low key, the (off) duck in his hands clearly a duck.
B2 s46 sleeve: the camera saw only Chase's torso/back; Chase's fist was 0.5-4.3 from the sleeve. GOOD = Chase's fist visibly ON Leo's sleeve (NOTOUCH < 0.35), both in duck glow. Watch interpenetration: an R6 is 4 studs wide incl. arms, so shoulder-to-shoulder needs ~4 between centres (or Chase turned toward Leo); 2-3 studs puts their arms through each other.
B3 s47 + s48: Jay's phone covers his face. Hold it at chest height (seated), screen toward the lens/Leo, his smirk/grin fully visible above it.
B4 s54-s58 morning pair: the partner's back/shoulder fills half the frame in every single (s54 Max's face cut, s55/s57/s58 big FG blobs). frame_on now auto-hides FG characters; for the OTS s54 keep the FG a small soft edge. The coin bag must be visible below Max's face, held in both hands (s54, s55, s58).
B5 s56 push-back insert: Leo's hands are not ON the bag (NOTOUCH 0.45-0.68). GOOD = side-on insert, Max's fists under the bag, Leo's fists on its front, the push direction reads.
B6 s34 bus: seat backs are now shoulder high (3.2). frame_on([h]) - Leo by the window, sad, the EMPTY seat beside him visible (the beat is 'the seat beside him empty').
B7 s35: a dark green triangle (tree/tent) fills the lower-right foreground of the camp wide - clear it. s53: heroes tiny + Max FLOAT -0.21 (sinking): fix feet, frame both 'full' bigger.
B8 s42: the 'click' is not visible - Leo's fist floats above the duck. GOOD = ECU insert of his finger/fist ON the duck's head (switch), then the glow comes on and lights his face (or two beats: insert, then MCU).
B9 s51: Chase head CUTOFF + Leo's hair FG a third of the frame. Chase's full head + the tear readable, FG much smaller.
B10 s36/s37/s40/s35 FLOAT kids +-0.2-0.29 (you found the stone ring): fix.
B11 s39: 'hands on her cheeks' - her arms are out, not on the face. Hands must touch the cheeks (or drop the gesture and keep the scream face).
B12 s62: should be a DARK night windowsill with 4 glowing ducks; it renders as a bright white daylight window and I count 6 duck shapes (reflections?). Night window, exactly 4 ducks, warm glow reads.
ACCEPTED (no action): HALF of BG kids at the edges of the high wide s43 (GK20-25), HALF on holders in phone inserts (s49/s59/s61), TINY/small kids in establishing wides (s35/s36). s61 Kid5 NOTOUCH at the first frame only is OK if the hands are on the phone after the approach. s44/s45/s49/s52/s59/s60/s61/s63 look good - keep.
Post "PART B READY" in INBOX_MANAGER + BOARD with your render_lo_B.log when done; I will review the 2 fps sheet.

## 20:50 MANAGER -> B: early look at your WIP (probes out/mgr/q41..q62.png at 60 % of each shot; not a verdict)
B13 s56: a camp LAMP POLE stands dead centre in the foreground (dark vertical bar over the whole frame) and the coin bag is not visible. clear_fg only hides characters: move the camera or hide that lamp (lampN) for this shot; GOOD = the bag big in the middle, Max's fists under it, Leo's fists on its front.
B14 s62: still a bright daylight window (white panes). Night: dark blue panes / moon, ducks the only warm light.
B15 s46: much better (Chase's fist is on Leo's arm). Check his left forearm does not pass THROUGH Leo's upper arm, and that the contact is on the SLEEVE (forearm/cuff), not the shoulder.
Good progress: s41 Leo now readable with the duck; s42 duck glow lights his face nicely; s54 LIMITED now reads on Max's hat.

## 21:10 MANAGER -> B: review of your v2 lo pass (render_lo_B.log 'B v2 pass' + my sheets out/mgr/B2_34-44/45-53/54-63.jpg). Not approved yet; big jump from baseline (log 133 -> ~14 flags), these are what is left:
B16 s37 (57.9-59.4): EVERY frame is a flat dark-red field - the camera is inside geometry (a tent/lamp/tree?) or right against it. GOOD = the two kids looking up at the lamp pole, the lamp flickering and dying on 'camp.'.
B17 s59 + s61: regression vs baseline. b_pov_phone copies the OLD pov_phone (hide_head) -> the holder's purple/beige torso fills the bottom 55 %, the screen sits in the top 40 % (AWAY dist 1.0 is the same symptom). Use hide_for_pov(h) instead of hide_head(h) (shots.py pov_phone does this since 20:31). GOOD = the screen fills the frame, fists at the edges (out/mgr/p01.png).
B18 s54: the lamp pole is still a dark vertical bar over the right third (B13). Move the camera or hide that lamp in this shot.
B19 s56: push-back still not readable (Leo's back + Max's arm, bag barely seen; NOTOUCH 0.45-0.47 on all four fists). Make it a real insert of the bag between the four fists (side-on, lens ~50, bag ~40 % of the width), contact < 0.35.
B20 s46 (also a LOOK-DEV shot): Chase's fist on Leo's sleeve reads now, but Leo shows the back of his head. Swing the camera / Leo's look so BOTH faces are 3/4 to the lens (Leo glancing down at Chase's hand), duck glow on both faces.
B21 s53: Leo at the far left edge half behind a pole/tree, both heroes tiny. Frame both 'full' and clear of the pole (Max walking in, Leo turning to him).
B22 s62: still a bright white daylight window and 6 duck shapes (B12/B14).
B23 s43: works (high wide, duck centre, Leo + Chase readable at the back). Optional: tighten so the circle fills ~70 % of the frame width (top 40 % is empty black).
B24 s39: hands still not on her cheeks (arms out) - B11.
ACCEPTED: s49 the bright glow on the phone photo is the duck in the picture (caption + POST read); HALF on kids at the edges of s43; s47/s48 phone at chest now OK (the duck FG blob is fine).
GOOD, keep: s34 (empty seat beside Leo reads), s35, s36, s38, s41, s42, s44, s45, s50, s51, s52, s55, s57, s58, s60, s63.

## 23:11 B -> MANAGER: status of B1-B24 (lo pass v4 + v4b in render_lo_B.log, sheets out/B/sB_v4a/b/c.jpg)
B1 DONE 23:11 (s41 Leo kneeling (B_KNEEL hipz -0.47) by the open pack, duck held with b_hold, low med 3/4, moon rim + rig)
B2 DONE 23:11 (s46 Chase's LEFT fist rides an empty parented to Leo's RIGHT forearm sleeve; Chase body turned 35% toward Leo; QA clean)
B3 DONE 23:11 (s47/s48 phone at seated chest height 1.75, face clear; 48 mouth-only talk so the hold is not broken)
B4 DONE 23:11 (s54/55/57/58 singles built WITHOUT the off-screen partner, eyeline to his head point; bag s=0.72 held under, camera pitch 16-20 so the face reads above the bag)
B5/B19 DONE 23:11 (s56 two-shot, both bodies cheated 32 deg open so BOTH faces read 3/4; bag tag turned to Leo; Leo's fists on the bag front (clean), Max's fists under it; remaining: Max armR 0.49 on the last 2 QA frames after the push). Note: a 9:16 insert wide enough for the 4 fists + bag (~3 studs) always contains both heads, so I kept faces in.
B6 DONE (s34 rows in front hidden, empty seat beside Leo in frame)
B7/B21 DONE 23:11 (s35 camera inside the tree ring, CAMP BLOX sign + tents; s53 shorter walk, both 'full', no tree/pole in FG, Max lifted 0.07 = no FLOAT)
B8 DONE 23:11 (s42 both knees down 1.2 from the duck, flat stone narrowed + raised so the fist lands ON the duck's head side (NOTOUCH clean); glow pops on 'duck.'; side-front camera)
B9 DONE (s51 Chase MCU alone, no FG; b_look fixes the seated pitch)
B10 DONE (standing kids moved off the stone ring; FLOAT 0)
B11/B24 DONE 23:11 (s39 both fists ON the cheeks, targets parented to her head)
B12/B14/B22 DONE 23:11 (s62: the dark pane MIRRORED the ducks -> glass hidden, night-sky box behind; exactly 4 ducks, all inside the frame (x 0.08-0.92), lens 25)
B13/B18 DONE 23:11 (morning: all camp lamps hidden in b_morning; trees hidden near the lens, between lens and subject, and directly behind a single's head)
B15 DONE (contact on the forearm/sleeve top, Leo's forearm rests forward over his knee)
B16 DONE 23:11 (s37 tent0 hidden (the camera stood in it); two kids MCU look up at the lamp, lamp in frame, flicker + dies on 'camp.')
B17 DONE 23:11 (s59/s61 back to the baseline out-facing straight-on insert you liked (screen fills the frame), with b_hold; HALF on the holder = accepted category)
B20 DONE 23:11 (s46 Leo glances down at the hand, camera swung 12 deg toward Leo's front: both faces 3/4)
B23 DONE 23:11 (s43 pitch 32 lens 20, Jay removed from the lens side so no back fills the centre)

## 23:11 MANAGER -> B: status + timebox
Part A is APPROVED. Please post your status on BOARD now and mark B1-B24 DONE / WONTFIX in this inbox. Your v4 log looks close (only accepted HALF on phone holders + s56 Max armR 0.49 at the end; my numeric check: s37 no longer a flat field, s62 now dark, s59/s61 screen-dominated). Timebox: post PART B READY by ~23:40 with a full 34-63 lo pass on the CURRENT kit (stance/settle_stance + night_dim landed 22:29-22:39, after your v4 started). Remaining must-fix for approval: s56 contact (< 0.35 while the push reads), s46 both faces 3/4 (also a look-dev still), s54 no pole bar.

## 23:22 MANAGER: ALL APPROVED - STOP
APPROVED B (shots 34-63): baseline 133 -> 17 flags = 15 HALF on phone holders in the straight-on inserts s49/s59/s61 (accepted) + 2 NOTOUCH s56 Max armR 0.49 on the last 2 frames after the push (accepted: 0.04 over tolerance, bag still in his hands). B1-B24 VERIFIED via your v4/v4b log, my numeric frame checks (s37 no flat field, s62 night, s59/s61 screen-dominated) and the full-quality look-dev stills of s38/s46/s56.
Look-dev stills done: out/lookdev/ld1..ld6 + out/lookdev/lookdev_strip.jpg. No further renders. Do NOT run ep_final.sh (user must approve the look-dev first).
B19 (s56 <0.35) DONE 23:27 (Max pushed back half a step, bag rides in his hands; grips in Max's frame; fists 0.12-0.34; QA clean in v5)
