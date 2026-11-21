# ENDING RULE (v2, owner decision 2026-11-18)

**The ending depends on the format.**

## In this town / In this world: NO like/share/follow ending (owner, 2026-11-18)
- The video ends on the last story line: a 3-8-word callback gag, an emotional truth line, a rule-reversal twist or a
  cliffhanger (`VIRAL_PLAYBOOK.md` section 3, ending formulas). Hard cut on the last word, no end card.
- No spoken "Like, share and follow", no "Comment X or Y" card. Comments come from the story itself (a mystery, a loophole
  people debate, an easter egg) - `VIRAL_PLAYBOOK.md` section 4.
- Why: the winners measured on 2026-11-17 end without a CTA (0 of 32 giant-channel videos end on a viewer question); our
  5.2-5.8 s outros were Gemini's #1 cost in the gap report. The kit (v5.1) draws no end card when the script has no
  "like ... follow" line.

## Blox City (storylines): the like/share/follow ending STAYS (user, 2026-11-15)
1. Last story line (twist / callback).
2. Narrator: "Like, share and follow for more." (wording can vary slightly, the three verbs stay).
3. Narrator: the episode's one-word, two-option question: "Would you ...? Comment X or Y." (LESSONS 2026-11-14).

On-screen, centre of the screen (user, 2026-11-15):
- A row in the middle (y ~0.50): heart pops in ON "Like", share arrow ON "share", then a red "+ FOLLOW" button; a white
  mouse cursor glides in and CLICKS it on "follow" (button presses, ripple, turns grey "FOLLOWING", click sound).
- On "Comment" the row fades and a big comment bubble pops in the centre; the two answer words pop in as buttons below.
- Pop-in: scale 0 -> 125 % -> 100 % over ~8 frames, slight wobble, short "pop" SFX a few dB under the voice.
- Captions move down to y 0.68 during the end card. Icon/cursor art is our own (no platform logos).
- Implementation: `tools/ep_endcard.py` (automatic from words.json when the script has the like ... follow line).
- Script budget: the end block adds ~12-16 words (~4-5 s).
