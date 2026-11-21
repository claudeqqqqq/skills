# MUSIC PLAYBOOK: what viral Roblox story videos actually use (researched 2026-11-15)

Method: YouTube search (sorted by views + Shorts shelves) in the built-in browser; for each video, the page data's
Content-ID music card ("videoAttributeViewModel"), the description, and on-screen text. View counts read from YouTube page
data on 2026-11-15. Not used: TikTok (pages blocked to our fetch tool), Gemini (needs the user's OK to send prompts),
comment scraping (blocked). Nothing here was heard by me: track names come from YouTube's own music match or on-screen text.

## 1. Findings
| # | Finding | Evidence | Confidence |
|---|---|---|---|
| 1 | The "In this town / In this world" background bed = **"Numbers" by TEMPOREX** (2:07) | YouTube Content-ID music card on 4xJgIbCeat0 ("the song in the background of in this world Roblox animations") reads "Numbers / TEMPOREX"; GiOEGQAduEQ ("songs used in background of story Roblox shorts", about the bed used by @Gneef and @GreenBroRants) shows "numbers." on screen at 0:11; ZvzpHWB2SJs ("why does every in this town video has this audio") plays it over @GreenBroRants' "You Must Paint To Get Things In This Town" (9,073,938 views). Gneef's "In This Town, You Are Not Allowed To Speak" = 4,914,182 views | HIGH (2 independent sources) |
| 2 | Most viral Roblox story Shorts show "Original sound": music is baked into the upload, so the platform does not name it | /shorts page data, e.g. VTJLSVSIfkQ (17,331,867 views) soundAttributionTitle "Original sound"; 17 of 18 viral story Shorts had no music card | HIGH |
| 3 | Sad / Brookhaven storylines use pop songs | Bloopo "SAD ORPHAN BOY STORY IN ROBLOX" (6,178,473 views): music card "Another Love (Radio Edit), Tom Odell" | HIGH for that video; pattern MEDIUM |
| 4 | "Scene break" meme music = **"Relaxed Scene", James Clarke** (1976 library track, Themes International) | _4WEcJwOD4w "Relaxed scene break in story roblox music 10 hours" (4,268,271 views), music card "Relaxed Scene / James Clarke"; Wikipedia draft | HIGH that it is used; licence = production library |
| 5 | Roblox rant beds: Chopin Nocturne Op. 9 No. 2 (piano) | zKkEav0nRGA music card "Nocturne in E Flat Major Op. 9 No. 2 (Chopin), Rousseau" (40,757 views) | MEDIUM (small video) |
| 6 | Old (2016-2021) Roblox "bully story" music videos use EDM/pop (Alan Walker, Marshmello, Galantis) | titles of Cryptize / Aqua Animation videos, 25-150M views | HIGH, but this is the music-video genre, not narrated stories |

### 1b. Storyline / Blox-City-style scan (2026-11-15, round 2)
45 viral (1M+) Roblox story Shorts from 10 searches (bully, poor boy, rich kid, Brookhaven sad, school, millionaire, noob,
twist, adopted, sad story); 14 had a YouTube Content-ID music card (the rest = "Original sound"):
| Track | Videos (views) | Fits |
|---|---|---|
| **"Another Love" (Radio Edit), Tom Odell** | Onion Stories "A sad story about the boy's difficult childhood" YR6uC_oRaZA (37,385,980); Onion Stories "Always respect poor people" r0ifHSBlSD0 (37,083,554); Bloopo "SAD ORPHAN BOY STORY" au8TnI0pbOM (6,178,514) | sad / poor-boy turns and endings: 3 of 14, the most repeated track |
| **Chopin Nocturne Op. 9 No. 2** (Drona Acharya recording) | Renovated Potato "SCHOOL RULES NEED TO CHANGE!" 6qejqOhPLn4 (22,714,344); also a rant-bed video (round 1) | school / calm-ironic beds; composition is public domain, so a PD/CC0 recording can be baked in legally |
| "Alone", Alan Walker | StreenMan "Roblox Bully Stories Be Like" NzNTJWk4t7I (7,777,831) | bully stories |
| "Džanum", Teya Dora | Respawn Animation "Little NOOB emotional story" ZzumHyUrYO0 (14,203,358) | emotional |
| "Bang Bang Bang (slowed)", Lil Yappa | Hawks RBX "School will start in 10 minutes" UtkCwB_GFmw (53,386,620) | comedy school |
| one each | "misery." pupsies (1.35M); "People You Know" Selena Gomez (1.55M); "Kamin" EMIN/JONY (4.15M); "MALA" 6ix9ine (3.56M); KPop Demon Hunters "What It Sounds Like" (1.90M); "I Don't Know" Erika (2.19M); "REAL MOONSHINE FUNK" DJ Robe (3.16M) | trend songs |

Gemini test (user-approved, 2026-11-15): asked to name the music in 7 videos incl. 2 controls with a known answer (Numbers;
Another Love). It said it processed the audio but returned UNKNOWN for all 7 with generic "piano + strings" descriptions,
failing both controls. => Gemini cannot identify tracks; do not use it for music IDs. Content-ID cards are the reliable source.

What this means: viral creators use COMMERCIAL songs (TEMPOREX, Tom Odell, library tracks), not Kevin MacLeod. My earlier
Kevin MacLeod picks were "free library music", not "what Roblox story creators use". Lesson logged.

## 2. Licensing reality for @rblxanimates
- Commercial songs baked into the MP4 = Content ID / Rights Manager risk (muted audio, blocked, or claimed), more so on a business account.
- How creators usually do it: post the video and add the song from Instagram's own music picker (only if the account type
  has that song). Business accounts get a reduced, commercial-cleared library; creator/personal accounts get more.
  UNVERIFIED whether "Numbers" (TEMPOREX) is in the Instagram library for this account: the user checks in the app.
- Public-domain compositions (Chopin) are safe only with a public-domain or CC0 RECORDING (e.g. Musopen), not the Rousseau recording.
- "Relaxed Scene" is production-library music: needs a library licence or the in-app picker.

## 3. Rules for the kit (every video)
1. Pick the bed from this playbook by format, not from free libraries:
   - In this town / In this world: "Numbers" (TEMPOREX) feel. Our approved AI-world bed stays the baked-in default.
   - Blox City storylines: per story, from what similar viral stories use (pop/emotional song for sad turns, a "scene break" library cue for jumps).
2. Render TWO masters when the bed is a commercial song: `final_nomusic.mp4` (voice + SFX + icons, music stem silent) for
   posting with the in-app song, and `final_preview.mp4` with the song mixed in for the user's review only (never posted).
   Superseded 2026-11-16 (owner): make ONE final video with the bed mixed in (kit v4.3: tools/ep_audio/bed.py + mix.py -> mix_final.wav -> out/final.mp4). See SKILL.md section 4.
3. Baked-in music must be commercial-OK (CC BY with credit, CC0, owned, or licensed). Write MUSIC_LICENSE.txt either way.
4. Never invent a track name. A name enters this file only from a platform music card, an on-screen credit, or the user's Shazam.
5. Update this file whenever a new viral reference is checked (append a row with video ID, views, date and evidence).
