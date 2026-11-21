# MUSIC_RESEARCH — which bed for which Roblox story video, and how to keep the narrator clear

Date: 2026-11-14. Research + measurement only (no renders, no ElevenLabs credits, no files downloaded).
Confidence tags: **[measured]** = run here with ffmpeg/earshot; **[sourced]** = web source below; **[unverified]** = genre
convention / my judgement, not confirmed by a source or a listen. I cannot hear audio: every "clear/dull" claim is a number.

## 1. What the genre does (short version)

- Web search did not surface any write-up of the exact tracks used by craftee_films or the "In this world / In this town"
  shorts (e.g. YouTube npdxivww0Xk); creators rarely credit beds. Identifying them needs a manual listen/Shazam by the user.
  **[unverified for specific tracks]**
- Roblox culture leans on **phonk / trap-phonk** (Memphis samples, heavy 808, cowbell) for edits and action
  ([Uppbeat: what is phonk](https://uppbeat.io/blog/what-is-phonk-music)) **[sourced, general]**. Story-narration shorts
  generally use a **constant low bed** under a first-person narrator, with **dips/silence before a reveal** and a **hit on
  the twist**; this matches our own REF1/REF4 notes (AUDIO.md, REF4_HORROR_STORY_AUDIO.md). **[unverified beyond our refs]**
- Typical tempo bands (convention, **[unverified]**): mystery/dystopian 70-95 BPM (or half-time feel), horror drone
  no pulse / 60-80, comedy 100-125 (pizzicato, ukulele, bassoon), emotional 60-80 piano/strings, chase/action 130-150
  (or 140-160 phonk).


### 1b. Reference videos opened (2026-11-14 follow-up, built-in browser)
| Video | Channel | Views | Description / music credit |
|---|---|---|---|
| youtube.com/shorts/npdxivww0Xk "You went back in time to save her..." | legendRBX | 5,067,003 | hashtags only (#roblox #love #wholesome #animation); **no music credit** |
| youtube.com/watch?v=E9TTaFj-YXU "His Cat CRAWLED Closer..." (1:40) | Haro Talks | 2,628,986 | one-line hook; **no music credit** |
| youtube.com/watch?v=zzu-VJTRlM8 "The Crows GATHERED..." (1:33) | Haro Talks | 1,423,165 | one-line hook; **no music credit** |

Not done / blocked: YouTube search and channel pages (craftee_films) did not render text in the browser pane; a page-script
scrape of more videos was refused by the permission classifier; Instagram audio labels and comment threads were not read;
an extended web search for track IDs returned nothing usable. Therefore **no track, artist, BPM or level for any
reference is verified** — only that top refs carry no music credit and no YouTube "Music" card was found in their page data
(suggests stock/unlisted beds or original audio). BPM was not measured (would require capturing the audio). Next step:
the user Shazams 3-5 refs or reads the IG audio label under each Reel.

## 2. Licensing for an Instagram brand/business account

- Instagram's in-app licensed library is for personal, non-commercial use; business accounts get only the
  Sound Collection / commercial library, and accounts can be treated as commercial from monetisation/branded content.
  Songs can vanish when deals change. Off-platform music is fine if *its* licence allows commercial use; CC BY-NC is NOT
  ok for a business account. ([Soundstripe: IG music library](https://www.soundstripe.com/blogs/instagram-music-library),
  [Sprintlaw UK guide](https://sprintlaw.co.uk/articles/how-to-add-music-to-instagram-reels-without-copyright-issues-the-definitive-guide-for-uk-businesses-creators/),
  [Foximusic 2026 guide](https://www.foximusic.com/blog/instagram-reels-music-copyright-legal-guide/)) **[sourced; vendor
  blogs, verify Meta Help Center before relying]**
- Rule for us: bake the bed into the MP4 from a commercial-OK source; never use "trending audio"/chart songs on @rblxanimates.
  Keep a `videos/<slug>/MUSIC_LICENSE.txt` (source URL, licence, credit line, date). The current AI-world bed: confirm how it
  was made (generated tool + tier) and record that licence too. **[action]**

### Shortlist (list only — nothing downloaded). Verify each licence page at use time.

| # | Source / track | URL | Licence (summary) | Mood / BPM | Suits |
|---|---|---|---|---|---|
| 1 | Meta Sound Collection (in Creator Studio / Ads) | https://www.facebook.com/sound/collection | Meta royalty-free, commercial use incl. ads | mixed | any; safest on IG |
| 2 | Kevin MacLeod — "Investigations" | https://incompetech.com | CC BY 4.0, credit "Title, Kevin MacLeod (incompetech.com) / Licensed under CC BY 4.0" [verified FAQ; IG not named → credit in caption] | mystery, ~mid-tempo [BPM unverified] | In-this-town mystery |
| 3 | Kevin MacLeod — "Sneaky Snitch" | https://incompetech.com | CC BY 4.0 | sneaky comedy, pizzicato ~ [BPM unverified] | comedy |
| 4 | Kevin MacLeod — "Monkeys Spinning Monkeys" | https://incompetech.com | CC BY 4.0 | goofy upbeat (overused) | comedy (use sparingly) |
| 5 | Kevin MacLeod — "Darkest Child" / "Ghost Story" | https://incompetech.com | CC BY 4.0 | horror drone/ambient | horror |
| 6 | Kevin MacLeod — "Volatile Reaction" | https://incompetech.com | CC BY 4.0 | driving action | chase/action |
| 7 | Pixabay Music (search "suspense", "phonk", "dystopian") | https://pixabay.com/music/ | Pixabay Content License: free use, no attribution, no standalone resale [verified summary page]; Content ID not mentioned on page → check per track [unverified] | varies | all; check each |
| 8 | Uppbeat (phonk / suspense collections) | https://uppbeat.io | free tier w/ credit, Premium for commercial [unverified: FAQ returned 429] | phonk 140-160, suspense | action, dystopian |
| 9 | Epidemic Sound (Commercial plan) | https://www.epidemicsound.com | paid sub; covers business social incl. IG; Content-ID cleared by channel | huge "dark/suspense/quirky" | all (best if budget) |
| 10 | Artlist | https://artlist.io | paid sub, social/commercial per plan | cinematic | drama, emotional |
| 11 | Freesound CC0 (risers, hits, drones) | https://freesound.org | CC0 only (filter) — CC BY needs credit, avoid NC | SFX/drones | horror, transitions |
| 12 | YouTube Audio Library | https://studio.youtube.com (Audio Library) | free; terms are YouTube-oriented — off-YouTube use not clearly granted → **avoid for IG** [uncertain] | varies | don't use for IG |
| 13 | NCS (NoCopyrightSounds) | https://ncs.io/usage-policy | creators free incl. sponsored, credit in description; a brand promoting its own products needs a commercial licence [verified usage policy; IG not named] | EDM 128-150 | action (with caution) |
| 14 | ElevenLabs Music (paid tier) | https://elevenlabs.io/music | commercial on paid plans; AI output copyrightability unclear | any brief | custom beds per genre |
| 15 | OpenGameArt CC0 music | https://opengameart.org | CC0 filter only | chiptune/game | comedy, Roblox-game feel |

## 3. Decision table — video type -> bed

Levels are of the **music stem as it sits under the voice** (voice stem ~ -16 LUFS before master; master -14 LUFS, -1.5 dBTP).

| Video type | Bed (mood, instruments) | BPM | Static bed vs voice | Duck while speaking | Structure / switches | SFX density |
|---|---|---|---|---|---|---|
| In this world / In this town (mystery-drama, dystopian) — **default** | AI-world bed (user rule), dark synth pad + soft pulse; bass shelf cut | as track (1.0x) | **-6 to -7 LU** | 3-4 dB (→ ~10 LU under during speech) | constant; -12 dB dip 0.45 s before reveal/twist cuts; hit on twist; 2 s fade on final flash | medium (whooshes on cuts, 1 hit per reveal) |
| Horror | drone/texture, sparse piano/music-box, sub booms | none / 60-80 | -8 to -10 LU | 4-6 dB | near-silence before scares, silence drop 0.3-0.8 s then hit; melodic ≤ 45 % runtime (AUDIO.md) | low but loud hits |
| Comedy | pizzicato/bassoon/ukulele/chiptune, light | 100-125 | -8 LU | 3 dB | music stops dead on punchline (record-scratch or silence), restarts next beat | high (pops, boings) |
| Emotional twist | piano + strings, warm | 60-80 | -8 to -10 LU | 2-3 dB | swell into the reveal, thin to piano under the last line | low |
| Chase / action | trap-phonk / hybrid percussion, 808 | 130-160 | -6 LU (needs energy) | 5-6 dB (busy) + bass shelf | riser into chase, beat drop on action, cut on capture | high |

Rule of thumb: the narrower the bed's spectrum overlap with the voice (bass-only, high-only), the closer it can sit.

## 4. Why EP1 sounded "dulled" (measured, number_lies stems)

**[measured]** EP1 bed = ai_world music.wav; voice at -16.0 LUFS, bed at -19.4 LUFS (3.4 LU gap, no EQ, no duck). Band
loudness (ffmpeg ebur128 on band-passed stems):

| band | voice | bed | bed − voice |
|---|---|---|---|
| 40-150 Hz | -27.2 | **-20.5** | **+6.7** |
| 150-500 Hz | -20.8 | -29.9 | -9.1 |
| 500-1000 Hz | -24.3 | -45.7 | -21 |
| 1-4 kHz | -23.0 | -46.7 | -24 |
| 4-12 kHz | -23.1 | -46.2 | -23 |

So the bed is a **bass-heavy track** (almost nothing above 500 Hz). The common "carve 1-4 kHz in the music" fix would do
nothing here. Dulling comes from: (a) the bed's low end ~7 LU *louder* than the voice's, which upward-masks the voice's
low-mids and eats master headroom — after loudnorm to -14 the voice is turned down to make room for sub/bass energy;
(b) only 3.4 LU overall gap (research recommends ≥10 LU commentary-over-music for clarity; non-experts accept ~4 LU less,
[Salford/AES, Ward & Shirley](https://salford-repository.worktribe.com/OutputFile/1486952)) **[sourced]**; (c) no ducking.

## 5. Fix recipe (ffmpeg; drop into make_audio_preview.py / mix.py)

zsh note: write `${VAR}` before `[label]` in filter strings (`$SC[m]` is zsh subscripting — it broke the first test).

```
V="highpass=f=80,equalizer=f=3000:t=o:w=1:g=2.5,volume=<gain to -16 LUFS>"      # voice: rumble cut + presence +2.5 dB
M="highpass=f=35,lowshelf=f=120:g=-6,volume=<gain to ~-22.5 LUFS>"               # bed: sub/bass shelf -6 dB
SC="sidechaincompress=threshold=0.125:ratio=2.5:attack=20:release=300:knee=3:makeup=1"   # ~3.7 dB duck under speech
-filter_complex "[0]${V},asplit[v][k];[1]${M}[m0];[m0][k]${SC}[m];[v][m]amix=inputs=2:normalize=0:duration=first"
then loudnorm=I=-14:TP=-1.5:LRA=11:linear=true (two-pass in mix.py)
```
For a bed that DOES have mids (orchestral, phonk with vocal chops, pads): add `equalizer=f=2500:t=o:w=1.5:g=-4` to M
(1-4 kHz scoop; iZotope prefers a multiband/dynamic cut there so the bed is not muffled between lines —
[iZotope mixing for video pt 4](https://www.izotope.com/en/learn/mixing-audio-for-video-part-4-mixing-techniques)). Duck
depth references: Resolve default 2.7 dB, 2-5 dB typical ([Larry Jordan](https://larryjordan.com/articles/automatically-duck-background-music-under-dialog-in-davinci-resolve/));
3-6 dB ([Vidpros](https://vidpros.com/fix-background-music-too-loud-video/)). **[sourced]**

**Measured results** (scratchpad test files, EP1 outputs untouched):

| mix | bed static | bed during speech | bed 40-150 Hz | master I / TP | earshot bands low / lowmid / presence | brightness |
|---|---|---|---|---|---|---|
| A = EP1 style | -19.4 (3.4 under) | -19.4 | -20.5 | -14.4 / -1.4 | -2.0 / -6.5 / -16.1 | 2413 Hz |
| C (too deep: thr 0.063, ratio 3) | -24.6 | -32.2 (16 LU under) | -33.5 | -14.8 / -1.5 | -5.6 / -3.7 / -12.7 | 2976 Hz |
| **D (recommended)** | **-22.6 (6.6 under)** | **-26.3 (~10 LU under)** | **-27.5 (≈ voice)** | -14 target / -1.4 | -4.4 / -4.3 / -13.3 | **2811 Hz** |

D moves the mix's energy from bass to low-mid/presence (+2.8 dB presence, +400 Hz spectral brightness vs A) while the bed
stays clearly present between lines (only ~3.7 dB of duck). C proves the duck can over-bury the bed — keep the duck ≤ 5 dB.
Not verified by ear: the user must listen to `D_fix_m.wav` vs `A_base_m.wav` in the scratchpad before adopting.

Targets to log in mix_report.json: `bed_under_voice_lu` 6-8 (static), 9-12 during speech; `bed_low_minus_voice_low` ≤ 0 dB
(40-150 Hz); duck 3-5 dB; master -14 ±1 LUFS, TP ≤ -1.5 dBTP; voice presence EQ +2-3 dB @ 3 kHz.

## Sources
- https://uppbeat.io/blog/what-is-phonk-music
- https://www.soundstripe.com/blogs/instagram-music-library
- https://sprintlaw.co.uk/articles/how-to-add-music-to-instagram-reels-without-copyright-issues-the-definitive-guide-for-uk-businesses-creators/
- https://www.foximusic.com/blog/instagram-reels-music-copyright-legal-guide/
- https://www.izotope.com/en/learn/mixing-audio-for-video-part-4-mixing-techniques
- https://salford-repository.worktribe.com/OutputFile/1486952
- https://larryjordan.com/articles/automatically-duck-background-music-under-dialog-in-davinci-resolve/
- https://vidpros.com/fix-background-music-too-loud-video/
- https://www.soundonsound.com/techniques/duck-tales
- https://incompetech.com/music/royalty-free/faq.html, https://pixabay.com/service/license-summary/, https://ncs.io/usage-policy (fetched 2026-11-14); Uppbeat, Epidemic, Artlist, Meta Sound Collection, YouTube Audio Library, ElevenLabs, OpenGameArt, Freesound licence pages NOT fetched — unverified.
