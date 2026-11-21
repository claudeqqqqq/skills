# EP3 "The Friend Who Sold My Secret" (Blox City, Day 02): script v1, 2026-11-16

Status: title A ("I Told ONE Secret. By Lunch, Everyone Knew."), script APPROVED 2026-11-16; music = "Numbers" bed for the whole video; voice take 1 approved; look-dev approved; rendered and posted.
Series: Blox City (custom content, references/BLOX_CITY.md). Ending per references/ENDING_RULE.md.
Production: kit v4.1 (frame_on, hold/props3, kneel_down, belly_laugh/crowd_laugh, QA + contact-sheet eye check), parallel team (references/TEAM_AGENTS.md).

## Title options (pick one)
1. **I Told ONE Secret. By Lunch, Everyone Knew.** (catalogue draft, chosen)
2. He Sold My Secret for 500 Coins
3. My Best Friend Sold My Secret for a Hat

## Cast
- Leo (me, narrator): 14, plain hoodie. Hero prop: a yellow duck night-light.
- Max: best friend since kindergarten. Gets a shiny "limited" hat halfway through.
- Chase: rich kid, runs the gossip account "Blox Tea". Secretly afraid of the dark.
- Classmates (extras), camp teacher (no lines).

## Length
328 spoken words. At 185 wpm about 106 s, at alex_ep1's ~200 wpm about 98 s, plus about 6-8 s of meme pauses = about 104-114 s.
Measured take: 100.05 s voice (197 wpm, 18 meme pauses), 100.85 s final.
If it runs over 120 s: shorten meme pauses first, then cut "Same bus seat."
TTS text only: "Blocks City", "Blocks Tea" (v3 mangles "Blox"). Captions keep "Blox".

## Script (one line = one beat; [SFX] marks are NOT spoken; Alex reads every line, quotes included)
```
I told my best friend one secret. By lunch, the whole school knew. And he got paid for it. [DUN DUN DUNNN]
Max and I had been best friends since kindergarten. Same lunch table. Same bus seat. A secret handshake with eleven steps. [SPARKLE]
So one night, on a call, I told him the thing nobody knew. I'm fourteen, and I can't sleep without my night-light. It's shaped like a duck. [QUACK] "Your secret's safe with me," Max said.
At Blox City High, there's an account called Blox Tea. Chase runs it. Chase is rich. And Chase pays five hundred coins for every secret you send him. [CHA-CHING]
Next morning, my phone would not stop buzzing. [BUZZ BUZZ BUZZ] Blox Tea had posted a drawing of me, hugging a duck. Two hundred comments. [POP POP POP] At lunch, the whole cafeteria quacked when I walked in. [QUACK CHORUS] Everyone laughed. Max didn't look up. [CRICKETS]
Then I saw his head. A brand new limited hat. Five hundred coins. [RECORD SCRATCH] I sat down across from him. "Was I worth five hundred coins?" He stared at his tray. "It was a limited, bro." [BRUH]
I didn't talk to him for two weeks. Then came the class camping trip. [FAST-FORWARD WHOOSH]
Night one, a storm knocked out every light at camp. [THUNDER + POWER-DOWN] Pitch black. Somebody screamed. Then everybody screamed. [CARTOON SCREAMS]
I opened my bag and switched on the duck. [CLICK + SOFT QUACK] One by one, the whole class sat down around it. Even Chase. Chase was shaking. Chase was holding my sleeve. [CROWD "OHHH"]
Someone held up a phone. "Post it, Leo. Blox Tea pays five hundred." I looked at Chase. I knew exactly how that felt. "Nah. Secrets aren't for sale." [AWW]
The next morning, Max found me by the tents. He held out five hundred coins. "I'm sorry. Take it." I pushed it back. "Keep it. You'll need it to buy a new best friend." [FAHHH]
That week, Chase deleted Blox Tea himself. And half my class ordered duck night-lights. [QUACK + DING]
Like, share and follow for more. [ICONS: heart on "Like", share on "share", + FOLLOW clicked by the cursor on "follow", pop each]
Would you give Max a second chance? Comment TRUST or BLOCK. [ICON: comment bubble on "Comment", then TRUST / BLOCK buttons]
```

