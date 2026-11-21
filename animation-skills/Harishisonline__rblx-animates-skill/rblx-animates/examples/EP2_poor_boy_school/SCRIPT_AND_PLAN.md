# EP2 "The Poor Boy Who Bought the School" (Blox City): script v2, 2026-11-15

Status: SCRIPT + MUSIC APPROVED by the user (2026-11-15). Next gates: meme SFX set, voice sample, look-dev stills (Claude Code on the Mac).
No voice, SFX generation or frames until those are approved.
Series: **Blox City** (user, 2026-11-15). Custom content: no In-this-town template (music, lint, CTA rules do not apply).
See knowledge/BLOX_CITY.md.

## Decisions (user, 2026-11-15)
- Title: **The Poor Boy Who Bought the School**
- Narrator: Alex (alex_ep1) reads everything, quoted lines included, like EP1 and the AI-world video. No character voices.
- Music: library tracks viral creators use (no ElevenLabs Music, not the AI-world bed); picks need approval (see Music).
- Ending: "Like, share and follow for more." + comment question with pop-up icons (knowledge/ENDING_RULE.md).
- Meme sound effects ("fahhh" and similar) on the comedy beats.

## Length
352 words (incl. the like/share/follow end line). EP1 pace (185 wpm) ~114 s + ~6 s of meme pauses = ~120 s; alex_ep1 post (~200 wpm) = ~112 s.
If the real take runs over 120 s: shorten meme pauses first, then cut "because I'm fourteen and somebody has to sign".
TTS note (LESSONS): v3 reads "Blox" as "Blocks"-ish; write **"Blocks City"** in the TTS text only, captions keep "Blox City".

## Script (one line = one beat; [SFX] marks are NOT spoken)
```
They laughed at my shoes for three years. Then, one Monday, I bought the school. [VINE-STYLE BOOM]
At Blox City High, I was the poor kid. Same hoodie. Same shoes. The left one had a hole you could fit a pencil through. [BOING]
Ryan made sure everyone noticed. Every morning, he knocked my books out of my hands. [BONK] "Maybe buy real shoes before you come here, Harry." [CROWD "OHHH"] Everyone laughed. Nobody helped. [CRICKETS]
Then they found Milo. Smallest kid in sixth grade. His lunch hit the floor. [SPLAT] I knelt down next to him. "It's okay. I've got you." Ryan grinned. "Look. The poor kid found a pet." [BRUH]
Nobody knew what I did after school. [FAST-FORWARD WHOOSH] Four o'clock, I delivered pizza. Seven, I fixed the neighbors' laptops. And at midnight, on a computer older than me, I built a game. A tycoon game where you build a school, brick by brick.
In March, it had ten players. [POP] In June, ten thousand. [POP] By September, four million. [CHA-CHING] I didn't buy shoes. I saved every coin.
Then a letter came home. Blox City High was closing. Sold, to be torn down for a parking lot. And the man buying it was Ryan's dad. [DUN DUN DUNNN]
On Monday, a black car stopped at the gates. I stepped out. Same hoodie. Same shoes. Grandpa followed me with a folder, because I'm fourteen and somebody has to sign. The principal stared. "Harry? You're here for the ownership meeting?" Ryan froze. [RECORD SCRATCH] "Ownership what?" [FAHHH]
In the auditorium, the principal tapped the mic. "Blox City High has a new owner. The money came from a game four million kids play." She looked at me. "Harry built it." [CROWD GASP + BOOM] Ryan's dad never got his parking lot. [SAD TROMBONE]
Later, Ryan found me by the lockers. "So are you kicking me out?" His books slipped out of his hands. I picked them up. [AWW] "No. But from today, nobody here eats lunch off the floor."
Then I called Milo on stage. Free lunch and new shoes, for every kid who needs them. [CHEER]
I kept mine, though. The hole still fits a pencil. [DING]
Like, share and follow for more. [ICONS: heart on "Like", share arrow on "share", follow + on "follow", each with a pop]
Would you forgive Ryan? Comment FORGIVE or FORGET. [ICON: comment bubble on "Comment", then FORGIVE / FORGET buttons]
```