## Meme SFX cue sheet (each in a word gap, 0-4 dB under the voice peak, music dips under it)
| cue | after the words | sound | source plan |
|---|---|---|---|
| 1 | "paid for it." | dun dun dunnn sting | reuse the EP2 original sting |
| 2 | "eleven steps." | sparkle | kit `sparkle` |
| 3 | "shaped like a duck." | single rubber-duck quack | ElevenLabs SFX (original) |
| 4 | "every secret you send him." | cash register | kit `cashier` |
| 5 | "stop buzzing." | phone buzz x3 | ElevenLabs SFX |
| 6 | "Two hundred comments." | pop x3 (notification pops) | kit `pop` |
| 7 | "when I walked in." | crowd of kids quacking | ElevenLabs SFX (original, not a clip) |
| 8 | "didn't look up." | crickets | kit `crickets` |
| 9 | "Five hundred coins." (hat) | record scratch | reuse EP2 |
| 10 | "a limited, bro." | "bruh" | reuse the EP2 Alex take |
| 11 | "camping trip." | fast-forward whoosh | kit `whoosh` |
| 12 | "every light at camp." | thunder + power-down hum | ElevenLabs SFX |
| 13 | "everybody screamed." | short cartoon kid screams | ElevenLabs SFX (original); meme_cues "nth": 2 |
| 14 | "switched on the duck." | switch click + soft quack | kit click + cue 3 pitched down |
| 15 | "holding my sleeve." | crowd "ohhh" | reuse EP2 |
| 16 | "aren't for sale." | soft "aww" | kit `aww` |
| 17 | "new best friend." | "FAHHH" | reuse the EP2 Alex take |
| 18 | "duck night-lights." | quack + sparkle ding | cue 3 + kit `ding` |
| 19-22 | "Like" / "share" / "follow" / "Comment" | pop + cursor click | kit `pop`, `click` (placed automatically) |

## Music
"Numbers" (TEMPOREX) for the whole video (the owner: "same music as in this town"). In this repository the default bed is
`assets/music/default_bed.wav` if you hold a licensed copy, otherwise an original score from tools/score.py (bed.py).

## Beat map (approx.) with kit v4.1 shot grammar
| t (s) | beat | shots | kit notes |
|---|---|---|---|
| 0-6 | hook | POV phone: Blox Tea post (drawing of Leo hugging a duck); MCU Leo; Max with the 500 coin bag | phone prop, hold() |
| 6-13 | best friends | two-shot outside school; lunch table; bus seat; the 11-step handshake (hands meet) | qa.touch on both fists |
| 13-24 | the secret | night bedroom, duck night-light glowing; call screen "MAX"; Max on his bed | duck_light (emissive) is the key light |
| 24-33 | Blox Tea | Chase MCU smug; insert app "SEND A SECRET, GET PAID 500"; coin bag | straight-on UI insert |
| 33-48 | exposed | phone buzzing with notifications; the post + "200 comments"; cafeteria; kids quack AT Leo; Max head down | crowd_laugh(target=Leo), not dancing |
| 48-60 | the hat | tilt up to the LIMITED hat; Leo sits across; OTS "Was I worth...", Max stares at his tray | tray rests on the table |
| 60-64 | two weeks | Leo alone on the bus | sit before the shot |
| 64-74 | blackout | camp at night, lightning, lights die; kids scream | night look, faces readable |
| 74-84 | the duck | Leo kneels, switches on the duck; class sits in a circle; Chase holds Leo's sleeve | kneel_down, seated kids, hand ON sleeve |
| 84-92 | the choice | kid holds up a phone; Leo looks at Chase; "Nah." | hold(), eyeline |
| 92-102 | Max returns | morning by the tents; Max holds out the coin bag; Leo pushes it back | hands touch the bag |
| 102-107 | resolution | "Account deleted" screen; Chase; duck lights in kids' windows | phone insert |
| 107-115 | end card | Leo MCU smiling with the duck; centre pop-ups, cursor clicks FOLLOW; TRUST / BLOCK | tools/ep_endcard.py |