## Meme SFX cue sheet (all placed in a word gap, never on top of a word: LESSONS "a word onset on a cut masks the hit")
| cue | after the words | sound | source plan |
|---|---|---|---|
| 1 | "I bought the school." | deep vine-style bass boom | kit pack `boom` (+ low-pass), or ElevenLabs SFX original |
| 2 | "fit a pencil through." | boing | kit pack `boing` |
| 3 | "out of my hands." | bonk | kit pack `bonk` |
| 4 | "...before you come here, Harry." | crowd "ohhh" | ElevenLabs SFX (original) |
| 5 | "Nobody helped." | crickets | kit pack `crickets` |
| 6 | "hit the floor." | splat | kit pack `splat` |
| 7 | "found a pet." | "bruh" | Alex short TTS take (our voice), or ElevenLabs SFX |
| 8 | "after school." | fast-forward / tape whoosh | kit `whoosh` + pitch-up |
| 9 | "ten players" / "ten thousand" | pop x2 | kit pack `pop` |
| 10 | "four million." | cash register | kit pack `cashier` |
| 11 | "Ryan's dad." | dramatic dun dun dunnn | ElevenLabs SFX (original 3-note sting) |
| 12 | "Ryan froze." | record scratch | ElevenLabs SFX |
| 13 | "Ownership what?" | "FAHHH" (exasperated) | Alex short TTS take or ElevenLabs SFX (original, not a ripped clip) |
| 14 | "Harry built it." | crowd gasp + boom | kit `gasp` + `boom` |
| 15 | "parking lot." | sad trombone "wah wah" | ElevenLabs SFX (original) |
| 16 | "I picked them up." | soft "aww" | kit pack `aww` |
| 17 | "every kid who needs them." | kids cheer | kit pack `cheer` |
| 18 | "fits a pencil." | sparkle ding | kit pack `ding`/`sparkle` |
| 19-22 | "Like" / "share" / "follow" / "Comment" | pop on each end-card icon | kit pack `pop` (bright, short) |
Licensing: famous meme clips (the original vine boom, "bruh", "fahhh" recordings) are third-party audio and can get a business
account's reel muted or claimed. We recreate the same feel with our own sounds: kit pack, ElevenLabs SFX generations, Alex takes.
Level: meme hits sit 0-4 dB UNDER the voice peak, music dips -6 to -10 dB under each meme hit (kit side-chain).

## Music - FINAL, APPROVED 2026-11-15 (supersedes everything below in this section)
- 0 s -> the auditorium line (~80 s): "Numbers" by TEMPOREX (the viral In-this-town/Roblox story bed; knowledge/MUSIC_PLAYBOOK.md).
- Auditorium reveal (~80 s) -> end: "Another Love" by Tom Odell (top viral poor-boy story track, 37M-view refs).
- Both are added by the user in Instagram's music picker at posting. We export:
  out/final_nomusic.mp4 (voice + meme SFX + icons, no music) = the file to post;
  out/final_preview.mp4 (both songs mixed in, for review only, never posted). The preview needs the song files from the user on the Mac.
- If Instagram allows only one song per reel: fall back to "Another Love" from ~80 s, or "Numbers" for the whole video (ask the user).
- The Kevin MacLeod picks (Sneaky Snitch etc.) were REJECTED by the user; files in music/EP2/ are unused.
### (history) earlier proposals
- Most-used creator library music is Kevin MacLeod (incompetech): NPR reports "Monkeys Spinning Monkeys" behind "millions of viral
  videos"; Chartmetric names "Sneaky Snitch" (drama/gossip videos) and "Fluffing a Duck" (semi-comedic tone). Licence CC BY 4.0
  (incompetech FAQ, fetched 2026-11-14): commercial use OK WITH a credit line in the caption.
- Proposed cue sheet (subject to the user's OK):
  1. 0-57 s bully + montage: "Sneaky Snitch" (cheeky drama groove; leaves room for meme hits). Alternative: "Fluffing a Duck".
  2. 57-80 s letter + arrival: same track drops out on the letter (2 s room tone), then the build; or "Monkeys Spinning Monkeys" for the montage only (overused, use sparingly).
  3. 80-120 s reveal + ending: an uplifting Kevin MacLeod piano/strings track, picked from incompetech's mood filter in the Mac session and played to the user before use (not chosen yet, no title invented).
- Caption credit per track: "<Title> Kevin MacLeod (incompetech.com) Licensed under Creative Commons: By Attribution 4.0 License".
  Write videos/<slug>/MUSIC_LICENSE.txt. After posting, check the reel is not muted or claimed (some libraries' tracks get
  registered by third parties: UNVERIFIED for these titles).
- Mix: mix D (voice clarity), music dips -6 to -10 dB under each meme hit, -14 LUFS, TP <= -1.5.

## Beat map (approx., at ~115 s)
| t (s) | beat | picture idea |
|---|---|---|
| 0-5 | hook | ECU worn shoe with the hole, laughter; hard cut to a black car door opening |
| 5-12 | who I am | Blox City High hallway wide, Harry in the same hoodie; insert pencil through the shoe hole |
| 12-24 | humiliation | Ryan knocks the books (hands ON the books), crowd laughs, crickets on empty hallway |
| 24-35 | Milo | lunch tray hits the floor; Harry kneels, hand on Milo's shoulder; Ryan grin MCU |
| 35-50 | unseen work | fast montage: pizza delivery, laptop repair, midnight coding on an old PC |
| 50-57 | growth ladder | game screen counter 10 -> 10,000 -> 4,000,000; coin jar filling |
| 57-65 | the threat | letter insert "CLOSING", parking-lot plan, Ryan's dad |
| 65-80 | arrival | black car at the gates, Harry + Grandpa with folder, principal stares, Ryan freezes |
| 80-94 | reveal | auditorium push-in, principal at the mic, shocked faces, Ryan's dad |
| 94-105 | reversal | lockers: Ryan's books fall, Harry picks them up (same framing as 12-24, roles swapped) |
| 105-110 | lift others | Milo on stage, free lunch + new shoes banner |
| 110-114 | callback | ECU the same shoe, pencil through the hole |
| 114-120 | end card (ALL videos) | Harry MCU smiling; heart, share and follow icons pop in ON the spoken words, then a comment bubble on "Comment" and FORGIVE / FORGET buttons; pop SFX on each icon |
